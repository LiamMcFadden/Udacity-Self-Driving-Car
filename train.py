import pandas as pd 
from sys import argv
import os
import numpy as np
from sklearn.model_selection import train_test_split


def_path = './train_data'

def load_data(path=None) :

    # determine path to data
    if (len(argv) > 1): path = argv[1]
    else: path = def_path

    # load the CSV file containg the data
    data_csv = pd.read_csv(os.path.join(path, 'driving_log.csv')).to_numpy()
    
    # separate the image data and the steering data
    x = np.array([data_csv[:, 0], data_csv[:, 1], data_csv[:, 2]]).transpose()
    y = data_csv[:, 3].transpose()
    
    # split into a training, testing, and validation set
    x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, random_state=0)
    return x_train, x_valid, y_train, y_valid


def main():
    x_train, x_valid, y_train, y_valid = load_data()
    




if __name__ == "__main__":
    main()

