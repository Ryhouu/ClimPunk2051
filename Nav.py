from ursina import *
from _config import *
from modified_api.Convo import Conversation
from modified_api.wp import WP
from Plots import Seaside

class Section(Entity) :
    def __init__(self, parent=None, title="", bg=None, scale=.055, **kwargs):
        super().__init__(parent=parent, **kwargs)
        self.title = title
        self.background = Sprite(
            bg, parent=self, scale=scale, color=color.light_gray, z=-1
        )
        self.enabled = False

        self.add_buttons()
    
    def add_buttons(self):
        # if self.title in manual_btns.keys:
        if self.title == "diseases":
            for src in manual_btns[self.title] :
                Button(
                    parent = self,
                    model = 'cube',
                    texture = f'assets\pics\manual\{src[0]}.png',
                    color = color.white10,
                    highlight_color = color.black33,
                    scale = src[1],
                    z = -2,
                    position = src[2],
                    on_click = Func(self.show_msg, src[0], src[3])
                )
        elif self.title in ["famine"]:
            for src in manual_btns[self.title] :
                Button(
                    parent = self,
                    model = 'cube',
                    texture = r'assets\pics\icon_exclamationSmall.png',
                    color = color.white66,
                    highlight_color = color.black33,
                    scale = src[1],
                    z = -2,
                    position = src[2],
                    on_click = Func(self.show_msg, src[0], src[3])
                )  
    
    def show_msg(self, name, msg):
        descr = dedent(msg).strip()
        WP(
            parent=self,
            title='Facts: ' + name,
            scale_x=1.2,
            content=(Text(descr, line_height=1.5), Space(height=0.5)),
            z = -3, 
            popup=True,
            enabled=True
        )


class Manual(Entity) :
    def __init__(self, parent=None, **kwargs):
        super().__init__(
            parent = parent, z=-2,
            **kwargs
        )
        self.enabled = False
        self.active = 0
        self.numSects = 4
        self.carousel = [
            Section(self, title="disasters", bg=r'assets\pics\manual\disaster.jpg', scale=.068),
            Section(self, title="diseases", bg=r'assets\pics\manual\diseases.jpg'),
            Section(self, title="economic", bg=r'assets\pics\manual\economic.jpg', scale=.065),
            Section(self, title="famine", bg=r'assets\pics\manual\famine.jpg', scale=.065)
            ]
 
        [Button(
            parent=self, model='cube', texture = "ship_A.png",
            color = color.white33, highlight_color = color.black33,
            scale=(0.1, 0.1), position = (arrow[0], 0, -2), rotation = Vec3(0, 0, arrow[1]),
            on_click=arrow[2]
        ) for arrow in[(-.6, -90, Func(self.slide, "left")), (.6, 90, Func(self.slide, "right"))]]
    
    def slide(self, dir="") :
        nxt = self.active + (1 if dir == "right" else -1)
        if nxt < 0 or nxt >= self.numSects:
            return
        self.carousel[self.active].disable()
        self.active = nxt
        self.carousel[self.active].enable()


    def enable(self) :
        print ("Enabled Manual..")
        self.enabled = True
        self.active = 0
        self.carousel[self.active].enable()
        
    def disable(self) :
        for c in self.carousel :
            c.disable()
        self.enabled = False


class News (Entity) :
    def __init__(self, parent=None, **kwargs):
        super().__init__(
            parent=parent, enabled=False, 
            scale=(1.25, 1.45), position=(0, 0.05), z=-2, **kwargs
            )

        self.set_scissor(Vec3(-.5,-.25,0), Vec3(.5,.25,0))
        
        self.base = Entity(
            parent=self, model='quad', 
            collider='box', visible_self=False)
        
        self.newspaper = Entity(
            parent=self.base, model='quad',
            text="newspaper here", texture=r"assets\pics\hokkaido\news_1.jpg"
        )

        self.inspect = Button(
            parent=self.base, text="More",
            position=(.06, -.36), scale=(.1, .05),
            on_click=None
        )
        
        self.base.add_script(Scrollable(min=-.3, max=.3))
        

    # def toggleSeaside(self) :
    #     self.base.disable()
    #     # Seaside().enable()

    def enable(self):
        self.enabled = True
        print("news enabled")

    