int Messwert;
float Quellspannung = 5;
int R1 = 150000;                                  //Vorwiderstand mit 150000 Ohm
float U2;                                        //Zu berechnende Spannung
void setup() {
  pinMode(13, OUTPUT);                           //Pin 13 als Ausgang für Pumpe
}

void loop() {
 
  Messwert = 0;                                   //Ermittlung des Mittelwerts aus 5 Messwerten zur Vermeidung von Messfehlern
  for (int i = 0; i < 5; i++) {
    Messwert += analogRead(5);
  }
  Messwert = trunc(Messwert / 5);
  U2 = (Quellspannung / 1023.0) * Messwert;        //Berechnung der Spannung zwischen den Elektroden
  if (U2 < 2) {
    digitalWrite(13, HIGH);                       //Einschalten der Pumpe, falls Pflanze zu trocken
  }
  else{
    digitalWrite(13,LOW);                         //Auschalten der Pumpe, falls Pflanze genügend Wasser hat
  }
  
  delay (400);
}
