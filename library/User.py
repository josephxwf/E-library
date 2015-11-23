

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


class Visitor:

    def __init__(self):

    def search_book(self):

    def register(self):

class RegisteredUser(Visitor):

    registered_user_count = 0 #total number of users in system

    def __init__(self, name, username, password, points):
        self.name = name
        self.username = username
        self.password = password
        self.points = points
        RegisteredUser.registered_user_count += 1

    def read_book(self):
        #first check if user have enough points to read book
        self.book_callnumber = ""
        self.book_read = False #sets bool to true once user reads the book

    def contribute_book(self):
        self.book_callnumber = "" #assign a unique callnumber to book
        self.ask_points = 0
        self.book = "" #read the book from input file

    def rate_book(self):
        self.book_callnumber = 1
        #first check if user had read the book

    def review_book(self):
        self.book_callnumber = 1
        #first check if user had read the book

    def read_reviews(self):
        self.book_callnumber = 1

    def send_complaints(self):

    def invite_users(self):

    def book_history(self):
        #record of books the user read. This will help suggest books to user in future



class SuperUser(RegisteredUser):

    super_user_count = 0 #total number of superuser in system

    def __init__(self):
        super().__init__()
        SuperUser.super_user_count += 1

    def approve_new_user(self):

    def book_approval(self):

    def book_updates(self):

    def process_complaints(self):

    def setup_reading_points(self):



