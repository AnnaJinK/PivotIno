/* 
|| @ file Pivot_Ino_V1.1.1.ino
|| @ author Heejoong 
|| # 2019-01-16 ~
|| @ 2019-01-27 edit? baud rate and rename some variables
*/
#include <MPU6050.h>
#define commandLine_OPEN "Rotate <"
#define commandLine_CLOSE ">"

//default I2C address 0x68
MPU6050 accelgyro;

int value = 0;
int16_t ax, ay, az;
int16_t gx, gy, gz;
const char * P_array[2];
const char * RotateMonitor(int x);

void setup() {
    Wire.begin();
    Serial.begin(115200);
    Serial.println("Initializing I2C devices...");
    accelgyro.initialize();
}

void loop() {
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    int mapped_ax = map(ax, -32768, +32767, -180, +180);
    //int mapped_ay = map(ay, -32768, +32767, -180, +180);
    //int mapped_az = map(az, -32768, +32767, -180, +180);

    P_array[0] = RotateMonitor(mapped_ax);
    if(P_array[value] != P_array[0]) {
      Serial.print(commandLine_OPEN);
      Serial.print(RotateMonitor(mapped_ax));
      Serial.println(commandLine_CLOSE);
      value = 0;
    }
    else { 
      P_array[1] = RotateMonitor(mapped_ax);
      value = 1;
    }
    delay(100);
}

const char * RotateMonitor(int x){
  if( x > -120 && x < -60) { return "Left"; }            //270 degrees
  else if(x > 60 && x < 120) { return "Right"; }       //90  degrees
  else { return "Idle"; }                             //0  degrees
}
