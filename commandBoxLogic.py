from functions import openGripper, closeGripper, stopGripper, connectBoard, disconnectBoard
from functions import write_to_box, rate, port

def commandGuides(textboxes):
    write_to_box(textbox= textboxes, reportStatusBox= None, inputString="\n"+ "Available Commands:" +'\n' + "OPEN - Opens the gripper" +'\n' + "CLOSE - Close the gripper" +'\n'+"STOP - Stop motor" ,rate=rate,port=port)

commandInputs = ""
writeBoxImports = None
statusBoxImports = None

def importVariables(commandInput,writeBoxImport,statusBoxImport):
    commandInputs = commandInput
    writeBoxImports = writeBoxImport
    statusBoxImports = statusBoxImport

    print(commandInputs,writeBoxImports,statusBoxImports)

    commandDictionary = {
    "Open": lambda: openGripper(writeBoxImports,statusBoxImports),
    "Close": lambda : closeGripper(writeBoxImports,statusBoxImports),
    "Stop": lambda: stopGripper(writeBoxImports,statusBoxImports),
    "Help": lambda: commandGuides(writeBoxImports)
}

    commandHelper(commandInputs,commandDictionary)

    commandInputs = ""
    writeBoxImports = None
    statusBoxImports = None

def commandHelper(commandInput,commandDictionary):
    commandDictionaries = commandDictionary
    
    keysList = commandDictionary.keys()

    if commandInput in keysList and commandInput != "Help" and commandInput not in [keysList(i) for i in range(3,len(keysList))]:
        commandDictionaries[commandInput]()

    elif commandInput == "Help":
        commandDictionaries[commandInput]()

