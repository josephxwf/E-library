

class User(object):
    def __init__(self):
        self.username = ""
        self.password = ""
        self.superUser = False
        self.point = 0
        self.readingHistory = []

    def __init__(self, username, password,):
        self.username = username
        self.password = password
        self.superUser = False
        self.point = 0
        self.readingHistory = []


    def setReadingHistory(self,list):
        self.readingHistory = list

