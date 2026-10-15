def clean_employees(employees):
    """Remove invalid salary records and calculate a 10% bonus."""
    cleaned = []

    for employee in employees:
        salary = employee.get("salary")

        if salary is None or salary <= 0:
            continue

        record = employee.copy()
        record["bonus"] = round(salary * 0.10, 2)
        cleaned.append(record)

    return cleaned