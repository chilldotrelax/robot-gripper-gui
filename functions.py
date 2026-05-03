import customtkinter
from serial_controller import SerialController
from datetime import datetime




boardControls = SerialController()

#Global Variables
rate = 0
port = ""


def write_to_box(textbox, inputString):
    textbox.configure(state="normal")
    textbox.insert("end", inputString + "\n")
    textbox.configure(state="disabled")

#Board Ops

def getBaudRate(textbox):
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred rate", title = "Baud Rate")
    input_value = getRate.get_input()
    if input_value is not None and input_value.isdigit() == True:
        global rate 
        rate = int(input_value)
        write_to_box(textbox, f"[{datetime.now().strftime('%H:%M:%S')}] Baud Rate set to {rate}.")
    else:
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Invalid Entry, please try again.")

def getPort(textbox):
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred port", title = "Port Selection")
    input_value = getRate.get_input()
    if input_value is not None:
        global port 
        port = input_value
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Port set to {port}.")

def connectBoard(textbox):
    boardControls.connect(port, rate)
    write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Successfully Connected!")

def disconnectBoard(textbox):
    boardControls.disconnect()
    write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Successfully Disconnected!")

def checkConnection(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, "Not connected")
    else:
        write_to_box(textbox, "Connected!")

#Motor Operations
def openGripper(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("o")
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Opening Gripper, please wait!")

def closeGripper(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("c")
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Closing Gripper, please wait!")

def stopGripper(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("s")
        write_to_box(textbox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Stopping Gripper, please wait!")
