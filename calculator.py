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

    def _dismember_digit(self):  # Separates the numbers from the digits.
        number = ''
        numbers, operators = [], []
        calc_text = self.ids.calc_input.text
        for caracter in calc_text + '_':  # The underscore is making the number enter in the 'else'
            if caracter.isalnum() == True:
                number += caracter
            else:
                numbers.append(number)
                operators.append(caracter)
                number = ''
        operators.remove('_')
        return numbers, operators

    def _sum(self):
        numbers = self.numbers
        operators = self.operators
        if numbers[0] == '':
            answer = 0
        else:
            answer = int(numbers[0])
        numbers.pop(0)
        while numbers:
            match operators[0]:
                case '+':
                    answer += int(numbers[0])
                    numbers.pop(0)
                    operators.pop(0)
                case '-':
                    answer = answer - int(numbers[0])
                    numbers.pop(0)
                    operators.pop(0)
        return answer

    def sum_buttom_pressed(self):
        calc_text = self.ids.calc_input.text
        self.numbers, self.operators = self._dismember_digit()
        try:
            answer = self._sum()
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'ERROR'


class Calculator(App):
    def build(self) -> None:
        Window.clearcolor = 0.10, 0.10, 0.15, 1
        return CalcLayout()


Calculator().run()