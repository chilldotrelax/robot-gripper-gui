# Gripper Control Panel

Robot gripper desktop GUI built with CustomTkinter and PySerial.

## Current Features

- Open, close, and stop gripper controls
- Manual serial port selection
- Manual baud rate selection
- Connect, disconnect, and connection status controls
- Output log and connection status display
- WIP command entry box for typed commands

## Command Protocol

The GUI sends these commands to the connected board:

| GUI action | Serial command |
| --- | --- |
| Open | `o` |
| Close | `c` |
| Stop | `s` |

Arduino or microcontroller sketch should listen for those characters and
map them to the matching gripper behavior.

## Command Box

List Of Commands. Case-sensitive -- Type only in uppercase.

| Typed command | Action |
| --- | --- |
| `OPEN` | Opens the gripper |
| `CLOSE` | Closes the gripper |
| `STOP` | Stops the gripper |
| `HELP` | Prints command guidance |


## Requirements

- Python 3.9 or newer recommended
- Arduino

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

## Portable Zip Build

Some releases are distributed as a portable zip file instead of source code.
To run the portable build:

1. Download and unzip the release folder.
2. Open the extracted folder.
3. Double-click **Gripper Control Panel.exe**.

Do not move, rename, delete, or edit the **_internal** folder. The executable
depends on files inside that folder, and the app may not start if those files
are changed.

Run the executable from the extracted folder, not directly from inside the zip
archive.

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
