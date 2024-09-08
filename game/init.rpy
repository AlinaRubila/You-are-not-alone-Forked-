# Персонажи

define mc = Character('[mcname]', ctc="ctc_atl", ctc_position="fixed", color="#51483f", image='mc', callback=name_callback, cb_name="mc")
define j = Character('Женя', ctc="ctc_atl", ctc_position="fixed", color="#51483f", image='jenya', callback=name_callback, cb_name="jenya")
define t = Character('Тимур', ctc="ctc_atl", ctc_position="fixed", color="#51483f", image='timur', callback=name_callback, cb_name="timur")
define a = Character('Александр', ctc="ctc_atl", ctc_position="fixed", color="#51483f", image='alex', callback=name_callback, cb_name="alex")
define e = Character('Ева', color="#51483f")
define un = Character('???', ctc="ctc_atl", ctc_position="fixed", color="#51483f")

#Теги для сообщений

define mc_nvl = Character("Я", kind=nvl, image="mcimage", callback=Phone_SendSound)
define j_nvl = Character("Женя Лис", kind=nvl, callback=Phone_ReceiveSound)
define a_nvl = Character("Староста", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#Теги для выделения спрайтов

define n = Character(callback=name_callback, cb_name=None)


image jenya normala = At('jenya normal', sprite_highlight('jenya'))
image jenya smilea = At('jenya smile', sprite_highlight('jenya'))
image jenya normal wintera = At('jenya normal winter', sprite_highlight('jenya'))
image jenya surprisea = At('jenya surprise', sprite_highlight('jenya'))
image jenya angrya = At('jenya angry', sprite_highlight('jenya'))
image jenya blusha = At('jenya blush', sprite_highlight('jenya'))
image jenya sada = At('jenya sad', sprite_highlight('jenya'))
image jenya normal smilea = At('jenya normal smile', sprite_highlight('jenya'))
image jenya angry wintera = At('jenya angry winter', sprite_highlight('jenya'))
image jenya blush wintera = At('jenya blush winter', sprite_highlight('jenya'))
image jenya grina = At('jenya grin', sprite_highlight('jenya'))
image jenya grin wintera = At('jenya grin winter', sprite_highlight('jenya'))
image jenya sad wintera = At('jenya sad winter', sprite_highlight('jenya'))
image jenya smile wintera = At('jenya smile winter', sprite_highlight('jenya'))
image jenya surprise wintera = At('jenya surprise winter', sprite_highlight('jenya'))
image jenya thoughtful wintera = At('jenya thoughtful winter', sprite_highlight('jenya'))
image jenya thoughtfula = At('jenya thoughtful', sprite_highlight('jenya'))
image jenya angry handsa = At('jenya angry hands', sprite_highlight('jenya'))
image jenya angry homea = At('jenya angry home', sprite_highlight('jenya'))
image jenya blush handsa = At('jenya blush hands', sprite_highlight('jenya'))
image jenya blush homea = At('jenya blush home', sprite_highlight('jenya'))
image jenya grin handsa = At('jenya grin hands', sprite_highlight('jenya'))
image jenya grin homea = At('jenya grin home', sprite_highlight('jenya'))
image jenya normal handsa = At('jenya normal hands', sprite_highlight('jenya'))
image jenya normal homea = At('jenya normal home', sprite_highlight('jenya'))
image jenya normal smile handsa = At('jenya normal smile hands', sprite_highlight('jenya'))
image jenya normal smile homea = At('jenya normal smile home', sprite_highlight('jenya'))
image jenya normal smile2 handsa = At('jenya normal smile2 hands', sprite_highlight('jenya'))
image jenya sad handsa = At('jenya sad hands', sprite_highlight('jenya'))
image jenya sad homea = At('jenya sad home', sprite_highlight('jenya'))
image jenya smile2 homea = At('jenya smile2 home', sprite_highlight('jenya'))
image jenya smile3 handsa = At('jenya smile3 hands', sprite_highlight('jenya'))
image jenya surprise handsa = At('jenya surprise hands', sprite_highlight('jenya'))
image jenya surprise homea = At('jenya surprise home', sprite_highlight('jenya'))
image jenya thoughtful handsa = At('jenya thoughtful hands', sprite_highlight('jenya'))
image jenya thoughtful homea = At('jenya thoughtful home', sprite_highlight('jenya'))
image jenya yawn homea = At('jenya yawn home', sprite_highlight('jenya'))
image jenya normal smile wintera = At('jenya normal smile winter', sprite_highlight('jenya'))


image mc normala = At('mc normal', sprite_highlight('mc'))
image mc smile crosseda = At('mc smile crossed', sprite_highlight('mc'))
image mc talk crosseda = At('mc talk crossed', sprite_highlight('mc'))
image mc normal wintera = At('mc normal winter', sprite_highlight('mc'))
image mc normal homea = At('mc normal home', sprite_highlight('mc'))
image mc normal handa = At('mc normal hand', sprite_highlight('mc'))
image mc angry crosseda = At('mc angry crossed', sprite_highlight('mc'))
image mc blush handa = At('mc blush hand', sprite_highlight('mc'))
image mc blush homea = At('mc blush home', sprite_highlight('mc'))
image mc blush wintera = At('mc blush winter', sprite_highlight('mc'))
image mc blusha = At('mc blush', sprite_highlight('mc'))
image mc normal homea = At('mc normal home', sprite_highlight('mc'))
image mc sad crosseda = At('mc sad crossed', sprite_highlight('mc'))
image mc sad handa = At('mc sad hand', sprite_highlight('mc'))
image mc sad homea = At('mc sad home', sprite_highlight('mc'))
image mc sad wintera = At('mc sad winter', sprite_highlight('mc'))
image mc sada = At('mc sad', sprite_highlight('mc'))
image mc smile handa = At('mc smile hand', sprite_highlight('mc'))
image mc smile homea = At('mc smile home', sprite_highlight('mc'))
image mc smile wintera = At('mc smile winter', sprite_highlight('mc'))
image mc smilea = At('mc smile', sprite_highlight('mc'))
image mc surprise handa = At('mc surprise hand', sprite_highlight('mc'))
image mc surprise homea = At('mc surprise home', sprite_highlight('mc'))
image mc surprise wintera = At('mc surprise winter', sprite_highlight('mc'))
image mc surprisea = At('mc surprise', sprite_highlight('mc'))
image mc thoughtful crosseda = At('mc thoughtful crossed', sprite_highlight('mc'))
image mc normal crosseda = At('mc normal crossed', sprite_highlight('mc'))


image timur normala = At('timur normal', sprite_highlight('timur'))
image timur angrya = At('timur angry', sprite_highlight('timur'))
image timur normal smilea = At('timur normal smile', sprite_highlight('timur'))
image timur sada = At('timur sad', sprite_highlight('timur'))
image timur smilea = At('timur smile', sprite_highlight('timur'))
image timur surprisea = At('timur surprise', sprite_highlight('timur'))
image timur thoughtfula = At('timur thoughtful', sprite_highlight('timur'))


image alex normala = At('alex normal', sprite_highlight('alex'))


# Музыка

define audio.city = "audio/music/first_dream.mp3"
define audio.snow = "audio/music/snowsteps.mp3"
define audio.base = "audio/Morning.ogg"
define audio.bumaga = "audio/perelist.mp3"
define audio.clock = "audio/signal.mp3"
define audio.steps = "audio/steps.mp3"
define audio.ambulance = "audio/ambulance.mp3"
define audio.shower = "audio/shower.mp3"
define audio.screamer = "audio/screamer.mp3"
define audio.room = "audio/room.mp3"
define audio.ambulance2 = "audio/ambulance2.mp3"
define audio.stuk = "audio/stuk.mp3"
define audio.evening = "audio/Past Sadness.mp3"
define audio.door = "audio/door.mp3"
define audio.wholesome = "audio/Wholesome.mp3"
define audio.cozy = "audio/Cozy.mp3"
define audio.park = "audio/park.mp3"
define audio.sincerely = "audio/Sincerely.mp3"
define audio.stamp = "audio/stamp.mp3"
define audio.bibika = "audio/bibika.mp3"
define audio.sadness = "audio/happy-sad.mp3"

# Переменные

init:
    $ right2 = Position (xalign=0.8, yalign=1.005)
    $ left2 = Position (xalign=0.2, yalign=1.005)

# Переменные отношений
default maxrelate = 100
default minrelate = 0

default relate_jenya = 0
default relate_timur = 0
default relate_alex = 0
default relate_eve = 0


#with moveoutleft\right
#with moveinleft\right
#with easeinleft
#with blinds
#with wipeleft
#with pushleft

# Код параллакса для главного меню
init 1 python:
    import pygame
    import math


    class TrackCursor(renpy.Displayable):

        def __init__(self, child, paramod, **kwargs):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)
            self.x = 0
            self.y = 0
            self.actual_x = 0
            self.actual_y = 0

            self.paramod = paramod
            self.last_st = 0



        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)
            minimum_speed = 0.5
            maximum_speed = 3
            speed = 1 + minimum_speed
            mouse_distance_x = min(maximum_speed, max(minimum_speed, (self.x - self.actual_x)))
            mouse_distance_y = (self.y - self.actual_y)
            if self.x is not None:
                st_change = st - self.last_st

                self.last_st = st
                self.actual_x = math.floor(self.actual_x + ((self.x - self.actual_x) * speed * (st_change )) * self.paramod)
                self.actual_y = math.floor(self.actual_y + ((self.y - self.actual_y) * speed * (st_change)) * self.paramod)


                if mouse_distance_y <= minimum_speed:
                    mouse_distance_y = minimum_speed
                elif mouse_distance_y >= maximum_speed:
                    mouse_distance_y = maximum_speed

                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.actual_x, self.actual_y))



            renpy.redraw(self, 0)
            return rv

        def event(self, ev, x, y, st):
            hover = ev.type == pygame.MOUSEMOTION
            click = ev.type == pygame.MOUSEBUTTONDOWN
            mousefocus = pygame.mouse.get_focused()
            if hover:

                if (x != self.x) or (y != self.y) or click:
                    self.x = -x /self.paramod
                    self.y = -y /self.paramod

