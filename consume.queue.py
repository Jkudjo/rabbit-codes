import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='myqueue')

# Consume messages from the queue
def callback(ch, method, properties, body):
    print("Received message:", body)

channel.basic_consume(queue='myqueue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

