class FuzzyGame:
    def __init__(self):
        # Fuzzy rules
        self.rules = {
            'attack': [('high', 'close'), ('high', 'medium')],
            'defend': [('medium', 'close'), ('low', 'medium')],
            'run': [('low', 'close'), ('medium', 'far')]
        }

        # Membership functions for energy (Low, Medium, High)
        self.energy_memberships = {
            'low': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'high': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

        # Membership functions for proximity (Close, Medium, Far)
        self.proximity_memberships = {
            'close': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'far': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

    def __fuzzify(self, value, memberships):
        # Fuzzification: Calculate membership degrees for each linguistic term
        return {term: func(value) for term, func in memberships.items()}

    def __infer(self, fuzzified_energy, fuzzified_proximity):
        # Inference: Apply rules based on fuzzified values of energy and proximity
        attack_degree = max(min(fuzzified_energy[energy], fuzzified_proximity[proximity]) for energy, proximity in self.rules['attack'])
        defend_degree = max(min(fuzzified_energy[energy], fuzzified_proximity[proximity]) for energy, proximity in self.rules['defend'])
        run_away_degree = max(min(fuzzified_energy[energy], fuzzified_proximity[proximity]) for energy, proximity in self.rules['run'])
        return {'attack': attack_degree, 'defend': defend_degree, 'run': run_away_degree}


    def __defuzzify(self, inferred_actions):
        # Defuzzification: Choose the action with the highest membership degree
        return max(inferred_actions, key=inferred_actions.get)

    def decide(self, energy, proximity):
        # Fuzzification for energy and proximity
        fuzz_energy = self.__fuzzify(energy, self.energy_memberships)
        fuzz_proximity = self.__fuzzify(proximity, self.proximity_memberships)
        # Inference: Apply rules to determine the action
        inferred_actions = self.__infer(fuzz_energy, fuzz_proximity)
        # Defuzzification: Choose the final action
        return self.__defuzzify(inferred_actions)


fuzzy = FuzzyGame()
test = fuzzy.decide(55, 40)
print(f'System result: {test} energy = 55, proximity = 40')