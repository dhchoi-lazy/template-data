## Overview

This template is designed to streamline the process of collecting, processing, and serving data. The project includes:

- Web crawlers for data collection
- Data processing pipelines for cleaning and transformation
- Database integration for data storage
- FastAPI endpoints for data access

## Project Structure

```
project/
│
├── data/                        # Data storage
│   ├── raw/                     # Raw scraped data
│   ├── processed/               # Processed data
│   └── tmp/                     # Temporary data
│
├── logs/                        # Log files directory
│
├── notebooks/                   # Jupyter notebooks for only exploration
│   ├── crawling/                # Crawling experiments
│   ├── processing/              # Data processing experiments
│   └── analysis/                # Data analysis and visualization
│
├── src/
│   ├── __init__.py              # Make src a proper package
│   ├── utils/                   # Shared utilities
│   │   ├── __init__.py
│   │   ├── config.py            # Configuration utilities
│   │   └── logging.py           # Logging setup
│   │
│   ├── crawler/
│   │   ├── __init__.py
│   │   ├── spiders/
│   │   └── utils/
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── cleaning.py
│   │   ├── transform.py
│   │   └── validate.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   ├── schema.py
│   │   ├── db.py
│   │
│   └── api/
│       ├── __init__.py
│       ├── routes.py
│       └── server.py
│
├── scripts/                     # Utility scripts
│   ├── crawl.py                 # Script to run crawlers
│   ├── process.py               # Script to process data
│   └── serve.py                 # Script to start FastAPI server
│
├── tests/                       # Basic tests
│   ├── test_crawler.py
│   ├── test_processing.py
│   └── test_api.py
│
├── config.yaml                  # Main configuration file
├── README.md                    # Project documentation
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore rules
├── .python-version              # Python version
├── pyproject.toml               # uv dependency manager
├── uv.lock                      # uv dependency lock file
└── RESEARCH.md                  # Research methodology and findings

```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dhchoi-lazy/template-data.git
   cd template-data
   ```

2. Set up the environment using uv:

   ```bash
   uv sync
   ```

3. Restart your shell or terminal to ensure the environment is properly activated.

## Usage

### Data Crawling

To run the data crawlers:

```bash
python scripts/crawl.py
```

The crawler will use the settings defined in the `config.yaml` file.

### Data Processing

To process the collected data:

```bash
python scripts/process.py
```

Processing parameters are configured in the `config.yaml` file.

### API Server

To start the FastAPI server:

```bash
python scripts/serve.py
```

The FastAPI server will be available at the host and port specified in the `config.yaml` file.

## Configuration

The project uses a central configuration file `config.yaml` for managing settings. Example configuration:

```yaml
# Example configuration
crawler:
  user_agent: "Web Crawler 1.0"
  rate_limit: 1 # requests per second
  sources:
    target_source:
      url: "https://example.com"

database:
  type: "postgresql"
  host: "localhost"
  port: 5432
  user: "postgres"
  password: "postgres"
  database: "postgres"

api:
  host: "0.0.0.0"
  port: 8000
  debug: false
```

## Development

For development work:

1. Create a new branch for your feature:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and run tests:

   ```bash
   python -m pytest
   ```

## Testing

Run the test suite:

```bash
python -m pytest
```

For specific test files:

```bash
python -m pytest tests/test_crawler.py
```
