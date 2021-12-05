import webbrowser
import os
from fpdf import FPDF


class PDFReport:
    """
    Creates a pdf file of the bill report
    which contains the flatmates name, their
    bill amount & the time period
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        """
        This function generates a pdf file having the split amount
        between the flatmates
        """

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add house rent icon
        pdf.image('data/house_rent_icon.jpg', w=75, h=75)

        # Insert title
        pdf.set_font(family='Times', size=32, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert Period label & value
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=100, h=50, txt='Period: ', border=0)
        pdf.cell(w=200, h=50, txt=bill.period, border=0, ln=1)

        # Insert Period label & value
        pdf.set_font(family='Times', size=14, )
        pdf.cell(w=100, h=50, txt=flatmate1.name, border=0)
        pdf.cell(w=200, h=50, txt=str(flatmate1.pays(bill, flatmate2)), border=0, ln=1)

        # Insert Period label & value
        pdf.cell(w=100, h=50, txt=flatmate2.name, border=0)
        pdf.cell(w=200, h=50, txt=str(flatmate2.pays(bill, flatmate1)), border=0, ln=1)

        os.chdir('data')
        pdf.output(f'{self.filename}.pdf')
        webbrowser.open(f'{self.filename}.pdf')