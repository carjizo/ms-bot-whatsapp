from paddleocr import PaddleOCR

class PaddleOCRModel():
    def __init__(self, img):
        self.img = img

    def getData(self):
        paddle_ocr = PaddleOCR(lang='es')
        paddle_result = paddle_ocr.ocr(self.img, cls=True)
        for rsp in paddle_result:
            for i in rsp:
                print(i)