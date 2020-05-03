import napalm
import pprint
import getpass
from napalm.base.exceptions import ConnectAuthError, ConnectionException
import sys
import os


def main(host, interface):
    """
    Get vlan information for a specific interface
    :param host: hostname or ip addr provided through command line
    :param interface: interface name provided through command line
    :return: None
    """
    if host is None:
        host = ask_for_device()

    if interface is None:
        interface = ask_for_interface()

    username, password = ask_for_credentials()

    driver = napalm.get_network_driver("ios")
    print("Connecting ...")
    try:
        # Connect:
        device = driver(
            hostname=host,
            username=username,
            password=password,
            optional_args={"secret": password},
        )
        device.open()
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(device.get_interfaces())
        pp.pprint(get_vlan_from_int(device, interface))
    except ConnectAuthError:
        print('Authentication Error!')
    except ConnectionException:
        print(f'Could not connect to {host}')

    device.close()
    print("Done.")


def ask_for_device():
    """
    Ask for the device hostname or ip address
    :return: (string) device hostname or ip address
    """
    return input("Device name or ip address : ")


def ask_for_interface():
    """
    Ask for the interface to check
    :return: (string) interface name
    """
    return input("Interface name : ")


def ask_for_credentials():
    """
    Ask for credentials
    :return: (string) username, (string) password
    """
    username = input("username : ")
    password = getpass.getpass("password : ")
    return username, password


def get_vlan_from_int(dev, int_name):
    """
    get vlan information for an interface
    :param dev: napalm device
    :param int_name: interface name
    :return:
    """
    return dev.get_interfaces()[int_name]


if __name__ == "__main__":
    device = interface = None
    if len(sys.argv) == 2:
        device = sys.argv[1]
    if len(sys.argv) == 3:
        interface = sys.argv[2]

    main(device, interface)
