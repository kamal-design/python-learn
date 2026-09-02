# Data Pipeline Helper

`data_pipeline_helper` is a small learning project for cleaning pandas
DataFrames, running CSV ETL pipelines, and creating parameterized SQL statements.

The PyPI distribution name is `data-pipeline-helper-kamal`, while the Python
import name is `data_pipeline_helper`. Before publishing, replace `kamal` with a
unique PyPI name if this distribution name is unavailable.

## Project structure

```text
DataCleaning/
├── data_pipeline_helper/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── etl.py
│   ├── sql_builder.py
│   └── utils.py
├── examples/
│   ├── customers.csv
│   └── example_usage.py
├── tests/
│   ├── __init__.py
│   ├── test_cleaning.py
│   ├── test_etl.py
│   └── test_sql_builder.py
├── pyproject.toml
├── setup.py
├── README.md
├── LICENSE
└── requirements.txt
```

## Install locally

From the `DataCleaning` folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Example

```python
from data_pipeline_helper import run_csv_pipeline

cleaned = run_csv_pipeline(
    "input.csv",
    "output/clean.csv",
    fill_values={"city": "Unknown"},
    required_columns=["customer_name", "city"],
)

print(cleaned)
```

Run the included example after installing the package:

```bash
python examples/example_usage.py
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Build and publish to PyPI

1. Create accounts on [TestPyPI](https://test.pypi.org/) and
   [PyPI](https://pypi.org/), then create API tokens.
2. Update the project URLs and confirm that the name in `pyproject.toml` is
   unique.
3. Install the publishing tools and build the distributions:

   ```bash
   python -m pip install --upgrade build twine
   python -m build
   python -m twine check dist/*
   ```

4. Upload to TestPyPI first:

   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

5. Test installation in a fresh virtual environment, then publish to PyPI:

   ```bash
   python -m twine upload dist/*
   ```

When Twine asks for a username, enter `__token__`. Use your API token as the
password. Never store a PyPI token in this repository.

PyPI releases cannot be overwritten. Increase the version in both
`pyproject.toml` and `data_pipeline_helper/__init__.py` for every new release.
