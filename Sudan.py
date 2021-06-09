from ursina import *
from modified_api.Convo import Conversation
from _config import *
from modified_api.wp import WP

class Options(ButtonGroup) :
    def __init__(self, options=("YES", "NO"), max_selection=1, **kwargs):
        super().__init__(
            options=options, default=None, 
            min_selection=1, max_selection=max_selection, 
            world_x=-.4,
            origin_x=-.8,
            selected_color=color.olive,
            **kwargs)



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
        self.task =Button(
            parent = self,
            model = 'cube',
            texture = r'assets\pics\icon_exclamationLarge.png',
            color = color.white66,
            highlight_color = color.black33,
            scale = .1,
            z = -2,
            position = (.4, .4),
            on_click = Func(self.show_msg, self.title, SUDAN_tasks[self.title])
        )

    def show_msg(self, name, msg):
        print(name, msg)
        descr = dedent(msg[0]).strip()
        WP(
            parent=self,
            title='Task: ' + name,
            scale_x=1.2,
            content=(Text(descr, line_height=1.5), Options(parent=self, options=msg[1], max_selection=msg[2])),
            z = -3, 
            popup=True,
            enabled=True
        )


class SouthSudan(Entity) :
    def __init__(self, parent=None, **kwargs):
        super().__init__(
            parent = parent, z=-2,
            **kwargs
        )
        self.background = Sprite(
            r'assets\pics\sudan\with_bruce.jpg', 
            parent=self, scale=.1, color=color.light_gray, z=-2, enabled=False
        )
        self.enabled = False
        self.active = 0
        self.numSects = 3
        self.stage = 0
        self.convo = Conversation(parent=self, z=-2.5, y=-.1)
        self.carousel = [
            Section(self, title="landuse", bg=r'assets\pics\sudan\landuse.png', scale=.063, y=-.05),
            Section(self, title="constraints", bg=r'assets\pics\sudan\constraints.png', scale=.063, x=-.02, y=-.05),
            Section(self, title="potential", bg=r'assets\pics\sudan\potential.png', scale=.065, y=-.08),
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

    def trailer(self) :
        self.background.enable()
        self.convo.start_conversation(
            '\n'.join(open(r'scripts\sudan_trailer.txt').readlines())
        )

    def enable(self) :
        print ("Nav to Sudan..")
        self.enabled = True
        self.active = 0
        if self.stage == 0 :
            self.trailer()
    
    def update(self) :
        if self.convo.enabled == False:
            self.background.disable()
            self.carousel[self.active].enable()
        
    def disable(self) :
        for c in self.carousel :
            c.disable()
        self.enabled = False