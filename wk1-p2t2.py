class TechnicalSystem:
    def __init__(self):
        self.reports = {}
        self.rules = []

    def add_report(self, category, description):
        self.reports[category] = description

    def add_rules(self, condition, solution):
        self.rules.append({"condition": condition, "solution": solution})

    def troubleshoot(self):
        for rule in self.rules:
            conditions_met = all(self.reports[condition] for condition in rule["conditions"])

            if conditions_met:
                return f"The patient is diagnosed with: {rule['solution']}"

        return "No specific solution based on the reported issue."

# Example Usage:
tech_system = TechnicalSystem()
tech_system.add_report("performance","Device is frozen")
tech_system.add_report("connectivity", "my internet is not working")

tech_system.add_rules("performance", "restart your device")
tech_system.add_rules("connectivity", "check wired connection")

result = tech_system.troubleshoot()
print(result)