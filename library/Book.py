import pickle


class Book():
    def __init__(self, title, cover_page, requestPoint, time=0.0):
        self.title = title
        self.author = ""
        self.summary = ""
        self.requestPoint = requestPoint
        self.type = ""
        self.NumOfRead = 0
        self.cover_page = cover_page
        self.book_file = None
        self.contribute_by = ""
        self.superuser_set_point = 0
        self.complain = []
        # self.UploadBookDate = 0
        self.last_time_read = time


    def add_to_database(self):
        with open('user_data.pkl', 'a') as output:
            pickle.dump(self, output)

    def read(self):
        self.NumOfRead += 1

    # def cover_page(self):
    #     self.readcoverpage = ""

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
