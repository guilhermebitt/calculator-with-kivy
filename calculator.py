from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty


# Settings
Builder.load_file('design_calculator.kv')
Window.size = 500, 700

class CalcLayout(Widget):
    def clear(self, instance):
        if instance.text == 'BS':
            self.ids.calc_input.text = self.ids.calc_input.text[:-1]
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = '0'
        else:
            self.ids.calc_input.text = '0'

    def digit(self, digit):
        calc_text = self.ids.calc_input.text  # Variable for the text in the inputtext widget

        if str(calc_text) == '0' and digit.text != '.' or str(calc_text) == 'ERROR':
            self.ids.calc_input.text = ''
        self.ids.calc_input.text += digit.text
    
    def change_sign(self):
        numbers, operators = self._dismember_digit()
        if not operators:
            self.ids.calc_input.text = '-' + self.ids.calc_input.text
        else:
            if str(self.ids.calc_input.text)[0] == '-':
                self.ids.calc_input.text = '' + str(self.ids.calc_input.text)[1:]
            elif str(self.ids.calc_input.text)[0] == '+':
                self.ids.calc_input.text = '-' + str(self.ids.calc_input.text)[1:]

    def _dismember_digit(self):  # Separates the numbers from the digits.
        number = ''
        numbers, operators = [], []
        calc_text = self.ids.calc_input.text
        for caracter in calc_text + '_':  # The underscore is making the number enter in the 'else'
            if caracter.isalnum() == True or caracter == '.':
                number += caracter
            else:
                numbers.append(number)
                operators.append(caracter)
                number = ''
        operators.remove('_')
        return numbers, operators

    def _calc(self):
        numbers = self.numbers
        operators = self.operators
        if numbers[0] == '':
            answer = 0
        else:
            answer = float(numbers[0])
        numbers.pop(0)
        while numbers:
            match operators[0]:
                case '+':
                    answer = answer + float(numbers[0])
                    numbers.pop(0)
                    operators.pop(0)
                case '-':
                    answer = answer - float(numbers[0])
                    numbers.pop(0)
                    operators.pop(0)
                case '*':
                    answer = answer * float(numbers[0])
                    numbers.pop(0)
                    operators.pop(0)
                case '÷':
                    answer = answer / float(numbers[0])
                    numbers.pop(0)
                    operators.pop(0)
                case '%':
                    answer = answer * (float(numbers[0]) / 100)
                    numbers.pop(0)
                    operators.pop(0)

        if str(answer)[-2:] == '.0':
            answer = int(answer)

        return answer

    def equals_buttom_pressed(self):
        self.numbers, self.operators = self._dismember_digit()
        operators_filter = ['+', '-', '*', '÷', '%', '.']
        try:
            for i in str(self.ids.calc_input.text):
                #print(i)
                if i not in operators_filter and i.isnumeric() == False:
                    raise Exception
            answer = self._calc()
            #print(self.numbers, self.operators + '1')  # For some reasson, I NEED to keep this in the code, otherwise it'll crash
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'ERROR'

class Calculator(App):
    def build(self) -> None:
        Window.clearcolor = 0.10, 0.10, 0.15, 1
        return CalcLayout()


Calculator().run()
