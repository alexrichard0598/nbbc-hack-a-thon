import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from matplotlib import animation

sample_rate = 1
frequency = 1
amplitude = 0
step_size = 1

fig = plt.figure()
ax = plt.axes(xlim=(0,1), ylim=(-2,2))

while True:
    x = np.arange(amplitude,sample_rate)
    y = [ np.sin(2 * np.pi * frequency * (x/sample_rate)) for i in x ]
    data = [x,y[0]]
    sample_rate += 1
    amplitude -= 1
    plt.ion()
    # thing
    plt.gca().cla()
    plt.plot(data[0],data[1])
    plt.title("SINE WAVE")
    plt.xlabel("Time")
    plt.ylabel("Label")
    plt.draw()
    plt.pause(0.01)


plt.show(block=True)
