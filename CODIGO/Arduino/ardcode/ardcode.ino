String dataString = "";
bool dataComplete = false;
int data = 0;

void setup() {
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}
 
void loop() {
  
  if(dataComplete) {
    data = dataString.toInt();

    task();

    dataString = "";
    dataComplete = false;
  }

}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    dataString += inChar;
    if (inChar == '\n') {
      dataComplete = true;
    }
  }
}
