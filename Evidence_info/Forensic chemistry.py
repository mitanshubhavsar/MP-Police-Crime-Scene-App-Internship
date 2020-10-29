from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text:"Forensic Chemistry"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.318,"y":0.85}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> Forensic laboratories and criminalistics laboratories perform numerous measurements and tests to support both criminal and civil legal actions. For Example- Measurement of blood & breath alcohol content, Quantification of controlled samples (net weight & purity), length measurement of firearm barrels."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.65}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> Equipment used in Forensic metrology are breath analyser, balances & scale, Callipers, Gas Chromatographs, IR Graphs, UV Absorption Graphs."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.55}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> Forensic chemist rely on three techniques "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.48}
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"1) Visual Examination & Inspection (Both Macroscopic & Microscopic Analysis)"
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.44}
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"2) Organic chemical Analysis"
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.396}
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"3) Inorganic chemical analysis"
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.35}               
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:" STEP 1: Analysis starts with quantitative wet chemical test, most of the test are based on observing results like Colour & Crystal Test which is used for testing drugs, gunshots residue and explosives."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.20}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"STEP2: The second step involves the separation and isolation of target components for identification. This step requires extraction and chromatography."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.10}





'''
class ForensicChemistry(MDApp): # <- Main Class
    def build(self):
        return Builder.load_string(KV)


ForensicChemistry().run()