from data import dataset
from validators.lib import *


def add_client_product(client_phone, buy_date, product_name):
    if client_phone in dataset:
        if buy_date in dataset[client_phone]:
            if product_name in dataset[client_phone][buy_date]:
                dataset[client_phone][buy_date][product_name] += 1
            else:
                dataset[client_phone][buy_date][product_name] = 1
        else:
            dataset[client_phone][buy_date] = {product_name: 1}
    else:
        new_data = dict()
        new_data[client_phone] = {buy_date: {product_name: 1}}
        print(new_data)
        dataset[client_phone] = new_data[client_phone]

print('first test')
number = get_client_number()
date = get_date()
product = get_product_name()
#Додати нового користувача та нову покупку
add_client_product(number, date, product)

print('second test')
date = get_date()
product = get_product_name()
#Додати існуючому користувачу нову покупку нового продукту
add_client_product('222-4444', date, product)


print('third test')
#Додати існуючому користувачу нову покупку існуючого продукту
add_client_product('222-4444', "10.12.2018", 'cheese')


print(dataset)
print(dataset['222-4444'])
print(dataset['111-2222'])
print("\n\n")