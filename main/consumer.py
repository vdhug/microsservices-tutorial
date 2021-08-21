import pika


params = pika.URLParameters(
    'amqps://zayhgiim:mSZ0s3COp4o1D86Vev_pPxIrVRxGXrcR@cattle.rmq2.cloudamqp.com/zayhgiim'
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(channel, method, properties, body):
    print("Received in main")
    print(body)

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()