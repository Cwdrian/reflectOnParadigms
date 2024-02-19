def flat_n_sort(arr):
    flat_arr = sum(arr, [])

    sort_arr = sorted(flat_arr)

    return sort_arr


result = flat_n_sort([[13, 4, 72],[54, 11, 6],[34, 16, 7]])
print(result)

"""
1. All variables are immutable in this solution.
2. This solution is a pure function it does not produce any side effects
3. This function is not a higher order function. it does not take a function as an argument nor returns a function.
4. This was easy enough and there was no need for OOP
5. Functional Programming is helpful for this solution because it allows simple and reusable code.
"""

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed *= 2


class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


podracer1 = Podracer(500, "perfect", 1000)
print("Before repair:", podracer1.condition)  
podracer1.repair()
print("After repair:", podracer1.condition)  

anakins_pod = AnakinsPod(600, "perfect", 1500)
print("Before boost:", anakins_pod.max_speed)  
anakins_pod.boost()
print("After boost:", anakins_pod.max_speed)  

sebulbas_pod = SebulbasPod(700, "perfect", 2000)
print("Before flame jet:", podracer1.condition)  
sebulbas_pod.flame_jet(podracer1)
print("After flame jet:", podracer1.condition)

"""
1. Encapsulation is demonstrated by bundling the data (attributes) and behavior (methods) related to a Podracer within the Podracer class
 Abstraction is demonstrated by hiding the implementation details of the Podracer class and its subclasses from everyone else
 Inheritance is demonstrated by the subclassing relationship between the Podracer class and its subclasses
 Polymorphism is demonstrated by both AnakinsPod and SebulbasPod are treated as Podracer objects

 2. OOP provides clear benefits in terms of code organization, modularity, and extensibility, making it a natural choice for this problem
"""

"""
Different coding styles like OOP, Procedural, and Functional Programming each have their own strengths.
OOP is good for modeling real-world things and making reusable code.
Procedural is straightforward and fast, especially for smaller projects.
Functional focuses on predictability and concise code but might be a bit harder to learn.
The best style depends on what you're making and what you're comfortable with, and sometimes mixing them up is the way to go!
"""