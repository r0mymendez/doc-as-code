---
title: Synthea Tables 
icon: material/lightbulb
status: new
tags: [Blue, Medications,Conditions]
---

# 🟣 Synthea Tables

| Tables         | Descriptions                                        |
|---------------|----------------------------------------------------|
| Patients     | Contains demographic and basic medical information.|
| Medications  | Records of prescribed medications.                 |
| Conditions   | Diseases and documented clinical conditions.       |

```mermaid
erDiagram
    PATIENTS ||--o{ CONDITIONS : "has condition"
    PATIENTS ||--o{ MEDICATIONS : "takes medication"
    PATIENTS ||--o{ IMMUNIZATIONS : "receives immunization"

    PATIENTS {
        string Id
        date BIRTHDATE
        date DEATHDATE
        string SSN
        string DRIVERS
        string PASSPORT
        string PREFIX
        string FIRST
        string LAST
        string SUFFIX
        string MAIDEN
        string MARITAL
        string RACE
        string ETHNICITY
        string GENDER
        string BIRTHPLACE
        string ADDRESS
        string CITY
        string STATE
        string COUNTY
        string FIPS
        string ZIP
        float LAT
        float LON
        float HEALTHCARE_EXPENSES
        float HEALTHCARE_COVERAGE
        int INCOME
    }

    CONDITIONS {
        date START
        date STOP
        string PATIENT
        string ENCOUNTER
        string CODE
        string DESCRIPTION
    }

    MEDICATIONS {
        date START
        date STOP
        string PATIENT
        string ENCOUNTER
        string CODE
        string DESCRIPTION
        float BASE_COST
        string PAYER
        float PAYER_COVERAGE
        int DISPENSES
        float TOTALCOST
        string REASONCODE
        string REASONDESCRIPTION
    }

    IMMUNIZATIONS {
        date DATE
        string PATIENT
        string ENCOUNTER
        string CODE
        string DESCRIPTION
        float BASE_COST
    }

```

----

# Example person table
## Person Table
{{table.person}}