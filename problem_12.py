from datetime import datetime

payments = [
    {
        "payment_id": "P1",
        "amount": 100,
        "timestamp": "2026-09-20 10:15:00"
    },
    {
        "payment_id": "P1",
        "amount": 150,
        "timestamp": "2026-09-20 12:30:00"
    },
    {
        "payment_id": "P2",
        "amount": 200,
        "timestamp": "2026-09-19 09:00:00"
    },
    {
        "payment_id": "P2",
        "amount": 250,
        "timestamp": "2026-09-20 08:00:00"
    }
]

def latest_payments(pay):
    p_dict = {}

    for p in pay:
        if p["payment_id"] not in p_dict:
            p_dict[p["payment_id"]] = p
        else:
            p_formatted_datetime = datetime.strptime(
                p["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )
            dict_formatted_datetime = datetime.strptime(
                p_dict[p["payment_id"]]["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            if p_formatted_datetime > dict_formatted_datetime:
                p_dict[p["payment_id"]] = p

    return list(p_dict.values())

if __name__ == '__main__':
    print(latest_payments(payments))