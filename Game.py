from Sudan import SouthSudan
from Amazon import Amazon
from ursina import *
# from ursina.prefabs.conversation import *
from modified_api.Convo import Conversation
from Nav import Manual, News
from _config import *
from Plots import *

class Hook (Entity) :
    def __init__(self, enabled=False, **kwargs):
        super().__init__(enabled=False, **kwargs)
        # self.title = 'Welcome to Chrono'
        
        self.popup = False
        self.enabled = enabled
        self.finished = False

        self.resp = False
        self.c_src = open("start_convo.txt")
        self.convo = Conversation(parent=self)

    def enable(self) :
        self.enabled = True
        if self.convo.enabled :
            self.convo.start_conversation('\n'.join(self.c_src.readlines()))
        else :
            self.disable()
    
    def disable(self) :
        self.enabled = False
        
    def update(self):
        if not self.convo.enabled :
            self.finished = True
            self.disable()
            # self.parent.nav.enable()
            self.parent.set_mode("world_map", prompt=True)



class MapIcon(Button) :
    def __init__(
        self, parent=None, active=False, 
        scale=.13, z=-2.5, **kwargs):
        self.active = active
        super().__init__(
            parent=parent,
            scale=scale,
            highlight_color=color.black33,
            z=z,
            **kwargs
        )
        self.active = active

    # def flip_active(self) :
    #     self.active = not self.active
    #     self.color = color.orange if self.active else color.light_gray

class NavBar(Entity) :
    class NavIcon(Button) :
        def __init__(self, parent=None, active=False, name="", **kwargs):
            super().__init__(
                parent=parent,
                scale=(0.1, 0.05),
                highlight_color=color.black33,
                alpha=.4,
                # enabled=False,
                **kwargs
            )
            self.name = name
            self.active = active

        def flip_active(self) :
            self.active = not self.active
            print("nav_btn", self.name, self.active)
            self.color = color.salmon if self.active else color.light_gray
            self.alpha=.4

    def __init__(self, parent=None, **kwargs):
        super().__init__(
            parent=parent, visible_self=False, 
            z=-3, position=(.4, -.42), **kwargs
        )

        self.active = "world_map"
        self.show_manual = self.NavIcon( 
            self, name="world_map",
            # r'station_A.png',  
            text="Manual", 
            # position=(.65, -.42), z=-3,
            color=color.light_gray,
            # x=self.x + 0.4, y = self.y,
            x=.24,
            on_click=Sequence(Func(self.parent.set_mode, "manual"))
        )

        self.show_news = self.NavIcon(
            self,
            # r'assets\pics\icon_plusSmall.png', 
            text="News", 
            # position=(.45, -.42), z=-3,
            color=color.light_gray,
            # x=self.x + 0.2, y=self.y,
            x=.12,
            on_click=Func(self.parent.set_mode, "news")
        )

        self.show_world_map = self.NavIcon(
            self, name="world_map",
            # r'assets\pics\icon_plusSmall.png', 
            text="Map", 
            # active=True, 
            color=color.orange,
            active=True,
            # x=self.x, y=self.y,
            on_click=Func(self.parent.set_mode, "world_map")
        ) 
    
    def set_active(self, tag) :
        prev = getattr(self, "show_" + self.active)
        self.active = tag
        btn = getattr(self, "show_" + tag)
        if btn != None:
            btn.flip_active()
        if prev != None:
            prev.flip_active()


class ChallengeMap(Entity) :
    def __init__(self, enabled=False, **kwargs):
        super().__init__(**kwargs)
        self.enabled = enabled

        for ic in mapIcons :
            MapIcon(self, f'assets\map_ele\{ic[0]}_w.png', ic[3], text=ic[2], position=ic[1])

        self.background = Sprite(
            'assets\pics\parchmentAncient.png', 
            parent=self, scale=.2, color=color.dark_gray, z=-1
        )

    def enable(self) :
        print ("Enable Map..")
        self.enabled = True
    
    def disable(self) :
        self.enabled = False


class WorldMap(Entity) :
    def __init__(self, enabled=False, **kwargs):
        super().__init__(**kwargs)
        self.enabled = enabled
        
        for site in plot_sites.keys() :
            MapIcon(
                parent=self, model='circle', color=color.orange.tint(.4), alpha=.4, 
                position=plot_sites[site]["position"], text=site,
                on_click=Func(self.toggle_plot, plot_sites[site]["plot"])
            )

        self.background = Sprite(
            'assets\pics\world_map.png', 
            parent=self, scale=.065, alpha=.4, color=color.light_gray, z=-2,
        )

    
    def toggle_plot(self, plt):
        self.parent.set_mode(plt, isPlot=True)

    def enable(self) :
        print ("\nEnable WorldMap..\n")
        self.fade_in()
        self.enabled = True
    
    def disable(self) :
        self.enabled = False


class Game(Entity) :
    def __init__(self, enabled=False, **kwargs):
        super().__init__(**kwargs)
        self.popup = False
        self.enabled = enabled
        
        self.plots = [Seaside(self), SouthSudan(self), Amazon(self)]
        self.world_map = WorldMap(parent=self)
        self.hook = Hook (parent=self)
        self.challenge_map = ChallengeMap (parent=self)
        self.manual = Manual (parent=self)
        self.news = News(parent=self)
        self.convo = Conversation(parent=self, enabled=False, z=-3)
        self.mode = self.challenge_map
        self.last_mode = None

        self.nav = NavBar(parent=self)

        self.back_btn = Button(
            "Back", parent=self, scale=(0.1,0.05), color=rgb(50,50,50),
            position=(-0.66, 0.44, -2), z=-3,
            on_click=self.back
        )
    
    def enable(self) :
        self.enabled = True
        self.hook.enable()
    
    def set_mode(self, mode, isPlot=False, prompt=False) :
        if self.enabled == False:
            self.enabled = True

        if mode == None :
            return
        if self.mode != None :
            print("disable mode", self.mode.name)
            self.mode.disable()
        self.last_mode = self.mode.name
        if isPlot :
            self.mode = self.toggle_plot(mode)
        else :
            self.nav.set_active(mode)
            self.mode = getattr(self, mode)
        self.mode.enable()

        if prompt and mode in game_prompts.keys():
            print("prompt", mode)
            self.convo.enable()
            self.convo.start_conversation(game_prompts[mode])

        
    def toggle_plot(self, plt) :
        return self.plots[plt]
    
    def back(self) :
        self.set_mode(self.last_mode)
    
    def back_to_menu(self) :
        print ("back_to_menu")
        # self.map.disable()
        self.disable()
        self.parent.esc()


if __name__ == "__main__" :
    app = Ursina()
    window.fps_counter.enabled = False
    game = Game(enabled=True)

    app.run()