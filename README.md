# Financial Data Pipeline

A professional data engineering repository for managing financial data pipelines.

## Project Structure

- **`src/`**: Python source code for the pipeline.
  - `ingestion/`: Scripts for extracting data from APIs and sources.
  - `processing/`: Business logic and data transformation scripts.
  - `utils/`: Shared helper functions and logging.
- **`sql/`**: SQL scripts for direct database manipulation.
  - `ddl/`: Table creation and schema definitions.
  - `dml/`: Data manipulation and seed scripts.
  - `views/`: SQL view definitions.
- **`dbt_project/`**: Core dbt transformation layer.
- **`dashboards/`**: Visualization definitions and assets (Metabase, Superset, etc.).
- **`data/`**: Local data storage for development (Git ignored).
  - `raw/`: Unprocessed landing zone.
  - `processed/`: Intermediate cleaned data.
  - `gold/`: Analytics-ready datasets.
- **`config/`**: Configuration files (YAML, JSON).
- **`tests/`**: Unit and integration tests.
- **`notebooks/`**: Exploratory data analysis (EDA).
- **`docs/`**: Project documentation.

## Setup

1. Create a virtual environment: `python -m venv .venv`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure your `.env` file.
