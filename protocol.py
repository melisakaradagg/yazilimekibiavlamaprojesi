from scapy.all import *
import netifaces
import logging

# Log dosyasını yapılandır
logging.basicConfig(filename="network_log.txt", level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

def list_interfaces():
    """Ağ arayüzlerini listele"""
    interfaces = netifaces.interfaces()
    print("Kullanılabilir ağ arayüzleri:")
    for i, iface in enumerate(interfaces, 1):
        print(f"{i}. {iface}")
    choice = int(input("Hangi arayüzü kullanmak istiyorsunuz? (1, 2, ...): ")) - 1
    return interfaces[choice]

def packet_callback(packet):
    """Yakalanan paketleri analiz et ve protokolleri tespit et"""
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        # FTP (port 20 veya 21)
        if src_port in [20, 21] or dst_port in [20, 21]:
            log_message = f"[FTP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
            print(log_message)
            logging.info(log_message)

        # SSH (port 22)
        elif src_port == 22 or dst_port == 22:
            log_message = f"[SSH] {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
            print(log_message)
            logging.info(log_message)

        # MySQL (port 3306)
        elif src_port == 3306 or dst_port == 3306:
            log_message = f"[MySQL] {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
            print(log_message)
            logging.info(log_message)

        # SQL Server (port 2382 veya 2383)
        elif src_port in [2382, 2383] or dst_port in [2382, 2383]:
            log_message = f"[SQL Server] {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
            print(log_message)
            logging.info(log_message)

def main():
    # Ağ arayüzünü seç
    interface = list_interfaces()
    print(f"Seçilen arayüz: {interface}")

    # Paket yakalama filtresi
    capture_filter = "tcp port 20 or tcp port 21 or tcp port 22 or tcp port 3306 or tcp port 2382 or tcp port 2383"

    try:
        print("Ağ dinleniyor... Çıkmak için Ctrl+C basın.")
        sniff(iface=interface, filter=capture_filter, prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\nDinleme durduruldu.")

if __name__ == "__main__":
    main()
