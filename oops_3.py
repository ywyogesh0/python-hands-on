from abc import ABC, abstractmethod


class Payment(ABC):

    def __init__(self, payment_id, amount):
        self.payment_id = payment_id
        self.amount = amount

    @abstractmethod
    def processing_fee(self):
        pass


class CardPayment(Payment):

    def __init__(self, payment_id, amount, card_type):
        super().__init__(payment_id, amount)
        self.card_type = card_type

    def processing_fee(self):
        return 0.02 * self.amount


class BankTransferPayment(Payment):

    def processing_fee(self):
        return 0.01 * self.amount


def total_processing_fee(pay):
    total = 0.0

    for p in pay:
        total += p.processing_fee()

    return total

if __name__ == "__main__":
    card = CardPayment("P1", 1000, "VISA")
    bank = BankTransferPayment("P2", 1000)

    print(card.payment_id)  # P1
    print(card.amount)  # 1000

    print(card.processing_fee())  # 20.0
    print(bank.processing_fee())  # 10.0

    payments = [
        CardPayment("P1", 1000, "VISA"),
        BankTransferPayment("P2", 2000),
        CardPayment("P3", 500, "VISA")
    ]

    print(total_processing_fee(payments))