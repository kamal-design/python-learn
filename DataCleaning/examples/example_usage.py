"""Example: clean a CSV file and build a safe SQL statement."""

from pathlib import Path

from data_pipeline_helper import build_insert, run_csv_pipeline


project_directory = Path(__file__).resolve().parents[1]
input_file = project_directory / "examples" / "customers.csv"
output_file = project_directory / "examples" / "clean_customers.csv"

cleaned_data = run_csv_pipeline(
    input_file,
    output_file,
    fill_values={"city": "Unknown"},
    required_columns=["customer_name", "city"],
)

statement, parameters = build_insert(
    "customers",
    {"name": cleaned_data.iloc[0]["customer_name"], "city": cleaned_data.iloc[0]["city"]},
)

print(cleaned_data)
print(statement)
print(parameters)
