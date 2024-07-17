'''
Challange/Task:
1. Write a function grade_classifier that takes a score as an argument.
2. Use conditional statements to classify the score into "A", "B", "C", "D", or "F".
3. Print the grade based on the score.
'''
def grade_classifier(score):
    if score >= 81 and score <= 100:
        grade = "A"
    elif score >= 61 and score <= 80:
        grade = "B"
    elif score >= 41 and score <= 60:
        grade = "C"
    elif score >= 35 and score <= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"The grade for the score: {score} is {grade}")

# This ensures the following code only runs when the script is executed directly
if __name__== "__main__":
    test_scores = [89, 56, 33, 75, 37.5,95]
    for score in test_scores:
        grade_classifier(score)