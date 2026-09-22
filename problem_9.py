payments = [
    {
        "payment_id": "P1",
        "customer": {
            "id": "C1",
            "name": "John"
        },
        "payment": {
            "amount": 100.50,
            "currency": "GBP"
        }
    },
    {
        "payment_id": "P2",
        "customer": {
            "id": "C2",
            "name": "Alice"
        },
        "payment": {
            "amount": 250.00,
            "currency": "USD"
        }
    }
]

def flatten_payments(pay):
    result = []

    for p in pay:
        try:
            result.append(
                {
                    "payment_id": p["payment_id"],
                    "customer_id": p["customer"]["id"],
                    "amount": float(p["payment"]["amount"]),
                    "currency": p["payment"]["currency"]
                }
            )
        except (KeyError, ValueError, TypeError):
            continue

    return result

def flatten_payments_comprehension_parser(p):
    try:
        return {
            "payment_id": p["payment_id"],
            "customer_id": p["customer"]["id"],
            "amount": float(p["payment"]["amount"]),
            "currency": p["payment"]["currency"]
        }
    except (KeyError, ValueError, TypeError):
        return None

def flatten_payments_comprehension(pay):
    return [
        p_result
        for p in pay
        if (p_result := flatten_payments_comprehension_parser(p)) is not None
    ]


if __name__ == '__main__':
    print(flatten_payments(payments))
    print(flatten_payments_comprehension(payments))