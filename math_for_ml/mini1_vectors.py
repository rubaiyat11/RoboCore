#Project to practice numpy in robots
"""
Robot Position and Rotation using NumPy:

1. Create your robot's position as a NumPy 
   vector: x=3.0, y=2.0, z=0.0

2. Create a rotation matrix for 45 degrees

3. Apply the rotation to the position vector
   using matrix multiplication
   Print before and after positions

4. Create a fleet of 3 robots as a 2D array
   each with different x, y, z positions

5. Move all robots forward by 1 step 
   simultaneously using NumPy array operations,
   no loops allowed

6. Calculate the distance of each robot from
   the origin (0,0,0) using np.linalg.norm

7. Find which robot is furthest from origin
   using np.argmax
"""












import numpy as np

#1.Robot's position
pose = np.array([3.0,2.0,0.0])

#2.Robot's rotation
angle = np.radians(45)
rotation = np.array([
    [np.cos(angle), -np.sin(angle), 0],
    [np.sin(angle), np.cos(angle), 0],
    [0,0, 1]
])

#3.Applying rotation to robot's position
new_pose = np.matmul(rotation, pose)

print(pose)
print(new_pose)

#4.Creating Fleet using 2D arrays
fleet = np.array([
    [4, 5, 6],
    [5, 2, 4],
    [10, 1, 2]
])

def move_all(fleet, amount):
    return fleet + amount

distance = np.linalg.norm(fleet, axis = 1)

furthest_index = np.argmax(distance)

print(f"Robot {furthest_index +1} is the furthest from origin")
print(f"It's distance from origin is {distance[furthest_index]}")

new_fleet = move_all(fleet, 1)
print(f"Fleet after moving:\n{new_fleet}")