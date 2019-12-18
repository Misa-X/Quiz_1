
class Spell:  #Parent class
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name +' '+ self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):  #Child class
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):  #Child class
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

def get_description(self):
    return 'Causes the victim to become confused and befuddled.'

def study_spell(spell):
    print(spell)

#
Spell = Accio()
print(Spell)
Spell.execute()
study_spell(Spell)
study_spell(Confundo())

#Answers:
# a. parent class > class Spell ; child classes > class Accio(Spell) and class Confundo(Spell)
# b. The code prints out : Accio
#                          Summoning Charm Accio
#                          No description
#                          Confundus Charm Confundo
#                          No description
# c. The first description method is called
# d. we need to add > print(Spell)