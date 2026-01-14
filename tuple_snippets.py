#1. Given list of employee records: (emp_id, name, dept, manager_id, salary, join_date)
# Build tuple tree structure (recursive nested tuples) representing company hierarchy starting from CEO (manager_id is None). Each node: (emp_data_tuple, (child1, child2, ...))

#generating required sample data first
employees = [
    (101, "Alice",   "CEO",       None,  500000, "2020-01-15"),
    (201, "Bob",     "CTO",       101,   320000, "2020-06-01"),
    (202, "Clara",   "CFO",       101,   310000, "2021-03-10"),
    (301, "David",   "Engineering",201, 180000, "2021-09-05"),
    (302, "Emma",    "Engineering",201, 165000, "2022-02-18"),
    (303, "Frank",   "Engineering",201, 170000, "2022-11-01"),
    (401, "Grace",   "Finance",    202, 145000, "2021-12-01"),
    (402, "Henry",   "Finance",    202, 138000, "2023-04-20"),
]


def build_hierarchy(employees):
    #Making a dictionary to find employee by ID quickly
    emp_by_id = {}
    for emp in employees:
        emp_id = emp[0]  # Assuming employee = (id, name, salary, manager_id)
        emp_by_id[emp_id] = emp

    # Making dictionary for manager -> list of direct reports
    children = {}
    for emp in employees:
        manager_id = emp[3]
        if manager_id is not None:
            if manager_id not in children:
                children[manager_id] = []
            children[manager_id].append(emp)

    #defining function to build the tree node
    def build_node(emp_id):
        record = emp_by_id[emp_id]
        # Get direct reports, or empty list if none
        direct_reports = children.get(emp_id, [])
        # Sorting by name (emp[1])
        direct_reports.sort(key=lambda e: e[1])
        # Building child nodes recursively
        child_nodes = []
        for child_emp in direct_reports:
            child_nodes.append(build_node(child_emp[0]))
        child_nodes = tuple(child_nodes)  # Convert to tuple
        return (record, child_nodes)

    # Finding the CEO (no manager)
    ceo_id = None
    for emp in employees:
        if emp[3] is None:
            ceo_id = emp[0]
            break

    # Building and returning  tree from CEO
    return build_node(ceo_id)


tree = build_hierarchy(employees)
print(tree)