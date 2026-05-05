# Gripper Control Panel

Controls the robot gripper.

## Command Protocol

The GUI sends these commands to the connected board:

| GUI action | Serial command |
| --- | --- |
| Open | `o` |
| Close | `c` |
| Stop | `s` |

The arduino opens a serial connection and listens for these characters. 

## Command Box

Incomplete. DO not type in anything, as it can risk the program crashing.

## Requirements

- Python 3.9 or newer recommended
- Arduino

The control panel also requires depenencies to be installed.
Python packages are listed in [requirements.txt](requirements.txt).

## Setup

Clone the repository and install the Python dependencies:

```bash
git clone https://github.com/chilldotrelax/robot-gripper-gui.git
cd robot-gripper-gui
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```

## Running the App

Start the GUI with:

```bash
python main.py
```

Then use the interface in this order:

1. Select the baud rate used by your board, such as `9600`.
2. Select the serial port, such as `/dev/cu.usbmodem1101`, `/dev/ttyUSB0`, or `COM3`.
3. Click **Connect**.
4. Use **Open**, **Close**, or **Stop** to control the gripper.
5. Click **Disconnect** before unplugging the board or closing the app.

## License

Licensed under the MIT License. See [LICENSE](LICENSE)
for details.

## Project Structure

```text
.
├── main.py                 # CustomTkinter app layout and button wiring
├── functions.py            # GUI command handlers and log helpers
├── commandBoxLogic.py      # WIP typed command routing
├── serial_controller.py    # PySerial connection wrapper
├── typography.py           # Shared font sizing and families
├── assets/
│   └── app_icon.png        # Window icon asset
├── .gitignore              # Local environment and build artifact ignores
├── requirements.txt        # Python package dependencies
└── README.md
```
