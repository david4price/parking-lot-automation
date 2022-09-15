import pickle


def save(obj_to_save, filename):
    with open(filename, "wb") as myfile:
        pickle.dump(obj_to_save, myfile)
        myfile.close()


def load(filename):
    with open(filename, "rb") as myfile:
        myfile.close()
        return pickle.load(myfile)


def remove_space(car_number):
    res = sum(not chr.isspace() for chr in car_number)
    return res