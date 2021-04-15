import gui
import subprocess
import sys
from typing import Final

if sys.platform == "win32":
    port: Final[str] = "COM3"
elif sys.platform == "darwin":
    port: Final[str] = "/dev/cu.usbserial-0001"
else:
    raise NotImplementedError("We only support macOS and Windows for now.")


def flash_nanoframework(device: str = "COM3") -> subprocess.CompletedProcess:
    """This flashes the .NET nanoFramework onto the device that is connected to the given port.
    :param device: The device to connect to or the port it is connected to, like "COM3" for example.
    :return: A completed Process
    """
    if sys.platform != "win32":
        raise RuntimeError("The nanoff tool seems to only work with Windows at the moment.")
    result = subprocess.run(["nanoff", "--target", "ESP32_WROOM_32", "--serialport", device, "--update"],
                            stdout=sys.stdout,
                            stderr=sys.stderr)
    return result


def flash_py(device: str = port, file: str = "esp32-idf4-20210202-v1.14.bin") -> subprocess.CompletedProcess:
    """This flashes microPython onto the device that is connected at the given port."""
    subprocess.run(["esptool.py", "--chip", "esp32", "--port", device, "erase_flash"])
    result = subprocess.run(["esptool.py", "--chip", "esp32", "--port", device, "--baud", "115200", "write_flash",
                             "-z", "0x1000", file])
    return result


def main() -> None:
    """Actually runs the GUI and then starts the flash"""
    framework: int = gui.show_flash_window()
    if framework == 0:
        flash_py()
    elif framework == 1:
        flash_nanoframework()
    else:
        raise ValueError("Unsupported framework value.")


if __name__ == "__main__":
    # This code only runs when executing the script directly instead of importing it.
    main()
