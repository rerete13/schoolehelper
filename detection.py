import easyocr
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def detect_text(img:str):

    reader = easyocr.Reader(['en'])
    resualt = reader.readtext(img, detail=0, batch_size=1, paragraph=True)
    
    return resualt


# print(detect_text('2.png'))


def get_text(img:str):
    x = detect_text(img)
    y = ''
    for i in x:
        y += i + '\n'
        
    return y
        
    
# print(get_text('2.png'))

