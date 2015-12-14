import pickle
import time

class Library():
    def __init__(self):    #constructor
        self.userData = self.loadUserData()
        self.bookData = self.loadBookData()

    def update_user_data(self, new_user, delete=False):
        """
        This function will update user object in user database
        :param new_user: user object which need update
        :return:
        """
        userData = self.loadUserData()
        newData = []
        find = False
        for user in userData:
            if user.username == new_user.username:
                if delete is False:
                    newData.append(new_user)
                find = True
            else:
                newData.append(user)
        if find is False:
            newData.append(new_user)

        with open('user_data.pkl', 'w') as output:
            pickle.dump(newData, output)

    def loadUserData(self):
        """
        This function will load all user object from user database.

        :return: user object list
        """
        try:
            with open('user_data.pkl', 'r') as input:
                try:
                    user = pickle.load(input)
                except:
                    user = None
        except:
            user=None
            with open('user_data.pkl', 'w') as output:
                pass
        return user

    def loadBookData(self, path='book_data.pkl'):
        """
        This function will load all book object from book database.

        :param path: string type, path of database
        :return: book object list
        """
        try:
            with open(path, 'r') as input:
                try:
                    book = pickle.load(input)
                except:
                    book = None
        except:
            book = None
            with open(path, 'w') as output:
                pass

        return book

    def update_book_data(self, new_book, path='book_data.pkl', delete=False):
        """
        this function will updata book database
        :param new_book: book object which need update
        :param path: string type, path of book database
        :param delete: boolean, if true, it will delete book object
        :return:
        """
        book_data = self.loadBookData(path)
        new_data = []
        find = False
        if book_data:
            for book in book_data:
                if book.title == new_book.title:
                    if delete == False:
                        new_data.append(new_book)
                    find = True
                else:
                    new_data.append(book)
            if find is False:
                new_data.append(new_book)
        else:
            new_data.append(new_book)

        with open(path, 'w') as output:
            pickle.dump(new_data, output)


    def searchBook(self, keyword):
        """
        This function will search book base on keyword. it will search book's title, author, type and summary.
        :param keyword:string type
        :return: book object list
        """
        result = []
        resultNum = 5

        bookData = self.loadBookData()
        if bookData:
            for book in bookData:
                if keyword.lower() in str(book.title.lower()):   # maybe need to convert keyword to str(keyword)
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in str(book.author).lower():   # check book author
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in str(book.type).lower():       # check book type
                    result.append(book)
                    resultNum -=1
                elif keyword.lower() in str(book.summary).lower():    # check book summary
                    result.append(book)
                    resultNum -=1
                if resultNum == 0:
                    break
        return result

    def searchUser(self, name):
        """
        This function will return user object by input string type username

        :param string (username)
        :return: user object
        """
        users = self.loadUserData() # load all users from database
        for user in users:
            if user.username == name:
                return user
        return None

    def searchTop5(self):
        """
        This function will return top 5 book base on number of read.
        :return:book object list
        """
        top5List = []
        book_data = self.loadBookData()
        if book_data:
            data = sorted(book_data, key=lambda book: book.NumOfRead, reverse=True)  # sort book data base on number of read
            index = 0
            if len(book_data) >= 5:
                index = 5
            else:
                index = len(book_data)
            for i in range(index):
                top5List.append(data[i])
        return top5List

    def search_book_by_type(self, type):
        """
        This function will return a book list(only 5 book) with input type
        :param string (type)
        :return:book list
        """
        book_data = self.loadBookData()
        book_list = []
        if book_data:
            index = 0
            for book in book_data:
                if book.type == type:     # check type
                    book_list.append(book)
                    index += 1
                    if index is 5:
                        break
            if index < 5:
                for book in book_data:
                    if book.type != type:
                     book_list.append(book)
                     index += 1
                     if index is 5:
                        break

        return book_list

    def search_book_by_title(self, title):
        """
        This function return book object by input book title
        :param title: string type
        :return: book object
        """
        book_data = self.loadBookData()  # load book from database
        if book_data:
            for book in book_data:
                if book.title == title:
                    return book
        return None



    def Catalog(self):
        BookList = []
        book_data = self.loadBookData()
        if book_data:
            bookdata = sorted(book_data, key=lambda book: book.title, reverse=True)
            for i in range(len(bookdata)):  #need to make the range equal total number of books in self.bookData
                BookList.append(bookdata[i])
        return BookList


    def remove_book_with_nobody_read(self):
        """
        This function will remove books which no one read for a certain time, and 5 points are deducted from the contributing RU
        :return:
        """
        books = self.loadBookData()
        time_for_now = time.time()
        book_owners = []
        if books:
            for book in books:
                if time_for_now - book.last_time_read >= 120000:
                    self.update_book_data(book,delete=True)  # remove book from book database
                    book_owners.append(book.contribute_by)

        if book_owners:
            for username in book_owners:
                user = self.searchUser(username)   # search user by username, get user object
                if user:
                    user.point -= 5                     # 5 points are deducted from the contributing RU
                    self.update_user_data(user)  # update user information on user database

