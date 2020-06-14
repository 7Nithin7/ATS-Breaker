import spacy
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from collections import Counter, OrderedDict

import docx2txt

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def extractor(text, skills):
    skills = [a.lower() for a in skills]
    doc = nlp(text)
    l = [token.text.lower() for token in doc if token.text.lower() in skills]
    
    # print(Counter(l).most_common())
    return Counter(l)


def wordfinder(filename, skills):
    if (filename.rsplit('.', 1)[1] == 'pdf'):
        text = convert_pdf_to_txt(filename)
    elif ((filename.rsplit('.', 1)[1] == 'doc') or (filename.rsplit('.', 1)[1] == 'docx')):
        text = convert_docx2txt(filename)
    return extractor(text, skills)
    


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def convert_docx2txt(path):
    return docx2txt.process(path)


def main():
    # print(convert_pdf_to_txt('CV_-_Nivin_C_George.pdf'))
    # print(convert_docx2txt('SUJA K MATHEW.docx'))
    wordfinder('SUJA K MATHEW.docx', ['windows'])


if __name__ == "__main__":
    main()
