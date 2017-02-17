/**
 * tempReport.ino
 *
 *  Created on: 20.10.2016
 *  by siczones
 */

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>

#include "DHT.h"

#define DHTPIN D2     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11
#define USE_SERIAL Serial

ESP8266WiFiMulti WiFiMulti;
const char* ssid     = "siczones";
const char* password = "1234567896";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
    //pinMode(LED_BUILTIN, OUTPUT);
    USE_SERIAL.begin(115200);
   // USE_SERIAL.setDebugOutput(true);
    pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
    dht.begin();
    
    USE_SERIAL.println();
    USE_SERIAL.println();
    USE_SERIAL.println();
    
    for(uint8_t t = 4; t > 0; t--) {
        USE_SERIAL.printf("[SETUP] WAIT %d...\n", t);
        USE_SERIAL.flush();
        delay(500);       
    }
    WiFiMulti.addAP(ssid, password);
}

void loop() {
    // wait for WiFi connection
    if((WiFiMulti.run() == WL_CONNECTED)) {
        // DHT section
        float humidity = dht.readHumidity();
        // Read temperature as Celsius (the default)
        float temperature = dht.readTemperature();
        Serial.print("Humidity: ");
        Serial.print(humidity);
        Serial.print(" %\t");
        Serial.print("Temperature: ");
        Serial.print(temperature);
  
        HTTPClient http;

        USE_SERIAL.print("\n[HTTP] begin...\n");
        // configure traged server and url
        //http.begin("https://192.168.1.12/test.html", "7a 9c f4 db 40 d3 62 5a 6e 21 bc 5c cc 66 c8 3e a1 45 59 38"); //HTTPS
        String host = "http://siczones.coe.psu.ac.th/cgi-bin/UploadThingSpeakWithSensor.py?key=abcd";
        String url[2];
        url[0] = host + "&Field7=" + temperature;
        url[1] = host + "&Field3=" + humidity;
        
        for(int i=0;i < 2;i++){
            http.begin(url[i]); //HTTP
    
            USE_SERIAL.print("[HTTP] GET...\n");
            // start connection and send HTTP header
            int httpCode = http.GET();
    
            // httpCode will be negative on error
            if(httpCode > 0) {
                // HTTP header has been send and Server response header has been handled
                USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);
    
                // file found at server
                if(httpCode == HTTP_CODE_OK) {
                    String payload = http.getString();
                    USE_SERIAL.println(payload);
                }
            } else {
                USE_SERIAL.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
            }
            
            http.end();
            digitalWrite(LED_BUILTIN, LOW);
            delay(6000);
            digitalWrite(LED_BUILTIN, HIGH); 
            delay(4000);  
        }    
    }
    else{
        Serial.println("=================================================================");
        Serial.println(".......................Wi-Fi is not connect!.....................");
        Serial.println("=================================================================");
        // DHT section
        float humidity = dht.readHumidity();
        // Read temperature as Celsius (the default)
        float temperature = dht.readTemperature();
        Serial.print("Humidity: ");
        Serial.print(humidity);
        Serial.print(" %\t");
        Serial.print("Temperature: ");
        Serial.println(temperature);
        //Serial.println("=================================================================");
        digitalWrite(LED_BUILTIN, LOW);
        delay(250);       
        digitalWrite(LED_BUILTIN, HIGH); 
        delay(250);  
    }
}

