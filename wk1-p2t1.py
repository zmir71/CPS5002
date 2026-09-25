class WeatherExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, result):
        self.rules.append((conditions, result))

    def infer(self):
        for conditions, result in self.rules:
            if all(condition in self.facts for condition in conditions):
                return result
        return "Default"

expert_system = WeatherExpertSystem()
facts = int(input("How many facts would you like to enter?: "))

for count in range(facts):
    user_fact = input("Enter fact: ")
    expert_system.add_fact(user_fact)

expert_system.add_fact("high_temperature")  # Example: High temperature
expert_system.add_fact("low_humidity")  # Example: Low humidity
expert_system.add_rule(["high_temperature", "low_humidity"], "Comfortable")
expert_system.add_rule(["high_wind_speed", "high_humidity"], "Uncomfortable")
expert_system.add_rule(["high_fog", "high_cloudy"], "Uncomfortable")
expert_system.add_rule(["low_wind_speed", "high_humidity"], "Comfortable")

results = expert_system.infer()
print(results)  # Output: Comfortable