#Credits
#Andy Huang --GUI Implementation & Arduino Code

import customtkinter,time
import tkinter
from pathlib import Path
from serial_controller import SerialController
from functions import openGripper, closeGripper, stopGripper, connectBoard, disconnectBoard, checkConnection, getBaudRate, getPort,reportStatus
from datetime import datetime 
from typography import (
    BUTTON_FONT_SIZE,
    LOG_FONT_SIZE,
    MONO_FONT_FAMILY,
    STATUS_FONT_SIZE,
    TITLE_FONT_SIZE,
    UI_FONT_FAMILY,
)


APP_ICON_PATH = Path(__file__).resolve().parent / "assets" / "app_icon.png"

BUTTON_FONT = (UI_FONT_FAMILY, BUTTON_FONT_SIZE, "bold")
STOP_BUTTON_FONT = (UI_FONT_FAMILY, BUTTON_FONT_SIZE, "bold")
TITLE_FONT = (UI_FONT_FAMILY, TITLE_FONT_SIZE, "bold")
LOG_FONT = (MONO_FONT_FAMILY, LOG_FONT_SIZE)
STATUS_FONT = (UI_FONT_FAMILY, STATUS_FONT_SIZE)


#Selection Buttons (Child Class)
class selectionButtons(customtkinter.CTkFrame):
    def __init__(self, master, values, commandDictionary, rowValue):
        super().__init__(master)
        self.values = values
        self.commandDictionary = commandDictionary

        for i, value in enumerate(self.values):
            y = self.commandDictionary.get(str(i))
            button = customtkinter.CTkButton(self, text=value, command=y, font=BUTTON_FONT)
            button.grid(row = rowValue, column = i+1, padx = 20, pady = (20,0), sticky = "w")


#Control Buttons (Child Class)
class buttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, values, commandDictionary, rowValue, title):
        super().__init__(master)        
        self.values = values
        self.commandDictionary = commandDictionary
        self.title = title
        self.buttons = []
        self.row = rowValue
    

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, font=TITLE_FONT)
        self.title.grid(row = 0, column = 2, padx=10,pady=(10,0),sticky="ew")

        for i, value in enumerate(self.values):
            x = self.commandDictionary.get(str(i))
            button = customtkinter.CTkButton(self, text=value, command=x, font=BUTTON_FONT, state="disabled")
            button.grid(row = rowValue, column = i+1, padx=20,pady= (20,0), sticky = "w")
            self.buttons.append(button)


#main
class App(customtkinter.CTk):
    time = datetime.now()
    def __init__(self):
        super().__init__()

        self.title("Gripper Control Panel")
        self._set_app_icon()
        self.geometry("633x760")

        self.button_frame1 = buttonFrame(self, values= ["Open", "Close", "Stop"], commandDictionary= {"0" : lambda: openGripper(self.writeBox,self.boxes), "1" : lambda: closeGripper(self.writeBox,self.boxes), "2" : lambda: stopGripper(self.writeBox,self.boxes)},rowValue = 1,title = "Gripper Controls")
        self.button_frame1.grid(row= 0 , column =0, padx = 20, pady = 20)
        self.button_frame1.buttons[2].configure(
            fg_color="#C62828",
            hover_color="#A61B1B",
            text_color="#FFFFFF",
            text_color_disabled="#F7F7F7",
            font=STOP_BUTTON_FONT,
        )

        self.button_frame2= buttonFrame(self, values = ["Connect", "Disconnect", "Check Connection"], commandDictionary ={"0" : lambda: connectBoard(self.writeBox,self.boxes), "1" : lambda: disconnectBoard(self.writeBox,self.boxes), "2" : lambda: checkConnection(self.writeBox,self.boxes)}, rowValue = 3, title = "Board Controls")
        self.button_frame2.grid(row = 2, column = 0, padx = 20, pady = 20)

        self.selectionButton = selectionButtons(self, values = ["Select Baud Rate", "Select Port"], commandDictionary ={"0" : lambda: getBaudRate(self.writeBox,self.boxes,self.button_frame2), "1" : lambda: getPort(self.writeBox,self.boxes,self.button_frame2)}, rowValue = 5)

        self.selectionButton.grid(row = 4, column = 0, padx = 20, pady = 20)

        self.writeBox = customtkinter.CTkTextbox(self, width=600, height=200, corner_radius=3, font=LOG_FONT)
        self.writeBox.grid(row=6, column=0, padx=20, pady=20)
        self.writeBox.configure(state="disabled")

        self.boxes = customtkinter.CTkTextbox(self, width=600, height=100, corner_radius=0, font=STATUS_FONT, fg_color="transparent")
        self.boxes.grid(row=9, column=0, padx=20, pady=20)
        self.boxes.configure(state="normal")
        self.boxes.insert("end", "Status: " + reportStatus() + " | © 2026 (MIT LICENSE)")
        self.boxes.configure(state="disabled")
        
    def _set_app_icon(self):
        if not APP_ICON_PATH.exists():
            return

        self._app_icon = tkinter.PhotoImage(file=str(APP_ICON_PATH))
        self.iconphoto(True, self._app_icon)



app = App()


app.mainloop()
