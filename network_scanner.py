import scapy.all as scapy
from get_interface import choose_interface_and_get_info
from get_argumens import get_arguments

my_machine = choose_interface_and_get_info()
arguments = get_arguments()


def show_contents_in_manner(list_of_answered_packets):
    print("----IP---------------MAC------------")
    for sent, received in list_of_answered_packets:
        print(f"{received.psrc}\t\t{received.src}")


def scan(ip, my_ip, my_mac):
    arp_packet = scapy.ARP(pdst=ip, psrc=my_ip, hwsrc=my_mac)
    broadcast_packet = scapy.Ether(src=my_mac, dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_packet
    answered = scapy.srp(combined_packet, timeout=1, verbose=False)[0]
    show_contents_in_manner(answered)



scan(arguments.range, my_machine['ip'], my_machine['mac'])

