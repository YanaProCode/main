
from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
      # Apply all filters
    for filter_func in filters:
        data = filter_func(data)
    # Apply column selection
    return selector(data)


def select(*columns: str) -> ModifierFunc:
    def inner(data: DataType) -> DataType:
        return [{col: row[col] for col in columns} for row in data]
    return inner

def field_filter(column: str, *values: Any) -> ModifierFunc:
    values_set = set(values)  # Use a set for more faster lookups
    def inner(data: DataType) -> DataType:
        return [row for row in data if row[column] in values_set]
    return inner




def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()

friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]



