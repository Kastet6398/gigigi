import locale
import os
import random
import sys
from stat import *

from cryptography.fernet import Fernet
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import config

secret_key = config.SECRET_KEY

cipher = Fernet(secret_key)

def encrypt_data(data):
    encoded_data = cipher.encrypt(str(data).encode())
    return encoded_data

def decrypt_data(encoded_data:str):
    decoded_data = cipher.decrypt(encoded_data.encode())
    decoded_data = eval(decoded_data.decode())
    return decoded_data

language = locale.getlocale()[0]
print(language)


def translate_text(id):
    if language.lower().startswith("ukrainian"):
        text = config.TRANSLATIONS["uk_UA"][id]
    elif language.lower() == "russian":
        text = config.TRANSLATIONS["ru_RU"][id]
    else:
        text = config.TRANSLATIONS["en_US"][id]
    return text


try:
    open("results.config", "r")
except:
    open("results.config", "w").close()

try:
    open("rules_showed.config", "r")
except:
    open("rules_showed.config", "w").close()

try:
    open("results_sum.config", "r")
except:
    f = open("results_sum.config", "w", encoding="utf-8")
    f.write(encrypt_data(10).decode())
    f.close()

try:
    open("attempts.config", "r")
except:
    f = open("attempts.config", "w", encoding="utf-8")
    f.write(encrypt_data(3).decode())
    f.close()

os.chmod("results.config", S_IREAD)
os.chmod("results_sum.config", S_IREAD)
os.chmod("attempts.config", S_IREAD)


class Frame(QWidget):
    def resizeEvent(self, a0: QResizeEvent) -> None:
        s = self.rect()
        s = QSize(s.width(), s.height())
        s3.resize(s)
        w_.resize(s)


app = QApplication(sys.argv)
w = Frame()
w.setStyleSheet(
    "padding:10px;font-family: Arial; font-style: normal;font-size: 20pt;")
b = QPushButton("X", w)
b.setCursor(Qt.PointingHandCursor)
b.show()
n = 0
s3 = QScrollArea(w)
w_ = QWidget(w)
l = QGridLayout(w_)
s3.setWidgetResizable(1)
globals()['score'] = 0
s3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
s3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
label = QLabel(translate_text(0), w)
w.showMaximized()
label.setAlignment(Qt.AlignCenter)
l.addWidget(label)
label.setWordWrap(1)
button = QPushButton(translate_text(1) + " →", w)
button.setCursor(Qt.PointingHandCursor)
button.setStyleSheet("background-color: lightblue")


