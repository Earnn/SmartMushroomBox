#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>
#include "DHT.h"
////////////////////////////////////////////////////////////////////////////////
//////////Define Pin///////////////////////////////////////////////////////////
#define USE_SERIAL Serial
int DHTPIN = 2;          //setpin of DHT at D0
int DHTTYPE = DHT22;     //set Dht Type 
/////////////////-----------------------------------//////////////////////////
int Cooler = 4;             //setpin of Refrigeratoe at D2
int Pump = 5;               //setpin of pump to D1
int Led_Red = 14;            //setpin of Led Red at D5
int Led_Green = 12;            //setpin of Led Red at D6
int Led_Blue = 13;            //setpin of Led Red at D7
///////////////////////////////////////////////////////////////////////////////
void SendData(float h , float t);     //Define Senddata Voide
void OnCooler();
void OffCooler();
void OnPump();
void OffPump();
void NoNet(float t,float h,int Tempcom,int Humicom,int Ontime,int Tempcom2,int Humicom2,int vred,int vgreen,int vblue);
unsigned long timet;
////////////Setup//////////////////////////////////////////////////////////////

const char* ssid     = "true_home2G_792";            //Set ssid
const char* password = "ilovestudy";                    //Set Password
const char* Server   = "192.168.1.55";                //set Server Domain or Server ip
const char* Port     = "8001";                         //Set Port
const char* Key      = "2345678909876543234567898765"; //Set Key
const char* Id       = "7212364994";
DHT dht(DHTPIN, DHTTYPE);                             //Start DHT
ESP8266WiFiMulti WiFiMulti;


void setup() 
{
    USE_SERIAL.begin(115200);
      for(uint8_t t = 6; t > 0; t--) 
      {
        USE_SERIAL.printf("[SETUP] WAIT %d...\n", t);
        USE_SERIAL.flush();
        delay(1000);
      }
    WiFiMulti.addAP(ssid, password);    //Set SSID and Password (SSID, Password)
    WiFi.begin(ssid, password);         //Set starting for Wifi
    Serial.println(WiFi.localIP());
    dht.begin();

    ////////////////////////////////SetuoPinMode//////////////////////////////////////////
    pinMode(Led_Red, OUTPUT);
    pinMode(Led_Green, OUTPUT);
    pinMode(Led_Blue, OUTPUT);
    pinMode(Pump,OUTPUT);
    pinMode(Cooler,OUTPUT);
    
                                            
}

////////////////////Loop////////////////////////////////////////////////////////////////////

void loop() 
{
   //float h = dht.readHumidity();      //Read Humidity
   //float t = dht.readTemperature();   //Read Temperature
   float t = 25.30;                                                  ////<<<<<<TEST VALUE
   float h = 50.99;                                                  ////<<<<<<TEST VALUE
   Serial.print("TEMPERATURE");
   Serial.println(t);
   Serial.print("HUMIDITY");
   Serial.println(h);
   if (isnan(t) || isnan(h)) 
  {
    Serial.println("FaiLed to read from DHT");
  } 
  else 
  {
    SendData(h,t);
  }
  Serial.print("Time: ");
  timet = millis();
  Serial.println(timet);
  delay(5000);
}

