# The following is a list (iterable) of the scores of 10 students in a Chemistry exam.
# Let's filter out those who passed with scores more than 75...using filter.

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def is_a_student(score):
    return score > 75


print(list(filter(is_a_student, scores)))
