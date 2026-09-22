transactions = [
    {"id": "P1", "amount": 100, "status": "SUCCESS"},
    {"id": "P2", "amount": 500, "status": "FAILED"},
    {"id": "P3", "amount": 300, "status": "SUCCESS"},
    {"id": "P4", "amount": 50,  "status": "SUCCESS"},
    {"id": "P5", "amount": 700, "status": "SUCCESS"},
]

def high_value_successful_payments(txn, threshold):
    return [
        t["id"]
        for t in txn
        if t["status"] == "SUCCESS" and t["amount"] > threshold
    ]


if __name__ == '__main__':
    print(high_value_successful_payments(transactions, 300))