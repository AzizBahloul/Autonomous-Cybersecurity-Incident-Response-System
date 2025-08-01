import scapy.all as scapy
from kafka import KafkaConsumer

def ingest_pcap(file_path):
    packets = scapy.rdpcap(file_path)
    print(f"Ingested {len(packets)} packets from {file_path}")

def consume_from_kafka(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='python-detector-group')

    for message in consumer:
        print(f"Consumed message: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    ingest_pcap("/home/siaziz/Desktop/Autonomous Cybersecurity Incident Response System/autocidr/detection/python-detector/src/example.pcap")
    consume_from_kafka("raw_traffic")
