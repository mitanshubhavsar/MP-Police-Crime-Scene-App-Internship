from kivy.lang import Builder
from kivymd.app import MDApp


KV = '''
# 


Screen:


    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    

                    MDToolbar:
                        md_bg_color: app.theme_cls.primary_color
                        title: "Investigation Support"
                        #elevation: 10
                        left_action_items: [["arrow-left", lambda x: x]]
                    
                    BoxLayout:
                        orientation:'vertical'
                        spacing:2
                        padding:(20,20,20,20)
                    #Widget:         
                         
                        Image:
                            source: 'Physical evidence image.jpeg'
                        MDRaisedButton:
                            text: "       Physical Evidence       "
                            pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        Image:
                            source:'chemical evidence image.jpeg'
                        MDRaisedButton:
                            text: "       Chemical Evidence       "
                            pos_hint: {"center_x": 0.5, "center_y": 0.2}
                        Image:
                            source:'Biological evidence image.jpeg'
                        MDRaisedButton:
                            text: "        Biological Evidence        "
                            pos_hint: {"center_x": 0.5, "center_y": 0.2}    
                                         
       
'''


class TypesofevidenceIndex(MDApp):
    def build(self):
        return Builder.load_string(KV)



TypesofevidenceIndex().run()
