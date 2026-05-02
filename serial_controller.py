import serial
import time


class SerialController:
    def __init__(self):
        self.arduino = None

    def connect(self, port: str, baud_rate: int = 9600):
        self.arduino = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connection Success. Baud Rate = {baud_rate}")
        time.sleep(2)  # Allows Arduino to reset after connection opens.

    def disconnect(self):
        if self.arduino and self.arduino.is_open:
            self.arduino.close()
        print("Board has been disconnected.")

    def is_connected(self):
        return self.arduino is not None and self.arduino.is_open #True

    def send_command(self, command: str):
        if not self.is_connected():
            raise ConnectionError("Arduino is not connected.")

        self.arduino.write(command.encode("utf-8")) #Encode 

    def read_line(self):
        if self.is_connected() and self.arduino.in_waiting > 0:
            return self.arduino.readline().decode(errors="ignore").strip()

        return None