from flat import Bill, Flatmate
from pdf_report import PDFReport

bill_amount = float(input("Hey User! Enter the bill amount: "))
bill_period = input("What is the bill period? E.g. December 2021 ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during the bill time period? "))

name2 = input("What is your flatmate's name? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill time period? "))

the_bill = Bill(bill_amount, bill_period)
first_flatmate = Flatmate(name=name1, days_in_house=days_in_house1)
second_flatmate = Flatmate(name=name2, days_in_house=days_in_house2)

print(f'{first_flatmate.name} Pays : {first_flatmate.pays(the_bill, second_flatmate)}')
print(f'{second_flatmate.name} Pays : {second_flatmate.pays(the_bill, first_flatmate)}')

pdf_report = PDFReport(filename=f'{the_bill.period} Bill')
pdf_report.generate(first_flatmate, second_flatmate, bill=the_bill)
