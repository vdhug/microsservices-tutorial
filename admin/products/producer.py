import pika


params = pika.URLParameters(
    'amqps://zayhgiim:mSZ0s3COp4o1D86Vev_pPxIrVRxGXrcR@cattle.rmq2.cloudamqp.com/zayhgiim'
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello, main!')
