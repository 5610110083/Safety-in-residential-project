/**
 *  MotionReport.ino
 *
 *  Created on: 22.10.2016
 *  by siczones
 *  
 *  Analog input : D2 
 */

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>

#define USE_SERIAL Serial

ESP8266WiFiMulti WiFiMulti;
const char* ssid     = "siczones";
const char* password = "1234567896";

//define input pin
int data_in = D2;
//define number of input sensor
int num_data_in = 1;

void setup() {
    //pinMode(LED_BUILTIN, OUTPUT);
    USE_SERIAL.begin(115200);
   // USE_SERIAL.setDebugOutput(true);
    pinMode(LED_BUILTIN, OUTPUT);     // Initialize the LED_BUILTIN pin as an output
    pinMode(data_in, INPUT);

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
        // -- Photo section --
        // Read input analog detect value
        int status = analogRead(data_in);
        // devide 10 levels
        status = (status/1023)*(10); 
        status = (status-10)*(-1);
        Serial.print("Status: ");
        Serial.print(status);
  
        // Upload data to server
        HTTPClient http;
        USE_SERIAL.print("\n[HTTP] begin...\n");
        // configure traged server and url
        //http.begin("https://192.168.1.12/test.html", "7a 9c f4 db 40 d3 62 5a 6e 21 bc 5c cc 66 c8 3e a1 45 59 38"); //HTTPS
        String host = "http://172.30.142.209/cgi-bin/UploadThingSpeakWithSensor.py?key=abcd";
        String url[num_data_in];
        url[0] = host + "&Field8=" + status;
        
        for(int i=0; i<num_data_in; i++){
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
            delay(4000);
            digitalWrite(LED_BUILTIN, HIGH); 
            delay(3000);  
            digitalWrite(LED_BUILTIN, LOW);
            delay(4000);
            digitalWrite(LED_BUILTIN, HIGH); 
            delay(3000);  
        }    
    }
    else{
        Serial.println("Wi-Fi is not connect!");
        // -- Photo section --
        // Read input analog detect value
        int status = analogRead(data_in);
        // devide 10 levels
        status = (status/1023)*(10); 
        status = (status-10)*(-1);
        Serial.print("Status: ");
        Serial.println(status);
        
        digitalWrite(LED_BUILTIN, LOW);
        delay(250);       
        digitalWrite(LED_BUILTIN, HIGH); 
        delay(250);  
    }
}

