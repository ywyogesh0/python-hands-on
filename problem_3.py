transactions = [
    {"payment_id": "P1", "customer": "C1", "amount": 100},
    {"payment_id": "P2", "customer": "C2", "amount": 200},
    {"payment_id": "P1", "customer": "C1", "amount": 100},
    {"payment_id": "P3", "customer": "C1", "amount": 150},
    {"payment_id": "P2", "customer": "C2", "amount": 200},
    {"payment_id": "P4", "customer": "C3", "amount": 300},
]

def find_duplicate_payments(txn):
    seen = set()
    dup = set()

    for t in txn:
        if t["payment_id"] not in seen:
            seen.add(t["payment_id"])
        else:
            dup.add(t["payment_id"])

    return dup

if __name__ == '__main__':
    print(find_duplicate_payments(transactions))