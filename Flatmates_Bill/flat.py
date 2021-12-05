class Bill:
    """
    A Bill object which will store the bill information
    like total bill amount & time period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    A Flatmate object who lives in the flat and
    stays for a specific amount of time there and thus
    needs to pay a portion of the amount
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        ratio = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * ratio, 2)