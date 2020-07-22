import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def clusterplot_3d(X, y):
    df = pd.DataFrame(X, columns=['Feature1', 'Feature2','Feature3'])
    df['Cluster'] = y

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_axis = np.array(df['Feature1'])
    y_axis = np.array(df['Feature2'])
    z_axis = np.array(df['Feature3'])
    labels = np.array(df["Cluster"])

    for lbl in np.unique(labels):
        indices = np.where(labels == lbl)
        x = x_axis[indices]
        y = y_axis[indices]
        z = z_axis[indices]
        ax.scatter(x, y, z, s=50, alpha=0.6, label=str(lbl), cmap='rainbow')

    ax.legend()

    plt.show()