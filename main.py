import json
from tkinter import *
from PIL import Image, ImageTk
import requests
import pickle


def main():
    exchangeRateDict = None

    infile = open("currencies.dat", 'rb')
    countryDict = pickle.load(infile)
    print(countryDict)
    infile.close()
    countries = [k for k in countryDict.keys()]
    countries.sort()

    def convert():
        amount = float(amtA.get())
        from_currency = countryDict[countries[countryFrom.curselection()[0]]][1]
        to_currency = countryDict[countries[countryTo.curselection()[0]]][1]

        if from_currency != to_currency:
            allDataDict=exchangeRateDict['data']
            dictionary1 = allDataDict[from_currency]
            rate1= dictionary1['value']
            dictionary2 = allDataDict[to_currency]
            rate2 = dictionary2['value']
            converted_amount = (amount * rate2)/rate1
            final_amount=round(converted_amount,2)
            amtB.set(str(final_amount))
        else:
            amtB.set(amtA.get())

    def changeCountryFrom(event):
        cntry = countryDict[countries[countryFrom.curselection()[0]]][1]
        imgFrom = "images/"+cntry + ".jpg"
        imgCntryFrom = Image.open(imgFrom)
        cntryFrom = ImageTk.PhotoImage(imgCntryFrom)
        cntryFromLabel.configure(image=cntryFrom)  #label which create line 94
        cntryFromLabel.image = cntryFrom

        country = countries[countryFrom.curselection()[0]]
        flagFrom = "images/"+country + ".JPG"
        imgFF = Image.open(flagFrom)
        imgFlagFrom = ImageTk.PhotoImage(imgFF)
        flagFromToLable.configure(image = imgFlagFrom)
        flagFromToLable.image = imgFlagFrom
        if amtA.get() != '':
            convert()

    def changeCountryTo(event):
        cntry = countryDict[countries[countryTo.curselection()[0]]][1]
        imgTo = "images/"+cntry + ".jpg"
        imgCntryTo = Image.open(imgTo)
        cntryTo = ImageTk.PhotoImage(imgCntryTo)
        cntryToLabel.configure(image=cntryTo)
        cntryToLabel.image = cntryTo

        country = countries[countryTo.curselection()[0]]
        flagTo = "images/"+country + ".JPG"
        imgFTo = Image.open(flagTo)
        imgFlagTo = ImageTk.PhotoImage(imgFTo)
        flagToLable.configure(image=imgFlagTo)
        flagToLable.image = imgFlagTo
        if amtA.get() != '':
            convert()

    def addDigit(n):
        oldval = amtA.get()
        amtA.set(oldval + n)
        convert()

    def addDot():
        oldval = amtA.get()
        amtA.set(oldval + ".")
        convert()

    def clear():
        amtA.set(" ")
        amtB.set(" ")


    def scrapeCurrencies():
        url = 'https://api.currencyapi.com/v3/latest?apikey=5wu2DiOfytWOsMqnj6y0Tb0W0R4PmxyCFk2Eqx4r'
        response = requests.get(url)
        return response.json()

    window = Tk()
    window.geometry("485x400")
    window.title("Currency Converter")

    imgArrow = Image.open("images/arrow.jpg")
    arrow = ImageTk.PhotoImage(imgArrow)

    imgFrom = "images/"+countryDict[countries[0]][1] + ".jpg"
    imgCntryFrom = Image.open(imgFrom)
    cntryFrom = ImageTk.PhotoImage(imgCntryFrom)

    flagFrom="images/"+countries[0] + ".JPG"
    flagFromOpen=Image.open(flagFrom)
    flagFromToUI=ImageTk.PhotoImage(flagFromOpen)

    imgTo = "images/"+countryDict[countries[0]][1] + ".jpg"
    imgCntryTo = Image.open(imgTo)
    cntryTo = ImageTk.PhotoImage(imgCntryTo)

    flagTo = "images/"+countries[0] + ".JPG"
    flagToOpen = Image.open(flagTo)
    flagToUI = ImageTk.PhotoImage(flagToOpen)

    title = Label(window, text="Currency Converter", font=('Calibri 18'), bg="blue", fg="yellow")
    title.grid(row=0, column=0, columnspan=7, sticky=NSEW)

    flagFromToLable =Label(window, image=flagFromToUI, width=55, height=40, bg="white")
    flagFromToLable.grid(row=1, column=0,pady=15, sticky=N)
    cntryFromLabel = Label(window, image=cntryFrom, width=55, height=40, bg="white")
    cntryFromLabel.grid(row=1, column=0, pady=15, sticky=S)

    yscroll1 = Scrollbar(window, orient=VERTICAL)
    yscroll1.grid(row=1, column=1, sticky=NSEW)
    conOfCountryFrom = StringVar()
    countryFrom = Listbox(window, exportselection=0, listvariable=conOfCountryFrom, yscrollcommand=yscroll1.set)
    countryFrom.grid(row=1, column=2, sticky=EW)
    conOfCountryFrom.set(tuple(countries))
    countryFrom.bind("<<ListboxSelect>>", changeCountryFrom)
    yscroll1["command"] = countryFrom.yview

    arrowLabel = Label(window, image=arrow)
    arrowLabel.grid(row=1, column=3)

    yscroll2 = Scrollbar(window, orient=VERTICAL)
    yscroll2.grid(row=1, column=4, sticky=NSEW)
    conOfCountryTo = StringVar()
    countryTo = Listbox(window, exportselection=0, listvariable=conOfCountryTo, yscrollcommand=yscroll2.set)
    countryTo.grid(row=1, column=5, sticky=EW)
    conOfCountryTo.set(tuple(countries))
    countryTo.bind("<<ListboxSelect>>", changeCountryTo)
    yscroll2["command"] = countryTo.yview

    flagToLable = Label(window, image=flagToUI, width=55, height=40, bg="white")
    flagToLable.grid(row=1, column=6, pady=15, sticky=N)
    cntryToLabel = Label(window, image=cntryTo, width=55, height=40, bg="white")
    cntryToLabel.grid(row=1, column=6, pady=15, sticky=S)

    buttonFrame = Frame(window)
    buttonFrame.grid(row=3, column=0, columnspan=7)

    btn1 = Button(buttonFrame, text="1", command=lambda: addDigit('1'), width=4, bg='light blue', font=('Calibri 18'))
    btn1.grid(row=0, column=0, padx=10, pady=5)
    btn1 = Button(buttonFrame, text="1", command=lambda: addDigit('1'), width=4, bg='light blue', font=('Calibri 18'))
    btn1.grid(row=0, column=0, padx=10, pady=5)
    btn2 = Button(buttonFrame, text="2", command=lambda: addDigit('2'), width=4, bg='light blue', font=('Calibri 18'))
    btn2.grid(row=0, column=1, padx=10, pady=5)
    btn3 = Button(buttonFrame, text="3", command=lambda: addDigit('3'), width=4, bg='light blue', font=('Calibri 18'))
    btn3.grid(row=0, column=2, padx=10, pady=5)
    btn4 = Button(buttonFrame, text="4", command=lambda: addDigit('4'), width=4, bg='light blue', font=('Calibri 18'))
    btn4.grid(row=0, column=3, padx=10, pady=5)
    btn5 = Button(buttonFrame, text="5", command=lambda: addDigit('5'), width=4, bg='light blue', font=('Calibri 18'))
    btn5.grid(row=0, column=4, padx=10, pady=5)
    btn6 = Button(buttonFrame, text="6", command=lambda: addDigit('6'), width=4, bg='light blue', font=('Calibri 18'))
    btn6.grid(row=0, column=5, padx=10, pady=5)
    btn7 = Button(buttonFrame, text="7", command=lambda: addDigit('7'), width=4, bg='light blue', font=('Calibri 18'))
    btn7.grid(row=1, column=0, padx=10, pady=5)
    btn8 = Button(buttonFrame, text="8", command=lambda: addDigit('8'), width=4, bg='light blue', font=('Calibri 18'))
    btn8.grid(row=1, column=1, padx=10, pady=5)
    btn9 = Button(buttonFrame, text="9", command=lambda: addDigit('9'), width=4, bg='light blue', font=('Calibri 18'))
    btn9.grid(row=1, column=2, padx=10, pady=5)
    btn0 = Button(buttonFrame, text="0", command=lambda: addDigit('0'), width=4, bg='light blue', font=('Calibri 18'))
    btn0.grid(row=1, column=3, padx=10, pady=5)
    btndot = Button(buttonFrame, text=".",command=lambda: addDot(), width=4, bg='light blue', font=('Calibri 18'))
    btndot.grid(row=1, column=4, padx=10, pady=5)
    btnClear = Button(buttonFrame, text="C",command=lambda: clear(), width=4, bg='light blue', font=('Calibri 18'))
    btnClear.grid(row=1, column=5, padx=10, pady=5)

    amtA = StringVar()
    amtToConvert = Label(window, textvariable=amtA, width=20, bg="black", fg="white", font=('Calibri 12'))
    amtToConvert.grid(row=4, column=0, columnspan=3, pady=20)

    amtB = StringVar()
    convertedAmount = Label(window, textvariable=amtB, width=20, bg="black", fg="white", font=('Calibri 12'))
    convertedAmount.grid(row=4, column=4, columnspan=3, pady=20)

    countryFrom.selection_set(first=0)     #default value set for listbox
    countryTo.selection_set(first=0)
    exchangeRateDict = scrapeCurrencies()
    window.mainloop()


main()
