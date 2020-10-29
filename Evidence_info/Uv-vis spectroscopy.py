from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text:"UV-Visible Spectroscopy"
        font_size:40
        text_size:self.size
        pos_hint:{"x":0.25,"y":0.75}

    MDLabel:
        size: self.texture_size
        text:"Ultraviolet and visible (UV-Vis) spectroscopy is helpful in :- "
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.65}
   
    MDLabel:
        size: self.texture_size
        text:"-> Detection of functional group"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.55}
    MDLabel:
        size: self.texture_size
        text:"-> Detection of impurities"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.45}
    MDLabel:
        size: self.texture_size
        text:"->  Qualitative Analysis"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.35}
    MDLabel:
        size: self.texture_size
        text:"-> Single compound without chromophore"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.25}
    MDLabel:
        size: self.texture_size
        text:"-> Drugs with chromophoric reagent"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.15}
    MDLabel:
        size: self.texture_size
        text:"-> Detection of conjugation of the compound"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.02,"y":0.05}

'''
class UVVisibleSpectroscopy(MDApp): # <- Main Class
    def build(self):
        return Builder.load_string(KV)


UVVisibleSpectroscopy().run()