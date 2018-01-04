import pickle
import nester
fileName = 'pickledata.txt'
try:
        with open(fileName, 'wb') as mysavedata:
                pickle.dump([1, 2, "three"], mysavedata)
        with open(fileName, 'rb') as myrestoredata:
                data = pickle.load(myrestoredata)
                nester.print_lol(data, indent=True, level=0)
except IOError as error:
        print("The data file is missing!" + str(error))
