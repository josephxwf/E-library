
class User(object):

    def __init__(self, username, password, super_user=False, point=100, activate=False):
        self.username = username
        self.password = password
        self.superUser = super_user
        self.point = point
        self.readingHistory = {}
        self.own_book = []
        self.activate = activate

        # self.book_time

    def setReadingHistory(self, list):
        self.readingHistory = list

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
        self.userid = " "

    def invite_users(self):
        self.userid = " "


# class SuperUser(User):
#
#     def __init__(self):
#         super().__init__()
#
#     def approve_new_user(self):
#         self.userid = ""
#
#     def book_approval(self):
#         self.bookcallnumber = ""
#
#     def book_updates(self):
#         self.bookcallnumber = ""
#
#     def process_complaints(self):
#         self.userid = ""
#
#     def setup_reading_points(self):
#         self.bookcallnumber = ""
