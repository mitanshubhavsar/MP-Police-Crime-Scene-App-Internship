from kivymd.app import MDApp
from kivy.lang import Builder

KV = """
#:import Window kivy.core.window.Window
#:set color_shadow [0, 0, 0, .2980392156862745]
#:import os os


<KitchenSinkTextFieldRound@MDTextFieldRound>
    size_hint_x: None
    normal_color: color_shadow
    active_color: color_shadow


Screen:

    BoxLayout:
        orientation: "vertical"
        spacing: "10dp"

        MDToolbar:
            md_bg_color: app.theme_cls.primary_color
            title: "Investigation Support"
            elevation: 10
            left_action_items: [["arrow-left", lambda x: x]]

        ScrollView:

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(48)
                spacing: dp(15)


                MDFillRoundFlatButton:
                    text: "Sign In"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release:os.system("Login.py")
                
                MDFillRoundFlatButton:
                    text: "Sign Up"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release:os.system("CreateAccount.py")
                    
                    


"""


class Welcome(MDApp):
    def build(self):
        return Builder.load_string(KV)


Welcome().run()
