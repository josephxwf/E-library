
class Book():
    def __init__(self):
        self.title = ""
        self.author = ""
        self.description = ""
        self.requestPoint = 0
        self.type = ""
        self.NumOfRead = 0

    def __init__(self, title, requestPoint):
        self.title = title
        self.author = ""
        self.description = ""
        self.requestPoint = requestPoint
        self.type = ""
        self.NumOfRead = 0

    # def __lt__(self, other):
    #     return self.NumOfRead < other.NumOfRead

    # def __init__(self, title, requestPoint, author, description, type):
    #     self.title = title
    #     self.author = author
    #     self.description = description
    #     self.requestPoint = requestPoint
    #     self.type = type
    #     self.NumOfRead = 0


    def read(self):
        self.NumOfRead += 1
