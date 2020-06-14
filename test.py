from pyresparser import ResumeParser
from fpdf import FPDF


def conv(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Courier', 'B', 16)
    pdf.cell(40, 10, data)
    pdf.output('a.pdf', 'F')
    data = ResumeParser('a.pdf').get_extracted_data()
    return data['skills']


def extract(filename):
    # print(filename,'fff')
    data = ResumeParser(filename).get_extracted_data()
    return data['skills']
