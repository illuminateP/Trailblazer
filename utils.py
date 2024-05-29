from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random

# 프로그램 종료 시 랜덤 종료 메시지를 생성하는 메서드 #
def farewell():
    messages = ['안녕', '잘가', '이건 테스트 메시지야', '이렇게 대충 좋은 말 하면서', '작별 인사를 하면', '좀', '있어 보이겠지?']
    random_num = random.randint(0, len(messages) - 1)
    return messages[random_num]

# 엔딩 메시지를 출력하는 메서드 #
def Ending_Messages(app):
    Message = farewell()
    print(Message)

    toast_label = Label(text=Message, font_name='chosun', size_hint_y=None, height=120)

    def cancel_toast(instance):
        toast_popup.dismiss()

    def close_toast(instance):
        toast_popup.dismiss()
        app.get_running_app().stop()    

    cancel_button = Button(text='닫기', font_name='youth')
    cancel_button.bind(on_press=lambda instance: close_toast(instance))

    close_button = Button(text='취소', font_name='youth')
    close_button.bind(on_press=lambda instance: cancel_toast(instance))

    Toast_Layout = BoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=20)
    Toast_Layout.add_widget(toast_label)

    Button_Layout = BoxLayout(orientation='horizontal', padding=[10, 10, 10, 10], spacing=20, size_hint=(1, None), height=60)
    Button_Layout.add_widget(cancel_button)
    Button_Layout.add_widget(close_button)

    Toast_Layout.add_widget(Button_Layout)

    toast_popup = Popup(title='잘 가요! 이거 만드느라 얼마나 고생했는지 당신은 모를 거에요', title_font='youth' , content=Toast_Layout, auto_dismiss=False, size_hint=(0.8, None), height=300)
    toast_popup.open()
