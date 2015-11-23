
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

    book_count = 0 #shared variable by all objects of type Book. Total number of books in catalog

    #def __init__(self, callnumber):
#       self.callnumber = callnumber
 #       Book.book_count += 1

    def cover_page(self):

    def summary(self):

    def clock(self):
        #timer for book reading durations

    def points_needed(self):

    def book_reviews(self, count):
        self.count = 0 #initially the number of reviews are 0

    def book_rating(self, rate):
        self.rate = 0 #initialize the rating to 0

    def weight(self):
        #weight of each review and rating for this book

    def remove_book(self):
