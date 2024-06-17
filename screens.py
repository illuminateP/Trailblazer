"""
# !rule #
1 . TrailBlazer.py -> 구동부
2. screens.py -> 화면 내 로직과 위젯 관리 , 위젯부와 로직부 분리할 지 생각 중이다. 현재는 스크린 내 로직도 작성되어 있다.
screen 명 작성 규칙 : snake 
★ screen 추가 시 1) 이름이 소문자인지 , snake 규칙을 따르는지 확인하고
2)
class first_screen(Screen):
    def __init__(self, app, **kwargs):
        super(first_screen, self).__init__(**kwargs)
        self.app = app
    으로 init시 app parameter passing 확인하며
3)
class MyApp(App):
    def build(self):
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.first_screen)
    로 screen_mananger에 스크린 등록하고 있는지 확인!  
    
3. utils.py -> 종료와 farewell 기능 불러오는 위젯이고 화면 구성 시 종료 , 취소 버튼과 screen 내에서 binding한다.
4. fonts.py -> 폰트 불러오는 모듈 , first_screen __init__가 아니라 myAPP build 시로 가야 한다.
5. strings.py -> 사용할 스트링 불러오는 모듈, fonts.py와 합쳐서 string 처리하도록 바꿔야 한다
6. map.py -> 지도 기능에 사용할 모듈이고 기능별로 모듈 분리할거면 first_screen 여기다 붙혀야 한다.


7. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야한다. 이는 비 라틴언어 모두에 해당하며 , 영어 제외하면 폰트 전부 적어줘야 한다.
8. 기능별로 모듈 분리할지 , 화면별로 분류해서 Screen.py에 배치할 지 생각 , 내부 로직부분과 분리하는 게 좋을 것 같은데

"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.core.window import Window

from kivy.uix.scatter import Scatter
from kivy.garden.mapview import MapView , MapMarker, MapSource
from kivy.utils import platform


from kivy.resources import resource_find


import fonts
import utils
import map
import input_text

# MyApp 외부 메서드 , 선언 규칙 : 스크린 = snake , 위젯 , 위젯 바인딩 메서드 = _pascal
class main_screen(Screen):
    def __init__(self, app, **kwargs):
        super(main_screen, self).__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        First_Button = Button(text='길찾기 기능!', size_hint=(1, 0.5), font_name='youth')
        First_Button.bind(on_press=self.First_Button_Clicked)
        self.layout.add_widget(First_Button)

        Second_Button = Button(text='2번째 기능', size_hint=(1, 0.5), font_name='youth')
        Second_Button.bind(on_press=self.Second_Button_Clicked)
        self.layout.add_widget(Second_Button)

        Third_Button = Button(text='3번째 기능', size_hint=(1, 0.5), font_name='youth')
        Third_Button.bind(on_press=self.Third_Button_Clicked)
        self.layout.add_widget(Third_Button)

        Exit_Button = Button(text='종료', size_hint=(1, 0.5), font_name='youth')
        Exit_Button.bind(on_press=self.Exit_Button_Clicked)
        self.layout.add_widget(Exit_Button)
        
        self.add_widget(self.layout)

    def First_Button_Clicked(self, instance):
        print("first button pressed")
        self.app.Switch_To('first_screen') 

    def Second_Button_Clicked(self, instance):
        print("second button pressed")

    def Third_Button_Clicked(self, instance):
        print("third button pressed")
        
    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)

    # 위치 정보 제공 동의 처리하는 팝업#
    def show_consent_popup(self):
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        label = Label(text='TrailBlazer는 고객의 정보를 소중하게 생각합니다. 제공된 위치 정보는 길찾기 기능 사용 시에만 사용되며, 앱 종료 시 지체 없이 파기합니다. 위치 정보를 제공하시겠습니까?', font_name='youth')
        consent_button = Button(text='동의', font_name='youth')
        decline_button = Button(text='거절', font_name='youth')


        if platform in ['win', 'linux', 'macosx']:
            consent_button.bind(on_press=self.user_consented_pc)
        elif platform in ['android', 'ios']:
            consent_button.bind(on_press=self.user_consented_mobile)
        else:
            print("플랫폼 감지 에러 !")
            self.popup.dismiss()
            
        decline_button.bind(on_press=lambda instance: self.popup.dismiss())    

        content.add_widget(label)
        content.add_widget(consent_button)
        content.add_widget(decline_button)

        self.popup = Popup(title='위치 정보 제공 동의', title_font='youth', content=content, size_hint=(0.8, 0.4))
        self.popup.open()

    ## PC 용 , PC환경에서는 gachon_free_wifi의 ip 주소를 사용하여 GPS 정보를 대략적으로 가져오고, 다른 무선 네트워크에 연결중일 경우 geoip로 사용자의 위치를 대략적으로 사용한다. 추후 추가 예정.
    def user_consented_pc(self, instance): 
        self.popup.dismiss()
        #self.get_user_location_pc()
        print("user consented for pc!")
        
    # 모바일 용 , 모바일에서는 plyer를 사용해 내장 gps를 제어해 사용자 위치를 대략적으로 가져온다. 추후 추가 예정.
    def user_consented_mobile(self, instance):
        self.popup.dismiss()
        print("user consented for mobile!")
        """
        try:
            global GPS
            GPS = gps()
            self.get_user_location_mobile()
        except Exception as e:
            print(f"Error initializing GPS: {e}")
        """
    
        
        

    # 길찾기 제공하는 화면 
class first_screen(Screen):

    def __init__(self, app, **kwargs):
        super(first_screen, self).__init__(**kwargs)

        self.app = app
        self.layout =  BoxLayout(orientation='vertical', spacing=0, padding=0)
        self.sublayout = BoxLayout(orientation='horizontal', spacing=10, padding=10)


        # InputForm 생성 시 핸들러 함수 input_text.py에서 바인딩.
        self.input_form_top = input_text.InputForm(self.layout, self.on_search)
        self.input_form_bottom = input_text.InputForm(self.layout, self.on_search)
        
        search_button = Button(text='검색', size_hint=(1, None), height=30, font_name='youth')
        search_button.bind(on_press=self.on_search)
        
        self.layout.add_widget(search_button)
        
        self.toolbar = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(0.3, 1))

        # main_screen으로 돌아가는 버튼
        Back_Button = Button(text='뒤로 가기', size_hint=(1, 1), font_name='youth')
        Back_Button.bind(on_press=self.Back_To_Main)
        self.toolbar.add_widget(Back_Button)
            
        First_Functional_Button = Button(text='첫 번째 기능', size_hint=(1, 1), font_name='youth')
        First_Functional_Button.bind(on_press=self.First_Functional_Button_Clicked)
        self.toolbar.add_widget(First_Functional_Button)
            
        Second_Functional_Button = Button(text='두 번째 기능',size_hint=(1, 1), font_name='youth')
        Second_Functional_Button.bind(on_press=self.Second_Functional_Button_Clicked)
        self.toolbar.add_widget(Second_Functional_Button)
            
            
        Third_Functional_Button = Button(text='세 번째 기능', size_hint=(1, 1), font_name='youth')
        Third_Functional_Button.bind(on_press=self.Third_Functional_Button_Clicked)
        self.toolbar.add_widget(Third_Functional_Button)

        Fourth_Functional_Button = Button(text='네 번째 기능', size_hint=(1, 1), font_name='youth')
        Fourth_Functional_Button.bind(on_press=self.Fourth_Functional_Button_Clicked)
        self.toolbar.add_widget(Fourth_Functional_Button)

        Fifth_Functional_Button = Button(text='다섯 번째 기능', size_hint=(1, 1), font_name='youth')
        Fifth_Functional_Button.bind(on_press=self.Fifth_Functional_Button_Clicked)
        self.toolbar.add_widget(Fifth_Functional_Button)
            
        # 닫기 버튼을 눌렀을 때 종료창 호출
        Exit_Button = Button(text='종료', size_hint=(1, 1), font_name='youth')
        Exit_Button.bind(on_press=self.Exit_Button_Clicked)
        self.toolbar.add_widget(Exit_Button)
            
        self.sublayout.add_widget(self.toolbar)

        # 맵뷰와 이미지 겹쳐 표시할 위젯
        self.map_layout = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint=(0.7, 1))
        self.map_view = MapView(zoom=11, size_hint=(1, 1))  
            
        # 커스텀 타일 소스 지정
        tile_source_path = resource_find('assets/blueprint.png')
        self.map_view.tile_source = tile_source_path

        if tile_source_path:
            # 커스텀 타일 소스 설정
            custom_map_source = MapSource(url=tile_source_path, tile_size=256, image_ext='png', min_zoom=0, max_zoom=20)
            self.map_view.map_source = custom_map_source

        self.map_layout.add_widget(self.map_view)
        self.sublayout.add_widget(self.map_layout)
        self.layout.add_widget(self.sublayout)
        self.add_widget(self.layout)

        # 고정 위치 마커 추가(임시)
        self.add_fixed_marker()
    
    def on_search(self, instance):
        print("search button clicked! further make handler function !")


    def add_fixed_marker(self):
        # 예시 고정 좌표 (위도, 경도)
        fixed_lat = 37.7749
        fixed_lon = -122.4194
        marker = MapMarker(lat=fixed_lat, lon=fixed_lon)
        self.map_view.add_marker(marker)

    def to_widget(self, x, y):
        return (self.map_view.x + x * self.map_view.width, self.map_view.y + y * self.map_view.height)


    def Back_To_Main(self, instance):
        self.app.Switch_To('main_screen') 

    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)
    
    def First_Functional_Button_Clicked(self,instance):
        print("First Functinal Button clicked!")
        
    def Second_Functional_Button_Clicked(self,instance):
        print("Second Functional Button clicked!")
    
    def Third_Functional_Button_Clicked(self,instance):
        print("Third Functional Button clicked!")
        
    def Fourth_Functional_Button_Clicked(self,instance):
        print("Fourth Functional Button clicked!")
          
    def Fifth_Functional_Button_Clicked(self,instance):
        print("Fifth Functional Button clicked!")
    

    
class MyScreenManager(ScreenManager):  # ScreenManager 추가
    def __init__(self, app, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = app       

class MyApp(App):
    def build(self):
        self.app = App
        self.screen_manager = MyScreenManager(self)
        fonts.register_fonts()
        self.title = "TrailBlazer"
        
        self.main_screen = main_screen(self, name='main_screen')  
        self.first_screen = first_screen(self, name='first_screen')  
        
        
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.first_screen)


        # 창에 상관없이 전역적으로 처리 
        Window.bind(on_request_close=self.on_request_close)
        return self.screen_manager
    
    def Switch_To(self, screen_name):
        self.screen_manager.current = screen_name

    def Toast_Messages(self, title, message):
        toast_label = Label(text=message, font_name='youth')
        toast_popup = Popup(title=title, content=toast_label, auto_dismiss=False, size_hint=(None, None), size=(200, 100))
        toast_popup.open()
    
    def Exit_Button_Clicked(self, instance):
        utils.Ending_Messages(self.app)
    
    def on_request_close(self, *args):
        utils.Ending_Messages(self.app)
        return True
    
    def on_start(self):
        # 앱 시작 시 platform 감지해 platform에 맞는 방법으로 사용자의 GPS 정보 제공 동의를 받는다.
        # 모바일 환경
        if platform == 'android' or platform == 'ios':
            #from plyer import gps
            self.main_screen.show_consent_popup()
        # pc 환경 
        else:
            #from geopy.geocoders import Nominatim
            self.main_screen.show_consent_popup()
        
        
    def on_stop(self):
        print("GPS! off!")
        """
        try:
            if platform in ['android', 'ios']:
                GPS.stop()
        except Exception as e:
            print(f"Error stopping GPS: {e}")
        """
    