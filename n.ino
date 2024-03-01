#include <Stepper.h> 
#define STEPS 200
#define btn1 8
#define btn2 9
#define main_btn 10
int dir = 2; // 1 - forward, 0, backward, 2 - stop
int speed = 250;
int time_for_delay = 500;
int step = 10;
int count = 0;
Stepper stepper(STEPS, 2, 3);
void setup() {
  stepper.setSpeed(speed);
  Serial.begin(9600);
  pinMode(btn1, INPUT_PULLUP);
  pinMode(btn2, INPUT_PULLUP);
  pinMode(main_btn, INPUT_PULLUP);
  calibri();
}

void calibri() {
  while (digitalRead(btn1) != 0) {
    stepper.step(-step);
  }
  dir = 2;
  stepper.step(200);
  delay(1000);
}
void loop() {
  
  // set direction
  if (digitalRead(btn1) == 0) {
    dir = 0;
    delay(time_for_delay);
  } else if (digitalRead(btn2) == 0) {
    dir = 1;
    delay(time_for_delay);
  } if (digitalRead(main_btn) == 0) {
    if (dir == 2) {
      dir = 0;
    } else {
      dir = 2;
    } 
    delay(time_for_delay);
  }
  Serial.print(dir);
  if (dir == 0) {
    stepper.step(step);
  } else if (dir == 1) {
    stepper.step(-step);
  } else if (dir == 2) {
    stepper.step(0);
  }
  count += step;
  Serial.println(count);
}