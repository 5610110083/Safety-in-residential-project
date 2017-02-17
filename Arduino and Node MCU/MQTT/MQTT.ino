#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char *ssid =	"siczones";
const char *pass =	"1234567896";

String MQTT_server("m10.cloudmqtt.com");
String MQTT_username = "pzhdyhzb";
String MQTT_password = "8CTJmtD7Hmbz";
String MQTT_topic = "compiler/data";
String MQTT_sub = "compiler/data";
int MQTT_port = 19587;

uint8_t led_pin = D0;

void callback(const MQTT::Publish& pub) {
  String payload = pub.payload_string();
  if (payload == "ON") {
    digitalWrite(led_pin, 1);
    Serial.println("TURN ON");
    Serial.println("==============================");
  } else if (payload == "OFF"){
    digitalWrite(led_pin, 0);
    Serial.println("TURN OFF");
    Serial.println("==============================");
  }
}

WiFiClient wclient;
PubSubClient client(wclient, MQTT_server, MQTT_port);

void setup() {
  Serial.begin(115200);
  pinMode(12, OUTPUT);
  delay(10);
  Serial.println();
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    WiFi.begin(ssid, pass);
    Serial.print("Connecting to ");
    Serial.print(ssid);
    Serial.println();
    while (WiFi.status() != WL_CONNECTED) {
      Serial.print(".");
      delay(50);
    }
    Serial.println();
    Serial.println("WiFi connected");
  }
  if (!client.connected()) {
      Serial.println("Connecting to MQTT server");
    while (!client.connect(MQTT::Connect("ESP8266-12").set_auth(MQTT_username, MQTT_password))) {
      Serial.print(".");
      delay(10);
    }
      Serial.println();
      Serial.println("Connected MQTT");
  } else {
      client.set_callback(callback);

    while (!client.publish(MQTT_topic,"hello world")) {
      delay(10);
    }
      Serial.print("Publish to ");
      Serial.print(MQTT_topic);
      Serial.println();
      Serial.println("==============================");
    while (!client.subscribe(MQTT_sub)) {
      delay(10);
    }
  }
  if (client.connected()){
      delay(1000);
      client.loop();
  }
}
