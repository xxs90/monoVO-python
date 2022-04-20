import numpy as np
import matplotlib.pyplot as plt


def draw_3d_test():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in range(10):
        y = np.random.random()
        ax.scatter(i, y, 2)
        plt.pause(0.05)

    plt.show()

def draw_3d_init():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlim3d(-500, 500)
    ax.set_ylim3d(-500, 500)
    ax.set_zlim3d(-500, 500)
    return fig, ax

def draw_3d_add(ax, x, y, z, color: str):
    ax.scatter(x, y, z, c=color, alpha=0.5)


if __name__ == "__main__":
    fig, ax = draw_3d_init()
    for i in range(10):
        x = np.random.uniform(0,1000)
        y = np.random.uniform(0,1000)
        z = np.random.uniform(0,1000)
        draw_3d_add(ax,x,y,z,color="g")
        # plt.pause(0.05)

    plt.show()