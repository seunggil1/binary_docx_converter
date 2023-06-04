# binary_docx_converter
- binary File을 Word 파일로, Word파일을 Binary File로 변환시켜주는 프로그램
- binary 파일을 base64 인코딩하고 그 내용을 word 파일에 저장하고, 반대로 그 과정을 진행해 돌리는 프로그램.  
`base64 : 바이너리 데이터를 문자 코드에 영향을 받지 않는 공통 ASCII 문자로 표현하기 위해 만들어진 인코딩.`
- txt나 pdf는 내용이 바뀌는 문제가 있어 docx 형식을 사용했습니다.


### 프로그램 용도
각종 파일(.exe, .zip) 전송을 막는 naver, gmail에서 파일을 보내거나,  
보안 문제로 바이너리 파일 반입을 막는 곳(...)에 몰래 넣을 때 사용합니다.


### 지원 파일 형식
- binary file : 문서 파일 말고 대부분의 해당(.exe, .msi, .zip 등등..)  
- word file : Microsoft word(.docx)  


### How To use
#### 기본 원리 : binary -> word -> 원하는 곳으로 전송(word 전송은 가능하다는 기준하에) -> 내부에서 다시 binary로 변환  

1. git clone or releases에서 [`converter.zip`](https://github.com/seunggil1/binary_docx_converter/releases) 다운로드 후 압축해제
2. (git clone한 경우) python과 python-docx 라이브러리 설치  
   `pip install python-docx`
3. converter.py(converter.exe) 있는 경로에 binary, docx 폴더 생성
4. binary폴더에 변환하고 싶은 파일 넣기.
5. converter.py or converter.exe 실행 
6. docx 폴더에 생성된 결과물을 원하는 곳으로 전송.
7. docx 파일을 받은 컴퓨터에서 다시 1~3 진행
8. docx파일을 docx 폴더에 넣기
9. 5번과정을 다시 진행하면 docx를 binary 파일로 변환하고 binary 폴더에 저장된다.
