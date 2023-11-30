# This is a sample Python script.
# coding: utf-8
import sys
from functools import partial

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from PySide6 import QtCore, QtWidgets, QtGui
import random

from PySide6.QtWidgets import QPushButton

from ui_main import Ui_Form

from PySide6.QtCore import Slot


class Cotroller:
    # 计算符号
    _arithmetic_symbol = ''
    # 当前展示内容
    _current_show_content = '0'
    # 当前输入
    _current_input = ['0']
    # 当前状态 0-初始状态，1-第一个数已输入状态，2-输入计算符号状态，3-第二个数已输入状态
    _input_status = 0
    _ui_form = Ui_Form()

    def start(self):
        app = QtWidgets.QApplication([])
        widget = QtWidgets.QWidget()
        self._ui_form.setupUi(widget)
        self.add_event()
        widget.show()
        sys.exit(app.exec_())

    # 添加事件
    def add_event(self):
        print('添加事件')
        properties = dir(self._ui_form)
        for item in properties:
            if item.startswith('pushButton'):
                # 是按键类型
                item_obj: QPushButton = getattr(self._ui_form, item)
                text = item_obj.text()
                item_obj.clicked.connect(partial(self.handle_event, text))

    # 处理事件
    @Slot()
    def handle_event(self, text):
        if text in '0123456789.':
            self.handle_num(text)
            return
        if text in '÷x-+':
            self.handle_arithmetic(text)
            return
        if text == '=':
            self.handle_sum()
            return
        if text == 'AC':
            self.handle_clear()
            return

    # 清零
    def handle_clear(self):
        self._current_input = ['0']
        self._current_show_content = '0'
        self._input_status = 0
        self.show_result()

    # 处理数字
    def handle_num(self, num_str):
        # 判定长度，超出则禁止输入
        if len(self._current_show_content) >= 10:
            return
        if num_str == '.':
            if '.' not in self._current_show_content:
                self._current_show_content = self._current_show_content + num_str
        else:
            if self._current_show_content == '0':
                self._current_show_content = num_str
            else:
                self._current_show_content = self._current_show_content + num_str
        if self._input_status == 0 or self._input_status == 3:

            self._current_input = [self._current_show_content]
        else:
            self._current_input.append(self._current_show_content)

        self.show_result()

    def handle_arithmetic(self, symbol):
        if len(self._current_input) > 1:
            self.handle_sum()
        self._arithmetic_symbol = symbol
        self._input_status = 1

    def handle_sum(self):
        if len(self._current_input) <= 1:
            return
        self._current_show_content = self.arithmetic(self._arithmetic_symbol, self._current_input[0],
                                                     self._current_input[1])
        self._current_input = [self._current_show_content]
        self._arithmetic_symbol = ''
        self._input_status = 0
        self.show_result()

    # 处理加减乘除
    @staticmethod
    def arithmetic(symbol, s1: str, s2: str):
        if symbol == '+':
            return str(float(s1) + float(s2))
        if symbol == '-':
            return str(float(s1) - float(s2))
        if symbol == 'x':
            return str(float(s1) * float(s2))
        if symbol == '÷':
            return str(float(s1) / float(s2))

    # 显示
    def show_result(self):
        self._ui_form.lineEdit.setText(self._current_show_content)


if __name__ == '__main__':
    Cotroller().start()
