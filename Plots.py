from re import M
from ursina import *
from modified_api.Convo import Conversation
from _config import *
from modified_api.wp import WP
from ursina.prefabs.radial_menu import RadialMenu, RadialMenuButton

class Seaside(Entity):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent=parent, scale=(1.5, 2), position=(0, 0), enabled=False, z=-2, **kwargs)
        self.enabled=False
        self.set_scissor(Vec3(-.5,-.25,0), Vec3(.5,.25,0))
        
        self.base = Entity(
            parent=self, model='quad', 
            collider='box', visible_self=False)
        
        self.process = 0
        self.background = Entity(
            parent=self.base, 
            model='quad',
            texture=r"assets\pics\hokkaido\seaside.png"
        )
        self.helper = []
        self.toggled = None

        self.events = [
            None, 
            WithFisherman(parent=self), 
            InspectSea(parent=self), 
            Task(parent=self)
            ]
        self.base.add_script(Scrollable(min=-.25, max=.25))


    def trailer(self):
        self.convo = Conversation(parent=self.base, scale_x=.6, scale_y=.5)
        self.convo.start_conversation(
            '''Welcome to Hokkaido! You looks still a bit blurred. How about just start with talking to some folks?
            \n    * That's great. (self.parent.parent.process += 1)
            '''
        )
        if self.process == 1:
            self.playNext()
    
    def playNext(self):
        # print(self.process)
        if self.process == 1:
            self.helper.append(Button(
                parent=self.base, model='quad',
                text='urban', texture=r'assets\pics\icon_exclamationSmall.png',
                position=(-.1, 0), scale=(.142, .1),
                color=color.orange, alpha=.6,
                on_click=Func(self.setToggled, 1)
            ))

            self.helper.append(Button(
                parent=self.base, model='quad',
                text='sea', texture=r'assets\pics\icon_exclamationSmall.png',
                position=(-.3, -.35), scale=(.142, .1),
                color=color.orange, alpha=.6,
                on_click=Func(self.setToggled, 2)
            ))

            # self.helper.append(Button(
            #     parent=self.base, model='quad',
            #     text='Task', 
            #     position=(0, 0), scale=(.142, .1),
            #     color=color.azure, alpha=.6,
            #     on_click=Func(self.setToggled, 3)
            # ))

    
    def setToggled(self, t) :
        if t == 0 :
            self.base.enable()
            return
        self.base.disable()
        if self.toggled != None:
            self.toggled.disable()
        self.toggled = self.events[t]
        self.toggled.enable()

    def enable(self):
        self.enabled = True
        self.base.enable()
        print("seaside enabled")
        if self.process == 0:
            self.trailer()
    
    def disable(self):
        self.enabled = False
        print("seaside disabled")


class WithFisherman(Entity):
    def __init__(self, **kwargs):
        super().__init__(enabled=False, **kwargs)
        self.enabled = False
        self.background = Entity(
            model='quad', texture=r"assets\pics\hokkaido\with_fisherman.jpg", 
            parent=self, scale=(1, .5), color=color.light_gray, y=0
        )
        self.convo = None
        # Conversation(parent=self, scale_x=.6, scale_y=.5, y=.1)
        self.stage = 1

    def start_convo(self, src):
        # self.convo = Conversation(parent=self, scale_x=.6, scale_y=.5, y=.1)
        self.convo = Conversation(parent=self, scale_x=.6, scale_y=.5, y=.1)
        self.convo.start_conversation('\n'.join(src.readlines()))

    def enable(self):
        print(self.stage)
        self.enabled = True
        self.start_convo(open(f"scripts\with_fisherman{self.stage}.txt"))

    def nextStage(self):
        self.stage += 1

    def update(self):
        if self.convo.enabled == False:
            if self.stage == 1:
                self.parent.setToggled(0)
            elif self.stage == 2:
                self.parent.setToggled(3)



class InspectSea(Entity) :
    class More(Button) :
        def __init__(self, parent=None, text="", position=(0, 0), on_click=None, **kwargs):
            super().__init__(
                parent=parent, model='quad',
                text=text, texture=r'assets\pics\icon_plusSmall.png',
                position=position, scale=(.13, .1),
                color=color.azure, alpha=.6,
                on_click=on_click, **kwargs
            )
    
    class InfoBox(Text) :
        def __init__(self, parent=None, text='', position=(0, 0), **kwargs):
            super().__init__(
                dedent(text).strip(), 
                parent=parent, 
                position=position, scale=(1, .8),
                line_height=.55,
                **kwargs)

    class InfoBtn(Button) :
        def __init__(self, text, hidenText="", **kwargs):
            super().__init__(text=text, scale=(.3, .05), **kwargs)
            self.hidenText = hidenText
        
        def on_click(self):
            self.text = self.hidenText

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enabled = False
        self.set_scissor(Vec3(-.5,-.25,0), Vec3(.5,.25,0))
        
        self.base = Entity(
            parent=self, model='quad', 
            collider='box', visible_self=False)

        self.background = Entity(
            parent=self.base, 
            model='quad',
            texture=r"assets\pics\hokkaido\sea.png"
        )
        self.base.add_script(Scrollable(min=-.25, max=.25))
        self.pH = [
            self.InfoBtn(parent=self.base, text="Click to test the pH Value", hidenText="-0.45 (from 1990s)", position=(0, .3)),
            # self.InfoBtn(parent=self.base, text="Temperature", hidenText="15.0", position=(0, .25))
        ]
        
        self.moreInfo = [
            self.More(
                parent=self.base, position=(.1, -.2), text="Fish", 
                on_click=Func(self.showInfo, "salmon")),
        ]
        
        self.info1 = self.InfoBox(
                parent=self.base, position=(-.4, .1),
                text=SEA_info['oa_effects'], enabled=False)
        
    def showInfo(self, msg) :
        self.info1.enabled = not self.info1.enabled
    
    def input(self, key):
        if key == "space" :
            self.parent.events[1].nextStage()
            self.disable()
            self.parent.enable()
            

class Task(Entity) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.enabled = False
        self.background = Sprite(
            r'assets\pics\hokkaido\acid_2.PNG', 
            parent=self, scale=(1.2, .045), y=.02, color=color.light_gray
        )

    #     self.rm = RadialMenu(
    #         parent=self,
    #         buttons = (
    #             RadialMenuButton(parent=self, text='1'),
    #             RadialMenuButton(parent=self, text='2'),
    #             RadialMenuButton(parent=self, text='3'),
    #             RadialMenuButton(parent=self, text='4'),
    #             RadialMenuButton(parent=self, text='5', scale=.5),
    #             RadialMenuButton(parent=self, text='6', color=color.red),
    #             ),
    #         enabled = False
    #         )
    #     self.checkboxes = [
    #         Button(
    #             parent=self, model='cube', color=color.orange, alpha=.4, position=(0, .2),
    #             on_click=Func(self.enable_rm, 1)
    #         )
    #     ]
    
    # def enable_rm(self, ind) :
    #     self.rm.enabled = True
    
    def input(self, key):
        if key == "space" :
            self.disable()
            self.parent.enable()
        