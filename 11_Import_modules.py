import matplotlib.pyplot as p # P is reference
from random import shuffle 
from statistics import mean, variance, median, stdev

num = [1,2,3,4,5,6,7,8,9]
print("Max: ",max(num))

shuffle(num)
p.plot(num,'miter')
p.ylabel('Numbers')
p.show()


