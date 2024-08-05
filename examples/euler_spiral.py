import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.special import fresnel

def main():
    t = np.linspace(-10, 10, 1000)
    plt.plot(*fresnel(t), c='k')
    plt.show()

if __name__ == '__main__':
    main()
