import os
import base64
from docx import Document

# 바이너리 파일 <> 워드 파일간 변환 프로그램

# 라이브러리 설치 필요
# pip install python-docx

BINARYDIR = "./binary"
WORDDIR = "./docx"
def binaryToWord(fileLocation : str, fileName : str):
    global BINARYDIR
    global WORDDIR

    with open(fileLocation, 'rb') as f:
        binaryData = b''.join(f.readlines())
        res = base64.b64encode(binaryData)
        res = res.decode('utf-8')
        doc = Document()
        doc.add_paragraph(res)
        doc.save(WORDDIR + "/" + fileName + '.docx')

def wordToBinary(fileLocation : str, fileName : str):
    global BINARYDIR
    global WORDDIR

    # binary to word
    doc = Document(fileLocation)
    data = doc.paragraphs[0].text
    data = data.encode(encoding='utf-8')
    res = base64.b64decode(data)
    with open(BINARYDIR + "/" + fileName[:fileName.rfind('.docx')], 'wb') as g:
            g.write(res)

def converter():
    bdir = os.listdir(BINARYDIR)
    wdir = os.listdir(WORDDIR)

    for fileName in bdir:
        if fileName == ".DS_Store" : # mac에서 사용하는 메타파일 제외
            continue
        # if os.path.isfile(dir) : -> mac에서 안먹혀서 일단 제외
        print("convert binaryFile to wordFile :", fileName)
        binaryToWord(BINARYDIR + "/" + fileName, fileName)
    
    for fileName in wdir:
        if fileName == ".DS_Store" :
            continue
        print("convert text to visx :", fileName)
        wordToBinary(WORDDIR + "/" + fileName, fileName)

if __name__ == '__main__':
    converter()