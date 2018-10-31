import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import pandas as pd

import design
from query import query_in, query_ins


DB_QUERY_ZAMENA = """Select * from zamena"""
DB_QUERY_REST = """Select * from rest"""
DB_QUERY_DEL_ZANYATIE = """delete from zanyatie"""
DB_QUERY_DEL_GROUPZAN = """delete from gruppazanyatie"""
DB_QUERY_INS_ZANYATIE = """insert into zanyatie values ('{}',{},'{}','{}','{}',{})"""
DB_QUERY_INS_GROUPZAN = """insert into gruppazanyatie values ('{}','{}',{},'{}',{})"""
DB_QUERY_UPD_ZANYATIE = """update zanyatie set Den_nedeli = '{}', 
                        Nomer_pari = {}, N_Auditorii = '{}', Nedela = {}
                        where Den_nedeli = '{}' AND Nomer_pari = {} AND N_Auditorii = '{}' AND Nedela = {}"""
DB_QUERY_DEL_ZAMENA = """delete from zamena where FIO_prep = '{}' 
                                AND Nazvanie_discipl = '{}'
                                AND Den_nedeli = '{}'
                                AND Nomer_pari = {}
                                AND Nedela = {}
                                AND N_Auditorii = '{}'
                                AND Den_nedeli2 = '{}'
                                AND Nomer_pari2 = {}
                                AND Nedela2 = {}
                                AND N_Auditorii2 = '{}'"""
DB_QUERY_FIO = """Select FIO,e_addr from stud X1 INNER JOIN 
                gruppazanyatie X2 ON (X1.N_Gruppi = X2.N_gruppi) INNER JOIN
                zanyatie X3 ON (X2.Nomer_pari = X3.Nomer_pari AND X2.Den_nedeli = X3.Den_nedeli 
                AND X2.N_Auditorii = X3.N_Auditorii)
                where X3.FIO_prep = '{}'"""
DB_QUERY_DEL_REST = """delete from rest"""
DB_QUERY_FIO_PREP = """Select e_addr from prepodavatel
                    where FIO = '{}'"""

SET_TEXT_TE = """{} -  {}  -  {}  -  {}  -  {}  -  {}  ->>  {}  -  {}  -  {}  -  {}"""


