import sys
import qrcode

def genQR(text):
    '''Commandline app which accepts a text as parameter and
    gives a png qrcode image as output
    run myqrcode.py [text]
    Author: ir. Erik Mols
    ep.mols@os-sci.com'''
    img = qrcode.make(text)
    type(img)
    img.save('MyQRCode1.png')

if __name__ == '__main__':
    QR = ""
    print("This is the output of the qrcode program\n")
    print(f"Arguments count: {len(sys.argv)}")
    for i in range (1, len(sys.argv), 1):
        QR = QR + sys.argv[i] + " "
    print("QR code in image = " + QR)
    genQR(QR)
    print("Saved as: MyQRCode1.png in program root")

