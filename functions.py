import customtkinter
from serial_controller import SerialController
from datetime import datetime
import time
from typography import DIALOG_FONT_SIZE, UI_FONT_FAMILY



boardControls = SerialController()
DIALOG_FONT = (UI_FONT_FAMILY, DIALOG_FONT_SIZE)

#Global Variables
rate = 0
port = ""
counter = 0

def reportStatus():
    if not boardControls.is_connected():
        return "Not Connected"
    else:
        return "Connected"

def write_to_box(textbox, reportStatusBox, inputString):
    textbox.configure(state="normal")
    textbox.insert("end", inputString + "\n")
    textbox.configure(state="disabled")

    reportStatusBox.configure(state="normal")
    reportStatusBox.delete("1.0", "end")
    reportStatusBox.insert("end", "Status: " + reportStatus() + " | 2026")
    reportStatusBox.configure(state="disabled")
internalCounter = 0
def counterFunction(counter,checkState):
    if counter:
        global internalCounter
        internalCounter += 1
    
    if internalCounter >= 2: modifyState(checkState)

def modifyState(checkState):
    for value in checkState.buttons:
        value.configure(state="normal")



#Board Ops

def getBaudRate(textbox,reportStatusBox,checkState):
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred rate", title="Baud Rate", font=DIALOG_FONT)
    input_value = getRate.get_input()
    if input_value is not None and input_value.isdigit() == True:
        counter = 0
        global rate 
        rate = int(input_value)
        time.sleep(1)
        counter += 1
        counterFunction(counter,checkState)
        write_to_box(textbox, reportStatusBox, f"[{datetime.now().strftime('%H:%M:%S')}] Baud Rate set to {rate}.")

    else:
        time.sleep(0.2)
        write_to_box(textbox,reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Invalid Entry, please try again.")

def getPort(textbox,reportStatusBox,checkState):
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred port", title="Port Selection", font=DIALOG_FONT)
    input_value = getRate.get_input()
    if input_value is not None:
        counter = 0
        global port 
        port = input_value
        time.sleep(1)
        counter += 1
        counterFunction(counter,checkState)
        write_to_box(textbox,reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Port set to {port}.")

def connectBoard(textbox,reportStatusBox):
    boardControls.connect(port, rate)  
    time.sleep(1)
    write_to_box(textbox,reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Successfully Connected!")

def disconnectBoard(textbox,reportStatusBox):
    boardControls.disconnect()
    time.sleep(1)
    write_to_box(textbox,reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Successfully Disconnected!")

def checkConnection(textbox,reportStatusBox):
    if not boardControls.is_connected():
        write_to_box(textbox,reportStatusBox, "Not connected")
    else:
        write_to_box(textbox,reportStatusBox, "Connected!")

#Motor Operations
def openGripper(textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep(1)

        write_to_box(textbox, reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("o")
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Opening Gripper, please wait!")

def closeGripper(textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep(1)
        write_to_box(textbox,reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("c")
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Closing Gripper, please wait!")

def stopGripper(textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Not connected, please connect to a board first!")
    else:
        boardControls.send_command("s")
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"{"["+datetime.now().strftime("%H:%M:%S")+"]"} Stopping Gripper, please wait!")
