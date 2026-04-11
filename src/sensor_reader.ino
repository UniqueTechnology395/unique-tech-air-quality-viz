// Unique Tech - Sensor Data Sender
// Project: ACSTAC 2026 Innovation

void setup() {
  Serial.begin(9600); // Ξεκινάμε τη σειριακή επικοινωνία
  // Εδώ θα αρχικοποιούσατε τους αισθητήρες σας (π.χ. SCD4x ή PMS5003)
}

void loop() {
  // Προσομοίωση μετρήσεων (αντικαταστήστε με τις πραγματικές τιμές των αισθητήρων)
  float co2 = 400 + random(0, 100); 
  float temp = 22.0 + (random(0, 50) / 10.0);

  // Στέλνουμε τα δεδομένα σε μορφή: CO2,Temperature
  Serial.print(co2);
  Serial.print(",");
  Serial.println(temp);

  delay(2000); // Καθυστέρηση 2 δευτερολέπτων μεταξύ των μετρήσεων
}
