import sqlite3
import pandas as pd
from jinja2 import Template
import shutil
import aiosql


def get_queries():
    sql = aiosql.from_path('template/db/queries', 'psycopg2')
    return sql

def get_version_data(db_name, query):
    """Connect to the database and get data about the query."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    cursor.execute(query)
    data = cursor.fetchone() 
    
    connection.close()
    
    return data

def load_template(template_path):
    """Read the file contents of the template."""
    with open(template_path, "r") as file:
        return file.read()

def render_template(template_str, data):
    """Render the template with the data."""
    template = Template(template_str)
    return template.render(data)

def update_file(output_path, content):
    """Update an output file with the rendered content."""
    with open(output_path, "w") as file:
        file.write(content)

def copy_file(src, dest):
    """Copy a template file if there are no changes."""
    shutil.copy(src, dest)

def get_table_person(db_name):
    """Get a DataFrame from the PATIENTS table."""
    query = get_queries().get_example_patients.sql 
    connection = sqlite3.connect(db_name)

    df = pd.read_sql_query(query, connection)
    
    connection.close()
    
    return df

def update_index_file(template_path, output_dir, db_name):
    """Update the index.md file."""
    query = get_queries().get_version_database.sql 
    version_data = get_version_data(db_name, query)
    if version_data:
        version, version_date = version_data
    else:
        version, version_date = "N/A", "N/A"

    data = {
        'database': {
            'version': version,
            'version_date': version_date
        }
    }

    template_content = load_template(template_path)
    rendered_content = render_template(template_content, data)

    output_file_name = f"{output_dir}/index.md"
    update_file(output_file_name, rendered_content)

def update_tables_file(template_path, output_dir, db_name):
    """Update the tables.md file"""
    df = get_table_person(db_name)
    
    # Convert the dataframe in markdown format
    data_dict = {
        'table': {
            'person': df.to_markdown(index=False)  
        }
    }

    template_content = load_template(template_path)
    rendered_content = render_template(template_content, data_dict)

    output_file_name = f"{output_dir}/tables.md"
    update_file(output_file_name, rendered_content)

def update_all_files(template_files, output_dir, db_name):
    """Update multiple template files."""
    # Actualizar el archivo index.md
    update_index_file("template/index.md", output_dir, db_name)

    # Actualizar el archivo tables.md
    update_tables_file("template/tables.md", output_dir, db_name)

    # Copiar otros archivos sin cambios
    for template_file in template_files:
        if template_file not in ["template/index.md", "template/tables.md"]:
            copy_file(template_file, f"{output_dir}/{template_file.split('/')[-1]}")

if __name__=='__main__':
    template_files = [
        "template/architecture.md",
        "template/glossary.md",
        # Agregar más archivos de plantilla aquí
    ]

    # Ejecutar la actualización
    update_all_files(template_files, ".", "template/db/data/hospital.db")
    print("The files have been successfully updated.")
