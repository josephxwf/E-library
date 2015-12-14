__author__ = 'Administrator'
import pickle
from User import User

if __name__ == '__main__':

    super_user = User("kaiying","1")
    super_user.superUser = True
    super_user.activate = True

    user = User("din", "1")
    user.activate = True
    user.superUser = False

    user1 = User("joe", "1")
    user1.readingHistory['Visages'] = 10
    user1.activate = True
    user1.superUser = False

    my_list = [super_user, user,user1]
    with open('user_data.pkl', 'w') as output:
        pickle.dump(my_list, output)
