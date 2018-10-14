from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
class Ui_Dialoga(object):
    def parametros(self, p, b, h):
        self.primeiro = p
        self.segundo = b
        self.altura = h


    def setupUi(self, Dialog):
        #data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #t = [15, 32, 53, 84, 45, 62, 75, 86, 97, 310]
        data = self.primeiro
        t = self.segundo


        fig = plt.figure()
        #fig.add_subplot(221)
        ax = fig.add_subplot(111)
        ax.plot(t,data)
        ax.set_title('Erro(%) x Número de Iterações', fontsize=18)
        ax.set_xlabel('Número de Iterações', fontsize=18)
        ax.set_ylabel('Erro(%)', fontsize=18)
        ax.xaxis.label.set_size(18);
        ax.yaxis.label.set_size(18);
        #ay = fig.add_subplot(222)
        #ay.plot(t,data)
        #ay.set_xlabel('X')
        #ay.set_ylabel('Y')
        #ax.spines['bottom'].set_color('red')
        #ax.spines['top'].set_color('red')
        #ax.xaxis.label.set_color('red')
        #ax.tick_params(axis='x', colors='red')
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialoga()
    ui.setupUi(Dialog)
    #Dialog.show()
    sys.exit(app.exec_())

