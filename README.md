# About 
Automated Accident Reporting with Drones and Advanced Technologies is a cutting-edge solution aimed at revolutionizing the way vehicular accidents are reported. This innovative approach leverages the power of drones and advanced technologies to accurately and quickly gather crucial information about accidents and their aftermath. With the ability to quickly survey the scene and capture data such as the location of vehicles, road conditions, and other relevant information, this solution can provide a much more efficient and effective way of reporting accidents. By reducing the time it takes to gather information, this solution can help first responders more effectively respond to accidents, which can in turn save lives and reduce the severity of injuries. Additionally, the data collected can be used to help improve road safety and prevent future accidents from occurring. With the use of advanced technologies and drones, this solution represents a major step forward in accident reporting and is poised to transform the way we respond to vehicular accidents.

## Block Diagram of the Project
<img width='100%' src='https://img001.prntscr.com/file/img001/qhsreyFZTXC3yQcBY01kug.png'/>


## Hardware used 

- MPU6050
- Arduino Uno
- GPS/GSM
- Tempruture Sensor `included inside the MPU6050`

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
