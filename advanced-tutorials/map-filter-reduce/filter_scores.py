# The following is a list of the scores of 10 students in a Chemistry exam
all_scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
print("all_scores    = %s" % all_scores)


# Find out those who passed with scores more than 75
def is_passed(score):
    return score > 75


passed_scores = list(filter(is_passed, all_scores))
print("passed_scores = %s" % passed_scores)
