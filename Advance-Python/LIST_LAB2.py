# 1.
# You have a list of employee records, and you need to create a new list that contains
# the names of employees who work in the 'Sales' department, all in uppercase

# employees = [
#                   {"name": "John Doe", "department": "Sales"},
#                   {"name": "Jane Smith", "department": "Marketing"},
#                   {"name": "Emily Johnson", "department": "Sales"},
#                   {"name": "Michael Brown", "department": "HR"}
#             ]

employees = [
    {"name": "John Doe", "department": "Sales"},
    {"name": "Jane Smith", "department": "Marketing"},
    {"name": "Emily Johnson", "department": "Sales"},
    {"name": "Michael Brown", "department": "HR"}
]

sales_person_list = [emp["name"].upper() 
                     for emp in employees
                        if emp["department"] == "Sales"]

print(sales_person_list)


# 2.
# You have a list of email addresses and you want to extract the domain part (the part
# after '@') from each email address.

# emails = [
# "alice@example.com",
# "bob@sample.org",
# "charlie@mydomain.net"

emails = ["alice@example.com","bob@sample.org","charlie@mydomain.net"]
domains = []

for email in emails:
    # TO CHECK ONE LIST ELEMENT END OR NOT
    capaturing = False
    domain = ""
    for ch in email:
        if capaturing:
            domain += ch
        if ch == "@":
            capaturing = True
    domains.append(domain)

print(domains)