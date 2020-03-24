students = [
    {"name": "Bill", "grade": 90},
    {"name": "Joe", "grade": 80},
    {"name": "Bob", "grade": 70},
    {"name": "Ted", "grade":60},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

    print((name) + " has a grade of " + str(grade) +".")