-- Snowflake Setup Script
-- Databases for Raw Landing and Data Warehouse

-- Create Databases
CREATE DATABASE IF NOT EXISTS FIN_PROD_RAW 
    COMMENT = 'Raw landing zone for incoming financial data';

CREATE DATABASE IF NOT EXISTS FIN_PROD_DWH 
    COMMENT = 'Production Data Warehouse for modeled financial data';

-- Create Landing Schema in RAW
USE DATABASE FIN_PROD_RAW;
CREATE SCHEMA IF NOT EXISTS LANDING;

-- Create Landing Table for JSON Market Data
-- Using VARIANT column for flexible JSON storage
CREATE OR REPLACE TABLE FIN_PROD_RAW.LANDING.MARKET_DATA_JSON (
    raw_content         VARIANT,
    metadata_filename   STRING,
    metadata_row_number NUMBER,
    ingested_at         TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
)
COMMENT = 'Landing table for raw JSON market data from external APIs';

-- (Optional) Create a stage for loading files if needed
-- CREATE OR REPLACE STAGE FIN_PROD_RAW.LANDING.STG_MARKET_DATA;
