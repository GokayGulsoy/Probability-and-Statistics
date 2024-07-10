# GÖKAY GÜLSOY
# Student number: 270201072
import numpy as np
import random
from matplotlib import pyplot as plt

# Computing theoretical probabilities

p1 = 1 - ((5 / 6) ** 5)  # probability that at least one dice is 3

# by using conditional probability formulae
# 0.570 is P(AandB)(at least one dice is three and at least one dice is even)
# 0.968 is P(B) (at least one dice is even)
p2 = (0.570) / (0.968)

# by using conditional probability formulae
# P(AandB)is 0.125(at least one dice is three and only one of the dice is even)  
# P(B) is 0.156(only one of the dice is even)
p3 = (0.125) / (0.156)

print("Theoratical probability P1 is: {:.3f}".format(p1))
print("Theoretical probability P2 is: {:.3f} ".format(p2))
print("Theoratical probability P3 is: {:.3f}\n".format(p3))


# function for rolling five dices
def roll_a_dice():
    array = []
    for n in range(5):
        dice_value = random.randint(1,6)
        array.append(dice_value)

    return array


# function for checking evens
def check_evens(array):
    count = 0
    for m in array:
        if m % 2 == 0:
            count += 1
    return count


# creating a list for repeating the experiment
N = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]

# list that will hold empirical probabilities
probs1 = []
probs2 = []
probs3 = []

for i in N:
    # initializing probability lists
    occurence1,occurence2,occurence3 = 0,0,0
    sample_space2, sample_space3 = 0, 0
    for j in range(i):
        dice_array = roll_a_dice()

        if 3 in dice_array:
            occurence1 += 1

        if check_evens(dice_array):
            sample_space2 += 1
            if 3 in dice_array:
                occurence2 += 1

        if check_evens(dice_array) == 1:
            sample_space3 += 1
            if 3 in dice_array:
                occurence3 += 1

    probs1.append(occurence1 / i)
    probs2.append(occurence2 / sample_space2)
    probs3.append(occurence3 / sample_space3)

# creating lines for theoratical probabilities
p1_line = np.array([p1, p1, p1, p1, p1, p1, p1, p1, p1, p1, p1])
p2_line = np.array([p2, p2, p2, p2, p2, p2, p2, p2, p2, p2, p2])
p3_line = np.array([p3, p3, p3, p3, p3, p3, p3, p3, p3, p3, p3])

# Emprical probabilities
print("Emprical probability P1 as N goes to infinity is: {:.3f}".format(probs1[-1]))
print("Emprical probability P2 as N goes to infinity is: {:.3f}".format(probs2[-1]))
print("Emprical probability P3 as N goes to infinity is: {:.3f}".format(probs3[-1]))

plt.title("Dice Roll Experiment")
plt.xlabel("Number of experiments")
plt.ylabel("Probabilities")
plt.xscale("log")
plt.plot(N, probs1, N, probs2, N, probs3, N, p1_line, N, p2_line, N, p3_line)

plt.show()
