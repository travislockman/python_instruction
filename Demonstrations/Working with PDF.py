from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import time

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
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

data = convert_pdf_to_txt('mmil.pdf')
datalist = data.split("\n")
holding_list = []
page_count = 0

for item in datalist:
    if 'Page' in item:
        page_count += 1

main_list = []
for x in range(page_count):
    main_list.append([])

print(main_list)
main_list_pos = -1

for item in datalist:
    print(item)
    if 'Page' in item:
        main_list_pos += 1

    try:
        item = int(item)
        main_list[main_list_pos].append(item)
        print(f"Found Integer: {item}!!!")

    except ValueError as e:
        pass

print(main_list)
print(len(main_list))
