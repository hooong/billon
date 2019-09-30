from django.shortcuts import render
from google.cloud import vision
import os, io, re
from recipt_test.settings import BASE_DIR

def ocr_test(request):
    # detect_text_uri("http://cfile227.uf.daum.net/image/14082C4F502CAABC3090D1")
    p = os.path.join(BASE_DIR,'recipt_image/4_.jpeg')
    
    recipt = detect_text(p)
    recipt_split = recipt.split('\n')

    # 합계금액
    total_amounts = TOTAL_AMOUNT(recipt)
    print("합계금액:", total_amounts)

    # 사업자번호
    bu_Regist_Number = BSNS_RGNMB(recipt)   
    print('사업자번호', bu_Regist_Number)

    # 거래일시
    deal_date = DEAL_DATE(recipt)
    print('거래일시', deal_date)

    return render(request,"ocr.html", {'recipt':recipt_split})

# uri이미지
def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations

# 로컬이미지
def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    # OCR로 읽은 전체 문자열
    recipt_text = texts[0].description
    print(recipt_text)

    return recipt_text

# 합계 금액
def TOTAL_AMOUNT(recipt_text):
    # .으로 오는 경우, ,으로 오는경우
    amount_form = re.compile(r'[0-9]*[.,][0-9]{3}')     # "00,000", "00.000"

    # 영수증에 있는 금액들 모두 불러오기
    amounts = amount_form.findall(recipt_text)
    amounts = list(set(amounts))    # 중복되는것 제거

    for i in range(len(amounts)):
        amounts[i] = int(re.sub('[,.]','',amounts[i]))

    return max(amounts)

# 사업자번호
def BSNS_RGNMB(recipt_text):
    number_form = re.compile(r'[0-9]{3}[-][0-9]{2}[-][0-9]{5}[\s]')     # "000-00-00000"
    rg_num = number_form.findall(recipt_text)

    return rg_num[0][:-1]

# 거래일시
def DEAL_DATE(recipt_text):
    date_form = re.compile(r'[0-9]{4}[-/][0-9]{2}[-/][0-9]{2}[\s][0-9]{2}[:][0-9]{2}')      # "0000-00-00 00:00", "0000/00/00 00:00"
    deal_date = date_form.findall(recipt_text)
    
    return deal_date[0]