import time #built in python, counts second in epoch
import threading #allows mutiple tasks/function calls to run at the same time
import csv

from stopwatch_layout import *
from PyQt5.QtWidgets import *


class Stopwatch(QMainWindow, Ui_Stopwatch): #QMainWindow comes from QtWidget

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.running = False
        self.started = False

        self.passed = 0
        self.previous_passed = 0
        self.lap = 1

        self.start_button.clicked.connect(self.start_stop)
        self.lap_button.clicked.connect(self.lap_reset)
        self.save_button.clicked.connect(self.save_laps)

    def start_stop(self):
        if self.running:
            self.running = False
            self.start_button.setText("Resume")
            self.lap_button.setText("Reset")
        else:
            self.running = True
            self.start_button.setText("Stop")
            self.lap_button.setText('Lap')
            self.lap_button.setEnabled(True)
            threading.Thread(target=self.stopwatch).start()
    def lap_reset(self):
        if self.running:
            if self.lap==1:
                self.label.setText(self.label.text() + f'{self.format_time(self.passed)}')
            elif self.lap ==2:
               self.label_2.setText(self.label_2.text() + f'{self.format_time(self.passed)}')
            elif self.lap ==3:
                self.label_3.setText(self.label_3.text() + f'{self.format_time(self.passed)}')
            elif self.lap == 4:
                self.label_4.setText(self.label_4.text() + f'{self.format_time(self.passed)}')
            elif self.lap == 5:
                self.label_5.setText(self.label_5.text() + f'{self.format_time(self.passed)}')
            elif self.lap > 5:
                self.error.setText(self.error.text() + f'Limit of laps is 5 please reset timer/laps to add new lap times')
            self.lap += 1
        else:
            self.start_button.setText("Start")
            self.lap_button.setText("Lap")
            self.lap_button.setEnabled(False)
            self.time.setText('00:00:00')
            self.passed = 0
            self.previous_passed =0
            self.label.setText('')
            self.label_2.setText('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
            self.error.setText('')
            self.name1.setText('')
            self.name2.setText('')
            self.name3.setText('')
            self.name4.setText('')
            self.name5.setText('')
            self.errorname5.setText('')
            self.errorname4.setText('')
            self.errorname3.setText('')
            self.errorname2.setText('')
            self.errorname1.setText('')

            self.lap =1
    def format_time(self, time_passed):
        secs = time_passed % 60
        mins = time_passed // 60
        hours = mins // 60
        milsec = (self.passed % 1) * 100
        return f'{int(hours):02d}:{int(mins):02d}:{int(secs):02d}:{int(milsec):02d}'

    def stopwatch(self):
        start = time.time()
        if self.started:
            until_now = self.passed
        else:
            until_now = 0
            self.started = True

        while self.running:
            self.passed = time.time() - start + until_now
            self.time.setText(self.format_time(self.passed))



    def save_laps(self):
        with open('student_times.csv', 'a+', newline='') as csvfile:
            content = csv.writer(csvfile)
            if self.label.text() > '':
                if self.name1.text() == '':
                    self.errorname1.setText("Please enter a student")
                else:
                    self.errorname1.setText('')
                    content.writerow([self.name1.text().upper(),self.label.text()])
            if self.label_2.text() > '':
                if self.name2.text() == '':
                    self.errorname2.setText("Please enter a student")
                else:
                    self.errorname2.setText('')
                    content.writerow([self.name2.text().upper(), self.label_2.text()])
            if self.label_3.text() > '':
                if self.name3.text() == '':
                    self.errorname3.setText("Please enter a student")
                else:
                    self.errorname3.setText('')
                    content.writerow([self.name3.text().upper(), self.label_3.text()])
            if self.label_4.text() > '':
                if self.name4.text() == '':
                    self.errorname4.setText("Please enter a student")
                else:
                    self.errorname4.setText('')
                    content.writerow([self.name4.text().upper(), self.label_4.text()])
            if self.label_5.text() > '':
                if self.name5.text() == '':
                    self.errorname5.setText("Please enter a student")
                else:
                    self.errorname5.setText('')
                    content.writerow([self.name5.text().upper(), self.label_5.text()])



