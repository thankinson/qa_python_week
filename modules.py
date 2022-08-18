import math
import random

def sqrtNum():
    number = float(input("enter a number: "))
    answer = math.sqrt(number)
    return answer



#########

def randomNum():
    return math.ceil(random.randint(1, 10) * math.pi)

for _ in range(5):
        print(randomNum())


#######



