# 🟣 What is Synthea?

Synthea is a synthetic patient data generator that simulates realistic medical records. It is useful for training machine learning models in the healthcare field.


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

>Data updated as of 2024-10-28T02:16:15.378831 with version 1. 