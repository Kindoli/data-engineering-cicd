
from src.transform import clean_employees


def test_calculates_bonus():
    employees = [{"name": "Alice", "salary": 1000}]

    result = clean_employees(employees)

    assert result[0]["bonus"] == 100


def test_removes_invalid_salaries():
    employees = [
        {"name": "Alice", "salary": 1000},
        {"name": "Bob", "salary": 0},
        {"name": "Carol", "salary": None},
    ]

    result = clean_employees(employees)

    assert len(result) == 1
    assert result[0]["name"] == "Alice"
    
def test_employee_ids_are_unique():
    employees = [
        {"employee_id": 1, "salary": 1000},
        {"employee_id": 2, "salary": 2000},
    ]

    ids = [employee["employee_id"] for employee in employees]

    assert len(ids) == len(set(ids))


def test_does_not_modify_input():
    employees = [{"name": "Alice", "salary": 1000}]

    clean_employees(employees)

    assert "bonus" not in employees[0]
