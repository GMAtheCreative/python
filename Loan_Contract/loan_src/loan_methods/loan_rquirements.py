from loan_methods.loan_user import User


class LoanContract:
    def __init__(self, user: User,loan_amount :int, yrl_loan_period :int):
        self.user = user
        self.loan_amount = loan_amount
        self.loan_period = yrl_loan_period
        self.interest_rate = 0.12
        self.months = yrl_loan_period * 12


    def monthly_payment(self):
        numerator = self.loan_amount * self.interest_rate
        denominator = 1-(1-(1+ self.months) ** self.months)
        return numerator / denominator

    def total_payment(self):
        return self.monthly_payment() * self.months
