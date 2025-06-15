# Spending Analyser

## :chart_with_upwards_trend: Project Overview
**Spending Analyser** is a personal finance tool which helps you better understand your finances, especially your spending. It works by ingesting a `.csv` of your bank statement, writting it to a database and exposing the data as an API. The future goal of the project will be to use that API to perform analysis, create views and charts, catagorise, filter and understand your spending.

### :bank: Currently Supported Bank Statements
Monzo

## :wrench: Current Features
- `.csv` ingestion for Monzo bank statements
- Parsing of the stements into transactions
- Storage of transactions in a local database
- ReSTful API to access transactions

## :building_construction: Future Features
- Support for more bank statements

## :open_file_folder: Project Structure
```plaintext
│
├── app/                                # Core application logic
│   ├── models/                         # Database models
│   │   └── transaction.py              # Transaction model
│   ├── api.py                          # API endpoints
│   ├── database.py                     # Database connection
│   └── ingest.py                       # Ingestion logic
│
├── test
│   └── unit/
│       ├── model/
│       │    └── test_transaction.py    # Unit tests for Transaction model
│       ├── test_api.py                 # Unit tests for API
│       ├── test_database.py            # Unit tests for Database
│       └── test_ingest.py              # Unit tests for Ingestion
│
├── .gitignore                          # Files to ignore in git
├── README.md                           # Project documentation
├── main.py                             # Entry point for the application
├── pytest.ini                          # Pytest configuration
├── requirements.txt                    # Python dependencies
└── setup.py                            # Setup script for packaging

```

## :rocket: Getting Started

### :checklist: Prerequisites

- Python 3.11
- pip (Python package installer)
- `venv` (optional but recommended for virtual environments)
- `terraform` (for deployment)

### :package: Installation

1. Clone the repository:
```bash
# Clone the repository
git clone https://github.com/yourusername/spending_analyser.git
cd spending_analyser

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt
```

### :test_tube: Running the Tests

To run the tests, ensure you have `pytest` installed (it should be in `requirements.txt`), navigate to the root directory and then execute:

```bash
pytest
```

### :hammer_and_wrench: Running the Application

#### :hut: Local
Create the local database file with:

```bash
python setup.db
```
This should create a `banking.db` file in the root directory. This is your local DB.

Next, run the ingestion with a sample Monzo CSV statement file:

```bash
python -c "from app.ingest import ingest_statement_csv; ingest_statement_csv('./test/test_data/obfuscated_live_files/statement_1_month_10_rows.csv')"
```

Finally, run the application:

```bash
python main.py
```

You can now access the API at `http://localhost:8000/transactions`.

### :cloud: Deployment

For deployment, you can use Terraform to set up the infrastructure. Ensure you have `terraform` installed and configured. Then run:

```bash
cd infra
terraform init
terraform apply
```
