transactions = [
    {"customer": "C1", "amount": 100},
    {"customer": "C2", "amount": 300},
    {"customer": "C1", "amount": 200},
    {"customer": "C3", "amount": 500},
    {"customer": "C2", "amount": 250},
    {"customer": "C4", "amount": 50},
]

def top_customers(txn, n):
    # aggregate
    agg_dict = {}
    for t in txn:
        agg_dict[t["customer"]] = agg_dict.get(t["customer"], 0) + t["amount"]

    # sort by total amount descending
    sorted_list = sorted(agg_dict.items(), key=lambda x: x[1], reverse=True)

    # return top n
    return sorted_list[:n]


if __name__ == '__main__':
    print(top_customers(transactions, 2))