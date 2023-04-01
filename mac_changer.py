"""
this file contains the implementation for physical address, i.e. MAC (Media Access Control).
:author: Lior Vinman
:version: 1.1
:date: 01/04/2023
"""

import subprocess
import optparse
import random
import re


def get_random_mac():
    """
    this function generates random MAC address
    :return: new generated MAC
    """
    octets = [random.randint(0x00, 0xff) for i in range(6)]
    octets[0] &= 0xfe
    random_mac = ":".join("{:02x}".format(octet) for octet in octets)
    return random_mac


def get_arguments():
    """
    this function gets arguments from standard input (-i <interface> -m <mac>)
    :return: options with interface and mac
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="inter",
                      help="Network interface that it's MAC-address should be changed")
    parser.add_option("-m", "--mac", dest="mac", help="new MAC-address to change to")
    (options, arguments) = parser.parse_args()
    if not options.inter:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.mac:
        parser.error("[-] Please specify a MAC-address, use --help for more info")
    else:
        return options


def change_mac(interface, mac):
    """
    this function changes the MAC address on given interface
    :param interface: network device to change MAC on
    :param mac: MAC to change to
    """
    new_mac = mac
    if mac == "random":
        new_mac = get_random_mac()
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    """
    this function returns the current MAC address on given interface
    :param interface: device to check current MAC
    :return: current address, if successes, else None
    """
    ifconfig_out = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_regex = re.compile(r"ether ([\da-fA-F]{2}(?::[\da-fA-F]{2}){5})")
    match = mac_regex.search(ifconfig_out)
    if match:
        mac_address = match.group(1)
        return mac_address
    else:
        return None


def main():
    opts = get_arguments()
    old_mac = get_current_mac(opts.inter)
    change_mac(opts.inter, opts.mac)
    new_mac = get_current_mac(opts.inter)
    if old_mac != new_mac:
        print(f"[+] {opts.inter} has changed MAC from {old_mac} to {new_mac}")
    else:
        print(f"[-] cannot change MAC on {opts.inter}")


if __name__ == "__main__":
    main()
