import customtkinter
from serial_controller import SerialController
from datetime import datetime

now = "["+datetime.now().strftime("%H:%M:%S")+"]"

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
    if input_value is not None:
        global rate 
        rate = int(input_value)
        write_to_box(textbox, f"{now} Baud Rate set to {rate}.")

def getPort(textbox):
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred port", title = "Port Selection")
    input_value = getRate.get_input()
    if input_value is not None:
        global port 
        port = input_value
        write_to_box(textbox, f"{now} Port set to {port}.")

def connectBoard(textbox):

    boardControls.connect(port, rate)
    write_to_box(textbox, f"{now} Successfully Connected!")

def disconnectBoard(textbox):
    boardControls.disconnect()
    write_to_box(textbox, f"{now} Successfully Disconnected!")

def checkConnection(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, "Not connected")
    else:
        write_to_box(textbox, "Connected!")

#Motor Operations
def openGripper(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, f"{now} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("o")
        write_to_box(textbox, f"{now} Opening Gripper, please wait!")


def closeGripper(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, f"{now} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("c")
        write_to_box(textbox, f"{now} Closing Gripper, please wait!")

def stopGripper(textbox):
    if not boardControls.is_connected():
        write_to_box(textbox, f"{now} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("s")
        write_to_box(textbox, f"{now} Stopping Gripper, please wait!")
