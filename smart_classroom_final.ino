#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
#include <SPI.h>
#include <MFRC522.h>        //include RFID library
#include <Wire.h> 
#define SS_PIN 53 //RX slave select
#define RST_PIN 6

//******************************************************************************************************************
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.
String CardID="";
int condition = 0;
#include <Servo.h>
Servo myservo;
Servo myservo1;
int temperature;
int sure = 0;
void setup() {
 pinMode(A0,INPUT);
 pinMode(A1,INPUT_PULLUP);
 pinMode(A2,INPUT_PULLUP);
 pinMode(A3,INPUT_PULLUP);
 pinMode(A4,INPUT);
 pinMode(A5,INPUT);
 pinMode(22,OUTPUT);//White 
 pinMode(23,OUTPUT);//white
 pinMode(24,OUTPUT);//lamp
 pinMode(25,OUTPUT);//fan
 myservo.attach(8);
 myservo1.attach(9);
 myservo.write(90);
 myservo1.write(90);
 delay(1000);
 digitalWrite(22,HIGH);
 digitalWrite(23,HIGH);
 digitalWrite(24,HIGH);
 digitalWrite(25,HIGH);
 delay(1000);
   Serial.begin(9600);
   SPI.begin();  // Init SPI bus
   mfrc522.PCD_Init(); // Init MFRC522 card
   lcd.begin(16, 2);
   lcd.setCursor(0, 0);
   lcd.print("     Welcome    ");
   lcd.setCursor(0, 1);
   lcd.print(" Smart classroom");
   delay(3000);
   lcd.clear();
}

void loop() {
   lcd.setCursor(0, 0);
   lcd.print("     Welcome    ");
   lcd.setCursor(0, 1);
   lcd.print(" Show your card ");
   if (condition == 1)
  {
     int val0=analogRead(A0);
 int val1=digitalRead(A1);
  int val2=digitalRead(A2);
  int val3=digitalRead(A3);
  int val4=analogRead(A4);//rain
   int val5=analogRead(A5);//temperature
   temperature = val5* 0.49;
   //Serial.print("tem =");
  //Serial.println(temperature);
  delay(10);
 if(val1==0){
  digitalWrite(22,LOW);
  delay(25000);
  digitalWrite(22,HIGH);
   digitalWrite(23,LOW);
   delay(25000);
   digitalWrite(23,HIGH);
 }
 else{
 digitalWrite(22,HIGH);
 digitalWrite(23,HIGH);
 }
 if((val2==0)&&(val4>700)){
 myservo.write(30);
 myservo1.write(150);

 }
 else{
 myservo.write(90);
 myservo1.write(90);
 }
 //Serial.println(val4);
 if(val0<100){
  if(val3==0){
  digitalWrite(24,HIGH);
  delay(1000);
 }
 else{
  digitalWrite(24,LOW);
  delay(1000);
 }
 }
 else{
  digitalWrite(24,HIGH);
 }
 
   
    if ( temperature > 90){
    sure = sure + 1;
    if(sure > 5)
    {
    digitalWrite(25,LOW);
    delay(3000);
    digitalWrite(25,HIGH);
    delay(1000);
    sure = 0;
    }
  }
  else{
    digitalWrite(25,HIGH);
  }
  }
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  //Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     //Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     //Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  //Serial.println();
  //Serial.print("Message : ");
  content.toUpperCase();
   if (content.substring(1) == "0A 44 A8 16" ) //change here the UID of the card/cards that you want to give access
  {
    Serial.println("student id 1");
    lcd.setCursor(0, 0);
    lcd.print("Student id 1    ");
    lcd.setCursor(0, 1);
    lcd.print("        recorded");
    delay(3000);
    lcd.clear();
    condition = 1;
  }
   else if (content.substring(1) == "9A 14 96 16" ) //change here the UID of the card/cards that you want to give access
  {
    Serial.println("student id 2");
    lcd.setCursor(0, 0);
    lcd.print("Student id 2    ");
    lcd.setCursor(0, 1);
    lcd.print("        recorded");
    delay(3000);
    lcd.clear();
    condition = 1;
  }
  else if (content.substring(1) == "0A 7B A3 16" ) //change here the UID of the card/cards that you want to give access
  {
    Serial.println("student id 3");
    lcd.setCursor(0, 0);
    lcd.print("Student id 3    ");
    lcd.setCursor(0, 1);
    lcd.print("        recorded");
    delay(3000);
    lcd.clear();
    condition = 1;
  }
  else if (content.substring(1) == "CA 68 9B 16" ) //change here the UID of the card/cards that you want to give access
  {
    Serial.println("student id 4");
    lcd.setCursor(0, 0);
    lcd.print("Student id 4    ");
    lcd.setCursor(0, 1);
    lcd.print("        recorded");
    delay(3000);
    lcd.clear();
    condition = 1;
  }
  else if (content.substring(1) == "3A 55 9E 16" ) //change here the UID of the card/cards that you want to give access
  {
    Serial.println("student id 5");
    lcd.setCursor(0, 0);
    lcd.print("Student id 5    ");
    lcd.setCursor(0, 1);
    lcd.print("        recorded");
    delay(3000);
    lcd.clear();
    condition = 1;
  }
}
