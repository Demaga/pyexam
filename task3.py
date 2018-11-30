
from data import dataset
from task1 import *

#   Написати рекурсивну функцію, що повертає інформацію: хто і скільки грошей витратив на свої покупки.
#   Рекурсивно необхідно пройтись по користувачам та спискам їх товарів.


#product_list - словник з dataset, що зберігає товар та список його покупок (цін)
def recursionByProducts(user_email, product_list, amount_of_money = 0):
    #TODO


def recursionByUsers(user_emails = list(dataset.keys()), result_dict = dict()):
    #TODO


print("Task 3")

result = recursionByUsers()
print(result)

print("\n\n")



