package main

import (
	"fmt"
	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func produceToKafka(topic string, message string) {
	p, err := kafka.NewProducer(&kafka.ConfigMap{"bootstrap.servers": "localhost:9092"})
	if err != nil {
		panic(err)
	}
	defer p.Close()

	deliveryChan := make(chan kafka.Event)
	_ = p.Produce(&kafka.Message{
		TopicPartition: kafka.TopicPartition{Topic: &topic, Partition: kafka.PartitionAny},
		Value:          []byte(message),
	}, deliveryChan)

	e := <-deliveryChan
	m := e.(*kafka.Message)
	if m.TopicPartition.Error != nil {
		fmt.Printf("Delivery failed: %v\n", m.TopicPartition.Error)
	} else {
		fmt.Printf("Delivered message to %v\n", m.TopicPartition)
	}
	close(deliveryChan)
}

func main() {
	fmt.Println("Go Monitor Service Initialized")
	produceToKafka("raw_traffic", "Sample packet data")
}
