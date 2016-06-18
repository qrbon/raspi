import qrcode, Tkinter as tk

class QR_Maker():
    # INPUTS AND CUSTOMISATION
    def __init__(self, string, size=1, pattern=10, bd=4, error=qrcode.constants.ERROR_CORRECT_H):
        self.URL_to_compile = str(string)
        self.sizeOfQR = size
        self.sizeOfPattern = pattern
        self.border = bd
        self.errorCorrecction = error
        return

    # GENERATING
    def compileToQR(self):
        qr = qrcode.QRCode(version=self.sizeOfQR, error_correction=self.errorCorrecction,
                           box_size=self.sizeOfPattern, border=self.border)
        qr.add_data(self.URL_to_compile)
        qr.make(fit=True)
        return qr.make_image()

    # SAVING
    def saveQR(self):
        outFile = open("QR_OUT.png", "w")
        out = self.compileToQR()
        out.save(outFile)
        return

    # DISPLAYING THE QR CODE
    def showCode(self):
        wn = tk.Tk()
        wn.configure(background='white')
        wn.attributes("-fullscreen", True)
        QR_img = tk.PhotoImage(file="QR_OUT.png")
        cv = tk.Canvas(wn, width=750, height=750)
        cv.configure(bg="white", bd=1)
        cv.pack()
        cv.create_image(0, 0, image=QR_img, anchor=tk.NW)
        wn.mainloop()
        return

    def run(self):
        self.saveQR()
        self.showCode()
        return
    pass

if __name__ == '__main__':
    QR = QR_Maker("Hallo, ich heisse Yorick.", size=12, pattern=8)
    QR.run()







