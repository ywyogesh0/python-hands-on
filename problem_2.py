transactions = [
    {"payment_id": "P1", "status": "SUCCESS"},
    {"payment_id": "P2", "status": "FAILED"},
    {"payment_id": "P3", "status": "SUCCESS"},
    {"payment_id": "P4", "status": "PENDING"},
    {"payment_id": "P5", "status": "FAILED"},
    {"payment_id": "P6", "status": "SUCCESS"}
]

def count_status(txn):
    status_dict = {}

    for t in txn:
        status_dict[t["status"]] = status_dict.get(t["status"], 0) + 1

    return status_dict


if __name__ == '__main__':
    print(count_status(transactions))