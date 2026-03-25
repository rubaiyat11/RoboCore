#Project to practice gradient descent using numpy
"""
Gradient Descent from scratch:

1. Define a simple function: y = (x - 3)²
   This is a curve with a minimum at x = 3

2. Define its derivative: dy/dx = 2(x - 3)
   This tells you the slope at any point

3. Start at a random x position, say x = 10

4. Run gradient descent for 100 iterations:
   - Calculate the slope at current x
   - Move x in the opposite direction of slope
   - x = x - learning_rate * slope
   - Print x and y value each iteration

5. Use learning_rate = 0.1

6. After 100 iterations print:
   - Final x value (should be close to 3)
   - Final y value (should be close to 0)
   - How many iterations it took to get within
     0.001 of the minimum
"""

import numpy as np

#1.defining function first
def f(x):
   return (x-3)**2

def derivative(x):
   return 2*(x-3)

x = 10 

i = 0
while i < 100:
   slope_x = derivative(x)
   x = x - 1.1 * slope_x
   if i % 10 == 0:
      print(x, f(x))
   if abs(x - 3) < 0.001:
      print(f"Minimum reached at iteration {i}")
      break
   else:
      i += 1
      continue

print(x, f(x))
