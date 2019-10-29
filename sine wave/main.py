import numpy as np
import matplotlib.pyplot as plt


sample_rate = 8000
frequency = 5

while True:
    sample_rate += 1000
    x = np.arange(sample_rate)
    y = np.sin(2 * np.pi * frequency * (x/sample_rate))
    plt.plot(x,y,"-.")
    plt.title("SINE WAVE")
    plt.show()
