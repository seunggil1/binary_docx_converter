import os
import json
import base64
from docx import Document
# import pdftotext

VSIXDIR = "./vsix"
TEXTDIR = "./text"
def vsixToText(fileLocation, fileName):
    global VSIXDIR
    global TEXTDIR

    with open(fileLocation, 'rb') as f:
        binaryData = b''.join(f.readlines())
        res = base64.b64encode(binaryData)
        res = res.decode('utf-8')
        doc = Document()
        doc.add_paragraph(res)
        doc.save(TEXTDIR + "/" + fileName + '.docx')
    # with open(fileLocation, 'rb') as f:
    #     binaryData = b''.join(f.readlines())
    #     res = base64.b64encode(binaryData)
    #     res = res.decode('utf-8')
    #     with open(TEXTDIR + "/" + fileName + '.txt', 'w', encoding='utf-8') as g:
    #         g.write(res)
def textToVsix(fileLocation, fileName):
    global VSIXDIR
    global TEXTDIR

    doc = Document(fileLocation)
    data = doc.paragraphs[0].text
    data = data.encode(encoding='utf-8')
    res = base64.b64decode(data)
    with open(VSIXDIR + "/" + fileName + '.vsix', 'wb') as g:
            g.write(res)

    # with open(fileLocation, 'r', encoding='utf-8') as f:
    #     data = ''.join(f.readlines())
    #     res = bytes(data, encoding='utf-8')
    #     res = base64.b64decode(res)
    #     with open(VSIXDIR + "/" + fileName + '.vsix', 'wb') as g:
    #         g.write(res)

def converter():
    r = os.listdir(VSIXDIR)
    r.reverse()
    for dir in r:
        # if os.path.isfile(dir) :
            print("convert vsix to text :", dir)
            vsixToText(VSIXDIR + "/" + dir, dir)
    
    for dir in os.listdir(TEXTDIR):
        # if os.path.isfile(dir) :
            print("convert text to visx :", dir)
            textToVsix(TEXTDIR + "/" + dir, dir)

if __name__ == '__main__':
    converter()