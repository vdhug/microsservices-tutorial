import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product


params = pika.URLParameters(
    'amqps://zayhgiim:mSZ0s3COp4o1D86Vev_pPxIrVRxGXrcR@cattle.rmq2.cloudamqp.com/zayhgiim'
)

connection = pika.BlockingConnection(parameters=params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(channel, method, properties, body):
    print("Received in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save(update_fields=['likes'])

    print("Product likes increased")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()

channel.close()