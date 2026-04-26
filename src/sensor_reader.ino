/* * ----------------------------------------------------------------------------
 * Project: Unique Tech Air Quality Visualization
 * Author: Unique Tech Team
 * License: MIT License
 * * Copyright (c) 2026 Unique Tech
 * * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * ----------------------------------------------------------------------------
 */

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
