from scapy.all import Ether, IP, TCP, wrpcap
import os

# Generate a sample PCAP file with one packet
packet = Ether() / IP() / TCP()
output_path = "/home/siaziz/Desktop/Autonomous Cybersecurity Incident Response System/autocidr/detection/python-detector/src/example.pcap"
wrpcap(output_path, [packet])

# Debugging statements to verify the successful creation of the PCAP file
if os.path.exists(output_path):
    print(f"Sample PCAP file successfully created at {output_path}")
else:
    print(f"Failed to create PCAP file at {output_path}")
