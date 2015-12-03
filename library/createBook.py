from Book import Book
import pickle

if __name__ == '__main__':
    my_book = Book("Four in Camp",20)
    my_book.author = "Ralph Henry Barbour"
    my_book.summary = "A STORY OF SUMMER ADVENTURES IN THE NEW HAMPSHIRE WOODS"
    my_book.type = "Adventures"
    my_book.NumOfRead = 18
    with open('book_data.pkl', 'a') as output:
        pickle.dump(my_book, output)

    my_book = Book("La chair et le sang",5)
    my_book.author = "Franois Mauriac"
    my_book.summary = "Since the introduction of the tungsten lamp some five years ago," \
                      " the manufacturers have attempted continually to produce smaller " \
                      "and smaller units in the standard voltages."
    my_book.type = "Education"
    my_book.NumOfRead = 8
    with open('book_data.pkl', 'a') as output:
        pickle.dump(my_book, output)

    my_book = Book("The Fifteen Watt Tungsten Lamp",25)
    my_book.author = "Clair Elmore Anderson"
    my_book.summary = "Since the introduction of the tungsten lamp some five years ago," \
                      " the manufacturers have attempted continually to produce smaller " \
                      "and smaller units in the standard voltages."
    my_book.type = "Education"
    my_book.NumOfRead = 22
    with open('book_data.pkl', 'a') as output:
        pickle.dump(my_book, output)

    my_book = Book("The Wonderful Wizard of Oz",35)
    my_book.author = "L. Frank Baum"
    my_book.summary = "Folklore, legends, myths and fairy tales have followed childhood " \
                      "through the ages, for every healthy youngster has a wholesome and" \
                      "instinctive love for stories fantastic, marvelous and manifestly unreal."
    my_book.type = "Adventures"
    my_book.NumOfRead = 55
    with open('book_data.pkl', 'a') as output:
        pickle.dump(my_book, output)

    my_book = Book("Visages",10)
    my_book.author = "Francis Chevassu"
    my_book.summary = "IL est certain que la gloire a un ge. Jean-Jacques nous apparat  " \
                      "quarante ans, Voltaire  soixante, Musset  vingt-cinq, Hugo cinquante,"
    my_book.type = "Education"
    my_book.NumOfRead = 3
    with open('book_data.pkl', 'a') as output:
        pickle.dump(my_book, output)