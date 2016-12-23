// analogRead.ino
int led = 13;
void setup() {
	pinMode(led, OUTPUT);
	Serial.begin(9600);
}

void loop() {
	int val = analogRead(A0);
  Serial.println(val);
	analogWrite(3, map(val, 0, 1023, 1023, 0));
	delay(100);
}

