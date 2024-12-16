from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        
        # GridLayoutを使用してボタンを配置
        layout = GridLayout(cols=4)
        
        # ボタンのラベルとそれに対応するアクションを設定
        buttons = [
            ('7', self.on_button_press), ('8', self.on_button_press), ('9', self.on_button_press), ('/', self.on_button_press),
            ('4', self.on_button_press), ('5', self.on_button_press), ('6', self.on_button_press), ('*', self.on_button_press),
            ('1', self.on_button_press), ('2', self.on_button_press), ('3', self.on_button_press), ('-', self.on_button_press),
            ('C', self.clear), ('0', self.on_button_press), ('=', self.calculate), ('+', self.on_button_press)
        ]
        
        for label, action in buttons:
            button = Button(text=label, on_press=action)
            layout.add_widget(button)
        
        layout.add_widget(self.result)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        new_text = current + instance.text
        self.result.text = new_text

    def clear(self, instance):
        self.result.text = ""

    def calculate(self, instance):
        try:
            # 入力された数式を評価して結果を表示
            equation = self.result.text
            self.result.text = str(eval(equation))
        except Exception:
            self.result.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()
