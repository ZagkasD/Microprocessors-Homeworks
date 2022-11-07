# Monte Carlo algorithm for calculating pi

# May the gods forgive me for the code I'm about to write

from math import sqrt
import random

# Counts the number of points inside the circle
def check_point_position(sample_size, points_matrix):
    counter = 0
    for i in range(sample_size):
        # Calculate distance of point from center of circle (0.5, 0.5)
        dist = sqrt((points_matrix[i][0]-0.5)**2 + (points_matrix[i][1]-0.5)**2)
        
        if dist < 0.5:
            counter += 1

    return counter


def main():
    a = 1   # The length of each side of the rectangular
    counter = 0 # Number of points inside the circle with radius = 0.5

    sample_size = 10000 # Number of points
    print('Sample size = ' + str(sample_size))
    
    points_matrix = [[round(random.random(),2) for e in range(2)] for e in range(sample_size)]
    #print(points_matrix)
    counter = check_point_position(sample_size, points_matrix) 
    print('Points inside the circle = '+str(counter))
    points_ratio = counter/(sample_size) # Points inside the circle / all points
    pi_approx = points_ratio * 4
    print('Π = '+str(pi_approx))
   
       

main()
