/*
C++ phase project summary:

Project 1: Basic syntax ✅
Project 2: Functions and control flow ✅
Project 3: Pointers ✅
Project 4: Robot Class ✅
Project 5: Smart pointers ✅
Project 6: Sensor Array ✅
Consolidation: Sensor Pipeline ✅
Before we start, what parts of RoboCore v0.1 do you want to rewrite in C++? Think about which components benefit most from C++ speed.

Planning:
    Where does c++ apply? : Clearly Motor and Sensor class. Fast and precise sensor gives information with less latency so more time to react. The reaction part is handled by motor. Less latency means more room
                            to react against unfamilliar situation in the right time. ** Motor & Sensor Class **;
    Previous Motor Class: Had init, rotate, move  methods.
    Previous Sensor Class: Had init, scan methonds.
                          We directly translate into c++ with proper memory management.
    Questions/Problems: 1.How do we recieve the actual fuel, battery and position values dynamically?
                        2.How do we write the rotation matrix maths in c++?
                        3.How do we use the already defined robot class in the v2 python file?
                        4.What should the movement logic even be?
                        5.What should the sensor logic be?
                        6.Most of the problems are based on how to do math in cpp which i dunno.
                        7.Should scan even be based on the noise level logic?

    I clearly dont have a full picture of what to build and how to build it.
    Decision: Just try to recreate the python motor and sensor class using cpp. No need to think
              about connecting python and cpp to use same variable value. I am not at that level yet.
              Somehow Apply every lesson that i learnt. Because all of them are directly connected to robot.
    
    Lessons I learnt: Pointers, references, smart pointers, classes, STL vectors, lambdas, function pointers.
            Building RoboCore v0.3 where Motor and Sensor become C++ components.

    Execution: We need to set fuel and battery variables here so that we can make the cpp code at least run
               without bugs.
              -For now forget about rotation since we dont know maths in cpp yet. We dont even know if maths
               are done using cpp or python.
              -Set variables like name, fuel, battery, position and then create classes.
              -We will only create class for motor and sensor. No need to create robot class cuz i think
               we will probably learn how to use python classes and cpp classes simultaneously and robot class
               belongs in python since it does not require speed.
              -In scan instead of random number for variables we set a exact variable and just print them.
               This might be bad since we are going down a level but i still dont know how to do mean and 
               maths in cpp. Either we messed up cpp learning roadmap big time or we probably dont need
               that much maths in cpp. EDIT: I think we keep some preassigned numbers and 
               calculate the average of distance or readings manually like in sensor cpp project.
              -We should build a robot class since we did learn it in project robot class.
            -New opinion: We just put everything we learnt in different cpp project together and implement here
                          with mainly motor and sensor as highlight.

Build standalone C++ file with Motor and Sensor classes:

MOTOR CLASS:
- Private members using smart pointers:
  unique_ptr<float> fuel (starts 100)
  float position[3] = {0, 0, 0}  (x,y,z)
  float orientation = 0.0

- Methods:
  move(string direction, int steps)
    updates position, consumes fuel
  rotate(float angle)
    updates orientation using cos/sin rotation matrix
    #include <cmath> for this
  get_fuel() returns current fuel
  print_status() prints position and fuel
  
- Use vector<float> to store last 5 
  fuel readings after each move

SENSOR CLASS:
- Private members:
  float true_temperature = 50.0
  float true_distance = 100.0
  float noise_level = 0.5
  vector<float> readings history

- Methods:
  scan() generates 5 noisy readings using rand()
    calculates and returns average
    stores readings in vector
  get_last_readings() prints all stored readings
  use a lambda to filter readings above threshold
  use a function pointer to normalize readings

MAIN:
- Create Motor and Sensor instances
- Run a simple command loop:
  user types move/rotate/scan/status/quit
- Apply everything learned:
  smart pointers, vectors, lambdas, 
  function pointers, references
*/


#include <iostream>
#include <memory>
#include <algorithm>
#include <vector>
#include <cmath>
#include <eigen3/Eigen/Dense>
#include <random>
using namespace std;

class Motor{
private:
    unique_ptr<float> fuel = make_unique<float>(100);
    float position[3] = {0.0, 0.0, 0.0};
    float orientation = 0.0;
    vector<float> fuel_readings;

public:
    void rotate(float angle, string turn){
        if(turn == "Clockwise" || turn == ""){
            orientation += angle;
        } else if(turn == "Counter-Clockwise"){
            orientation -= angle;
        } else{
            cout << "Give a proper turning side." << endl;
        }
    }