def next(button):
    button.hide()
    inp = QLineEdit(w)
    inp.setClearButtonEnabled(1)
    button = QPushButton(w)
    button.setStyleSheet("background-color: lightblue")
    shop = QPushButton("👜 " + translate_text(2), w)
    shop.setStyleSheet("background-color: lightblue")
    main_screen = QPushButton("← " + translate_text(5), w)
    main_screen.setStyleSheet("background-color: lightblue")
    l.addWidget(main_screen, 1, 0, alignment=Qt.AlignCenter)
    button.clicked.connect(lambda: "")
    inp.returnPressed.connect(lambda: "")
    inp.setStyleSheet(
        "QLineEdit {border: 3px solid black;} QLineEdit:focus {border: 3px solid #0083FF;}")
    inp.setFocus()
    button.setCursor(Qt.PointingHandCursor)
    shop.setCursor(Qt.PointingHandCursor)
    main_screen.setCursor(Qt.PointingHandCursor)

    def show_shop():
        ps = w.styleSheet()
        w_.setStyleSheet(
            "padding:10px;font-family: Arial; font-style: normal;font-size: 20pt;")
        text = label.text()
        label.setText(translate_text(2))
        label.setStyleSheet(
            "padding:10px;font-family: Arial; font-style: normal;font-size: 40pt;")
        inp.hide()
        button.hide()
        attempts = open("attempts.config", encoding="utf-8").read()
        results_sum = open("results_sum.config", encoding="utf-8").read()
        r = int(decrypt_data(results_sum))
        r2 = int(decrypt_data(attempts))
        label3 = QLabel(w)
        label3.setText(
            f"""💰 {translate_text(3)}: {r}
{translate_text(4)}: {r2 - 1}""")
        label3.setStyleSheet(
            'font-family: Arial; font-style: normal;font-size: 12pt;')
        l.addWidget(label3, 4, 0, alignment=Qt.AlignCenter)
        s3 = QScrollArea(w)
        s3.setWidgetResizable(1)
        l.addWidget(s3, 5, 0, alignment=Qt.AlignCenter)
        s2 = QWidget(s3)
        s = QVBoxLayout(s2)
        s2.setLayout(s)
        l.removeWidget(shop)

        def go_back():
            label.setStyleSheet("")
            try:
                label2.hide()
            except:
                pass
            label3.hide()
            label.setText(text)
            inp.show()
            inp.setFocus()
            button.show()
            s3.hide()
            shop.setText("👜 " + translate_text(2))
            shop.clicked.disconnect()
            shop.clicked.connect(show_shop)
            w_.setStyleSheet(ps)
        label2 = QLabel(w)
        label2.setText(translate_text(7))
        l.addWidget(label2, 5, 0, alignment=Qt.AlignCenter)
        s3.hide()
        for _ in range(r // (r2-1)):
            s3.show()
            label2.hide()
            b = QPushButton("➕ " + translate_text(11).format(r2 - 1, translate_text(
                13 if str(r2-1)[-1] == "1" else 14 if str(r2-1)[-1] in ["2", "3", "4"] else 12)))
            b.setStyleSheet("background-color: lightblue")
            s.addWidget(b)

            def buy(_=_):
                os.chmod("results_sum.config", S_IWUSR | S_IREAD)
                os.chmod("attempts.config", S_IWUSR | S_IREAD)
                f1 = open("results_sum.config", "w", encoding="utf-8")
                f1.write(encrypt_data(r - r2 + 1).decode())
                f1.close()
                f2 = open("attempts.config", "w", encoding="utf-8")
                f2.write(encrypt_data(r2 + 1).decode())
                f2.close()
                os.chmod("results_sum.config", S_IREAD)
                os.chmod("attempts.config", S_IREAD)
                go_back()
                show_shop()

            b.clicked.connect(buy)
            b.setCursor(Qt.PointingHandCursor)
        s3.setWidget(s2)
        l.addWidget(shop, 6, 0, alignment=Qt.AlignCenter)
        shop.setText("← " + translate_text(6))
        shop.clicked.disconnect()
        shop.clicked.connect(go_back)

    shop.clicked.connect(show_shop)

    def select(l1=None):
        inp.setFocus()
        try:
            if not l1:
                l1 = int(inp.text().replace(".", "l"))
            r = random.randint(1, 10*l1)
            n = 0
            inp.clear()
            w_.setStyleSheet(
                "padding:10px;font-family: Arial;font-style: normal;font-size: 20pt;")
            inp.setPlaceholderText("Your number...")
            r = random.randint(1, 10*l1)
            attempts = open("attempts.config", encoding="utf-8").read()
            a = int(decrypt_data(attempts)) - n - 1
            label.setText(translate_text(18).format(a, translate_text(20 if str(
                a)[-1] == "1" else 21 if str(a)[-1] in ["2", "3", "4"] else 19), 10*l1))
            label.adjustSize()
            w_.adjustSize()
            shop.hide()
            main_screen.hide()

            def on_click(r, n):
                shop.hide()
                inp.setFocus()
                w_.setStyleSheet(
                    "padding:10px;font-family: Arial;font-style: normal;font-size: 20pt; background-color:red")
                try:
                    inp1 = int(inp.text().replace(".", "l"))
                    inp.clear()
                    n += 1
                    if inp1 < 1 or inp1 > 10*l1:
                        label.setText("⛔ " + translate_text(16))
                        label.adjustSize()
                        w_.adjustSize()
                        return
                    if inp1 == r:
                        globals()["score"] += 1
                        w_.setStyleSheet(
                            "padding:10px;font-family: Arial;font-style: normal;font-size: 20pt;\
background-color:green")
                        main_screen.show()
                        os.chmod("results.config", S_IWUSR | S_IREAD)
                        os.chmod("results_sum.config", S_IWUSR | S_IREAD)
                        f = open("results.config", "a", encoding="utf-8")
                        f.write(
                            f"\n{encrypt_data(globals()['score']).decode()}""")
                        f.close()
                        results_sum = open("results_sum.config", encoding="utf-8").read()
                        f1 = int(decrypt_data(results_sum))
                        end_score = l1 + f1
                        f2 = open("results_sum.config", "w", encoding="utf-8")
                        f2.write(encrypt_data(end_score).decode())
                        f2.close()
                        os.chmod("results.config", S_IREAD)
                        os.chmod("results_sum.config", S_IREAD)
                        button.setText(translate_text(26) + " →")
                        bonus = ""

                        if not globals()['score'] % 10:
                            r2 = int(decrypt_data(results_sum))
                            os.chmod("results_sum.config", S_IWUSR | S_IREAD)
                            f2 = open("results_sum.config", "w", encoding="utf-8")
                            f2.write(encrypt_data(r2 + 50).decode())
                            f2.close()
                            os.chmod("results_sum.config", S_IREAD)
                            bonus = translate_text(-1)

                        label.setText("✅ " + translate_text(25) + "!!! " + bonus)
                        inp.hide()



                        def nn():
                            inp.show()
                            select(l1)

                        button.clicked.disconnect()
                        button.clicked.connect(nn)
                        return

                    attempts = open("attempts.config", encoding="utf-8").read()
                    if n < int(decrypt_data(attempts)) - 1:
                        a = int(decrypt_data(attempts)) - n - 1
                        s = translate_text(22).format(a, translate_text(
                            20 if str(a)[-1] == "1" else 21 if str(a)[-1] in ["2", "3", "4"] else 19))
                        if inp1 < r:
                            label.setText(s + translate_text(23))
                        elif inp1 > r:
                            label.setText(s + translate_text(24))

                        button.clicked.disconnect()
                        button.clicked.connect(lambda: on_click(r, n))
                        inp.returnPressed.disconnect()
                        inp.returnPressed.connect(lambda: on_click(r, n))
                    else:
                        inp.hide()
                        os.chmod("results.config", S_IWUSR | S_IREAD)
                        os.chmod("results_sum.config", S_IWUSR | S_IREAD)
                        f = open("results.config", "a", encoding="utf-8")
                        f.write(
                            f"\n{encrypt_data(globals()['score']).decode()}""")
                        f.close()
                        results_sum = open("results_sum.config", encoding="utf-8").read()
                        f1 = int(decrypt_data(results_sum))
                        end_score = globals()["score"] * l1 + f1
                        f2 = open("results_sum.config", "w", encoding="utf-8")
                        f2.write(encrypt_data(end_score).decode())
                        f2.close()
                        os.chmod("results.config", S_IREAD)
                        os.chmod("results_sum.config", S_IREAD)
                        results_config = open(
                                "results.config", encoding="utf-8").read().split("\n")[1:]
                        m = max([int(decrypt_data(x)) for x in results_config])
                        label.setText("⛔ " + translate_text(27).format(globals()['score'], translate_text(29 if str(globals()['score'])[-1] == "1" else 30 if str(
                            globals()['score'])[-1] in ["2", "3", "4"] else 28), m, translate_text(29 if str(m)[-1] == "1" else 30 if str(m)[-1] in ["2", "3", "4"] else 28)))
                        label.adjustSize()
                        w_.adjustSize()
                        main_screen.show()

                        def restart():
                            inp.show()
                            inp.setFocus()
                            main_screen.hide()
                            globals()["score"] = 0
                            n = 0
                            attempts = open("attempts.config", encoding="utf-8").read()
                            a = int(decrypt_data(attempts)) - n - 1
                            r = random.randint(1, 10*l1)
                            button.setText("✔ " + translate_text(15))
                            w_.setStyleSheet(
                                "padding:10px;font-family: Arial;font-style: normal;font-size: 20pt;")
                            label.setText(translate_text(18).format(a, translate_text(20 if str(
                                a)[-1] == "1" else 21 if str(a)[-1] in ["2", "3", "4"] else 19), 10*l1))
                            button.clicked.disconnect()
                            button.clicked.connect(lambda: on_click(r, 0))
                            inp.returnPressed.disconnect()
                            inp.returnPressed.connect(lambda: on_click(r, 0))
                        button.setText("🔄 " + translate_text(31))
                        button.clicked.disconnect()
                        button.clicked.connect(restart)
                except:
                    
                    inp.clear()
                    label.setText("⛔ " + translate_text(16))
                    label.adjustSize()
                    w_.adjustSize()

            inp.returnPressed.disconnect()
            inp.returnPressed.connect(lambda: on_click(r, n))
            button.setText("✔ " + translate_text(15))
            button.clicked.disconnect()
            button.clicked.connect(lambda: on_click(r, n))
        except:

            import traceback
            traceback.print_exc()
            inp.clear()
            w_.setStyleSheet(
                "padding:10px;font-family: Arial;font-style: normal;font-size: 20pt; background-color:red")
            label.setText("⛔ " + translate_text(17))
            label.adjustSize()
            w_.adjustSize()

    def main():
        global n
        n = 0
        button.setText(translate_text(8) + " →")
        label.setText(translate_text(9))
        inp.setPlaceholderText(translate_text(10))
        w_.setStyleSheet(
            "padding:10px;font-family: Arial;font-style: normal;font-size: 20pt;")
        shop.show()
        inp.show()
        inp.setFocus()
        l.addWidget(label, 1, 0, alignment=Qt.AlignCenter)
        l.addWidget(inp, 2, 0, alignment=Qt.AlignCenter)
        l.addWidget(button, 3, 0, alignment=Qt.AlignCenter)
        l.addWidget(shop, 4, 0, alignment=Qt.AlignCenter)
        main_screen.hide()
        globals()["score"] = 0
        l.addWidget(main_screen, 5, 0, alignment=Qt.AlignCenter)
        button.clicked.disconnect()
        button.clicked.connect(select)
        inp.returnPressed.disconnect()
        inp.returnPressed.connect(select)
    main_screen.clicked.connect(main)

    main()


if open("rules_showed.config").read():
    next(button)


def ns():
    f = open("rules_showed.config", "w", encoding="utf-8")
    f.write("​")
    f.close()
    next(button)


button.clicked.connect(ns)
s3.setWidget(w_)
l.addWidget(button, 1, 0, alignment=Qt.AlignCenter)
w.setWindowTitle("Guess-the-number game")
w.show()
app.exec_()
os.chmod("results.config", S_IWUSR | S_IREAD)
f = open("results.config", "a", encoding="utf-8")
f.write(f"\n{encrypt_data(globals()['score']).decode()}")
f.close()
os.chmod("results.config", S_IREAD)
