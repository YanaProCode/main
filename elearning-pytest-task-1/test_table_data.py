import pytest

def test_table_data(table_cursor):
    table_cursor.execute('select id, name from items')
    result = table_cursor.fetchall()
    assert result == [(1, "books")], f"Expected [(1, 'books')] but got {result}"

