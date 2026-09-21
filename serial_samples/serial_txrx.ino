int a;
int rpm;
int pressure;
int temp;
String statu;
String data;
void setup()
{
pinMode(13, OUTPUT);
  rpm=30;
  pressure=50;
  temp=20;
  statu="active";
  data="";
Serial.begin(9600);
while (!Serial);
Serial.println("Input 1 to Turn LED on and 2 to off");
}

void loop() {
    data ="rpm=";
    data+=rpm;
    data +=",pressure=";
    data+=pressure;
    data +=",temp=";
    data+=temp;
    data +=",status=";
    data+=statu;
    Serial.println(data);
    rpm++;pressure++;temp++;
    if(rpm==100)
    {rpm=30;}
    if(pressure==200)
    {pressure=50;}
    if(temp==70)
    {
      temp=20;
    statu="active";
    }
  delay(500); 
  
if (Serial.available())
{
String state = Serial.readString();
state.trim();
//Serial.println(state);
if (state == "1")
{
digitalWrite(13, HIGH);
Serial.println("Command completed LED turned ON");
}
else if (state == "2")
{
digitalWrite(13, LOW);
Serial.println("Command completed LED turned OFF");
}
else if (state == "stop" ||state == "STOP")
{
Serial.println("!!!!!!!!!!--STOP--!!!!!!!!!!");
statu="inactive";
}
else
{
  Serial.println("INVALID");
}
}
}
