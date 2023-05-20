
my_list = [6, 2, 8, 2]

def print_data(seq):
    for elem in seq:
        print(elem)


print("Outside the function:", id(my_list))
print_data(my_list)


def multiply_by_two(seq):
    for i in range(len(seq)):
        seq[i] *= 2

print("Outside the function", id(my_list))
multiply_by_two((my_list))

print(my_list)


class Sale:
    def __init__(self, amount):
        self.amount = amount

def find_total(sales_list):
    total=0

    for sale in sales_list:
        total+= sale.amount

    return total

january_sales = [Sale(400), Sale(345), Sale(45)]

print(find_total(january_sales))