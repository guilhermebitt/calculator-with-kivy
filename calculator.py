from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# Settings
Builder.load_file('design_calculator.kv')
Window.size = 500, 700

class CalcLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def digit(self, digit):
        calc_text = self.ids.calc_input.text  # Variable for the text in the inputtext widget

        if str(calc_text) == '0':
            self.ids.calc_input.text = ''
        self.ids.calc_input.text += digit.text

    def add(self):
        self.ids.calc_input.text += '+'

    def subtract(self):
        self.ids.calc_input.text += '-'

    def multiply(self):
        self.ids.calc_input.text += 'x'

    def divide(self):
        self.ids.calc_input.text += '÷'

    def sum(self):
        calc_text = self.ids.calc_input.text
        answer = 0

        # Addition
        if '+' in calc_text:
            num_list = calc_text.split('+')
            for number in num_list:
                answer += int(number)
            self.ids.calc_input.text = str(answer)


class Calculator(App):
    def build(self) -> None:
        Window.clearcolor = 0.10, 0.10, 0.15, 1
        return CalcLayout()


Calculator().run()