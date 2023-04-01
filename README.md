# MacAddressChanger

The MAC-Address-Changer program is a Python script that allows you to change the MAC (Media Access Control) address of a NIC (network interface card) on a Debian-based system.

## Requirements
Before using the MacAddressChanger program, make sure your system meets the following requirements:
-   Python version 3
-   Debian-based system

## Building and Installing
You can install the MacAddressChanger program by following these steps:

1.  Clone this repository to your local machine using the following command:<br/>`git clone https://github.com/liorvi35/MacAddressChanger.git` 
    
2.  Install the required modules by running the following command:<br/>`pip install -r requirements.txt` 
    
3.  To view the script's help page, run the following command:<br/>`python3 mac_changer.py -h` 

## Usage
To use the MacAddressChanger program, you need to provide two arguments via flags:
1.  The name of the NIC you want to change, specified using the `-i` or `--interface` flag.
2.  The new MAC address you want to set, specified using the `-m` or `--mac` flag.

To change the MAC address of a NIC, run the following command:
`sudo python3 mac_changer.py -i <NIC> -m <MAC>` 

Replace `<NIC>` with the name of the interface you want to change and `<MAC>` with the new MAC address you want to set.

You can also use the keyword `random` to generate a random MAC address.
<br/>For example: `sudo python3 mac_changer.py -i wlan0 -m random` 
<br/>This command will set a random MAC address for the `wlan0` interface.

## Skills
- Python programming.
- Version control with Git.
- Linux command line.
- Computers-Communication knowledge about MAC addresses.

## Disclaimer
Please note that changing the MAC address of a device without proper authorization may be illegal in some jurisdictions.<br/>Distinction: changing of MAC address will probably also change your local IP (Internet-Protocol) address.<br/>This program is provided for educational purposes only. Use it at your own risk.
