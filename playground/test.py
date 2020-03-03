import pickle
import os.path

if os.path.exists('test.pickle'):
    cont = input('Continue? (y/n): ')
    if cont == 'y':
        with open('test.pickle', 'rb') as pf:
            obj1 = pickle.load(pf)
    else:
        obj1 = {'a': 8, 'b': 9, 'c': 10}
else:
    obj1 = {'a': 8, 'b': 9, 'c': 10}

# with open('test.pickle', 'wb') as pf:
#    pickle.dump(obj1, pf)

print(obj1)
