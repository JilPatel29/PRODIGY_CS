from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        protocol_name = "Unknown"

        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol_name}")

        if TCP in packet:
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"Payload (first 50 bytes): {payload[:50]}")

        print("-" * 50)

def main(interface):
    print(f"Sniffing on interface {interface}...") 
    print("Press Ctrl+C to stop.")   
    try:
        sniff(iface=interface, prn=packet_callback, store=0, count=50)
    except KeyboardInterrupt:
        print("\nSniffing stopped.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <interface>")
        print("Press Ctrl+C to stop.")

        sys.exit(1)
    
    main(sys.argv[1])
