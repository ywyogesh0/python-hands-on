transactions = [
    {"customer": "C1", "amount": 100},
    {"customer": "C2", "amount": 200},
    {"customer": "C1", "amount": 150},
    {"customer": "C3", "amount": None},
    {"customer": "C2", "amount": 50},
    {"customer": "C1", "amount": 75}
]

def aggregate_transactions(txn):
    agg_txn_dict = {}

    for t in txn:
        if t["amount"] is None:
            continue

        if t["customer"] in agg_txn_dict:
            agg_txn_dict[t["customer"]] += t["amount"]
        else:
            agg_txn_dict[t["customer"]] = t["amount"]

    return agg_txn_dict

if __name__ == '__main__':
    print(aggregate_transactions(transactions))
