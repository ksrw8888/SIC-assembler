from PyQt5 import QtWidgets
from ui import Ui_MainWindow
import sys
import sic
import os
import function


def clear_global_variable():
    sic.Symbol.clear()
    sic.MC.clear()
    sic.LOCAL = 0
    sic.InitialValue = 0
    sic.error_index = 0


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.file_name = ''
        self.sic = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_file_name.clicked.connect(self.set_file_name)
        self.ui.op_table.clicked.connect(self.op_table)
        self.ui.symbol_table.clicked.connect(self.symbol_table)
        self.ui.object_code.clicked.connect(self.object_code)
        self.ui.object_program_format.clicked.connect(self.object_program_format)

    def set_file_name(self):
        file_name = self.ui.textEdit.toPlainText()
        if file_name.find('.txt') == -1:
            file_name += '.txt'

        d_list = os.listdir()
        self.ui.textBrowser.clear()
        if file_name not in d_list:
            self.set_message(1)
            self.file_name = ''

        elif file_name == self.file_name:
            self.set_message(2)

        else:
            self.ui.textBrowser.clear()
            self.file_name = file_name
            self.set_message(3)
            self.create_sic()
            self.set_message(4)
            self.sic.start()

    def create_sic(self):
        clear_global_variable()
        self.sic = sic.SIC(self.file_name)

    def set_message(self, index):
        global choice_language
        choice_language = 0

        if self.ui.language.currentText() == 'English':
            choice_language = 1
        elif self.ui.language.currentText() == '繁體中文':
            choice_language = 2
        else:
            choice_language = 3

        if index == 1:
            if choice_language == 1:
                self.ui.textBrowser.insertPlainText("Can't find the file.\n")
            elif choice_language == 2:
                self.ui.textBrowser.insertPlainText('無法找到檔案。\n')
            else:
                self.ui.textBrowser.insertPlainText('ファイルが見つかりません。\n')

        elif index == 2:
            if choice_language == 1:
                self.ui.textBrowser.insertPlainText('The file has loaded.\n')
            elif choice_language == 2:
                self.ui.textBrowser.insertPlainText('檔案已載入。\n')
            else:
                self.ui.textBrowser.insertPlainText('ファイルが読み込まれた。\n')

        elif index == 3:
            if choice_language == 1:
                self.ui.textBrowser.insertPlainText('Loading......\n')
            elif choice_language == 2:
                self.ui.textBrowser.insertPlainText('讀取中......\n')
            else:
                self.ui.textBrowser.insertPlainText('読み込み中......\n')

        elif index == 4:
            if choice_language == 1:
                self.ui.textBrowser.insertPlainText('Loading completed.\n')
            elif choice_language == 2:
                self.ui.textBrowser.insertPlainText('讀取完成。\n')
            else:
                self.ui.textBrowser.insertPlainText('読み込み完了。\n')

        elif index == 5:
            if choice_language == 1:
                self.ui.textBrowser.insertPlainText("You don't input the file name or the file name is error.\n")
            elif choice_language == 2:
                self.ui.textBrowser.insertPlainText('你沒有輸入檔案名或是檔案名稱錯誤。\n')
            else:
                self.ui.textBrowser.insertPlainText('まだファイル名を入力されていません、またはファイル名がエラーです。\n')

    def object_code(self):
        self.ui.textBrowser.clear()
        if self.file_name == '':
            self.set_message(5)
            pass
        else:
            line_count = 1
            self.ui.textBrowser.insertPlainText('Line\t Loc\t\t\tSource statement\t\t\tObject code\n')
            for i in range(len(self.sic.instruction)):
                temp = self.sic.instruction[i]
                if temp.machineCode == 'error':
                    self.ui.textBrowser.insertPlainText('\t\tInstruction is error, so can not get the result\n')
                else:
                    line = '{:>4}'.format(str(line_count)) + '\t'
                    if temp.order == 'END':
                        line += '\t'
                    else:
                        line += temp.leftAddress + '\t'
                    line += '{:<18}'.format(temp.symbol) + '\t'
                    line += temp.order + '\t\t'
                    line += '{:<18}'.format(temp.label) + '\t    '
                    line += temp.machineCode + '\n'
                    self.ui.textBrowser.insertPlainText(line)
                    line_count += 1

    def op_table(self):
        self.ui.textBrowser.clear()
        if self.file_name == '':
            self.set_message(5)
            pass
        else:
            op_table = sic.OPTABLE.items()
            count = 0
            for each in op_table:
                count += 1
                self.ui.textBrowser.insertPlainText('{:<20}'.format(str(each)) + '\t')
                if count % 5 == 0:
                    self.ui.textBrowser.insertPlainText('\n')

    def symbol_table(self):
        self.ui.textBrowser.clear()
        if self.file_name == '':
            self.set_message(5)
            pass
        else:
            count = 0
            for each in sic.Symbol:
                count += 1
                self.ui.textBrowser.insertPlainText(each+ '\t')
                if count % 3 == 0:
                    self.ui.textBrowser.insertPlainText('\n')

    def object_program_format(self):
        self.ui.textBrowser.clear()
        if self.file_name == '':
            self.set_message(5)
            pass
        else:
            left = '00'
            temp = self.sic
            instruction_len = len(temp.instruction)
            header = 'H^' + temp.instruction[0].symbol + '\t' + left + temp.instruction[0].leftAddress + '^'
            txt_begin = function.hex_to_dec(temp.instruction[0].leftAddress)
            txt_end = function.hex_to_dec(temp.instruction[instruction_len-1].leftAddress)
            header += left + function.dec_to_hex(txt_end - txt_begin)
            self.ui.textBrowser.insertPlainText(header + '\n')
            size = 0
            begin_index = 1
            lines = []
            b = []
            sizes = []
            line = ''
            b.append(begin_index)
            while True:
                if begin_index == instruction_len - 1:
                    lines.append(line)
                    sizes.append(size)
                    b.append(begin_index)
                    break
                elif size + (len(sic.MC[begin_index]) / 2) > 30:
                    lines.append(line)
                    sizes.append(size)
                    b.append(begin_index)
                    line = ''
                    size = 0
                elif sic.MC[begin_index] == '':
                    lines.append(line)
                    sizes.append(size)
                    b.append(begin_index+1)
                    line = ''
                    size = 0
                if sic.MC[begin_index] == 'error':
                    pass
                elif sic.MC[begin_index] == '':
                    pass
                else:
                    line += '^' + function.fill_zeros(sic.MC[begin_index])
                    size += (len(sic.MC[begin_index]) / 2)
                begin_index += 1

            for i in range(len(lines)):
                line = ''
                if lines[i] == '':
                    pass
                else:
                    line += 'T^' + left + temp.instruction[b[i]].leftAddress + '^'
                    if sizes[i] < 16:
                        line += '0'
                    line += function.dec_to_hex(int(sizes[i])) + lines[i] + '\n'
                    self.ui.textBrowser.insertPlainText(line)
            self.ui.textBrowser.insertPlainText('E^00' + temp.instruction[0].leftAddress)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
