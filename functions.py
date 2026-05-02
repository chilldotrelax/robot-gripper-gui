import customtkinter
from serial_controller import SerialController

boardControls = SerialController()

#Global Variables
rate = 0
port = ""

def getBaudRate():
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred rate", title = "Baud Rate")
    input_value = getRate.get_input()
    if input_value is not None:
        global rate 
        rate = int(input_value)

def getPort():
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred port", title = "Port Selection")
    input_value = getRate.get_input()
    if input_value is not None:
        global port 
        port = input_value

#Motor Operations

def connectBoard():
    print("Connecting... Please wait...")
    try:
        boardControls.connect(port, rate)
   
    except:
        exit()

def openGripper():
    print("Opening Gripper...")

def closeGripper():
    print("Closing Gripper...")

def stopGripper():
    print("Stopping Gripper.")


def disconnectBoard():
    boardControls.disconnect()

def checkConnection():
    print("Placeholder")
