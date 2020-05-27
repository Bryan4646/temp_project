#include <iostream>
using namespace std;

int ledPin = 10;

void setup() {
    pinMode(ledPin, OUTPUT);
}


void tempachieved(){
    
    digitalWrite(ledPin, HIGH);
    delay(10000);
    digitalWrite(ledPin, LOW);
}

void tempnotachieved(){
    digitalWrite(ledPin, HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
}


void loop(){

    //Particle.publish("State", PRIVATE);
}