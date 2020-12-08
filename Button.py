class Button:
    def __init__(self, x, y, w, h, buttonText):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.buttonText = buttonText
        self.textSize = textSize(23)
    
    def show(self):
        rectMode(CENTER)
        fill(255)
        rect(self.x, self.y, self.w, self.h)
        fill(0)
        text(self.buttonText, self.x - 27, self.y + 5, 10)
    
    #Check of de muis over de button hovered
    def mouseOverButton(self):
        if mouseX > self.x - self.w / 2 and mouseX < self.x + self.w:
            if mouseY > self.y - self.h / 2 and mouseY < self.y + self.h:
                return True