    void move(string direction, int steps){
        float new_position[3] = {0.0, 0.0, 0.0};
        if(direction == "forward"){
            new_position[0] += steps;
        } else if(direction == "backward"){
            new_position[0] -= steps;
        } else if(direction == "right"){
            new_position[1] += steps;
        } else if(direction == "left"){
            new_position[1] -= steps;
        } else if(direction == "up"){
            new_position[2] += steps;
        } else if(direction == "down"){
            new_position[2] -= steps;
        } else{
            cout << "Invalid Direction" << endl;
        }
        *fuel -= 10;
        
        fuel_readings.push_back(*fuel);
        if (fuel_readings.size() > 5) {
            fuel_readings.erase(fuel_readings.begin());
        }

        float rad = orientation * M_PI / 180.0;
        Eigen::Matrix3f rot;
            rot <<  cos(rad), -sin(rad), 0,
                    sin(rad),  cos(rad), 0,
                    0,         0,        1;

        Eigen::Vector3f step = {new_position[0], new_position[1], new_position[2]};
        Eigen::Map<Eigen::Vector3f>(position) += rot * step;

    }

    float get_fuel(){
        return *fuel;
    }

    void print_status(){
        cout << "Position: [" << position[0] << ", " << position[1] << ", " << position[2] << "]" << endl;
        cout << "Fuel: " << *fuel << endl;
    }

};

float normalize(float value){
    return value / 10;
}

struct ScanResult {
    float dist_avg;
    float temp_avg;
};

class Sensor{
private:
    float true_temperature = 50.0;
    float true_distance = 100.0;
    float noise_level = 0.5;
    float distance_readings[5]; 
    float temperature_readings[5];
    vector<float> sensor_readings;
    float (*norm)(float) = normalize;
        
public:

    ScanResult scan(){
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dist100(1, 100);
        uniform_int_distribution<> dist50(1, 50);
        for(int i = 0; i < 5; i++) {
            distance_readings[i] = (float)dist100(gen);
            temperature_readings[i] = (float)dist50(gen);
            
            sensor_readings.push_back(distance_readings[i]);
            sensor_readings.push_back(temperature_readings[i]);
        }
        float sum_dist = 0;
        float sum_temp = 0;
        for(int i=0; i < 5; i++){
            sum_dist += distance_readings[i];
            sum_temp += temperature_readings[i];
        }

        float dist_avg = sum_dist / 5;
        float temp_avg = sum_temp / 5;

        return {dist_avg, temp_avg};
    }

    void get_last_readings(){
        for(int i =0; i < 5; i++){
            cout << "Sensor Reading: " << sensor_readings[i] << endl;
        }
        
        auto filter = [](float value){
            if(value > 100.5){cout << "HIGH(distance): " << value << endl;}
        };
        
        for_each(begin(distance_readings), end(distance_readings), filter);

        for(int i = 0; i < 5; i++){
            float value = sensor_readings[i];
            float norm_value = norm(value);
            cout << "Reading " << i << ": " << value 
                 << " | Normalized: " << norm_value << endl;
        }

    }



};


int main(){
    Motor robot_motor;
    Sensor robot_sensor;
    cout << "--- RoboCore v0.3 Initialized ---" << endl;
    cout << "Commands: move, rotate, scan, status, quit" << endl;

    string cmd;
    
    while(robot_motor.get_fuel() > 0){   
        cout << "What is your command? " << endl;
        cout << "\n> ";
        cin >> cmd;
        transform(cmd.begin(), cmd.end(), cmd.begin(), ::tolower);

        if (cmd == "quit") {
            break;
        }
        
        if (cmd == "move") {
            string dir; int s;
            cout << "Direction (forward/up/down) and steps: ";
            cin >> dir >> s;
            if(cin.fail()){
                cout << "Wrong command" << endl;
                cin.clear();
                cin.ignore(1000, '\n');
                continue;
            }
            transform(dir.begin(), dir.end(), dir.begin(), ::tolower);
            if(dir != "forward" && dir != "backward" && dir != "up" && dir != "down" && dir != "left" && dir != "right"){
                cout << "Invalid Direction" << endl;
            } else if(s > 10){
                cout << "Too high step count" << endl;
            } else if(s <= 0){
                    cout << "Step count must be positive." << endl;
            }else{
               robot_motor.move(dir, s); 
            }
            
        } 
        else if (cmd == "rotate") {
            float ang;
            string turn;
            cout << "Angle: ";
            cin >> ang;
            cout << "Turn: ";
            cin >> turn;
            if(cin.fail()){
                cout << "Give a valid angle and turning." << endl;
            } else{
                robot_motor.rotate(ang, turn);
            }
        } 
        else if (cmd == "scan") {
            ScanResult result = robot_sensor.scan();
            cout << "Average Distance: " << result.dist_avg << endl;
            cout << "Average Temperature: " << result.temp_avg << endl;
            robot_sensor.get_last_readings();
        } 
        else if (cmd == "status") {
            robot_motor.print_status();
        } else{
            cout << "Invalid Command" << endl;
        }
    }


    return 0;
}