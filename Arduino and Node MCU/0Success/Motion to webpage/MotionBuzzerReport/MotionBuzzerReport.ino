/**
 *  MotionReport.ino
 *
 *  Created on: 5.11.2016
 *  by siczones
 *
 *  NodeMCU : Motion pin : D2
 *            Buzzer pin : D3
 *            Led Alert pin : D1
 */

#include <Arduino.h>

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>

int ledPin = D1;
int motion = D2;
int buzzer = D3;

ESP8266WiFiMulti WiFiMulti;
const char* ssid     = "siczones";
const char* password = "1234567896";

int num_data_in = 1;  //define number of input sensor

void setup() {
    Serial.begin(115200);
    
    pinMode(LED_BUILTIN, OUTPUT);  // To show connection state
    pinMode(buzzer, OUTPUT);
    pinMode(ledPin, OUTPUT);
    pinMode(motion, INPUT);
    
    Serial.println();
    Serial.println();
    for(uint8_t t = 4; t > 0; t--) {
        Serial.printf("[SETUP] WAIT %d...\n", t);
        Serial.flush();
        delay(500);
    }
    //WiFiMulti.addAP(ssid, password);
}

void loop() {
    int value = digitalRead(motion);

    /*
    // LED Status when Wi-Fi not connect
    if(!(WiFiMulti.run() == WL_CONNECTED)) {
        digitalWrite(LED_BUILTIN, LOW);
        delay(250);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(250);
    }
    */
    
    if (value == HIGH)
    {
        Serial.println("High");
        digitalWrite(LED_BUILTIN, LOW);
        delay(1) ;

        // Play alarm from buzzer and LED blink
        for (int i = 0; i < 262; i++) {
            analogWrite(buzzer, i);
            if(i%4 == 0)
                digitalWrite(ledPin, HIGH);
            else
                digitalWrite(ledPin, LOW);
            delay(1);
        }
        for (int i = 30; i > 0; i--) {
            analogWrite(buzzer, i);
            delay(10);
        }
        /*
        if((WiFiMulti.run() == WL_CONNECTED)) {
            // -- Motion section --
            // Read input digital detect value
            int status = 1;

            // Upload data to server
            HTTPClient http;
            Serial.print("\n[HTTP] begin...\n");
            // configure traged server and url
            //http.begin("https://192.168.1.12/test.html", "7a 9c f4 db 40 d3 62 5a 6e 21 bc 5c cc 66 c8 3e a1 45 59 38"); //HTTPS
            String host = "http://172.30.142.209/cgi-bin/UploadThingSpeakWithSensor.py?key=abcd";
            String url;
            url = host + "&Field8=" + status;
            http.begin(url); //HTTP
            Serial.println("[HTTP] GET...\n");
            // start connection and send HTTP header
            int httpCode = http.GET();

            // httpCode will be negative on error
            if(httpCode > 0) {

                // HTTP header has been send and Server response header has been handled
                Serial.printf("[HTTP] GET... code: %d\n", httpCode);

                // file found at server
                if(httpCode == HTTP_CODE_OK) {
                    String payload = http.getString();
                    Serial.println(payload);
                }
            }
            else {
                Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
            }

            http.end();
        }
        */
    }
    else
    {
        Serial.println("Low");
        digitalWrite(LED_BUILTIN, HIGH);
        digitalWrite(ledPin, LOW);
        analogWrite(buzzer, LOW);
    }
}
