class Chatbot:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, responses):
        self.rules.append({"condition": condition, "response": responses})


    def apply_rule(self, prompt):
        for r in self.rules:
            if r['condition'] in prompt.lower():
                return r['response']
        return 'Error'

bot = Chatbot()
bot.add_rule("hello",'Hello')
bot.add_rule('goodbye',"Goodbye")
bot.add_rule('can you recommend any movies?', 'Yes I can, can you enter your preferred genre of movie?')
bot.add_rule('horror', 'According to IMD, The Night House, Gretel & Hansel and Scare Me are some great options!')
bot.add_rule('comedy', 'According to IMD, I Want You Back, Palm Springs and Uncle Frank are some great options!')
bot.add_rule('adventure', 'According to IMD, The Bluff, The Weight and Anaconda are some great options!')
bot.add_rule('drama', 'According to IMD, F1:The Movie, Sinners and The Life of Chuck are some great options!')
bot.add_rule('romance', 'According to IMD, The Practical Magic, The Drama and Voicemails for Isabelle are some great options!')
bot.add_rule('thriller', 'According to IMD, Crime 101, The Housemaid and Tuner are some great options!')
bot.add_rule('mystery', 'According to IMD, The Sheep Detectives, Wake Up Dead Man and The End of Oak Street are some great options!')

while True:
    user_input = input('You')
    response = bot.apply_rule(user_input)
    print(response)

    if user_input.lower() == 'goodbye':
        break