import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Send message to the queue
channel.basic_publish(exchange='', routing_key='myqueue', body='Hello, RabbitMQ!')

connection.close()

