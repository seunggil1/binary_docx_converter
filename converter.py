import os
import json
import base64
import pdfkit
# import pdftotext

VSIXDIR = "./vsix"
TEXTDIR = "./text"
# config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
def vsixToText(fileLocation, fileName):
    global VSIXDIR
    global TEXTDIR
    global config
    with open(fileLocation, 'rb') as f:
        binaryData = b''.join(f.readlines())
        res = base64.b64encode(binaryData)
        res = res.decode('utf-8')
        with open(TEXTDIR + "/" + fileName + '.txt', 'w', encoding='utf-8') as g:
            g.write(res)
def textToVsix(fileLocation, fileName):
    global VSIXDIR
    global TEXTDIR
    with open(fileLocation, 'r', encoding='utf-8') as f:
        data = ''.join(f.readlines())
        res = bytes(data, encoding='utf-8')
        res = base64.b64decode(res)
        with open(VSIXDIR + "/" + fileName + '.vsix', 'wb') as g:
            g.write(res)

def converter():
    for dir in os.listdir(VSIXDIR):
        # if os.path.isfile(dir) :
            print("convert vsix to text :", dir)
            vsixToText(VSIXDIR + "/" + dir, dir)
    
    for dir in os.listdir(TEXTDIR):
        # if os.path.isfile(dir) :
            print("convert text to visx :", dir)
            textToVsix(TEXTDIR + "/" + dir, dir)

if __name__ == '__main__':
    converter()