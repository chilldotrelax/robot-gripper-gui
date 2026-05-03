# Robot Gripper GUI

A small desktop control panel for an Arduino-driven robot gripper. The app uses
CustomTkinter for the interface and PySerial to send simple single-character
commands over a serial connection.

## Current Features

- Open, close, and stop gripper controls
- Manual serial port selection
- Manual baud rate selection
- Connect, disconnect, and connection status controls
- Text log area for user feedback

## Command Protocol

The GUI sends these commands to the connected board:

| GUI action | Serial command |
| --- | --- |
| Open | `o` |
| Close | `c` |
| Stop | `s` |

Your Arduino or microcontroller sketch should listen for those characters and
map them to the matching gripper behavior.

## Requirements

- Python 3.9 or newer recommended
- A serial-capable Arduino or compatible microcontroller
- A USB or serial connection to the board

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

## Project Structure

```text
.
├── main.py                 # CustomTkinter app layout and button wiring
├── functions.py            # GUI command handlers and log helpers
├── serial_controller.py    # PySerial connection wrapper
├── requirements.txt        # Python package dependencies
└── README.md
```
