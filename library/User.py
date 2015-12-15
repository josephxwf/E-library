import collections


class User(object):
    def __init__(self, username, password, super_user=False, point=100, activate=False):
        self.username = username
        self.password = password
        self.superUser = super_user
        self.point = point
        self.commentsHistory = collections.OrderedDict()  #A dictionary which remembers the number of times any user read
                                                          #any book. Each user will have their own dictionary.
        self.readingHistory = collections.OrderedDict()
        self.own_book = []
        self.activate = activate
        self.inviteDic = {}
        self.black_list = False
        self.number_of_book_delete = 0