# Код параллакса для игры
init 2 python:
    class MouseParallax(renpy.Displayable):
        def __init__(self,layer_info):
            super(renpy.Displayable,self).__init__()
            self.xoffset,self.yoffset=0.0,0.0
            self.sort_layer=sorted(layer_info,reverse=True)
            cflayer=[]
            masteryet=False
            for m,n in self.sort_layer:
                if(not masteryet)and(m<41):
                    cflayer.append("master")
                    masteryet=True
                cflayer.append(n)
            if not masteryet:
                cflayer.append("master")
            cflayer.extend(["transient","screens","overlay"])
            config.layers=cflayer
            config.overlay_functions.append(self.overlay)
            return
        def render(self,width,height,st,at):
            return renpy.Render(width,height)
        def parallax(self,m):
            func = renpy.curry(trans)(disp=self, m=m)
            return Transform(function=func)
        def overlay(self):
            ui.add(self)
            for m,n in self.sort_layer:
                renpy.layer_at_list([self.parallax(m)],n)
            return
        def event(self,ev,x,y,st):
            import pygame
            if ev.type==pygame.MOUSEMOTION:
                self.xoffset,self.yoffset=((float)(x)/(config.screen_width))-0.5,((float)(y)/(config.screen_height))-0.5
            return
    MouseParallax([(40,"farback"),(20,"back"),(-20,"front"),(-40,"inyourface")])

    def trans(d, st, at, disp=None, m=None):
        d.xoffset, d.yoffset = int(round(m*disp.xoffset)), int(round(m*disp.yoffset))
        return 0

# Код для галлереи
init 3 python:

    g = Gallery()

    g.locked_button = "images/posters/lock.png"

    g.button("poster1")
    g.condition("persistent.poster1")
    g.image("cj_mc_jenya")

    g.button("poster2")
    g.condition("persistent.poster2")
    g.image("cj_aftertalk")

    g.button("poster3")
    g.condition("persistent.poster3")
    g.image("cj_gift")

    g.button("poster4")
    g.condition("persistent.poster4")
    g.image("cj_eat_cake")

    g.button("poster5")
    g.condition("persistent.poster5")
    g.image("cj_goodbye")

    g.button("poster6")
    g.condition("persistent.poster6")
    g.image("cj_eat_cake")


transform tremble:
        alpha 1.0 xoffset 0
        choice:
            block:
                linear 0.05 xoffset 10
                linear 0.05 xoffset -10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
        choice:
            block:
                linear 0.05 xoffset -10
                linear 0.05 xoffset 10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
        linear 0.07 xoffset 0
