import os
import numpy as np

def main():
    print('Hello, world')

def data():
    here = os.path.dirname(os.path.abspath(__file__))
    print('{}/data/test.dat'.format(here))
    X, Y = np.loadtxt('{}/data/test.dat'.format(here), unpack=True)
    for x, y in zip(X, Y):
        print(x, y)

if __name__ == '__main__':
    main()
    data()
