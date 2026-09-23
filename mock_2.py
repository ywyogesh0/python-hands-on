# Requirements: Implement a Python function that selects the highest-version event for each payment,
# excludes events that are not successful or have an invalid amount,
# and returns the total successful amount per customer. The function must not mutate the input.

# For this exercise, an amount is valid if it is a positive integer or float;
# None, zero, negative values and booleans are invalid.
# Assume payment_id, customer_id, status and version are present,
# and versions are integers with a unique highest version per payment.

# expected result: {"C1": 120, "C3": 300}

payments = [
    {"payment_id": "P1", "customer_id": "C1", "amount": 100, "status": "SUCCESS", "version": 1},
    {"payment_id": "P1", "customer_id": "C1", "amount": 120, "status": "SUCCESS", "version": 2},
    {"payment_id": "P2", "customer_id": "C2", "amount": 200, "status": "SUCCESS", "version": 1},
    {"payment_id": "P2", "customer_id": "C2", "amount": 200, "status": "FAILED",  "version": 2},
    {"payment_id": "P3", "customer_id": "C1", "amount": None, "status": "SUCCESS", "version": 1},
    {"payment_id": "P4", "customer_id": "C3", "amount": 300, "status": "SUCCESS", "version": 2},
    {"payment_id": "P4", "customer_id": "C3", "amount": 400, "status": "FAILED", "version": 1}
]

def customer_successful_totals(payment):
    latest_by_payment = {}
    totals_by_customer = {}

    # Select the highest-version event for each payment.
    for p in payment:
        payment_id = p["payment_id"]

        if (
            payment_id not in latest_by_payment
            or p["version"] > latest_by_payment[payment_id]["version"]
        ):
            latest_by_payment[payment_id] = p

    # Validate the latest events and aggregate by customer.
    for payment in latest_by_payment.values():
        amount = payment["amount"]

        if (
            payment["status"] == "SUCCESS"
            and type(amount) in (int, float)
            and amount > 0
        ):
            customer_id = payment["customer_id"]

            totals_by_customer[customer_id] = (
                totals_by_customer.get(customer_id, 0) + amount
            )

    return totals_by_customer


if __name__ == "__main__":
    print(customer_successful_totals(payments))