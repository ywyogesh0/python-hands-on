transactions = [
    {"payment_id": "P1", "timestamp": "2026-09-18T10:00:00", "amount": 100},
    {"payment_id": "P2", "timestamp": "2026-09-18T10:05:00", "amount": 200},
    {"payment_id": "P1", "timestamp": "2026-09-18T10:10:00", "amount": 150},
    {"payment_id": "P3", "timestamp": "2026-09-18T10:15:00", "amount": 300},
    {"payment_id": "P2", "timestamp": "2026-09-18T09:55:00", "amount": 180},
]

def latest_payments(txn):
    latest_payment_dict = {}

    for t in txn:
        if t["payment_id"] not in latest_payment_dict:
            latest_payment_dict[t["payment_id"]] = t
        else:
            previous_txn = latest_payment_dict[t["payment_id"]]

            if t["timestamp"] > previous_txn["timestamp"]:
                latest_payment_dict[t["payment_id"]] = t

    return list(latest_payment_dict.values())


if __name__ == '__main__':
    print(latest_payments(transactions))