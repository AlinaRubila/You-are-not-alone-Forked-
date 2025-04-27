define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "Я" ##The name of the main character, used to place them on the screen
define Jenya = "Женя Лис"
define Alex = "Alexander"
define Timur = "Тимур"

init -1 python:
    phone_position_x = 0.3
    phone_position_y = 0.5

    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")
    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0


transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0


transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100


screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    vbox:
        ypos -30
        xsize 495
        for id_d, d in enumerate(dialogue):
            if d.who == None: # Narrator
                frame:
                    xsize 550
                    xpos -20
                    background Frame("phone_send_frame.png", 23,23,23,23)
                    text d.what:
                        xpos -335
                        ypos 0.0
                        xsize 350
                        text_align 0.5
                        italic True
                        size 22
                        slow_cps False
                        id d.what_id
                        if d.current:
                            at message_narrator
            else:
                if d.who == MC_Name:
                    $ message_frame = "phone_send_frame.png"
                else:
                    $ message_frame = "phone_received_frame.png"
                if previous_d_who == d.who:
                    null height 3
                else:
                    null height 12

                hbox:
                    if d.who == MC_Name:
                        box_reverse True
                        xpos 25

                    #If this is the first message of the character, show an icon
                    if previous_d_who != d.who:
                        if d.who == MC_Name:
                            $ message_icon = "phone_send_icon.png"
                        elif d.who == Jenya:
                            $ message_icon = "phone_received_icon_jenya.png"
                        elif d.who == Alex:
                            $ message_icon = "phone_received_icon_alex.png"
                        elif d.who == Timur:
                            $ message_icon = "phone_received_icon_timur.png"
                        else:
                            $ message_icon = "phone_received_icon.png"

                        add message_icon:
                            size (75,75)
                            yalign 0.25
                            if d.current:
                                at message_appear_icon()
                    else:
                        null width 75
                    null width 10
                    frame:
                        padding (20,10,20,15)
                        background Frame(message_frame, 23,23,23,23)

                        xsize 370
                        vbox:
                            spacing -10
                            if d.who != MC_Name and previous_d_who != d.who:
                                text d.who:
                                    ypos -10
                                    color "#5c5c5c"
                            elif d.who == MC_Name and previous_d_who != d.who:
                                text d.who:
                                    xpos 310
                                    ypos -10
                                    color "#5f5f5f"
                            if d.current:
                                if d.who == MC_Name:
                                    at message_appear(1)
                                else:
                                    at message_appear(-1)

                            text d.what:
                                pos (0,0)
                                xsize 360
                                slow_cps False


                                if d.who == MC_Name :
                                    color "#000000"
                                    text_align 1.0
                                    xpos -560
                                else:
                                    color "#000000"

                                id d.what_id
            $ previous_d_who = d.who

style phoneFrame is default

style phoneFrame_frame:
    background Transform("phone_background.png", xcenter=0.5,yalign=0.5)
    foreground Transform("phone_foreground.png", xcenter=0.5,yalign=0.5)

    ysize 815
    xsize 495

style phoneFrame_viewport:
    yfill True
    xfill False

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True
