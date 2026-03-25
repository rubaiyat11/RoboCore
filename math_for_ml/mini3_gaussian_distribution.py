#Project to practice gaussian distribution application on different sensor readings of robot
""" 
Noisy Sensor Simulation:

1. Define a "true" distance to an obstacle: 5.0 meters

2. Create a function called sensor_reading(true_distance, noise_level)
   that returns a single noisy reading using np.random.normal
   with mean = true_distance and std = noise_level

3. Simulate 3 different quality sensors:
   - Cheap sensor: noise_level = 0.5
   - Mid sensor: noise_level = 0.2  
   - Premium sensor: noise_level = 0.05

4. For each sensor take 100 readings and store in a NumPy array

5. For each sensor calculate and print:
   - Mean of readings (should be close to 5.0)
   - Standard deviation of readings
   - Min and max readings
   - How far the mean is from true distance (error)

6. Show how averaging helps:
   - Take 1 reading from cheap sensor
   - Take 10 readings and average them
   - Take 100 readings and average them
   - Take 1000 readings and average them
   - Print each average and how close it is to 5.0
"""
import numpy as np

true_distance = 5.0 

def sensor_reading(true_distance, noise_level, size):
   return np.random.normal(true_distance, noise_level, size)

cheap_sensor = 0.5
mid_sensor = 0.2
premium_sensor = 0.05



def calculate(readings):
   mean_readings = np.mean(readings)
   std_readings = np.std(readings)
   max_readings = np.max(readings)
   min_readings = np.min(readings)
   error = true_distance  - mean_readings
   return (mean_readings, std_readings, max_readings, min_readings, error)


cheap_readings = sensor_reading(true_distance, 0.5, 100)
mean, std, max_val, min_val, error = calculate(cheap_readings)

print("For cheap sensor:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")

mid_readings = sensor_reading(true_distance, 0.2, 100)

mean, std, max_val, min_val, error = calculate(mid_readings)
print("For mid sensor:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")

premium_readings = sensor_reading(true_distance, 0.05, 100)
mean, std, max_val, min_val, error = calculate(premium_readings)
print("For premium sensor:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")


cheap_readings1 = sensor_reading(true_distance, 0.5, 1)
mean, std, max_val, min_val, error = calculate(cheap_readings1)

print("For cheap sensor with 1 reading:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")


cheap_readings2 = sensor_reading(true_distance, 0.5, 10)
mean, std, max_val, min_val, error = calculate(cheap_readings2)

print("For cheap sensor with 10 readings:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")

cheap_readings3 = sensor_reading(true_distance, 0.5, 100)
mean, std, max_val, min_val, error = calculate(cheap_readings3)

print("For cheap sensor with 100 readings:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")

cheap_readings4 = sensor_reading(true_distance, 0.5, 1000)
mean, std, max_val, min_val, error = calculate(cheap_readings4)

print("For cheap sensor with 1000 readings:")
print(f"Mean: {mean:.3f} | Std: {std:.3f} | Max: {max_val:.3f} | Min: {min_val:.3f} | Error: {error:.3f}")

