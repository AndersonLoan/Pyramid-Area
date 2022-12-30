# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Anderson Loan
# Section:         574
# Assignment:   6.12
# Date:         27 9 2022
#

from math import sqrt

length = float(input('Enter the side length in meters: '))
layers = float(input('Enter the number of layers: '))

topArea = (length*layers)**2/4 * sqrt(3) #area from top down of pyramid from God's eye view
sideArea = 0
def sideAreaAdd(h):
    global sideArea
    sideArea += 3 * length**2 * h #calculate the area of each side
    if h > 0:#don't continue past h=0
        sideAreaAdd(h-1) #the function calls itself on the next layer down
      
sideAreaAdd(layers)
area = sideArea + topArea #add the areas together
print(f'You need {area:.2f} m^2 of gold foil to cover the pyramid') #print result
