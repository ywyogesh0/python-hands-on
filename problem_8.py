records = [
    "P1,C1,100.50,SUCCESS",
    "P2,C2,ABC,FAILED",
    "P3,C1",
    "P3,C1,150.75,SUCCESS"
]

def parse_payments(rec):
    result = []

    # your implementation
    for r in rec:
        try:
            r_arr = r.split(",")
            result.append(
                {
                    "payment_id": r_arr[0],
                    "customer_id": r_arr[1],
                    "amount": float(r_arr[2]),
                    "status": r_arr[3]
                }
            )
        except (ValueError, IndexError):
            continue

    return result


if __name__ == '__main__':
    print(parse_payments(records))