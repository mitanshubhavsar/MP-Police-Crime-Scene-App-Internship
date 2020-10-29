from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

KV = '''
# Menu item in the DrawerList list.
#:import MDFillRoundFlatButton kivymd.uix.button.MDFillRoundFlatButton
#:import MDIconButton kivymd.uix.button.MDIconButton
#:import os os
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
        


<ContentNavigationDrawer>:
    orientation: "vertical"
    
    ScrollView:
        
        DrawerList:
            id: md_list


Screen:

    NavigationLayout:

        ScreenManager:

            Screen:
            
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDToolbar:
                        title: "Investigation Support"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    
                    MDIconButton:
                        icon: 'image-plus'
                        user_font_size: "64sp"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                    
                    MDFillRoundFlatButton:
                        text: "Upload New Image"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                        
                    MDIconButton:
                        icon: 'view-grid'
                        user_font_size: "64sp"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                    
                    MDFillRoundFlatButton:
                        text: "Grid Management"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                        
                    MDIconButton:
                        icon: 'magnify'
                        user_font_size: "64sp"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                    
                    MDFillRoundFlatButton:
                        text: "Object Identification"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                        
                    MDIconButton:
                        icon: 'file-document-box-multiple'
                        user_font_size: "64sp"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                    
                    MDFillRoundFlatButton:
                        text: "Securing Evidence"
                        pos_hint: {'center_x' :0.5, 'center_y' :0.5}
                        on_release:os.system("Evidence_Index.py")
                    
                
                    
                    Widget:
        


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "file-plus": "New Project",
            "file": "Existing Projects",
            "view-grid": "Grid Management",
            "eye": "Object Detection",
            "checkbox-marked": "Object Classification",
            "security": "Securing Evidence",
            "alert-circle-outline": "About",
            "phone": "Contact us"
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name], divider="Full")
            )


TestNavigationDrawer().run()
