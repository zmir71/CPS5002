class FuzzyTemp:
    def __init__(self):
        # Rules list
        self.rules = {
            'fan_on': ['hot','very_hot'],
            'fan_off': ['cold','very_cold','warm'],
            'heater_on': ['cold','very_cold'],
            'heater_off': ['hot','very_hot','warm']
        }

        # Linguistic terms and membership functions
        self.memberships = {
            'very_cold': lambda x: max(0, 1 - abs(x - 0) / 10),
            'cold': lambda x: max(0, 1 - abs(x - 10) / 10),
            'warm': lambda x: max(0, 1 - abs(x - 20) / 10),
            'hot': lambda x: max(0, 1 - abs(x - 30) / 10),
            'very_hot': lambda x: max(0, 1 - abs(x - 40) / 10)
        }

    def __fuzzify(self, temp_value):
        # Fuzzification: Calculate membership degrees for linguistic terms
        fuzz = {term: func(temp_value) for term, func in self.memberships.items()}
        return fuzz


    def __infer(self, antecedents):
        # Rule Evaluation: Apply rules to determine the consequent
        heater_degree_on = max(antecedents[term] for term in self.rules['heater_on'])
        fan_degree_on = max(antecedents[term] for term in self.rules['fan_on'])
        heater_degree_off = max(antecedents[term] for term in self.rules['heater_off'])
        fan_degree_off = max(antecedents[term] for term in self.rules['fan_off'])
        return {'heater_on': heater_degree_on, 'fan_on': fan_degree_on, 'heater_off': heater_degree_off, 'fan_off': fan_degree_off}


    def __defuzzify(self, consequent):
        # Defuzzification: Choose the consequent with the highest aggregated degree of membership
        if consequent['heater_on'] > consequent['fan_on']:
            return 'Heater On'
        elif consequent['fan_on'] > consequent['heater_on']:
            return 'Fan On'
        elif consequent['heater_off'] > consequent['heater_on']:
            return 'Heater Off'
        elif consequent['fan_off'] > consequent['fan_on']:
            return 'Fan Off'
        elif (consequent['fan_off'] and consequent['heater_off']) > (consequent['fan_on'] or consequent['heater_on']):
            return 'Heater Off' and 'Fan Off'
        else:
            return 'Off'


    def evaluate(self, temperature):
        # Fuzzification for input temperature
        fuzz = self.__fuzzify(temperature)
        # Inference: Apply rules to determine the consequent
        infer_result = self.__infer(fuzz)
        # Defuzzification: Choose the final operation
        return self.__defuzzify(infer_result)

fuzzy = FuzzyTemp()

