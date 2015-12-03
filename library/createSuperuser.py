import pickle
from User import User



if __name__ == '__main__':
    super_user = User("kaiying","111111")
    super_user.superUser = True
    with open('user_data.pkl', 'a') as output:
        pickle.dump(super_user, output)