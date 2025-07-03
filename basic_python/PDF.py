high_income = True
good_credit = False

message = "Grant Loan" if high_income and good_credit else "Not Eligible"
print(message)
