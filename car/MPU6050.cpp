#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
Adafruit_MPU6050 mpu;
void setup(void) {
  pinMode(2,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
	Serial.begin(115200);
	// Try to initialize!
	if (!mpu.begin()) {
		Serial.println("Failed to find MPU6050 chip");
		while (1) {
		  delay(10);
    
		}
	}
	Serial.println("MPU6050 Found!");
	// set accelerometer range to +-8G
	mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
	// set gyro range to +- 500 deg/s
	mpu.setGyroRange(MPU6050_RANGE_500_DEG);
	// set filter bandwidth to 21 Hz
	mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
	delay(100);
}
void loop() {
	/* Get new sensor events with the readings */
	sensors_event_t a, g, temp;
	mpu.getEvent(&a, &g, &temp);        
	/* Print out the values */
	Serial.print("Acceleration X: ");
	Serial.print(a.acceleration.x);
	Serial.print(", Y: ");
	Serial.print(a.acceleration.y);
	Serial.print(", Z: ");
	Serial.print(a.acceleration.z);
	Serial.println(" m/s^2");
	Serial.print("Rotation X: ");
	Serial.print(g.gyro.x);
	Serial.print(", Y: ");
	Serial.print(g.gyro.y);
	Serial.print(", Z: ");
	Serial.print(g.gyro.z);
	Serial.println(" rad/s");
	Serial.print("Temperature: ");
	Serial.print(temp.temperature);
	Serial.println(" C");
	Serial.println("");
  digitalWrite(2,HIGH);
  digitalWrite(2,LOW);
  delay(150);
  digitalWrite(2,LOW);
  digitalWrite(2,HIGH);
  delay(100);
	delay(500);
  
  if (g.gyro.x > 0.45 or g.gyro.x < -0.45) { 
  digitalWrite(4, HIGH); 
  digitalWrite(2,LOW);
  delay(100);
  Serial.print("Accident detect on gyro : ");
  Serial.print(g.gyro.y);                      
  digitalWrite(4, LOW);
  digitalWrite(2,LOW);  
  delay(100);
  };
  if (g.gyro.y > 0.45 or g.gyro.y < -0.45) { 
  digitalWrite(4, HIGH); 
  digitalWrite(2,LOW);
  delay(100);
  Serial.print("Accident detect on gyro : ");
  Serial.print(g.gyro.y);                      
  digitalWrite(4, LOW);
  digitalWrite(2,LOW);  
  delay(100);
  };
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

  if (temp.temperature > 45) { 
  digitalWrite(4, HIGH);
  digitalWrite(2,LOW); 
  delay(100);
  Serial.print("temprature is HIGH : "); 
  Serial.print(temp.temperature);                     
  digitalWrite(4, LOW);
  digitalWrite(2,LOW);  
  delay(100);
  };
}
