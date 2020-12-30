from matplotlib import pyplot as plt
import random
import math

def in_circle(x, y, straal, center_circle_x, center_circle_y):
    x_in_circle = x - center_circle_x
    y_in_circle = y - center_circle_y

    diagonal_line = math.sqrt(x_in_circle**2 + y_in_circle**2)

    if diagonal_line <= straal:
        return True
    else:
        return False
def mc():
    lenList = 99

    random_x_coordinates = [(random.randrange(0,60,1))/10 for _ in range(lenList)]
    random_y_coordinates = [(random.randrange(0,60,1))/10 for _ in range(lenList)]

    #uncommend for seeing the plot of the falled balls
    #plt.scatter(1.5, 1.5, s=3000, marker="s")
    #plt.scatter(3.5, 1.5, s=15000, edgecolors='r')
    #plt.scatter(random_x_coordinates, random_y_coordinates)
    #plt.show()

    circle_counter = 0
    square_counter = 0

    for x, y in zip(random_x_coordinates, random_y_coordinates):
        if in_circle(x, y, 1, 3.5, 1.5):
            circle_counter+=1

        if 0.9 < x and x < 1.9 and 0.9 < y and y < 1.9:
            square_counter+=1

    verhouding_cirkel = circle_counter / (circle_counter + square_counter) * 100
    verhouding_vierkant = square_counter / (circle_counter + square_counter) * 100
    #print("De verhouding is", verhouding_cirkel, "% cirkel en ", verhouding_vierkant, "% vierkant")
    return verhouding_cirkel, verhouding_vierkant

counter = 0
list_x = []
list_y = []

for _ in range(100):
    verhouding = mc()
    list_x.append(counter)
    list_y.append(verhouding[0]-verhouding[1])
    counter+=1
plt.title("-100% = alles in vierkant +100% alles in rondje op de y-as")
plt.plot(list_x, list_y)
plt.ylim(-100, 100)
plt.show()

