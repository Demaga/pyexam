import re


#перевірка тел. номеру клієнта, має бути у форматі 222-4444
def get_client_number():

    user_input = input('Client number:\n')

    if re.match(r"^\d{3}-\d{4}$", user_input):
        return user_input
    else:
        return False


#перевіряє назву покупки, яка має містити не більше 10 символів лат. абетки
def get_product_name():
    user_input = input('Product name:\n')

    if re.match(r"^[a-zA-Z]{1,10}$", user_input):
        return user_input
    else:
        return False


#перевіряє дати, формат: 10.12.2018
def get_date():
    user_input = input('Date:\n')

    if re.match(r"^\d{2}\.\d{2}\.\d{4}$", user_input):
        return user_input
    else:
        return False
