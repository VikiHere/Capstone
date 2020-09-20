#include<LiquidCrystal.h>
#include<SoftwareSerial.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int incomingByte = 0;

SoftwareSerial myser(10, 11);

void setup() {
    Serial.begin( 9600 );    //  baud rate 9600 for the serial Bluetooth communication
    myser.begin(9600);
    
    lcd.begin(16, 2);
    lcd.clear();
 
      lcd.setCursor(0,0); 
      lcd.print("Right");
      lcd.setCursor(0,1);
      lcd.print("Car Horn");
}
void loop() {
    if ( myser.available() > 0) {  
      
    // read a numbers from serial port
    int inputVal = myser.parseInt();
    Serial.println(String(inputVal));
    incomingByte = myser.read(); 
    //Serial.println(String(incomingByte));   
    if (inputVal == 1) { 
      lcd.clear();
      lcd.setCursor(0,0); 
      lcd.print("Right");
    }
    else if (inputVal == 2) { 
      lcd.clear();
      lcd.setCursor(0,0); 
      lcd.print("Left");
    }
    else if (inputVal == 4) { 
      lcd.clear();
      lcd.setCursor(0,0); 
      lcd.print("Front");
    }
    else{ //if (inputVal == 3) { 
      lcd.clear();
      lcd.setCursor(0,0); 
      lcd.print("Behind");
    }
    delay(100);
    }
}
