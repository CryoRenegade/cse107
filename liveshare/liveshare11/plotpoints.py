import matplotlib.pyplot as plt
import numpy as np
def main():
    xs = range(-5, 15)
    ys = [-(x - 2) ** 2 for x in xs]
    plt.plot(xs, ys, color = 'blue', linestyle = 'dashed')
    plt.title('Plot of $-(x - 2)^2$')
    maximum_index = np.argmax(ys)
    plt.annotate('max', xy=(2, 0), xytext=(2, -22),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == "__main__":
    main()