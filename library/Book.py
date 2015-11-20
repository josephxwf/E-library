
class Book():
    def __init__(self):
        self.title = ""
        self.author = ""
        self.description = ""
        self.point = 0
        self.type = ""
        self.NumOfRead = 0

    def read(self):
        self.NumOfRead +=1
