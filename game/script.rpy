# Начало игры


init python:
    # все команды, после которых нужно прятать текстбокс в режиме auto
    # необязательная строка, просто бесит, когда пустой текстбокс на экране остается
    config.window_auto_hide = [ "pause", "hide", "show", "with", "scene", "call" ]
    renpy.music.register_channel("background", "sfx", loop=True)

    # автоматическое объявление всех спрайтов, включая webp
    # формат webp занимает гораздо меньше места, но при этом качество выше
    # функция находится в модуле 7dots.rpy, можно удалить эту строку вместе с файлом
    images_auto()

    # положение картинки зависит от курсора мыши
    def pan_f(trans, st, at):
        x, y = renpy.get_mouse_pos()

        # проверки на случай неправильного масштабирования окна с пустыми полями
        if x < 0:
            x = 0
        if x >= config.screen_width:
            x = config.screen_width - 1

        # определение относительных координат по горизонтали
        trans.xalign = x * 1. / config.screen_width
        return 0

init:
    # трансформ с нужной функцией
    transform pan:
        function pan_f
    transform zoomin:
        zoom 1 xpos 950 ypos 530 anchor(0.5, 0.5)
        linear 10 zoom 3


image bg_room_morning_blur = im.Blur("bg/bg_room_morning.jpg", 1.5)

init python:
    onn = ImageDissolve("eye.png", 1.0, 20, reverse=False)
    off = ImageDissolve("eye.png", 1.0, 20, reverse=True)

