class LightFuzzyTemp:
    def __init__(self):
        # Rules list
        self.rules = {
            'brighten': [('low','partial'),('low','full')],
            'maintain': [('medium','partial')],
            'dim': [('high','unoccupied'),('high','partial')]
        }

        # Linguistic terms and membership functions
        self.light_memberships = {
            'low': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'medium': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'high': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }

        self.occupancy_memberships = {
            'unoccupied': lambda x: max(0, 1 - abs(x - 15) / 15) if 0 <= x <= 30 else 0,
            'partial': lambda x: max(0, 1 - abs(x - 50) / 20) if 31 <= x <= 70 else 0,
            'full': lambda x: max(0, 1 - abs(x - 85) / 15) if 71 <= x <= 100 else 0
        }


    def __fuzzify(self, value, membership):
        # Fuzzification: Calculate membership degrees for linguistic terms
        fuzz = {term: func(value) for term, func in membership.items()}
        return fuzz


    def __infer(self, fuzz_light, fuzz_occupancy):
        # Rule Evaluation: Apply rules to determine the consequent
        brighten_degree = max(min(fuzz_light[light], fuzz_occupancy[occupancy]) for light, occupancy in self.rules['brighten'])
        maintain_degree = max(min(fuzz_light[light], fuzz_occupancy[occupancy]) for light, occupancy in self.rules['maintain'])
        dim_degree = max(min(fuzz_light[light], fuzz_occupancy[occupancy]) for light, occupancy in self.rules['dim'])
        return {'brighten': brighten_degree, 'maintain': maintain_degree, 'dim': dim_degree}


    def __defuzzify(self, consequent):
        # Defuzzification: Choose the consequent with the highest aggregated degree of membership
        return max(consequent, key=consequent.get())


    def decision(self, light, occupancy):
        # Fuzzification for input temperature
        fuzz_light = self.__fuzzify(light, self.light_memberships)
        fuzz_occupancy = self.__fuzzify(light, self.occupancy_memberships)
        # Inference: Apply rules to determine the consequent
        infer_result = self.__infer(fuzz_light,fuzz_occupancy)
        # Defuzzification: Choose the final operation
        return self.__defuzzify(infer_result)

fuzzy = LightFuzzyTemp()
test = fuzzy.decision(25,50)
print('System result: ',test, 'for light = 25, occupancy = 50')