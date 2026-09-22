from collections import defaultdict

payments = [
    {"payment_id": "P1", "customer_id": "C1", "amount": 100},
    {"payment_id": "P2", "customer_id": "C2", "amount": 200},
    {"payment_id": "P3", "customer_id": "C1", "amount": 300},
    {"payment_id": "P4", "customer_id": "C2", "amount": 400},
    {"payment_id": "P5", "customer_id": "C1", "amount": 500},
]

def group_payments_by_customer(pay):
    payments_by_customer = {}

    for p in pay:
        payments_by_customer.setdefault(p["customer_id"], []).append(p)

    return payments_by_customer

def group_payments_by_customer_default_dict(pay):
    payments_by_customer = defaultdict(list)

    for p in pay:
        payments_by_customer[p["customer_id"]].append(p)

    return dict(payments_by_customer.items())

if __name__ == '__main__':
    print(group_payments_by_customer(payments))
    print(group_payments_by_customer_default_dict(payments))