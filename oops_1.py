class Payment:

    def __init__(self, payment_id, customer_id, amount, status):
        self.payment_id = payment_id
        self.customer_id = customer_id
        self.amount = amount
        self.status = status

    def is_successful(self):
        return self.status == "SUCCESS"

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self._amount = amount

if __name__ == "__main__":
    p1 = Payment("P1", "C1", 100.50, "SUCCESS")
    p2 = Payment("P2", "C2", 250.00, "FAILED")

    print(p1.payment_id)
    print(p1.amount)
    print(p1.is_successful())
    print(p2.is_successful())