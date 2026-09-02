import unittest

from data_pipeline_helper.sql_builder import build_insert, build_select


class SqlBuilderTests(unittest.TestCase):
    def test_build_insert_returns_sql_and_parameters(self):
        sql, parameters = build_insert(
            "customers", {"name": "Kamal", "city": "Chennai"}
        )

        self.assertEqual(
            sql,
            "INSERT INTO customers (name, city) VALUES (%s, %s)",
        )
        self.assertEqual(parameters, ("Kamal", "Chennai"))

    def test_build_select_with_filters(self):
        sql, parameters = build_select(
            "customers",
            columns=["name", "city"],
            where={"city": "Chennai"},
            placeholder="?",
        )

        self.assertEqual(sql, "SELECT name, city FROM customers WHERE city = ?")
        self.assertEqual(parameters, ("Chennai",))

    def test_rejects_unsafe_identifier(self):
        with self.assertRaises(ValueError):
            build_select("customers; DROP TABLE customers")

    def test_rejects_empty_placeholder(self):
        with self.assertRaises(ValueError):
            build_select("customers", where={"city": "Chennai"}, placeholder="")


if __name__ == "__main__":
    unittest.main()
