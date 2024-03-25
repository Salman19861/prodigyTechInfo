import socket

# Create a raw socket
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Function to print the packets
def print_packet(packet):
    # Unpack the header
    ip_header = packet[:20]
    version_ihl = ip_header[0]
    ihl = version_ihl & 0xF
    iph_length = ihl * 4
    protocol = ip_header[9]
    s_addr = socket.inet_ntoa(ip_header[12:16])
    d_addr = socket.inet_ntoa(ip_header[16:20])

    # Calculate the total length
    total_length = len(packet)

    # Extract the payload
    payload = packet[iph_length:total_length]

    # Print the information
    print("Source IP: {}\nDestination IP: {}\nProtocol: {}\nPayload: {}".format(s_addr, d_addr, protocol, payload))

# Capture the packets
while True:
    packet = sock.recvfrom(6565)
    print_packet(packet[0])