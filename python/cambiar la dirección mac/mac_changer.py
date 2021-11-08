# encoding: utf-8
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "interface para cambiar Direccion MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "nueva Direccion MAC")
    (options, arguments) = parser.parse_args() 
    if not options.interface:
        parser.error("[-] Por favor indicar una interfaz, usa --help para más información")
    elif not options.new_mac:
        parser.error("[-] Por favor indicar una Direccion MAC, usa --help para más información")
    return options

def change_mac(interface, new_mac):
    print("[+] Cambiando dirección MAC para " + interface  + "  a " +  new_mac)

    subprocess.call(["ifconfig" , interface , "down"])
    subprocess.call(["ifconfig" , interface , "hw","ether", new_mac])
    subprocess.call(["ifconfig" , interface , "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
