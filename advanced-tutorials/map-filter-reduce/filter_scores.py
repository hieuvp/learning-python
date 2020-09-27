# The following is a list of the scores of 10 students in a Chemistry exam
all_students = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


# Find out those who passed with scores more than 75
def is_passed(score):
    return score > 75


passed_students = list(filter(is_passed, all_students))

print("all_students    = %s" % all_students)
print("passed_students = %s" % passed_students)
