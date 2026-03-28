"""
A complete robot system using proper OOP with:
- Multiple classes representing different 
  robot components
- All CS50P concepts integrated
- Clean inheritance structure
- Properties with validation
- A command interface to control it
"""
"""
Planning:
    Clases:
        Robot — the main brain, coordinates everything
        Sensor — handles all sensor readings
        Motor — handles movement and tacks fuel
        Battery — tracks and manages power
        CommandInterface — handles user input loop
    Inside each class:
        Robot: will contain the main identity of the robot like name, position, battery, fuel. Coordinates other classes by storing instances.
        Sensor: Will update obstacle distance and temperature.
        Motor: Will work on changing position by moving. Keeps fuel in limit and in check.
        Battery: Tracks which function costs what battery and keeps battery in a limit and in check
        CommandInterface: will put the motor and sensor skill to use.
    Methods:
    Robot: _innit_ will contain identity.
    Sensor: methods for each - obstacle distance updating, temperature checking
    Motor: move method will contain the x y z coord and how they change through move function
           and how many steps user takes. Has a property to track and keep fuel in limit and shut down when hits 0.
    Batter: Battery method checks battery and battery property keeps it in the limit. 
    CommandInterface: Connects all the command input by user and connecting it to the applicable class

    Robot:
  __init__: name, creates sensor/motor/battery instances
  status(): prints full robot report
  __str__: clean one line summary

Sensor:
  scan(): returns random obstacle distance and temperature
  __str__: current readings

Motor:
  move(steps): updates x,y,z, consumes fuel
  fuel property: validates 0-100
  __str__: position and fuel

Battery:
  consume(amount): reduces battery
  recharge(amount): increases battery
  battery property: validates 0-100
  __str__: current battery level

CommandInterface:
  __init__: takes a Robot instance
  run(): the while True command loop

#Build in this exact order:

Battery class first, it's the simplest
Motor class second
Sensor class third
Robot class fourth, connects everything
CommandInterface last, uses everything

Fix: Build robot class first. Needs identity first.
"""
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.sensor = Sensor()
        self.battery = Battery()
        self.motor = Motor()

    def status(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.motor.x}, {self.motor.y}, {self.motor.z}")
        print(f"Fuel: {self.motor.fuel}")
        print(f"Battery: {self.battery.battery}")

    def is_operational(self):
        return self.battery.battery > 0 and self.motor.fuel > 0

    def __str__(self):
        return f"Name: {self.name} | Temperature: {self.sensor.temperature} | Obstacle Distance: {self.sensor.obstacledist} | Current battery: {self.battery.battery} | Position(x,y,z): {self.motor.x}, {self.motor.y}, {self.motor.z}"

class Battery:
    def __init__(self, battery = 100):
        self.battery = battery

    def consume(self, amount):
        self.battery -= amount
        
        
    def recharge(self, amount):
        self.battery += amount

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        if value > 100:
            self._battery = 100
        elif value < 0:
            self._battery = 0
        else:
            self._battery = value

class Motor:
    def __init__(self, fuel = 100, x= 0, y = 0, z = 0):
        self.fuel = fuel
        self.x = x
        self.y = y
        self.z = z

    def move(self, direction, steps):
        if direction == "Forward":
            self.x += steps
        elif direction == "Backward":
            self.x -= steps
        elif direction == "Right":
            self.y += steps
        elif direction == "Left":
            self.y -= steps
        elif direction == "Up":
            self.z += steps
        elif direction == "Down":
            self.z -= steps
        else:
            print("Specify the steps")

        self.fuel -= 10 * steps

    @property
    def fuel(self):
        return self._fuel
    
    @fuel.setter
    def fuel(self, value):
        if value > 100:
            self._fuel = 100
        elif value < 0:
            self._fuel = 0
        else:
            self._fuel = value
    
    def __str__(self):
        return f"Position(x,y,z): {self.x}, {self.y}, {self.z}, Fuel: {self.fuel}"



class Sensor:
    def __init__(self,):
        self.temperature = random.randint(20,80)
        self.obstacledist = random.randint(0,500)

    def scan(self):
        self.temperature = random.randint(20, 80)
        self.obstacledist = random.randint(0, 500)
        
        return (self.temperature, self.obstacledist)

    def __str__(self):
        return f"Temperature: {self.temperature}, Obstacle Distance: {self.obstacledist}"
    
class Commands:
    def __init__(self, robot):
        self.robot = robot

    def run(self):
        while self.robot.is_operational():
            self._commands = input("What is your command? ").title()
            self.parts = self._commands.split()
            
            if len(self.parts) == 0:
                continue
            self.command = self.parts[0]

            if self.command == "Move":
                try:
                    self.robot.motor.move(self.parts[1], int(self.parts[2]))
                    print(self.robot.motor)
                except (ValueError, IndexError):
                    print("Specify steps")
            elif self.command == "Scan":
                temp, dist = self.robot.sensor.scan()
                print(f"Temperature: {temp} | Obstacle Distance: {dist}")
            elif self.command == "Status":
                self.robot.status()
            elif self.command == "Recharge":
                try:
                    self.robot.battery.recharge(int(self.parts[1]))
                    print(f"Battery: {self.robot.battery.battery}")
                except (ValueError, IndexError):
                    print("Specify amount")
            elif self.command == "Quit":
                print("Goodbye")
                break
            else:
                print("Invalid Command")
            

robot1 = Robot("RoboCore")
interface = Commands(robot1)
interface.run()