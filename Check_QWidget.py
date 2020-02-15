from PyQt5.QtWidgets import QWidget
import sys,os
def demo_check_QWidget():
    dir(QWidget)
    help(QWidget)

if __name__ == "__main__":
    out = sys.stdout
    sys.stdout = open('./help.QWidget.txt','w')
    demo_check_QWidget()
    sys.stdout.close()
    sys.stdout = out