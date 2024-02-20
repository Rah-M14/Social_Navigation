import serial
from serial.tools import list_ports
import time

def find_arduino_port():
    arduino_ports = [p.device for p in list_ports.comports() if 'Arduino' in p.description]
    if not arduino_ports:
        print("Arduino not found. Please check the connection.")
        return None
    elif len(arduino_ports) > 1:
        print("Multiple Arduinos found. Please select the correct one:")
        for i, port in enumerate(arduino_ports):
            print(f"{i + 1}. {port}")
        selection = input("Enter the number of the correct Arduino: ")
        try:
            index = int(selection) - 1
            if 0 <= index < len(arduino_ports):
                return arduino_ports[index]
            else:
                print("Invalid selection. Exiting.")
                return None
        except ValueError:
            print("Invalid input. Exiting.")
            return None
    else:
        return arduino_ports[0]

def send_command(command):
    ser.write(command.encode())

arduino_port = find_arduino_port()
if arduino_port is None:
    exit()

ser = serial.Serial(arduino_port, 9600)

try:
    while True:
        user_input = input("Enter command (F/B/L/R/S, K to exit): ")

        if user_input.upper() == 'K':
            print("Exiting program.")
            break
        elif user_input.upper() in ['F', 'B', 'L', 'R', 'S']:
            send_command(user_input.upper())
        else:
            print("Invalid command. Please use F/B/L/R/S/K.")

except KeyboardInterrupt:
    pass

finally:
    ser.close()
    print("Serial connection closed.")