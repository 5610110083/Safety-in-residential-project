#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

WiFiUDP Udp;

const char* ssid = "ranee";
const char* password = "1234567896";

IPAddress local_ip = {192,168,1,200};
IPAddress gateway = {192,168,1,1};
IPAddress subnet = {255,255,255,0};

int relayPin = 5;
int ledPin = 16;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(10);
  
  pinMode(relayPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  digitalWrite(relayPin, LOW);
  digitalWrite(ledPin, HIGH);
       
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA); 
  WiFi.begin(ssid, password);
  //if not need fix ip please comment
  //WiFi.config(local_ip, gateway, subnet);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  // Start the server
  Udp.begin(49999);
  Serial.println("UDP Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());

}

void loop() {

// Check if a client has connected
  Udp.parsePacket();
  while(Udp.available()){
    Serial.print(Udp.remoteIP());
    Serial.print(" : ");
    String req = Udp.readStringUntil('\r');
    //char req = Udp.read();
    Serial.println(req);
    if (req.indexOf("on") != -1) {
       digitalWrite(relayPin, HIGH);
       digitalWrite(ledPin, LOW);
    }
    if (req.indexOf("off") != -1) {
       digitalWrite(relayPin, LOW);
       digitalWrite(ledPin, HIGH);       
    }
       
    Udp.flush();
    delay(5);
  }
 
}

