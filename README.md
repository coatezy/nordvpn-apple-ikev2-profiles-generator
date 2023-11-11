# NordVPN Apple IKEv2 Profiles Generator

This Python 3 script utilizes the NordVPN API to gather all IKEv2 servers, creating .mobileconfig files with your specified credentials for Apple devices, including Apple TV. Additionally, it installs the NordVPN Root CA on your device.

The inspiration for this script came from artembrening's [PowerShell implementation](https://github.com/artembrening/Create-NordVPNMobileConfig/blob/main/README.md).

## How to Use:

1. Visit [NordVPN Manual Configuration](https://my.nordaccount.com/dashboard/nordvpn/manual-configuration/) and retrieve your service username and password.

2. Run the Python 3 script:
    ```
    python nordvpn_apple_ikev2_profiles_generator.py
    ```

3. Enter your service username and password when prompted.

4. Enter your preferred output directory when prompted (defaults to ./profiles).

5. Wait for the script to finish, then copy the necessary VPN .mobileconfig files to your Apple device.

6. Download "Apple Configurator" from the App Store on your Mac.

7. Run "Apple Configurator" and choose "Paired Devices" in the top navigation bar.

8. On your Apple TV, navigate to Settings > Remotes and Devices > Remote-App and Devices.

9. If the devices are on the same network, pair your Apple TV with your Mac using the 6-digit code.

10. Once paired, click "Add" > "Profiles" and select all .mobileconfig files for the specific VPN connections you desire.

11. Install the profiles on your Apple TV.

## Leaving Feedback:
If you encounter issues, have suggestions, or want to provide feedback, please open an issue on the [GitHub repository](https://github.com/coatezy/nordvpn-apple-ikev2-profiles-generator). Clearly describe the problem or suggestion, and include relevant details such as operating system, Python version, etc. Your feedback is valuable and helps improve the script for everyone!

