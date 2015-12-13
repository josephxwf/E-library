from Book import Book
import pickle
import time

if __name__ == '__main__':
    book_list = []

    my_book = Book("Four in Camp","QUINNEYS.jpg", 20)
    my_book.author = "Ralph Henry Barbour"
    my_book.summary = "A STORY OF SUMMER ADVENTURES IN THE NEW HAMPSHIRE WOODS"
    my_book.type = "Adventures"
    my_book.NumOfRead = 18
    my_book.cover_page = "QUINNEYS.jpg"
    my_book.book_file = "Four in Camp.txt"
    my_book.contribute_by = "kaiying"
    my_book.superuser_set_point = 0
    my_book.complain = []
    my_book.last_time_read = time.time()
    book_list.append(my_book)

    my_book = Book("La chair et le sang","QUINNEYS.jpg", 5)
    my_book.author = "Franois Mauriac"
    my_book.summary = "Since the introduction of the tungsten lamp some five years ago," \
                      " the manufacturers have attempted continually to produce smaller " \
                      "and smaller units in the standard voltages."
    my_book.type = "Education"
    my_book.book_file = "La chair et le sang.txt"
    my_book.NumOfRead = 8
    my_book.cover_page = "QUINNEYS.jpg"
    my_book.contribute_by = "kaiying"
    my_book.superuser_set_point = 0
    my_book.complain = []
    my_book.last_time_read = time.time()
    book_list.append(my_book)

    my_book = Book("The Fifteen Watt Tungsten Lamp","QUINNEYS.jpg",25)
    my_book.author = "Clair Elmore Anderson"
    my_book.summary = "Since the introduction of the tungsten lamp some five years ago," \
                      " the manufacturers have attempted continually to produce smaller " \
                      "and smaller units in the standard voltages."
    my_book.type = "Education"
    my_book.book_file = "The Fifteen Watt Tungsten Lamp.txt"
    my_book.NumOfRead = 22
    my_book.superuser_set_point = 0
    my_book.cover_page = "QUINNEYS.jpg"
    my_book.contribute_by = "kaiying"
    my_book.complain = []
    my_book.last_time_read = time.time()
    book_list.append(my_book)

    my_book = Book("The Wonderful Wizard of Oz","QUINNEYS.jpg",35)
    my_book.author = "L. Frank Baum"
    my_book.summary = "Folklore, legends, myths and fairy tales have followed childhood " \
                      "through the ages, for every healthy youngster has a wholesome and" \
                      "instinctive love for stories fantastic, marvelous and manifestly unreal."
    my_book.type = "Adventures"
    my_book.book_file = "The Wonderful Wizard of Oz.txt"
    my_book.NumOfRead = 55
    my_book.superuser_set_point = 0
    my_book.cover_page = "The Wonderful Wizard of Oz.jpg"
    my_book.contribute_by = "kaiying"
    my_book.complain = []
    my_book.last_time_read = time.time()
    book_list.append(my_book)


    my_book = Book("Visages","QUINNEYS.jpg",10)
    my_book.author = "Francis Chevassu"
    my_book.summary = "IL est certain que la gloire a un ge. Jean-Jacques nous apparat  " \
                      "quarante ans, Voltaire  soixante, Musset  vingt-cinq, Hugo cinquante,"
    my_book.type = "Education"
    my_book.NumOfRead = 3
    my_book.cover_page = "QUINNEYS.jpg"
    my_book.book_file = "Visages.txt"
    my_book.superuser_set_point = 0
    my_book.contribute_by = "kaiying"
    my_book.complain = []
    my_book.last_time_read = time.time()
    book_list.append(my_book)

    my_book = Book("Quinneys","QUINNEYS.jpg", 30)
    my_book.author = "Horace Annesley Vachell"
    my_book.summary = "With his back to the man, Quinney smiled.  He could remember the day, " \
                      "not so long ago, when Pinker, the grocer, called him 'My lad.' "
    my_book.type = "history"
    my_book.NumOfRead = 55
    my_book.superuser_set_point = 0
    my_book.cover_page = "QUINNEYS.jpg"
    my_book.book_file = "Quinneys.txt"
    my_book.contribute_by = "kaiying"
    my_book.complain = []
    my_book.last_time_read = time.time()
    book_list.append(my_book)

    with open('book_data.pkl', 'w') as output:
        pickle.dump(book_list, output)
