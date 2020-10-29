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

                KitchenSinkTextFieldRound:
                    icon_left: 'email'
                    hint_text: 'Example@Domain'

                KitchenSinkTextFieldRound:
                    icon_left: 'key-variant'
                    icon_right: 'eye-off'
                    hint_text: 'Password'
                    
                KitchenSinkTextFieldRound:
                    icon_left: 'key-variant'
                    icon_right: 'eye-off'
                    hint_text: 'Confirm Password'
                    
                MDFillRoundFlatButton:
                    text: "Sign Up"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release:os.system("Home_page.py")

"""

class CreateAccount(MDApp):
    def build(self):
        return Builder.load_string(KV)

CreateAccount().run()
