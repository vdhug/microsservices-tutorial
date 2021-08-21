import pika


params = pika.URLParameters(
    'amqps://zayhgiim:mSZ0s3COp4o1D86Vev_pPxIrVRxGXrcR@cattle.rmq2.cloudamqp.com/zayhgiim'
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(channel, method, properties, body):
    print("Received in admin")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print("Started consuming")

channel.start_consuming()

channel.close()