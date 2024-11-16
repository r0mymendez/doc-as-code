# ¿Qué es Synthea?

Synthea es un generador de datos sintéticos de pacientes que simula registros médicos realistas. Es útil para entrenamiento de modelos de machine learning en el campo de la salud.

```mermaid
mindmap
  root((patients.csv))
    id(Administration)
      careplans.csv
      providers.csv
      supplies.csv
      organizations.csv
    id(Electronic Medical Records)
      id(Conditions)
        allergies.csv
        conditions.csv
        observations.csv
      id(Visit)
        encounters.csv
      id(Drugs)
        medications.csv
      id(procedures)
         procedures.csv
         immunizations.csv
         imaging_studies.csv      
      
```

> Datos actualizados al 2024-10-28T02:16:15.378831 con la version 1
