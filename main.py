import napalm
from napalm.base.exceptions import ConnectAuthError, ConnectionException
import sys
import os


def main(host, interface):

    driver = napalm.get_network_driver("nxos")

    if host == None:
        host = AskForDevice()

    if interface == None:
        interface = AskForInterface()

    Username, Password = AskForCredentials()


    print("Connecting ...")
    try: 
        # Connect:
        device = driver( hostname=host, username=Username, password=Password)
        device.open()
    except ConnectAuthError:
        print('Authentication Error!')
    except ConnectionException:
        print(f'Could not connect to {host}')

    device.close()
    print("Done.")


def AskForDevice():
    return input("Device name or ip address : ")


def AskForInterface():
    return input("Interface name : ")


def AskForCredentials():
    Username = input ("username : ")
    Password = input ("password : ")
    return Username, Password


if __name__ == "__main__":
    device = interface = None
    if len(sys.argv) == 2:
        device = sys.argv[1]
    if len(sys.argv) == 3:
        interface = sys.argv[2]


    main(device, interface)
