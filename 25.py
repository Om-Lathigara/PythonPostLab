import serial
import time

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

message = "Hello Arduino!"
arduino.write(message.encode())
print("Message sent:", message)

arduino.close()

# Arduino Code
# void setup() {
#   Serial.begin(9600);
# }

# void loop() {
#   if (Serial.available()) {
#     String msg = Serial.readString();
#     Serial.println("Received: " + msg);
#   }
# }
