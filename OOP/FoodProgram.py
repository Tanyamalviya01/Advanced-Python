import FoodClass as fc

def main():
    data = { # transaction data
        'The Octoveg': {'price': 16.00, 'customer_id': 570},
        'The Octoburger': {'price': 20.00, 'customer_id': 570},
        'The Lone Patty': {'price': 17.00, 'customer_id': 569},
        'The Octobreakfast': {'price': 18.00, 'customer_id': 569}
    }
    
    id = int(input('Enter customer ID: ')) # get customer info
    name = input('Enter name: ')
    address = input('Enter address: ')
    email = input('Enter email: ')
    phone = input('Enter phone: ')
    member_input = input('Enter member status (True/False): ')
    
    if member_input == 'True':
        member = True
    else:
        member = False
    
    c = fc.Customer(id, name, address, email, phone, member) # create customer
    
    orders = []  # create transactions for this customer
    for item in data:
        if data[item]['customer_id'] == id:
            t = fc.Transaction('2024-01-15', item, data[item]['price'], id)
            orders.append(t)
    
    print('Customer Name:', c.get_name()) # display results
    print('Phone:', c.get_phone())
    
    total = 0.0
    for order in orders:
        print('Order Item:', order.get_item(), ' Price: $' + format(order.get_cost(), '.2f'))
        total = total + order.get_cost()
    
    print('Total Cost: $' + format(total, '.2f'))
    
    if c.get_member():
        discount = total * 0.20
        print('Member Discount: $' + format(discount, '.2f'))
        final = total - discount
        print('Total Cost after discount: $' + format(final, '.2f'))

main()
