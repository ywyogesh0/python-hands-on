customers = [
    {"customer_id": "C1", "name": "John", "country": "UK"},
    {"customer_id": "C2", "name": "Alice", "country": "US"},
    {"customer_id": "C3", "name": "Bob", "country": "IN"}
]

payments = [
    {"payment_id": "P1", "customer_id": "C1", "amount": 100},
    {"payment_id": "P2", "customer_id": "C2", "amount": 200},
    {"payment_id": "P3", "customer_id": "C1", "amount": 300},
    {"payment_id": "P4", "customer_id": "C4", "amount": 400}
]

def join_payments_customers(pay, cus):
    join_result = []

    cus_dict = {
        c["customer_id"]: c
        for c in cus
    }

    for p in pay:
        try:
            cus_result = cus_dict.get(p["customer_id"])

            join_result.append(
                {
                    "payment_id": p["payment_id"],
                    "customer_id": p["customer_id"],
                    "amount": p["amount"],
                    "name": cus_result["name"] if cus_result else None,
                    "country": cus_result["country"] if cus_result else None
                }
            )

        except KeyError:
            continue

    return join_result

if __name__ == '__main__':
    print(join_payments_customers(payments, customers))