def send_email(subject, body_text, emails):
    fromaddr = "volooooodya66564@gmail.com"
    mypass = "88884444"
    msg = MIMEMultipart()
    msg['From'] = "SUAI"
    msg['To'] = emails
    msg['Subject'] = subject
    body = body_text
    msg.attach(MIMEText(body, 'plain'))

    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, emails, text)
        server.quit()

    except:
        print("Сообщение не отправлено")


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        self.page = 0
        self.query = []
        self.X1 = []
        self.log = [False, False, False, False, False]
        super().__init__()
        self.setupUi(self)
        self.viv(0)
        self.viv2()
        self.pushButton.clicked.connect(self.btn_clk)
        self.pushButton_2.clicked.connect(self.btn2_clk)
        self.pushButton_3.clicked.connect(self.btn3_clk)
        self.pushButton_5.clicked.connect(self.btn5_clk)
        self.pushButton_6.clicked.connect(self.btn6_clk)
        self.pushButton_4.clicked.connect(self.btn4_clk)
        self.pushButton_7.clicked.connect(self.btn7_clk)
        self.checkBox.clicked.connect(self.chk1_clk)
        self.checkBox_2.clicked.connect(self.chk2_clk)
        self.checkBox_3.clicked.connect(self.chk3_clk)
        self.checkBox_4.clicked.connect(self.chk4_clk)
        self.checkBox_5.clicked.connect(self.chk5_clk)

    def viv(self, cortage):
        self.query = query_in(DB_QUERY_ZAMENA)
        for i in range(0, 5):
            try:
                if self.query[cortage + i][4] == 1:
                    day_cb1 = 'Верх'
                if self.query[cortage + i][4] == 2:
                    day_cb1 = 'Низ'
                if self.query[cortage + i][4] == 0:
                    day_cb1 = ''
                if self.query[cortage + i][8] == 1:
                    day_cb2 = 'Верх'
                if self.query[cortage + i][8] == 2:
                    day_cb2 = 'Низ'
                if self.query[cortage + i][8] == 0:
                    day_cb2 = ''

                if i == 0:
                    self.textEdit.setText(SET_TEXT_TE.format(self.query[cortage + i][0], self.query[cortage + i][1],
                                                        self.query[cortage + i][2], str(self.query[cortage + i][3]),
                                                        day_cb1, self.query[cortage + i][5], self.query[cortage + i][6],
                                                        str(self.query[cortage + i][7]), day_cb2,
                                                        self.query[cortage + i][9]))
                if i == 1:
                    self.textEdit_2.setText(SET_TEXT_TE.format(self.query[cortage + i][0], self.query[cortage + i][1],
                                                        self.query[cortage + i][2], str(self.query[cortage + i][3]),
                                                        day_cb1, self.query[cortage + i][5], self.query[cortage + i][6],
                                                        str(self.query[cortage + i][7]), day_cb2,
                                                        self.query[cortage + i][9]))
                if i == 2:
                    self.textEdit_3.setText(SET_TEXT_TE.format(self.query[cortage + i][0], self.query[cortage + i][1],
                                                        self.query[cortage + i][2], str(self.query[cortage + i][3]),
                                                        day_cb1, self.query[cortage + i][5], self.query[cortage + i][6],
                                                        str(self.query[cortage + i][7]), day_cb2,
                                                        self.query[cortage + i][9]))
                if i == 3:
                    self.textEdit_4.setText(SET_TEXT_TE.format(self.query[cortage + i][0], self.query[cortage + i][1],
                                                        self.query[cortage + i][2], str(self.query[cortage + i][3]),
                                                        day_cb1, self.query[cortage + i][5], self.query[cortage + i][6],
                                                        str(self.query[cortage + i][7]), day_cb2,
                                                        self.query[cortage + i][9]))
                if i == 4:
                    self.textEdit_5.setText(SET_TEXT_TE.format(self.query[cortage + i][0], self.query[cortage + i][1],
                                                        self.query[cortage + i][2], str(self.query[cortage + i][3]),
                                                        day_cb1, self.query[cortage + i][5], self.query[cortage + i][6],
                                                        str(self.query[cortage + i][7]), day_cb2,
                                                        self.query[cortage + i][9]))

            except:
                pass

    def viv2(self):
        query = query_in(DB_QUERY_REST)
        for i in range(0, len(query)):
            self.textEdit_6.append(query[i][0] + "\t" + str(query[i][1]) + "\t" + str(query[i][2]) + "\t" + query[i][3])

    def btn7_clk(self):
        query_ins(DB_QUERY_DEL_ZANYATIE)
        query_ins(DB_QUERY_DEL_GROUPZAN)

    def btn4_clk(self):
        file_name = QFileDialog.getOpenFileName()
        try:
            fd = pd.read_excel(file_name[0], sheet_name=0)
            for i in fd.index:
                if fd['Верх/низ/-'][i] == "Верх":
                    ND = 1
                if fd['Верх/низ/-'][i] == "Низ":
                    ND = 2
                if fd['Верх/низ/-'][i] == "-":
                    ND = 0

                try:
                    query_ins(DB_QUERY_INS_ZANYATIE.format(fd['День недели'][i],
                                                           fd['Номер пары'][i],
                                                           fd['Аудитория'][i],
                                                           fd['Преподаватель'][i],
                                                           fd['Название дисципл'][i],
                                                           ND))
                except:
                    pass

                try:
                    query_ins(DB_QUERY_INS_GROUPZAN.format(fd['Группа'][i],
                                                           fd['День недели'][i],
                                                           fd['Номер пары'][i],
                                                           fd['Аудитория'][i],
                                                           ND))
                except:
                    pass
        except:
            pass

    def chk1_clk(self):
        self.log[0] = not(self.log[0])

    def chk2_clk(self):
        self.log[1] = not(self.log[1])

    def chk3_clk(self):
        self.log[2] = not(self.log[2])

    def chk4_clk(self):
        self.log[3] = not(self.log[3])

    def chk5_clk(self):
        self.log[4] = not(self.log[4])

    def btn_clk(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        if self.page != 0:
            self.page = self.page - 5

        self.viv(self.page)

    def btn2_clk(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        if self.page / 5 < len(self.query) // 5:
            self.page = self.page + 5
        self.viv(self.page)

    def btn3_clk(self):
        self.msg = ''

        for i in range(0, 5):
            if self.log[i]:
                query_ins(DB_QUERY_UPD_ZANYATIE.format(self.query[self.page + i][6],
                                                       int(self.query[self.page + i][7]),
                                                       self.query[self.page + i][9],
                                                       int(self.query[self.page + i][8]),
                                                       self.query[self.page + i][2],
                                                       int(self.query[self.page + i][3]),
                                                       self.query[self.page + i][5],
                                                       int(self.query[self.page + i][4])))

                query_ins(DB_QUERY_DEL_ZAMENA.format(self.query[self.page + i][0],
                                                     self.query[self.page + i][1],
                                                     self.query[self.page + i][2],
                                                     self.query[self.page + i][3],
                                                     self.query[self.page + i][4],
                                                     self.query[self.page + i][5],
                                                     self.query[self.page + i][6],
                                                     self.query[self.page + i][7],
                                                     self.query[self.page + i][8],
                                                     self.query[self.page + i][9]))

                self.msg = SET_TEXT_TE.format(self.query[self.page + i][0],
                                                    self.query[self.page + i][1],
                                                    self.query[self.page + i][2],
                                                    self.query[self.page + i][3],
                                                    self.query[self.page + i][4],
                                                    self.query[self.page + i][5],
                                                    self.query[self.page + i][6],
                                                    self.query[self.page + i][7],
                                                    self.query[self.page + i][8],
                                                    self.query[self.page + i][9])
                self.query_fio = query_in(DB_QUERY_FIO_PREP.format(self.query[self.page + i][0]))

                subject = "Перенос пары"
                body_text = "совершен перенос пары {}.".format(self.msg)
                body_text2 = "Ув. {},".format(self.query[self.page + i][0])
                txt = body_text2 + body_text
                send_email(subject, txt, self.query_fio[0][0])

        self.checkBox.setCheckState(False)
        self.checkBox_2.setCheckState(False)
        self.checkBox_3.setCheckState(False)
        self.checkBox_4.setCheckState(False)
        self.checkBox_5.setCheckState(False)
        self.log = [False, False, False, False, False]
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.page = 0
        self.viv(0)

    def btn5_clk(self):
        self.query_fio2 = []
        for i in range(0, 5):
            if self.log[i]:

                query_ins(DB_QUERY_DEL_ZAMENA.format(self.query[self.page + i][0],
                                                     self.query[self.page + i][1],
                                                     self.query[self.page + i][2],
                                                     self.query[self.page + i][3],
                                                     self.query[self.page + i][4],
                                                     self.query[self.page + i][5],
                                                     self.query[self.page + i][6],
                                                     self.query[self.page + i][7],
                                                     self.query[self.page + i][8],
                                                     self.query[self.page + i][9]))
                self.msg = SET_TEXT_TE.format(self.query[self.page + i][0],
                                              self.query[self.page + i][1],
                                              self.query[self.page + i][2],
                                              self.query[self.page + i][3],
                                              self.query[self.page + i][4],
                                              self.query[self.page + i][5],
                                              self.query[self.page + i][6],
                                              self.query[self.page + i][7],
                                              self.query[self.page + i][8],
                                              self.query[self.page + i][9])

                self.query_fio2 = query_in(DB_QUERY_FIO_PREP.format(self.query[self.page + i][0]))
                subject = "Перенос пары"
                body_text = "отказано в переносе пары {}.".format(self.msg)
                body_text2 = "Ув. {},".format(self.query[self.page + i][0])
                txt = body_text2 + body_text
                send_email(subject, txt, self.query_fio2[0][0])
        self.checkBox.setCheckState(False)
        self.checkBox_2.setCheckState(False)
        self.checkBox_3.setCheckState(False)
        self.checkBox_4.setCheckState(False)
        self.checkBox_5.setCheckState(False)
        self.log = [False, False, False, False, False]
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.textEdit_4.clear()
        self.textEdit_5.clear()
        self.page = 0
        self.viv(0)

    def btn6_clk(self):
        self.X1 = query_in(DB_QUERY_REST)
        for i in range(0, len(self.X1)):
            self.query = query_in(DB_QUERY_FIO.format(self.X1[i][0]))
            subject = "ОПОВЕЩЕНИЕ отсутсвие преподавателя {}".format(self.X1[i][0])
            if self.X1[i][3] == "":
                body_text = "Преподаватель {} будет отутсвовать с {} по {}".format(self.X1[i][0],
                                                                                   str(self.X1[i][1]),
                                                                                   str(self.X1[i][2]))
            if self.X1[i][3] != "":
                body_text = "Преподаватель {} будет отутсвовать с {} по {}. Его будет заменять преподаватель {}".format(
                    self.X1[i][0],
                    str(self.X1[i][1]),
                    str(self.X1[i][2]),
                    self.X1[i][3])

            for ii in range(0, len(self.query)):
                body_text2 = "Ув. {},".format(self.query[ii][0])
                txt = body_text2 + body_text
                send_email(subject, txt, self.query[ii][1])
        query_ins(DB_QUERY_DEL_REST)
        self.textEdit_6.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()