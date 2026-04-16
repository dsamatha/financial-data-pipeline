# financial-data-pipeline

graph LR
    %% Data Sources Layer
    subgraph Data_Sources ["1. Data Acquisition"]
        API[API: Financial Market Data<br/>or Kaggle Fin Dataset]
    end

    %% Ingestion Layer
    subgraph Ingestion ["2. Ingestion (Python ETL)"]
        Extraction[Python Extract Script<br/>'raw_data_loader.py']
    end

    %% Cloud Storage / Landing Zone
    subgraph Landing_Zone ["3. Landing Zone (AWS)"]
        S3_Bucket[AWS S3 Bucket<br/>s3://project-raw-data]
    end

    %% Data Warehouse Layer (Snowflake)
    subgraph Snowflake_Warehouse ["4. Modern Data Warehouse (Snowflake)"]
        
        %% Database Structure
        subgraph Databases
            DB_RAW[DB_PROD_RAW<br/>(Schema: MARKET)]
            DB_TRANSFORM[DB_PROD_DWH<br/>(Schema: ANALYTICS)]
        end

        %% Process Tools inside Snowflake
        SP[Snowpipe<br/>Auto-Load]
        SF_Warehouse_Compute[Snowflake Virtual<br/>Warehouse]
    end

    %% Transformation & Orchestration Layer
    subgraph Transformation_Layer ["5. Transformation (dbt)"]
        DBT[dbt Cloud / dbt Core<br/>SQL Models]
    end

    %% Analytics & BI Layer
    subgraph Analytics_Layer ["6. Analytics & BI"]
        PBI[Power BI Desktop/Service]
    end

    %% Orchestration (Github Actions is good for beginners)
    subgraph Orchestration ["0. Orchestration"]
        G_Actions[Github Actions]
    end

    %% Data Flow Connections
    Data_Sources --> Ingestion
    Ingestion --> Landing_Zone
    
    %% Snowflake Loading
    Landing_Zone --> SP --> DB_RAW
    
    %% Transformation Loop
    DB_RAW <--> DBT
    DBT --> DB_TRANSFORM
    
    %% Link Compute
    SF_Warehouse_Compute -. Applies Compute .-> DB_RAW
    SF_Warehouse_Compute -. Applies Compute .-> DB_TRANSFORM
    
    %% Final Consumption
    DB_TRANSFORM --> Analytics_Layer

    %% Orchestration triggers (Optional but good)
    G_Actions -. Triggers ETL .-> Ingestion
    G_Actions -. Triggers Transformations .-> DBT

    %% Styles for readability
    classDef storage fill:#fff,stroke:#333,stroke-width:1px;
    classDef cloud fill:#ff9900,stroke:#fff,stroke-width:2px,color:white;
    classDef sf fill:#29b5e8,stroke:#fff,stroke-width:2px,color:white;
    classDef bi fill:#f2c811,stroke:#333,stroke-width:1px,color:black;
    
    class S3_Bucket cloud;
    class DB_RAW,DB_TRANSFORM,SP,SF_Warehouse_Compute sf;
    class PBI bi;
