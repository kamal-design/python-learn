import unittest

import pandas as pd

from data_pipeline_helper.cleaning import (
    drop_missing_rows,
    fill_missing_values,
    normalize_column_names,
    remove_duplicates,
)


class CleaningTests(unittest.TestCase):
    def test_normalize_column_names_does_not_change_input(self):
        original = pd.DataFrame({" Customer Name ": ["Kamal"], "Order-Total": [100]})

        cleaned = normalize_column_names(original)

        self.assertEqual(list(cleaned.columns), ["customer_name", "order_total"])
        self.assertEqual(list(original.columns), [" Customer Name ", "Order-Total"])

    def test_remove_duplicates_resets_index(self):
        data = pd.DataFrame({"name": ["Kamal", "Kamal", "Anita"]})

        cleaned = remove_duplicates(data)

        self.assertEqual(cleaned["name"].tolist(), ["Kamal", "Anita"])
        self.assertEqual(cleaned.index.tolist(), [0, 1])

    def test_fill_missing_values(self):
        data = pd.DataFrame({"city": [None, "Chennai"]})

        cleaned = fill_missing_values(data, {"city": "Unknown"})

        self.assertEqual(cleaned["city"].tolist(), ["Unknown", "Chennai"])

    def test_drop_missing_rows(self):
        data = pd.DataFrame({"name": ["Kamal", None], "city": ["Chennai", "Pune"]})

        cleaned = drop_missing_rows(data, subset=["name"])

        self.assertEqual(len(cleaned), 1)
        self.assertEqual(cleaned.iloc[0]["name"], "Kamal")


if __name__ == "__main__":
    unittest.main()
