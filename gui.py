import PySimpleGUI as sg
from pprint import pprint as print

sg.change_look_and_feel("SystemDefaultForReal")


def show_flash_window() -> int:
    """Asks the user whether to flash nanoFramework or microPython.
    
    This function returns 0 when the user wants to flash microPython and 1 when the user wants to flash nanoFramework.
    Flashing NanoFramework will only work on Windows, so if the OS is not Windows, this is just a No-Op and returns 0."""
    layout = [[sg.Text("Select a framework to flash.")],
    [sg.Button(button_text="Flash nanoFramwork", key="NANOFRAMEWORK", )],
    [sg.Button(button_text="Flash microPython", key="MICROPYTHON")],
    [sg.Cancel()]]
    event, _ = sg.Window(title="ESP32 Flashing Tool", layout=layout, modal=True).read(close=True)
    if event.upper() == "CANCEL":
        raise SystemExit(1)
    elif event == "NANOFRAMEWORK":
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(show_flash_window())