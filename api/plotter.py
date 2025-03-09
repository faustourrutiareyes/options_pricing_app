import matplotlib.pyplot as plt

def simulations_plot(paths, K: float):
    ax = plt.subplot()
    ax.plot(paths, color="gray")
    ax.axhline(K)
    return ax
    

