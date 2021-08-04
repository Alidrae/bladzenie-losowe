import matplotlib.pyplot as plt

from random_walk import RandomWalk

#przygotowanie danych bladzenia losowego i wyswietlanie punktow
while True:
    rw=RandomWalk(50000)
    rw.fill_walk()

#wyswietlanie punktow bladzenia losowego
    plt.style.use('classic')
    fig, ax = plt.subplots(#figsize=(10, 6),
        dpi = 128)
    point_nummbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_nummbers, cmap=plt.cm.Blues, edgecolor='none')
    ax.scatter(0, 0, c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    #ukrycie osi
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()
    keep_running = input("Utworzyc kolejne bladzenie losowe? (t/n):")
    if keep_running == "n":
        break
