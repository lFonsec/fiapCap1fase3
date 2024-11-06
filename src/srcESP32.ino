#include <DHT.h>


int fosforoPin = 23;
int potassioPin = 4;
int ldrPin = 33;
int pinoDHT =  32;
int relePin = 2;
int releState = false;
DHT dht(pinoDHT, DHT22);

void setup() {
  Serial.begin(115200);
  // inicia o sensor dht
  dht.begin();
  //inicia o pin do rele
  pinMode(relePin, OUTPUT);
  //inicia os botoes
  pinMode(fosforoPin, INPUT_PULLUP);
  pinMode(potassioPin, INPUT_PULLUP);

}

void loop() {
  //pega o calor da temperatura e da umidade
  float temp = dht.readTemperature();
  float umi = dht.readHumidity();
  // pega o valor do sensor ldr
  int ldrvalue = analogRead(ldrPin);
  // seta os botoes do fosforo e do potassio
  int fosforoState = HIGH;
  fosforoState = digitalRead(fosforoPin);
  int postassioState = HIGH;
  postassioState = digitalRead(potassioPin);

  // imprime o valor da temperatura e da umidade
  Serial.print("Temperatura: ");
  Serial.print(temp);
  Serial.println("°C");
  Serial.print("Umidade: ");
  Serial.print(umi);
  Serial.println("%");

  // detecta se os botoes foram pressionados
  if(fosforoState == LOW){
    Serial.println("Fosforo apertado ");
  }
  if(postassioState == LOW){
    Serial.println("Postassio apertado");
  }

  //caso a temperatura esteja acima dos 35 graus ou a umidade esteja abaixo dos 45 
  // o rele ira ativar o led vermelho sinalizando o começo do processo de irrigação
  if(temp > 35 || umi < 45){
    digitalWrite(relePin, HIGH);
    Serial.println("Bombas de irrigação ligadas");
  } else {
    digitalWrite(relePin, LOW);
    Serial.println("Bombas de irrigação desligadas");
  }
  Serial.println("-------");

  delay(2000);
}
