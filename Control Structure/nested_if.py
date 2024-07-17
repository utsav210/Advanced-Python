# Function to determine loan eligibility based on multiple criteria
def loan_eligibility(credit_score, income, existing_debt, employment_status, age):
    # Check if credit score is excellent
    if credit_score >= 750:
        # Nested condition: Check if income is sufficient
        if income >= 50000:
            # Further nested condition: Check existing debt
            if existing_debt < 20000:
                # Further nested condition: Check employment status
                if employment_status == "employed":
                    # Further nested condition: Check age
                    if 25 <= age <= 65:
                        print("Loan Approved: Excellent credit score, sufficient income, low debt, employed, and within eligible age range.")
                    else:
                        print("Loan Denied: Excellent credit score, sufficient income, low debt, employed, but age not within eligible range.")
                else:
                    print("Loan Denied: Excellent credit score, sufficient income, low debt, but not employed.")
            else:
                print("Loan Denied: Excellent credit score, sufficient income, but high existing debt.")
        else:
            print("Loan Denied: Excellent credit score, but insufficient income.")
    # Check if credit score is good
    elif 700 <= credit_score < 750:
        if income >= 60000:
            if existing_debt < 15000:
                if employment_status == "employed" or employment_status == "self-employed":
                    if 30 <= age <= 60:
                        print("Loan Approved: Good credit score, sufficient income, low debt, employed or self-employed, and within eligible age range.")
                    else:
                        print("Loan Denied: Good credit score, sufficient income, low debt, employed or self-employed, but age not within eligible range.")
                else:
                    print("Loan Denied: Good credit score, sufficient income, low debt, but not employed or self-employed.")
            else:
                print("Loan Denied: Good credit score, sufficient income, but high existing debt.")
        else:
            print("Loan Denied: Good credit score, but insufficient income.")
    # Check if credit score is fair
    elif 650 <= credit_score < 700:
        if income >= 70000:
            if existing_debt < 10000:
                if employment_status == "self-employed":
                    if 35 <= age <= 55:
                        print("Loan Approved: Fair credit score, sufficient income, low debt, self-employed, and within eligible age range.")
                    else:
                        print("Loan Denied: Fair credit score, sufficient income, low debt, self-employed, but age not within eligible range.")
                else:
                    print("Loan Denied: Fair credit score, sufficient income, low debt, but not self-employed.")
            else:
                print("Loan Denied: Fair credit score, sufficient income, but high existing debt.")
        else:
            print("Loan Denied: Fair credit score, but insufficient income.")
    # If credit score is poor
    else:
        print("Loan Denied: Poor credit score.")

# Example usage
if __name__ == "__main__":
    applicants = [
        {'credit_score': 780, 'income': 55000, 'existing_debt': 10000, 'employment_status': 'employed', 'age': 30},
        {'credit_score': 720, 'income': 65000, 'existing_debt': 5000, 'employment_status': 'self-employed', 'age': 45},
        {'credit_score': 680, 'income': 75000, 'existing_debt': 2000, 'employment_status': 'self-employed', 'age': 40},
        {'credit_score': 640, 'income': 45000, 'existing_debt': 15000, 'employment_status': 'unemployed', 'age': 50},
    ]

    for applicant in applicants:
        print(f"\nEvaluating applicant: {applicant}")
        loan_eligibility(applicant['credit_score'], applicant['income'], applicant['existing_debt'], applicant['employment_status'], applicant['age'])
