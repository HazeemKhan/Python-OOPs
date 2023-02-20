class Sword:
    # PRIVATE x_value : INTEGER
    # PRIVATE y_value : INTEGER
    # PRIVATE Type :STRING

    def __init__(self, X, Y, T):
        self.x_value = X
        self.y_value = Y
        self.Type = T

    def displayType(self):
        return self.type


DarkSword = Sword(35, 46, "Katana")

temp = DarkSword.displayType()
print(temp)
