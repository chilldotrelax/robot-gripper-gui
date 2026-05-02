import customtkinter 
from serial_controller import SerialController
from functions import openGripper, closeGripper, stopGripper, connectBoard, disconnectBoard, checkConnection, getBaudRate, getPort

#Selection Buttons (Child Class)
class selectionButtons(customtkinter.CTkFrame):
    def __init__(self, master, values, commandDictionary, rowValue):
        super().__init__(master)
        self.values = values
        self.commandDictionary = commandDictionary

        for i, value in enumerate(self.values):
            y = self.commandDictionary.get(str(i))
            button = customtkinter.CTkButton(self, text = value, command = y )
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
            button = customtkinter.CTkButton(self, text = value, command = x)
            button.grid(row = rowValue, column = i+1, padx=20,pady= (20,0), sticky = "w")
            self.buttons.append(button)

#main
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gripper Control Panel")
        self.geometry("600x600")

        self.button_frame = buttonFrame(self, values= ["Open", "Close", "Stop"], commandDictionary= {"0" : openGripper, "1" : closeGripper, "2" : stopGripper},rowValue = 1,title = "Gripper Controls")
        self.button_frame.grid(row= 0 , column =0, padx = 20, pady = 20)

        self.button_frame = buttonFrame(self, values = ["Connect", "Disconnect", "Check Connection"], commandDictionary ={"0" : connectBoard, "1" : disconnectBoard, "2" : checkConnection}, rowValue = 3, title = "Board Controls")
        self.button_frame.grid(row = 2, column = 0, padx = 20, pady = 20)

        self.selectionButton = selectionButtons(self, values = ["Select Baud Rate", "Select Port"], commandDictionary ={"0" : getBaudRate, "1" : getPort}, rowValue = 5)

        self.selectionButton.grid(row = 4, column = 0, padx = 20, pady = 20)




app = App()

app.mainloop()