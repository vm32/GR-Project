# About 
Automated Accident Reporting with Drones and Advanced Technologies is a cutting-edge solution aimed at revolutionizing the way vehicular accidents are reported. This innovative approach leverages the power of drones and advanced technologies to accurately and quickly gather crucial information about accidents and their aftermath. With the ability to quickly survey the scene and capture data such as the location of vehicles, road conditions, and other relevant information, this solution can provide a much more efficient and effective way of reporting accidents. By reducing the time it takes to gather information, this solution can help first responders more effectively respond to accidents, which can in turn save lives and reduce the severity of injuries. Additionally, the data collected can be used to help improve road safety and prevent future accidents from occurring. With the use of advanced technologies and drones, this solution represents a major step forward in accident reporting and is poised to transform the way we respond to vehicular accidents.

## Block Diagram of the Project
<img width='100%' src='https://img001.prntscr.com/file/img001/qhsreyFZTXC3yQcBY01kug.png'/>


## Hardware used 
- MPU6050
- Arduino Uno
- pixhawk flight controller `Drone MC`    
- GPS/GSM
- Temperature Sensor `included inside the MPU6050`
- Arduino Uno (R3).
- Accelerometer Sensor.
- Temperature sensor.
- GPS/GSM Module.
- RC Power Supply Distribution Board.
- Quadcopter Frame.
- Flight Controller.
- Remote Controller.
- EWRF Drone Camera.
- GPS Antenna.
- Radio Telemetry.
- Brushless Motors.
- 40A Brushless ESC.
- 4 Pairs Quadcopters Multirotor.
- 4s Lipo battery 5000.
- Smart Balance Lipo Charger.

## Software Requirements
- Arduino Platform (Open-Source IDE).
-  Thinker CAD (Open-Source Simulation Platform).
- Microsoft Visual Studio Code (Open-Source Framework).
- Mission Planner (Open-Source Drone Simulation).
- QGraoundControl (Open-Source Drone Calibration).

## How to detect the accident using MPU6050 

1- by measure any change in accelerometer 

    if (a.acceleration.x > 0.06) { 
    digitalWrite(4, HIGH);
    digitalWrite(2,LOW); 
    delay(100);
    Serial.print("Accident detect on acceleration : "); 
    Serial.print(a.acceleration.x);                    
    digitalWrite(4, LOW);
    digitalWrite(2,LOW);  
    delay(100);
    };
 
<img width='50%' src='https://img001.prntscr.com/file/img001/8LoVwwFRTzOrRGZwK_exgg.png'/>

2- by measure any change in Rotation by the gyro

    if (g.gyro.y > 0.45) { 
    digitalWrite(4, HIGH);
    digitalWrite(2,LOW); 
    delay(100);
    Serial.print("Accident detect on gyro  : "); 
    Serial.print(g.gyro.y);                    
    digitalWrite(4, LOW);
    digitalWrite(2,LOW);  
    delay(100);
    };
 
<img width='50%' src='https://img001.prntscr.com/file/img001/GRhQyPLESw6kxD3F0_3fJQ.png'/>

 3- by measure any change in temperature 
 
    if (temp.temperature > 45) { 
    digitalWrite(4, HIGH);
    digitalWrite(2,LOW); 
    delay(100);
    Serial.print("temprature is HIGH   : "); 
    Serial.print(temp.temperature);                    
    digitalWrite(4, LOW);
    digitalWrite(2,LOW);  
    delay(100);
    };
    
<img width='50%' src='https://img001.prntscr.com/file/img001/7QWsx3l3QdeilpaXLUOuYg.png'/>

## cloud side  
Front-end `using Github Pages`

<img width='50%' src='https://img001.prntscr.com/file/img001/ShpI3edLSVKgu5-Ut5p0sg.png'/>

Back-end `using Github Pages`

<img width='50%' src='https://img001.prntscr.com/file/img001/2oWur0Y-SKOqoCYATWw5TQ.png'/>

# significant benefits in real-life situations

The project "Revolutionizing Accident Reporting: Automated Vehicular Incident Detection and Analysis with Drone and Cutting-Edge Technologies" will have significant benefits in real-life situations, particularly in emergency response and accident management.

Firstly, the automated detection and analysis of vehicular incidents using drones and advanced technologies will significantly reduce the response time of emergency services. With real-time data capture and analysis, emergency responders can quickly assess the situation, deploy the appropriate resources, and provide timely medical attention to victims. This rapid response could potentially save lives and reduce the severity of injuries.

Secondly, the project's automated incident detection and analysis capabilities will provide more accurate and reliable data for accident reporting. This data can be used by policymakers and city planners to identify high-risk areas, formulate effective safety policies, and allocate resources to prevent future accidents. This information can also be used by insurance companies to more accurately assess accident claims, potentially leading to faster and fairer compensation for victims.

Lastly, the project's innovative approach to accident reporting will help reduce the economic burden of accidents. By reducing the response time of emergency services, providing accurate data for accident reporting, and improving safety policies and practices, this project has the potential to reduce the costs associated with accidents, such as medical expenses, vehicle repair costs, and lost productivity.

In summary, the project's automated incident detection and analysis capabilities, enabled by drones and advanced technologies, will have significant benefits in real-life situations, including faster emergency response times, more accurate accident reporting, and reduced economic burden. These outcomes have the potential to save lives, reduce costs, and improve public safety.