///////////////////////SednData//////////////////////////////////////////////////////////////////
void SendData(float h,float t) 
{
  int vred;
  int vgreen;
  int vblue;
  int Tempcom;
  int Humicom;
  int Tempcom2;
  int Humicom2;
  int Ontime;  
  // wait for WiFi connection
    if((WiFiMulti.run() == WL_CONNECTED)) 
    {
        HTTPClient http;
        //String str = "http://" +String(Server)+":5000" +"/data/" + String(t)+"/"+String(h);
        String str = "http://" +String(Server)+":"+String(Port)+"/control"+"/data/"+String(Id)+"/"+ String(t)+"/"+String(h)+"/"+String(Key)+"/";
        Serial.println(str);
        http.begin(str);
        int httpCode = http.GET();
        USE_SERIAL.printf("[HTTP] GET... code: %d\n", httpCode);
        if(httpCode > 0) 
        {
            if(httpCode == HTTP_CODE_OK) 
              {
                String payload = http.getString();
                
      //-------------------Control----------------------------//
                USE_SERIAL.print("payload");
                USE_SERIAL.println(payload);
                String getTempCom = payload.substring(0,3);
                String getHumiCom = payload.substring(4,7);
                String getOntime = payload.substring(8,11);
                String getTempCom2 = payload.substring(12,15);
                String getHumiCom2 = payload.substring(16,19);
                String Red = payload.substring(20,23);
                String Green = payload.substring(24,27);
                String Blue = payload.substring(28,31);
                int vred = Red.toInt();
                int vgreen = Green.toInt();
                int vblue = Blue.toInt();
                int Tempcom = getTempCom.toInt();
                int Humicom = getHumiCom.toInt();
                int Tempcom2 = getTempCom2.toInt();
                int Humicom2 = getHumiCom2.toInt();
                int Ontime = getOntime.toInt();
                //Serial.print("temp_onlight");
                Serial.println(Tempcom);
                Serial.println(Humicom);
                Serial.println(Ontime);
                Serial.println(Tempcom2);
                Serial.println(Humicom2);
                Serial.println(vred);
                Serial.println(vgreen);
                Serial.println(vblue);
                timet = millis();
  int timeHr = timet/3600000;
  Serial.print("Time_Hr");
  Serial.println(timeHr);
  if(Ontime<timeHr)
  {
                if(t<Tempcom)
                {
                  OnCooler();
                }
                else
                {
                  OffCooler();
                }
                if(h<Humicom)
                {
                  OnPump();
                }
                else
                {
                  OffPump();
                }
                analogWrite(Led_Red,vred);
                analogWrite(Led_Green,vgreen);
                analogWrite(Led_Blue,vblue);
  }
  if(Ontime>=timeHr)
  {
    if(t<Tempcom2)
     {
      OnCooler();
     }
     else
     {
      OffCooler();
     }
     if(h<Humicom2)
     {
      OnPump();
     }
      else
     {
     OffPump();
     }
     int closelight = 0;
     analogWrite(Led_Red,closelight);
     analogWrite(Led_Green,closelight);
     analogWrite(Led_Blue,closelight);
  }
              }
              else
              {
                NoNet(t,h,Tempcom,Humicom,Ontime,Tempcom2,Humicom2,vred,vgreen,vblue);
              }
          }
          else
          {
            NoNet(t,h,Tempcom,Humicom,Ontime,Tempcom2,Humicom2,vred,vgreen,vblue);
          }
        http.end();
    }
    else
    {
     NoNet(t,h,Tempcom,Humicom,Ontime,Tempcom2,Humicom2,vred,vgreen,vblue);
    }
    delay(500);
}

void NoNet(float t,float h,int Tempcom,int Humicom,int Ontime,int Tempcom2,int Humicom2,int vred,int vgreen,int vblue)
{
  Serial.println("No-Net");
  timet = millis();
  int timeHr = timet/3600000;
  Serial.print("Time_Hr");
  Serial.println(timeHr);
  if(Ontime<timeHr)
  {
                if(t<Tempcom)
                {
                  OnCooler();
                }
                else
                {
                  OffCooler();
                }
                if(h<Humicom)
                {
                  OnPump();
                }
                else
                {
                  OffPump();
                }
                analogWrite(Led_Red,vred);
                analogWrite(Led_Green,vgreen);
                analogWrite(Led_Blue,vblue);
  }
  if(Ontime>=timeHr)
  {
    if(t<Tempcom2)
     {
      OnCooler();
     }
     else
     {
      OffCooler();
     }
     if(h<Humicom2)
     {
      OnPump();
     }
      else
     {
     OffPump();
     }
     int closelight = 0;
     analogWrite(Led_Red,closelight);
     analogWrite(Led_Green,closelight);
     analogWrite(Led_Blue,closelight);
  }
                
}

////////////////OnCooler//////////////////////////////////////////////////////////////

void OnCooler()
{
  digitalWrite(Cooler,HIGH);
  //delay(100);                   //Set Delay for Refrigterator
}

/////////////////OffCooler//////////////////////////////////////////////////////////////

void OffCooler()
{
  digitalWrite(Cooler,LOW);
  delay(100);
}

//////////////////OnPump//////////////////////////////////////////////////////////////////

void OnPump()
{
  digitalWrite(Pump,HIGH);
}
////////////////OffPump///////////////////////////////////////////////////////////////////

void OffPump()
{
  digitalWrite(Pump,LOW);
}


