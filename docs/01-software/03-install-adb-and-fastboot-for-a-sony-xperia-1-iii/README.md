# Install ADB and fastboot for a Sony Xperia 1 III

Here’s a step-by-step guide to install ADB and fastboot on a Windows PC, specifically to use with a Sony Xperia 1 III. In fact, one needs to just follow these simple steps:

1. Download ADB and Fastboot Tools

Go to the official Android SDK Platform Tools download page from Google:
[https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools)

Download the Windows version.

1. Extract the Platform Tools

After downloading the ZIP file, extract it to a folder on your PC, for example:
C:\platform-tools

1. Setting up Environment Variables (optional but recommended)

Adding the platform-tools folder to your system PATH lets you run ADB and Fastboot commands from any Command Prompt window.

Press Win + S, type Environment Variables, and select Edit the system environment variables and then click on “Environment Variables” and under System variables, find and select Path, then click Edit. Then click New and add the path to your platform-tools folder, e.g.,
C:\platform-tools and click OK to save all changes.

1. Enable developer options and USB debugging
1. Connect Your Phone to the PC

Use a USB cable to connect your Xperia 1 III to your PC.

If prompted on your phone, allow USB debugging permission.

1. Verify ADB Connection

Open Command Prompt (press Win + R, type cmd, and press Enter) and yype the command:

adb devices

If you see your device’s serial number listed, ADB is working!

You might need to install Sony’s USB Drivers if Windows doesn't recognize the device properly:
[https://developer.sony.com/develop/drivers/](https://developer.sony.com/develop/drivers/). Unlocking bootloader on Sony devices requires a special unlock code from Sony’s website (if you plan to flash or modify).

## Contenuti

- [Fastboot mode (PC + USB cable)](01-fastboot-mode-pc-usb-cable.md)