#Анимация снега
image splashbg = Color("#FBF0D9")
image snow1 = Fixed(SnowBlossom("gui/snow1.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))
image snow2 = Fixed(SnowBlossom("gui/snow2.png", 50, xspeed=(20, 50), yspeed=(100, 200), start=50))

#Анимация продолжения диалога
image ctc_atl:
    "gui/ctc.png",
    subpixel True
    yalign 0.93 xalign 0.5
    parallel:
        block:
            linear 2.0 alpha 1.0
            linear 1.0 alpha 0.3
            repeat

#Выбор подсаживания
screen rutChoice():
    imagebutton:
        xalign 0.5189
        yalign 0.411
        auto "images/rutChoice/jenya_button_%s.png" focus_mask True action [Jump("jenya_cp1")]
    imagebutton:
        xalign 0.7889
        yalign 0.825
        auto "images/rutChoice/alex_button_%s.png" focus_mask True action [Jump("alexander")]
    imagebutton:
        xalign 0.914
        yalign 0.563
        auto "images/rutChoice/timur_button_%s.png" focus_mask True action [Jump("timur")]

    if persistent.ending122:
        imagebutton:
            xalign 0.5798
            yalign 0.308
            auto "images/rutChoice/eve_button_%s.png" focus_mask True action [Jump("eve")]


init python:
    #список достижений (пока не трогаем, работает так себе)
    allAchievements = {"Печенька дружбы": "Печенька дружбы",
    "Исследователь университетов": "Исследователь университетов"}
    #функция добавления ачивок
    persistent.AddAchieve = []
    def AddAchieve(achieve):
        if not achieve in persistent.AddAchieve:
            persistent.AddAchieve.append(achieve)
            renpy.show_screen("notifyAchieve", achieve)
label start:

    play background wind fadein 1.0
    #Чёрный экран с анимацией падающего снега, на фоне звуки ветра.
    stop music fadeout 2.5
    $ set_quick_menu(False)
    scene black

    show snow1
    show snow2
    with dissolve
    pause 3

    $ quick_menu = True

    "Конец января."

    "Давно у меня не было возможности стоять и просто любоваться снежинками."

    "Они маленькие, совсем хрупкие, аккуратно садятся мне на нос, щёки, ресницы и тут же тают. От каждого этого мимолётного «поцелуя» зимы я ощущаю, как по спине бегут мурашки."

    play sound snow

    "Где-то в глубине непроглядной темноты я почувствовал чьё-то еле уловимое присутствие. Ну, как присутствие… Может ли кто-то «присутствовать» прямо в небе?"

    "В тот же миг мне показалось, что земля и небо поменялись местами, и это не снежинки падают мне на лицо, а я сам, как снежинка, падаю в холодный сугроб."

    play sound snow

    pause 2

    un "Кто ты такой?"

    "Около правого уха раздался незнакомый мне звонкий женский голос. Я сразу представил раскрасневшееся от холода лицо той девушки, которая решила подойти к такому странному человеку, как я. Я стоял на одном месте, как истукан."

    "Однако стоило мне только сделать усилие, чтобы повернуться, я внезапно ощутил, что никак не могу пошевелиться."

    "Тело настойчиво не хотело меня слушаться, и, только чтобы не показаться грубияном, я с усилием выпалил…"

    "Я…"

    play sound bumaga

    $ mcname = renpy.input("Ваше имя", length=8, default="", allow="йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ").strip()
    if mcname == "":
        $ mcname = "Антон"

    mc "Я [mcname]."

    mc "А ты кто?"

    "Я всё ещё не мог пошевелиться, мороз как будто цепями сковал моё тело, а девушка так и не спешила подойти и посмотреть мне в лицо."

    un "[mcname]… ты первый за долгое время, с кем я могу поговорить."

    un "Меня зовут…"

    stop background

    play sound clock

    scene black with off

    pause 1

    $ set_quick_menu(False)

    centered "{size=+24}{color=#ffffff}Стой, не уходи!"

    centered "{size=+24}{color=#ffffff}Не оставляй меня одну!"

    stop sound

    #объявление первой главы

    scene cj_chapter1 with dissolve

    pause 1

    play sound stamp

    scene cj_chapter12 at tremble
    with dissolve

    pause 3

    scene black with dissolve

    #начало игры

    scene bg_room_morning_blur with onn

    scene bg_room_morning #at pan
    with dissolve

    play sound room

    $ quick_menu = True

    mc "Стой! Я не расслышал! Как твоё имя? Что это за мелодия?"

    hide snow1
    hide snow2

    play music chill

    stop sound

    "Это мой будильник. А ведь всё было настолько реальным… Даже не верится, что это сон. И почему я так странно себя чувствую после этого?.."

    "Ну и приснится же такое…"

    if persistent.first_note != True:
        $ renpy.notify("В дневнике появилась новая запись!")
    $ persistent.first_note = True

    "Пора собираться, не хватало ещё в первый день опоздать. А то я уже на горьком опыте знаю, к чему это приводит."

    "Конечно, для меня это не самый первый день в универе. Но это первый день на пути к моей мечте! Прошлый семестр для меня был в тягость, специальность была не по мне. Зато теперь я точно знаю, в каком направлении двигаться!"

    "Отец был очень недоволен, когда я ушёл с юридического и поступил на it. Но я уверен, он поймет меня, ведь я наконец-то займусь интересующим меня делом."

    "С соседом надо бы нормально познакомиться. Какой-то он угрюмый… И в комнате было не убрано, когда я заезжал. Как ни приду, он спит. Может, он работает? И почему он не просыпается на пары, ведь уже пора? Но будить его я побаиваюсь…"

    "А сколько вообще времени?"

    "Я взял телефон с тумбочки. Сквозь трещины разбитого экрана я смог разглядеть цифры: 8:47."

    "Блин, в первый же день опаздываю!"

    "Я быстро привёл себя в порядок в ванной, собрал рюкзак, оделся и побежал по коридорам к выходу."

    play sound steps

    scene bg_post with dissolve

    "Живот неприятно скрутило."

    "На еду нет времени. В следующий раз заранее подумаю об этом и не буду опаздывать."

    "Под протесты желудка я выбежал на улицу."

    scene black with dissolve

    scene bg_street_morning_winter with dissolve

    play sound city

    "Зимний холодный воздух ударил мне в лицо, неприятно покалывая щёки. Дорога из общаги в университет была мне пока не знакома, но я осознавал, что ещё много раз побываю на ней."

    "Даже не могу определить, что я чувствую. Волнение, страх, неуверенность, сонливость, а может, голод? Всё это смешалось во мне и не давало покоя"

    "Вместе с проезжающими мимо меня машинами всё дальше уходили воспоминания о недавнем странном сне."

    "А аудитория-то какая?.. Я и не посмотрел."

    "Я залез в рюкзак рукой и, немного покопавшись там, достал телефон."

    nvl_narrator "{size=+8}{color=#000000}Айти и прочие радости жизни"
    mc_nvl "Ребят, какая у нас аудитория?"
    a_nvl "3305. Дай бог, чтобы ты вообще дошёл до неё..."
    j_nvl "Давай быстрее пока препод не пришёл!"
    mc_nvl "Понял, спасибо)"

    nvl clear

    play sound city

    "Так, кажется, аудитория 3305, а где это?.. "

    stop sound

    scene bg_hallway with dissolve

    hide bg_street_night_winter with dissolve

    "На первый взгляд, всё просто. Третий корпус, третий этаж, пятый кабинет. Но на деле трудности начались ещё на первом этапе."

    "Поиск третьего корпуса напоминал головоломку с лабиринтом. На месте были и указатели, ведущие в тупик, и развилки, ведущие в неизвестном направлении."

    "Лишь спустя десять минут я зашёл в нужное здание. Но на этом трудности не закончились."

    "Пролетев лестничные пролёты, я оказался в длинном коридоре."

    play sound steps

    scene bg_uni_morning with dissolve

    "Вдоль стен шла очередь одинаковых дверей, ведущих в аудитории. Но ни одна из них не вела в нужную мне."

    "Казалось, я попал в дом Винчестеров, только призраков здесь не было."

    scene bg_door with dissolve

    "Завернув за угол, я наткнулся на очередную дверь. На табличке сверху красовалось число: 3305."

    mc "Да неужели!"

    stop music fadeout 2.5

    play sound door

    play background people

    if persistent.ending1 and persistent.ending122:
        scene bg_rut with dissolve
    else:
        scene bg_rutnoeve with dissolve

    "Повезло, препод ещё не пришёл."

    "Нужно выбрать, с кем сесть."

    scene bg_rutscreen

call screen rutChoice
