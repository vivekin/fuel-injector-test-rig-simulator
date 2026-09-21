int a;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  a=1;
}

void loop() {
  // put your main code here, to run repeatedly:
 if (a<=100)
 {
    Serial.println(a);
    a++;
    if(a==100)
    {a=1;}
  }
  delay(500); 
}
