from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(60, 10, 501, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setLineWidth(1)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(60, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(50, 520, 511, 31))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(60, 140, 47, 13))
        self.label4.setObjectName("label4")
        self.age = QtWidgets.QSpinBox(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(86, 136, 42, 22))
        self.age.setObjectName("age")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(150, 140, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.sex = QtWidgets.QComboBox(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(180, 138, 71, 21))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.smoking = QtWidgets.QComboBox(self.centralwidget)
        self.smoking.setGeometry(QtCore.QRect(180, 170, 69, 22))
        self.smoking.setObjectName("smoking")
        self.smoking.addItem("")
        self.smoking.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 170, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.backbleeding = QtWidgets.QComboBox(self.centralwidget)
        self.backbleeding.setGeometry(QtCore.QRect(60, 230, 131, 22))
        self.backbleeding.setObjectName("backbleeding")
        self.backbleeding.addItem("")
        self.backbleeding.addItem("")
        self.headheight = QtWidgets.QComboBox(self.centralwidget)
        self.headheight.setGeometry(QtCore.QRect(210, 230, 101, 22))
        self.headheight.setObjectName("headheight")
        self.headheight.addItem("")
        self.headheight.addItem("")
        self.capsule = QtWidgets.QComboBox(self.centralwidget)
        self.capsule.setGeometry(QtCore.QRect(330, 230, 121, 22))
        self.capsule.setObjectName("capsule")
        self.capsule.addItem("")
        self.capsule.addItem("")
        self.pmspike = QtWidgets.QComboBox(self.centralwidget)
        self.pmspike.setGeometry(QtCore.QRect(480, 230, 111, 22))
        self.pmspike.setObjectName("pmspike")
        self.pmspike.addItem("")
        self.pmspike.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ant_post = QtWidgets.QComboBox(self.centralwidget)
        self.ant_post.setGeometry(QtCore.QRect(60, 310, 71, 22))
        self.ant_post.setObjectName("ant_post")
        self.ant_post.addItem("")
        self.ant_post.addItem("")
        self.three_four = QtWidgets.QComboBox(self.centralwidget)
        self.three_four.setGeometry(QtCore.QRect(150, 310, 61, 22))
        self.three_four.setObjectName("three_four")
        self.three_four.addItem("")
        self.three_four.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 280, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.handedness = QtWidgets.QComboBox(self.centralwidget)
        self.handedness.setGeometry(QtCore.QRect(250, 310, 121, 22))
        self.handedness.setObjectName("handedness")
        self.handedness.addItem("")
        self.handedness.addItem("")
        self.mov = QtWidgets.QComboBox(self.centralwidget)
        self.mov.setGeometry(QtCore.QRect(400, 310, 69, 22))
        self.mov.setObjectName("mov")
        self.mov.addItem("")
        self.mov.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 370, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 410, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 450, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.out_c_score = QtWidgets.QLabel(self.centralwidget)
        self.out_c_score.setGeometry(QtCore.QRect(200, 398, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(16)
        font.setUnderline(True)
        self.out_c_score.setFont(font)
        self.out_c_score.setObjectName("out_c_score")
        self.log_out = QtWidgets.QLabel(self.centralwidget)
        self.log_out.setGeometry(QtCore.QRect(200, 449, 91, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.log_out.setFont(font)
        self.log_out.setObjectName("log_out")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 410, 311, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(280, 450, 381, 20))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(250, 350, 111, 31))
        self.run.setObjectName("run")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.run.clicked.connect(lambda: self.clicked())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NKR_Ortho_Tool_1.v1.0"))
        self.label1.setText(_translate("MainWindow", "Outcome Prediction in proximal humerous fracture patients\n"
"undergoing ORIF\n"
"Poor outcome includes: Non-union, Low Conststant score, \n"
"Avascular Necrosis and Revision surgery* "))
        self.label2.setText(_translate("MainWindow", "Patient Details:"))
        self.label3.setText(_translate("MainWindow", "* The model is trained based on the data provided by Dr. Kirubakaran et al. \n"
"Ref:"))
        self.label4.setText(_translate("MainWindow", "Age"))
        self.label5.setText(_translate("MainWindow", "Sex:"))
        self.sex.setItemText(0, _translate("MainWindow", "Male"))
        self.sex.setItemText(1, _translate("MainWindow", "Female"))
        self.smoking.setItemText(1, _translate("MainWindow", "Yes"))
        self.smoking.setItemText(0, _translate("MainWindow", "No"))
        self.label.setText(_translate("MainWindow", "Smoking:"))
        self.label_2.setText(_translate("MainWindow", "Findings:"))
        self.backbleeding.setItemText(0, _translate("MainWindow", "Backbleeding Present"))
        self.backbleeding.setItemText(1, _translate("MainWindow", "Backbleeding Absent"))
        self.headheight.setItemText(0, _translate("MainWindow", "Headheight>2mm"))
        self.headheight.setItemText(1, _translate("MainWindow", "Headheight<2mm"))
        self.capsule.setItemText(0, _translate("MainWindow", "Capsule attached"))
        self.capsule.setItemText(1, _translate("MainWindow", "Capsule not attached"))
        self.pmspike.setItemText(0, _translate("MainWindow", "PM Spike present"))
        self.pmspike.setItemText(1, _translate("MainWindow", "PM Spike absent"))
        self.label_3.setText(_translate("MainWindow", "Fracture Pattern:"))
        self.ant_post.setItemText(0, _translate("MainWindow", "Anterior"))
        self.ant_post.setItemText(1, _translate("MainWindow", "Posterior"))
        self.three_four.setItemText(0, _translate("MainWindow", "3 Part"))
        self.three_four.setItemText(1, _translate("MainWindow", "4 Part"))
        self.label_4.setText(_translate("MainWindow", "Other Details:"))
        self.handedness.setItemText(0, _translate("MainWindow", "Dominant Hand"))
        self.handedness.setItemText(1, _translate("MainWindow", "Non Dominant Hand"))
        self.mov.setItemText(1, _translate("MainWindow", "MOV high"))
        self.mov.setItemText(0, _translate("MainWindow", "MOV low"))
        self.label_5.setText(_translate("MainWindow", "Predicted Outcome:"))
        self.label_6.setText(_translate("MainWindow", "Constant Score: "))
        self.label_7.setText(_translate("MainWindow", "Outcome:"))
        self.run.setText(_translate("MainWindow", "Run Program"))

        
        self.out_c_score.setText(_translate("MainWindow", "0"))
        self.log_out.setText(_translate("MainWindow", "NA"))
        self.label_8.setText(_translate("MainWindow", "(R^2 value of the model: 0.74574 and RMS error:  6.09)"))
        self.label_9.setText(_translate("MainWindow", "(Accuracy: 93.75%, Sensitivity: 70% and Specificity: 100%)"))

    def clicked(self):
        ##getting values:
        age_val=self.age.value()
        sex_val=self.sex.currentIndex()
        smoking_val=self.smoking.currentIndex()
        backbleeding_val=self.backbleeding.currentIndex()
        headheight_val=self.headheight.currentIndex()
        capsule_val=self.capsule.currentIndex()
        pmspike_val=self.pmspike.currentIndex()
        ant_post_val=self.ant_post.currentIndex()
        three_four_val=self.three_four.currentIndex()
        handedness_val=self.handedness.currentIndex()
        mov_val=self.mov.currentIndex()

        c_score = 86.012 -(0.0803*backbleeding_val)-(7.9069*headheight_val)-(7.179*capsule_val)-(0.2627*age_val)-(5.885*sex_val)-(9.9189*three_four_val)-(0.3706*ant_post_val)-(1.5872*pmspike_val)-(4.4166*smoking_val)+(0.7488*handedness_val)+(2.5524*mov_val)

        nkr = -0.99681589 +(1.4871101*backbleeding_val)+(1.15596723*headheight_val)+(0.93317617*capsule_val)-(0.04234088*age_val)+(0.47240506*sex_val)+(0.62912151*three_four_val)+(0*ant_post_val)+(1.05908633*pmspike_val)+(0*smoking_val)-(0*handedness_val)-(0.37399923*mov_val)

        self.out_c_score.setText(str(round(c_score,2)))

        if nkr>=0:
            self.log_out.setText("Poor")
        else:
            self.log_out.setText("Good")

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
