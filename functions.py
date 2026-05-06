import customtkinter
from serial_controller import SerialController
from datetime import datetime
import time
from typography import DIALOG_FONT_SIZE, UI_FONT_FAMILY

timeNow = datetime.now().strftime('%H:%M:%S')

#Import Serial Controller Class and create instance for use in functions
boardControls = SerialController()

#Setup Typography
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

def write_to_box(textbox, reportStatusBox, inputString,rate,port):
    textbox.configure(state="normal")
    message = inputString.strip()
    textbox.insert("end", f"\n[{timeNow}] {message}\n")
    textbox.configure(state="disabled")
    if reportStatusBox is not None and rate is not None or port is not None:
        reportStatusBox.configure(state="normal")
        reportStatusBox.delete("1.0", "end")
        reportStatusBox.insert("end", "Status: " + reportStatus() + "| Baud Rate: " + str(rate)+ " | Port: " + str(port),"center")
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
    getRate = customtkinter.CTkInputDialog(text="Type in your preferred baud rate. Default should be set to 9600.", title="Baud Rate", font=DIALOG_FONT)
    input_value = getRate.get_input()
    if input_value is not None and input_value.isdigit() == True:
        counter = 0
        global rate 
        rate = int(input_value)
        time.sleep(1)
        counter += 1
        counterFunction(counter,checkState)
        write_to_box(textbox, reportStatusBox, f"Baud Rate set to {rate}.",rate=rate,port=port)
    elif input_value.isdigit() == False:
        time.sleep(0.2)
        write_to_box(textbox,reportStatusBox, f"Invalid Entry, please try again.",rate=rate,port=port)
    else:
        time.sleep(0.2)

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
        write_to_box(textbox,reportStatusBox, f"Port set to {port}.",rate=rate,port=port)

def connectBoard(textbox,reportStatusBox,enableButtons):
    boardControls.connect(port, rate)  
    time.sleep(1)
    write_to_box(textbox,reportStatusBox, f"Successfully Connected.",rate=rate,port=port)
    for value in enableButtons.buttons:
        value.configure(state="normal")

def disconnectBoard(textbox,reportStatusBox,disableButtons):
    boardControls.disconnect()
    time.sleep(1)
    write_to_box(textbox,reportStatusBox, f"Successfully Disconnected.",rate=rate,port=port)
    for value in disableButtons.buttons:
        value.configure(state="disabled")

def checkConnection(textbox,reportStatusBox):
    if not boardControls.is_connected():
        write_to_box(textbox,reportStatusBox,f"Not connected.",rate=rate,port=port)
    else:
        write_to_box(textbox,reportStatusBox, f"Connected.",rate=rate,port=port)

#Motor Operations
def openGripper(textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep(1)

        write_to_box(textbox, reportStatusBox, f"Not connected, please connect to a board first.",rate=rate,port=port)
    else:
        boardControls.send_command("o")
        write_to_box(textbox, reportStatusBox, f"Opening Gripper, please wait 6 seconds. Do not press any other buttons.",rate=rate,port=port)

def closeGripper(textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep(1)
        write_to_box(textbox,reportStatusBox, f"Not connected, please connect to a board first!",rate=rate,port=port)
    else:
        boardControls.send_command("c")
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"Closing Gripper, please wait!",rate=rate,port=port)

def stopGripper(textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"Not connected, please connect to a board first!",rate=rate,port=port)
    else:
        boardControls.send_command("s")
        time.sleep(1)
        write_to_box(textbox, reportStatusBox, f"Stopping Gripper, please wait!",rate=rate,port=port)

def jogMotor(keyWord,textbox,reportStatusBox):
    if not boardControls.is_connected():
        time.sleep (0.2)
        write_to_box(textbox, reportStatusBox, f"Not connected, please connect to a board first!",rate=rate,port=port)
    
    if keyWord.split()[1] == "FORWARD":
        boardControls.send_command("JOG FORWARD")
        time.sleep(0.5) #Give time for serial to accept second input
        boardControls.send_command(int(keyWord.split()[2]))
    elif keyWord.split()[1] == "REVERSE":
        boardControls.send_command("JOG REVERSE")
        time.sleep(0.5) #Give time for serial to accept second input
        boardControls.send_command(int(keyWord.split()[2]))