import numpy as np
import random
import matplotlib.pyplot as plt
import pickle


def draw(resultPklPath, savePath):
    with open(resultPklPath, 'rb') as f:
        data = pickle.load(f)

    x, y = [], []
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    for i, item in enumerate(data):
        x.extend(item["x"])
        y.extend(item["y"])
    print(len(x))
    plt.figure()
    for i in range(5):
        start_index = sum([d["num"] for d in data[:i]])
        end_index = sum([d["num"] for d in data[:i + 1]])
        plt.scatter(x[start_index:end_index],
                    y[start_index:end_index],
                    color=colors[i], label=f'Class {i + 1}', alpha=0.5, s=10)

    plt.xticks(np.arange(0, 1.1, 0.2))
    plt.yticks(np.arange(0, 1.1, 0.2))
    plt.title('t-SNE cluster result')
    plt.legend()
    plt.savefig(savePath)
