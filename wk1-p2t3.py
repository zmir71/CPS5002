class LoanSystem:
    def __init__(self):
        self.fact = {}
        self.rules = []

    def add_fact(self, types, value):
        if types in self.fact:
            self.fact[types] = value
        else:
            self.fact[types] = value

    def add_rule(self, goal, condition):
        self.rules.append({"goal": goal, "conditions": condition})

    def check_loan_eligibility(self, goal):
        if not all(self.fact.values()):
            return "Incomplete information"
        for rule in self.rules:
            if rule["goal"] == goal:
                conditions_met = all(self.fact[condition] >= threshold for condition, threshold in rule["conditions"].items())
                if conditions_met:
                    return f"The customer is eligible for a {goal} loan."
        return f"The customer is not eligible for a loan"

# Example Usage:
loan_system = LoanSystem()

# Add purchase history
loan_system.add_fact("income", 30000)
loan_system.add_fact("credit_score", 500)

# Define rules for discount eligibility based on overall purchase amount
loan_system.add_rule("mortgage", {'income': 40000, "credit_score": 600})
loan_system.add_rule("business", {'income': 20000, "credit_score": 700})
loan_system.add_rule("personal", {'income': 10000, "credit_score": 450})

# Check discount eligibility
result = loan_system.check_loan_eligibility("mortgage")
print(result)