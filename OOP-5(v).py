class Balloon:
    # PRIVATE Health : INTEGER
    # PRIVATE Colour, DefenceItem : STRING

    def __init__(self, DefenseItemPP, ColourPP):

        self.Health = 100
        self.Defense = DefenseItemPP
        self.Colour = ColourPP

    def GetDefenseItem(self):
        return self.Defense

    def ChangeHealth(self, RecoverHealth):
        self.Health = self.Health + int(RecoverHealth)

    def CheckHealth(self):
        if self.Health <= 0:
            return True
        else:
            return False


UserDefence = input("Enter the Defence Item: ")
UserColour = input("Enter your Colour: ")

Balloon1 = Balloon(UserColour, UserDefence)


def Defend(BalloonObject):
    strength = int(input("Enter the Balloon's strength: "))
    BalloonObject.ChangeHealth(-strength)
    print("Your Current Defence is: ", BalloonObject.GetDefenseItem)

    if BalloonObject.CheckHealth == True:
        print("No Health left, Defence didn't work")
    else:
        print("Health remains, Defence worked")

    return BalloonObject


Balloon1 = Defend(Balloon1)