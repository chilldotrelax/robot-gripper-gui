from functions import openGripper, closeGripper, stopGripper, connectBoard, disconnectBoard,jogMotor
from functions import write_to_box, rate, port

def commandGuides(textboxes):
    write_to_box(textbox= textboxes, reportStatusBox= None, inputString="\n"+ "COMMANDS:" +'\n' + "OPEN - OPENS THE GRIPPER" +'\n' + "CLOSE - CLOSES THE GRIPPER" +'\n'+"STOP - STOP MOTOR" +'\n'+"JOG FORWARDS :VALUE: - JOGS MOTOR FORWARD BY N STEPS."+'\n'+"JOG REVERSE :VALUE: - JOGS MOTOR BACKWARD BY N STEPS.",rate=rate,port=port)

def unknownCommand(textboxes):
    write_to_box(textbox= textboxes, reportStatusBox= None, inputString="\n"+"Unknown command. Type HELP for help.", rate=rate,port=port)

commandInputs = ""
writeBoxImports = None
statusBoxImports = None

def importVariables(commandInput,writeBoxImport,statusBoxImport):
    commandInputs = commandInput

    writeBoxImports = writeBoxImport
    statusBoxImports = statusBoxImport
    steps = 0
    if len(commandInputs.split()) == 2 and str([i for i in commandInputs.split()][2]).isdigit() == True:
        newSteps = int(commandInputs.split()[2])
        steps = newSteps


    commandDictionary = {
    "OPEN": lambda: openGripper(writeBoxImports,statusBoxImports),
    "CLOSE": lambda : closeGripper(writeBoxImports,statusBoxImports),
    "STOP": lambda: stopGripper(writeBoxImports,statusBoxImports),
    "HELP": lambda: commandGuides(writeBoxImports),
    "CONNECT": lambda: connectBoard(writeBoxImports,statusBoxImports),
    "DISCONNECT": lambda: disconnectBoard(writeBoxImports,statusBoxImports),
    "JOG FORWARDS": lambda: jogMotor(steps,writeBoxImports,statusBoxImports),
    "JOG REVERSE": lambda: jogMotor(steps,writeBoxImports,statusBoxImports),
    "UNKNOWN COMMAND": lambda: unknownCommand(writeBoxImports)
}
    commandHelper(commandInputs, commandDictionary)

    commandInputs = ""
    writeBoxImports = None
    statusBoxImports = None

def commandHelper(commandInput,commandDictionary):
    commandDictionaries = commandDictionary
    
    keysList= [i for i in commandDictionary.keys()]

    #Open, close,stop
    if commandInput in keysList and commandInput != "Help" and commandInput not in [keysList[i] for i in range(3,6)]:
        commandDictionaries[commandInput.strip]()
    
    #Connect, Disconnect
    elif commandInput in [keysList[i] for i in range(3,6)]: 
        commandDictionaries[commandInput]()

    #REVERSE FORWARD
    elif " ".join(commandInput.split()[:2]) in [keysList[i] for i in range(6,len(keysList))]:
        ammendInput =  " ".join(commandInput.split()[:2])
        commandDictionaries[ammendInput]()


    elif commandInput == "HELP":
        commandDictionaries[commandInput]()

    else:
       commandDictionaries["UNKNOWN COMMAND"]()

