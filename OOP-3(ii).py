class Picture:

    # PRIVATE Description : STRING
    # PRIVATE Width : INTEGER
    # PRIVATE Height : INTEGER
    # PRIVATE FrameColour : STRING

    def __init__(self, Des, W, H, C):
        self.Description = Des
        self.Width = W
        self.Height = H
        self.Colour = C

    def GetDescription(self):
        return self.Description

    def GetHeight(self):
        return self.Height

    def GetWidth(self):
        return self.Width

    def GetColour(self):
        return self.Colour

    def SetDescription(self, Des):
        self.Description = Des
