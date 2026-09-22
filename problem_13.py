records = [
    "P1,C1,100.00,SUCCESS",
    "P2,C2,200.00,FAILED",
    "P3,C1,300.00,SUCCESS",
    "INVALID",
    "P4,C2,150.00,SUCCESS",
    "P5,C1,ABC,SUCCESS",
    "P6,C3,500.00,SUCCESS",
    "P7,C1,200.00,SUCCESS",
]

def customer_totals(rec):
    cus = {}

    for r in rec:
        # Skip malformed records.
        try:
            # Parse each CSV string.
            r_arr = r.split(",")

            # Only include SUCCESS payments.
            if r_arr[3] == "SUCCESS":
                # Aggregate total successful amount by customer.
                cus[r_arr[1]] = cus.get(r_arr[1], 0) + float(r_arr[2])

        except (IndexError, ValueError, TypeError):
            continue

    # Return customers sorted by total amount descending.
    sorted_list = sorted(cus.items(), key=lambda x: x[1], reverse=True)

    return sorted_list


if __name__ == '__main__':
    print(customer_totals(records))