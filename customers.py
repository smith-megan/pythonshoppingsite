"""Customers at Ubermelon."""


class Customer(object):
    """Ubermelon customer."""
    def __init__(self,
                first_name,
                last_name,
                email,
                password):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password
        self.email=email

    def __repr__(self):
        return f"<customer: {self.first_name}, {self.last_name}, {self.password}, {self.email}>"


def read_customers_from_file(filepath):

    customers={}

    with open(filepath) as file:
        for line in file:
            (first_name,
            last_name,
            email,
            password
            ) = line.strip().split("|")
            customers[email]=Customer(first_name,
                                    last_name,
                                    password,
                                    email)
    print(customers)
    return customers

def get_customer_id(customer_email):
    return customer_list[customer_email]

customer_list = read_customers_from_file("customers.txt")
