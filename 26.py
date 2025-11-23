import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

while True:
    command = input("Enter command (ON/OFF): ").strip()
    if command in ["ON", "OFF"]:
        ser.write((command + '\n').encode())
        print(f"Sent: {command}")
    else:
        print("Invalid command. Enter ON or OFF.")


# Arduino Code
#define LED_PIN 13

# void setup() {
#   Serial.begin(9600);
#   pinMode(LED_PIN, OUTPUT);
# }

# void loop() {
#   if (Serial.available() > 0) {
#     String command = Serial.readStringUntil('\n');
#     command.trim();
#     if (command == "ON") {
#       digitalWrite(LED_PIN, HIGH);
#       Serial.println("LED Turned ON");
#     } else if (command == "OFF") {
#       digitalWrite(LED_PIN, LOW);
#       Serial.println("LED Turned OFF");
#     }
#   }
# }
