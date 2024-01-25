import random
from faker import Faker

from datetime import datetime
from confluent_kafka import SerializingProducer


fake = Faker()


def generate_sales_transactions():

    # 1. Create Simple profile
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),
        "productName": random.choice(['laptop', 'mobile', 'tablet', 'watch', 'headphone', 'speaker']),
        'productCategory': random.choice(['electronic', 'fashion', 'grocery', 'home', 'beauty', 'sports']),
        'productPrice': round(random.uniform(10, 1000), 2),
        'productQuantity': random.randint(1, 10),
        'productBrand': random.choice(['apple', 'samsung', 'oneplus', 'mi', 'boat', 'sony']),
        'currency': random.choice(['USD', 'GBP']),
        'customerId': user['username'],
        'transactionDate': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'online_transfer'])
    }

# 2 Specify main function Serializing Producer
def main():
    topic = 'financial_transactions'
    producer = SerializingProducer({
        "bootstrap.servers": 'localhost:9092'
    })

    curr_time = datetime.now()

    while ((datetime.now - curr_time)).seconds < 120:
        try:
            transaction = generate_sales_transactions()
            transaction['totalAmount'] = transaction['productPrice'] * transaction['productQuantity']

            print(transaction)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
