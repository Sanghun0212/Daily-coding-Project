// ----- Pin settings -----
const int LDR_PIN    = A0;  // LDR sensor pin (analog)
const int LED_PIN    = 8;   // LED pin (digital)
const int BUZZER_PIN = 9;   // Buzzer pin (digital)

// ----- Threshold -----
int threshold = 400;  // Adjust this value after checking Serial Monitor

void setup() {
  // Serial for debugging
  Serial.begin(9600); // Serial Monitor 9600 baud

  // Pin modes
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  // 1. Read LDR value
  int ldrValue = analogRead(LDR_PIN); // range: 0 ~ 1023

  // 2. Print to Serial Monitor
  Serial.print("LDR value: ");
  Serial.println(ldrValue);

  // 3. Compare with threshold
  if (ldrValue < threshold) {
    // Dark environment
    digitalWrite(LED_PIN, HIGH);        // Turn LED ON
    tone(BUZZER_PIN, 1000);   
    // int freq = map(ldrValue, 0, 1023, 2000, 200);

    // tone(BUZZER_PIN, freq);
              // Play 1000 Hz tone
  } else {
    // Bright environment
    digitalWrite(LED_PIN, LOW);         // Turn LED OFF
    noTone(BUZZER_PIN);                 // Stop tone
  }

  // Small delay for stability
  delay(100); // 100 ms
}