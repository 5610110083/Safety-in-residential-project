// analogRead.ino

void setup() {
	Serial.begin(9600);
}

void loop() {
	int val = analogRead(D2);
	Serial.println(val);
  
	delay(1000);
}

