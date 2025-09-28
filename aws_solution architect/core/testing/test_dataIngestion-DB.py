import unittest
import pyodbc
from pyodbc_unittest import Dbtest
from DbConn import msSQlconn


CONNECTION_STRING = r'msSQlconn()'


class TestSelect(unittest.TestCase):
    def test_data(self):
        database = Dbtest(CONNECTION_STRING)
        sql = "SELECT 1 AS ONE"
        file_name = "SELECTONE"
        self.assertEqual(
            database.from_db(sql, file_name), database.from_file(file_name)
        )
        database.close()
