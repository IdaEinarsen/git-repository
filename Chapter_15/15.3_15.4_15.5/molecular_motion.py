import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    
    rw = RandomWalk(5000)
    rw.fill_walk()

    
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))

    
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    
    ax.scatter(0, 0, c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

   
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break