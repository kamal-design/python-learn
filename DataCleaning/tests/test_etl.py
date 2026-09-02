from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import pandas as pd

from data_pipeline_helper.etl import run_csv_pipeline, transform_data


class EtlTests(unittest.TestCase):
    def test_transform_data_runs_cleaning_steps(self):
        data = pd.DataFrame(
            {
                "Customer Name": ["Kamal", "Kamal", "Anita"],
                "City": ["Chennai", "Chennai", None],
            }
        )

        transformed = transform_data(
            data,
            fill_values={"city": "Unknown"},
            required_columns=["customer_name", "city"],
        )

        self.assertEqual(len(transformed), 2)
        self.assertEqual(transformed["city"].tolist(), ["Chennai", "Unknown"])

    def test_run_csv_pipeline_writes_output(self):
        with TemporaryDirectory() as temporary_directory:
            temporary_path = Path(temporary_directory)
            input_file = temporary_path / "input.csv"
            output_file = temporary_path / "output" / "clean.csv"
            pd.DataFrame({"Name": ["Kamal", "Kamal"]}).to_csv(input_file, index=False)

            transformed = run_csv_pipeline(input_file, output_file)

            self.assertTrue(output_file.is_file())
            self.assertEqual(transformed["name"].tolist(), ["Kamal"])


if __name__ == "__main__":
    unittest.main()
