from ursina import *
from modified_api.Convo import Conversation
from _config import *
from modified_api.wp import WP

from Sudan import Options

class Section(Entity) :
    def __init__(self, parent=None, title="", **kwargs):
        super().__init__(parent=parent, **kwargs)
        self.title = title
        self.background = Sprite(
            r'assets\pics\parchmentFolded.png', parent=self, scale=.2, color=color.light_gray, z=-1
        )
        self.enabled = False

        self.add_entities()
    
    def add_entities(self):
        # if self.title in manual_btns.keys:
        self.header = Text(VIRUS_info[self.title][0], scale=1.2, parent=self, x=-.2, y=.3, z=-2)
        self.symptoms = Text(dedent(VIRUS_info[self.title][1]).strip(), parent=self, x=-.55, z=-2, y=.2, line_height=1.5)
        self.when = Text(dedent(VIRUS_info[self.title][2]).strip(), parent=self, z=-2, x=-.55, y=.0, 
            line_height=1.5, background=color.dark_gray)

class Task(Entity) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enabled = False
        self.background = Sprite(
            r'assets\pics\amazon\task.jpg', parent=self, scale=.1, color=color.light_gray, z=-2.5
        )

class Amazon(Entity) :
    def __init__(self, parent=None, **kwargs):
        super().__init__(
            parent = parent, z=-2,
            **kwargs
        )
        self.enabled = False
        self.active = 0
        self.numSects = 4
        self.stage = 0
        self.convo = Conversation(parent=self)
        self.carousel = [
            Section(self, title="hepatitis_a"),
            Section(self, title="west_nile"),
            Section(self, title="lyme"),
            Section(self, title="cfp"),
            ]
        self.task_btn = Button(
            parent = self,
            model = 'cube',
            texture = r'assets\pics\icon_exclamationSmall.png',
            color = color.white66,
            highlight_color = color.black33,
            scale = .2,
            z = -2,
            position = (-.5, .3),
            on_click = Func(self.showTask)
        )  
        self.task = Task(parent=self)
 
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
        self.convo.start_conversation(
            '\n'.join(open(r'scripts\amazon_trailer.txt').readlines())
        )

    def enable(self) :
        print ("Nav to Sudan..")
        self.enabled = True
        self.active = 0
        if self.stage == 0 :
            self.trailer()
    
    def showTask(self) :
        # self.carousel.disable()
        self.task.enabled = True
 
    def update(self) :
        if self.convo.enabled == False:
            self.carousel[self.active].enable()

    def input(self, key) :
        if key == 'space' and self.task.enabled == True:
            self.task.disable()
            # self.carousel.enable()
        
    def disable(self) :
        for c in self.carousel :
            c.disable()
        self.enabled = False