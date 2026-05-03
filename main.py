#Credits
#Andy Huang --GUI Implementation & Arduino Code

import customtkinter,time
from serial_controller import SerialController
from functions import openGripper, closeGripper, stopGripper, connectBoard, disconnectBoard, checkConnection, getBaudRate, getPort,reportStatus
from datetime import datetime 



#Selection Buttons (Child Class)
class selectionButtons(customtkinter.CTkFrame):
    def __init__(self, master, values, commandDictionary, rowValue):
        super().__init__(master)
        self.values = values
        self.commandDictionary = commandDictionary

        for i, value in enumerate(self.values):
            y = self.commandDictionary.get(str(i))
            button = customtkinter.CTkButton(self, text = value, command = y,font=customtkinter.CTkFont(size=14,family="Courier New"))
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
    

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius = 6)
        self.title.grid(row = 0, column = 2, padx=10,pady=(10,0),sticky="ew")

        for i, value in enumerate(self.values):
            x = self.commandDictionary.get(str(i))
            button = customtkinter.CTkButton(self, text = value, command = x,font=customtkinter.CTkFont(size=14,family="Courier New"))
            button.grid(row = rowValue, column = i+1, padx=20,pady= (20,0), sticky = "w")
            self.buttons.append(button)


#main
class App(customtkinter.CTk):
    time = datetime.now()
    def __init__(self):
        super().__init__()

        self.title("Gripper Control Panel")
        self.geometry("700x800")

        self.button_frame = buttonFrame(self, values= ["Open", "Close", "Stop"], commandDictionary= {"0" : lambda: openGripper(self.writeBox,self.boxes), "1" : lambda: closeGripper(self.writeBox,self.boxes), "2" : lambda: stopGripper(self.writeBox,self.boxes)},rowValue = 1,title = "Gripper Controls")
        self.button_frame.grid(row= 0 , column =0, padx = 20, pady = 20)

        self.button_frame = buttonFrame(self, values = ["Connect", "Disconnect", "Check Connection"], commandDictionary ={"0" : lambda: connectBoard(self.writeBox,self.boxes), "1" : lambda: disconnectBoard(self.writeBox,self.boxes), "2" : lambda: checkConnection(self.writeBox,self.boxes)}, rowValue = 3, title = "Board Controls")
        self.button_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

        self.selectionButton = selectionButtons(self, values = ["Select Baud Rate", "Select Port"], commandDictionary ={"0" : lambda: getBaudRate(self.writeBox,self.boxes), "1" : lambda: getPort(self.writeBox,self.boxes)}, rowValue = 5)

        self.selectionButton.grid(row = 4, column = 0, padx = 20, pady = 20)

        self.writeBox = customtkinter.CTkTextbox(self, width=600, height=200, corner_radius=3,font=customtkinter.CTkFont(size=14,family="Courier New"))
        self.writeBox.grid(row=6, column=0, padx=20, pady=20)
        self.writeBox.configure(state="disabled")

        self.boxes = customtkinter.CTkTextbox(self, width=600, height=100, corner_radius=0,font=customtkinter.CTkFont(size=14,family="Courier New"),fg_color="transparent")
        self.boxes.grid(row=9, column=0, padx=20, pady=20)
        self.boxes.configure(state="normal")
        self.boxes.insert("end", "Status: " + reportStatus() + " | 2026")
        self.boxes.configure(state="disabled")
        


app = App()


app.mainloop()
