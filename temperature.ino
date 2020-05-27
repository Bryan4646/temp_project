#include "Adafruit_DHT.h" //using Adafruit_DHT library

#define DHTPIN 2 //DHT connected to pin 2
#define DHTTYPE DHT22 //DHT 22 Model (AM2302)

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
    dht.begin();
    
}

void loop()
{
    delay (60UL * 60UL * 1000UL); //this code is used to delay by an hour each check by an hour.

    int t = dht.getTempCelcius();
    Spark.variable("temperature", &t, INT);
    Particle.publish("temp", String(t), PRIVATE);
}



   