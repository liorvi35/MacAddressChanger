"""
this file contains the implementation for physical address, i.e. MAC (Media Access Control).
:author: Lior Vinman
:date: 01/04/2023
"""

import subprocess
import optparse
import re


def get_args():
    """
    this function is getting the interface name MAC address from standard input
    :return: settings from input, if successes
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface")
    parser.add_option("-m", "--mac", dest="mac", help="Mac")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.mac:
        parser.error("[-] Please specify a MAC address, use --help for more info")

    return options


def change_mac(interface, new_mac):
    """
    this function is changing the MAC address on the given interface
    :param interface: the device to change to the MAC address
    :param new_mac: the new address to set
    """
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def current_mac(interface):
    """
    this function returns the current MAC address on given interface
    :param interface: device to check current MAC
    :return: current address, if successes
    """
    ifconfig_out = subprocess.call(["ifconfig", interface])
    res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_out))

    if res:
        return res
    else:
        print("[-] Cannot find MAC address")


def main():
    options = get_args()
    m = current_mac(options.interface)
    change_mac(options.interface, options.mac)
    m = current_mac(options.interface)


if __name__ == "__main__":
    main()
