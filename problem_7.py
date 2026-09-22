transactions = [
    {"id": "P1", "amount": 100, "status": "SUCCESS"},
    {"id": "P2", "amount": 500, "status": "FAILED"},
    {"id": "P3", "amount": 300, "status": "SUCCESS"},
    {"id": "P4", "amount": 50,  "status": "SUCCESS"},
    {"id": "P5", "amount": 700, "status": "FAILED"},
]

def filter_payments(txn, status="SUCCESS", min_amount=0):
    return [
        t
        for t in txn
        if t["status"] == status and t["amount"] >= min_amount
    ]


if __name__ == '__main__':
    print(filter_payments(transactions))
    print(filter_payments(transactions, status="FAILED", min_amount=400))
    print(filter_payments(transactions, min_amount=400, status="FAILED"))