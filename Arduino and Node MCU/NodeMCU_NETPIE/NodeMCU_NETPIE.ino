#include <AuthClient.h>
#include <MicroGear.h>
#include <MQTTClient.h>
#include <SHA1.h>
#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <EEPROM.h>
#include <MicroGear.h>

const char* ssid     = "WIFI-MAXNET";
const char* password = "macrol3ios";

#define APPID   "WebApp"
#define KEY     "24dxjlLA3LAvyWk"
#define SECRET  "aAU6wX2Iynl9KJXwNXW7fUSW8"
#define ALIAS   "esp8266"

WiFiClient client;
AuthClient *authclient;

int timer = 0;
MicroGear microgear(client);

/*----- Test send to webapp -----*/
int check_connected = 0;
char* test_message = "Hello World !";
/*-------------------------------*/

void onMsghandler(char *topic, uint8_t* msg, unsigned int msglen) {
    Serial.print("Incoming message --> ");
    char* readMsg = (char *)msg;
    msg[msglen] = '\0';
    Serial.println((char *)msg);

    if ((readMsg[0] == 'L') && (readMsg[5] == 'N')) {
//      Serial.println("LED ON");
      digitalWrite(D2, HIGH);
    }

    if ((readMsg[0] == 'L') && (readMsg[5] == 'F')) {
//      Serial.println("LED OFF");
      digitalWrite(D2, LOW);
    }
    
}

void onFoundgear(char *attribute, uint8_t* msg, unsigned int msglen) {
    Serial.print("Found new member --> ");
    for (int i=0; i<msglen; i++)
        Serial.print((char)msg[i]);
    Serial.println();  
}

void onLostgear(char *attribute, uint8_t* msg, unsigned int msglen) {
    Serial.print("Lost member --> ");
    for (int i=0; i<msglen; i++)
        Serial.print((char)msg[i]);
    Serial.println();
}

void onConnected(char *attribute, uint8_t* msg, unsigned int msglen) {
    Serial.println("Connected to NETPIE...");
    microgear.setName("esp8266");
}


void setup() {

    pinMode(D2, OUTPUT);

    microgear.on(MESSAGE,onMsghandler);
    microgear.on(PRESENT,onFoundgear);
    microgear.on(ABSENT,onLostgear);
    microgear.on(CONNECTED,onConnected);

    Serial.begin(115200);
    Serial.println("Starting...");

    if (WiFi.begin(ssid, password)) {

        while (WiFi.status() != WL_CONNECTED) {
            delay(500);
            Serial.print(".");
        }
    }

    Serial.println();
    Serial.println("WiFi connected");  
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    microgear.init(KEY,SECRET,ALIAS);
    microgear.connect(APPID);
}

void loop() {
  
    if (microgear.connected()) {

        if (check_connected != 1) {
          Serial.println("connected");
        }
        check_connected = 1;

        microgear.loop();
        if (timer >= 1000) {
            microgear.chat("htmlgear", test_message);
            timer = 0;
            
        } else {
          timer += 100;
        }
        
    } else {
        Serial.println("connection lost, reconnect...");
        if (timer >= 5000) {
            microgear.connect(APPID);
            timer = 0;
        } else {
          timer += 100;
        }
    }
    
    delay(100);
    
}