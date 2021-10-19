#include "Wire.h"
#include <MPU6050_light.h>

MPU6050 mpu(Wire);

long timer = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  
  byte status = mpu.begin(2, 3);
  // stop everything if could not connect to MPU6050
  while(status!=0){ }
  
  mpu.setFilterGyroCoef(.9);
  
  // gyro and accelero
  mpu.calcOffsets(true,true); 
  Serial.println("Done!\n");
  
}

void loop() {
  mpu.update();
  Serial.print("x ");
  Serial.print(map(mpu.getAngleX(), 1000, -1000, 0, 360));
  Serial.print(" z ");
  Serial.print(map(mpu.getAngleZ(), -1000, 1000, 0, 360));
  Serial.println("");
  delay(10);
}
