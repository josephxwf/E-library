
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

    def read(self):
        self.NumOfRead += 1

    def cover_page(self):
        self.readcoverpage = ""

    def summary(self):
        self.readsummary = ""

    def clock(self):
        self.time = ""
        #timer for book reading durations

    def book_reviews(self, count):
        self.count = count

    def book_rating(self, rate):
        self.rate = 0 #initialize the rating to 0

    def remove_book(self):
        self.bookcallnumber = ""
