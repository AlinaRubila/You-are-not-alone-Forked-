# Начало первой главы рута Жени

#Переменные этого рута

define cookie = False
define eda = False
define excursion = False
define favorite_food = False #для 3 главы
define skolko_mest_na_excursion = 0
define visitCanteen = True
define visitPark = True
define visitLibrary = True
define askJenya = False
define askTimur = False
define askAlex = False
define askMargo = False
define askedJenya = False
define askedTimur = False
define askedAlex = False
define askedMargo = False
define askedPerson = 0

#Выбор печенья

image bg_classroom = "bg/bg_classroom.jpg"
image bg_street_d = "bg/bg_street_day.jpg"
image cookieCG = "coockieChoice/cg_cookie.jpg"
image cookieYes = "coockieChoice/cg_yescookie.jpg"
image cookieNo = "coockieChoice/cg_nocookie.jpg"


image bg_classroom_blur = im.Blur("bg/bg_rutnoeve.jpg", 1.5)

screen cookieChoice():
    imagebutton:
        xalign 0.600
        yalign 0.676
        auto "images/coockieChoice/cookie_button_%s.png" focus_mask True action [SetVariable("cookie", True), Return(value=None)]
    imagebutton:
        xalign 0.053
        yalign 0.22
        auto "images/coockieChoice/lid_button_%s.png" focus_mask True action [Return(value=None)]

screen guyChoice():
    if askJenya == False:
        imagebutton:
            xalign 0.5189
            yalign 0.411
            auto "images/rutChoice/jenya_button_%s.png" focus_mask True action [Jump("aJenya"), Return(value=None)]
    if askAlex == False:
        imagebutton:
            xalign 0.7889
            yalign 0.825
            auto "images/rutChoice/alex_button_%s.png" focus_mask True action [Jump("aAlex"), Return(value=None)]
    if askTimur == False:
        imagebutton:
            xalign 0.914
            yalign 0.563
            auto "images/rutChoice/timur_button_%s.png" focus_mask True action [Jump("aTimur"), Return(value=None)]
    if askMargo == False:
        imagebutton:
            xalign 0.0895
            yalign 0.357
            auto "images/rutChoice/margo_button_%s.png" focus_mask True action [Jump("aMargo"), Return(value=None)]

label jenya_cp1:
    $ save_name = _("Глава 1. Женя")
    if persistent.ending1 and persistent.ending122:
        scene bg_rut
    else:
        scene bg_rutnoeve

    "Она выглядит дружелюбной."

    "Я направился к рыжеволосой девушке."

    "Она что-то рассматривала в окне. Не знаю, что именно привлекло её внимание, но своим внезапным появлением я её отвлёк."

    "На меня смотрели яркие зелёные глаза, в них горел какой-то задорный огонёк, что не могло не заинтересовать."

    scene cj_meet_jenya with dissolve

    stop background fadeout 2.0
    play music cozy

    mc "Привет. Не против, если подсяду?"

    scene cj_meet_jenya_smile with dissolve

    un "Привет! Садись, конечно!"

    scene cj_meet_jenya_smile with dissolve

    "Я скинул с себя куртку и положил на сиденье рядом с собой."

    j "Я тебя раньше не видела. Меня, кстати, Женя зовут."

    scene cj_meet_jenya with dissolve

    mc "А меня [mcname], приятно познакомиться!"

    scene cj_meet_jenya_smile with dissolve

    j "Взаимно!"

    scene cj_meet_jenya_smile with dissolve

    "Женя широко улыбнулась мне, и я понял, что сесть к ней было правильным выбором. Какая-то у неё позитивная энергетика, она сразу расположила меня к себе. Думаю, мы даже сможем подружиться."

    scene cj_meet_jenya_search with dissolve

    "Неожиданно Женя отвернулась и принялась копошиться в сумке."

    "Через мгновение я почувствовал приятный запах. Такой аромат у меня сразу ассоциируется с домашним теплом и уютом."

    j "Ой, хочешь печеньку?"

    scene cookieCG with dissolve

    "Я задумался."

    call screen cookieChoice
    if cookie:
        scene cookieYes with dissolve

        $ relate_jenya += 5

        mc "Спасибо большое."

        j "Да не за что!"

        "Из-за того, что опаздывал, не успел даже поесть."

        "Выглядит вкусно."

        "Я откусил печенье. Оно быстро таяло во рту, оставляя приятное шоколадное послевкусие."

        "Похожее печенье делала мне моя мама, я его просто обожал."

        "Выпечка была свежей: казалось, что её совсем недавно достали из духовки. Неужели Женя приготовила его сама?"

        "Я не заметил, как быстро съел угощение. Всё-таки отсутствие завтрака дало о себе знать."
        scene bg_classroom_blur with dissolve

    else:
        scene cookieNo with dissolve

        scene bg_classroom_blur with dissolve

        mc "Спасибо, но я откажусь"

        $ relate_jenya -= 5

        show jenya smilea at right2 with dissolve

        j "Значит, мне больше достанется"

        "Ай, ну я же сегодня ещё не ел."

        "В подтверждение моих мыслей у меня вновь заболел живот."

        "Наверное, мне стоило согласиться. И это печенье так аппетитно пахнет."

        "От мыслей о еде меня отвлекла моя новая знакомая."


    show jenya normal smilea at right2 with dissolve

    show mc normala at left2 with dissolve

    j "Слушай, я про стольких одногруппников успела узнать! Хочешь, расскажу?"

    mc "Давай."

    show jenya thoughtfula at right2 with dissolve

    j "Про кого ты хочешь узнать?"
    hide jenya thoughtfula at right2 with dissolve
    hide mc normala at left2 with dissolve
    scene bg_rutnoeve with dissolve

    #После выбора снова на фоне аудитория и спрайт Жени и гг
    #Если есть ещё про кого спросить, то снова появляется изображение с выбором
    call screen guyChoice
    label aJenya:
        if askJenya == False:
            scene bg_classroom_blur with dissolve
            show jenya smilea at right2 with dissolve
            show mc normala at left2 with dissolve

            j "Поживёшь — увидишь."

            show jenya blusha at right2 with dissolve

            n "Женя смущённо отводила взгляд, но по её улыбке я понял, что ей было приятно моё любопытство."
            hide jenya blusha at right2 with dissolve
            hide mc normala at left2 with dissolve

            scene bg_rutnoeve with dissolve

            $ askJenya = True
            $ askedPerson += 1
            if askedPerson <= 2:
                $ relate_jenya += 5
            if askedPerson < 4:
                call screen guyChoice
    label aAlex:
        if askAlex == False:
            scene bg_classroom_blur with dissolve
            show jenya grina at right2 with dissolve
            show mc normala at left2 with dissolve

            j "Многоуважаемый господин староста! Очень серьёзный человек. Думаю, со своими обязанностями он точно справляется."

            j "Говоря между нами, он душноватый. Не думаю, что мы с ним подружимся. Но прозвище «Шнурок» забавное. И как же он возмутился, когда я его так назвала!"

            n "Шнурок сидел на первом ряду и всем своим видом давал понять, что он здесь не ради шуточек и общения. Его светлые волосы были аккуратно зачёсаны назад, а одежда была идеально выглаженной и чистой."

            "Даже сейчас он что-то проверял в своих записях и недовольно поглядывал на болтающих парней сзади."
            hide jenya grina at right2 with dissolve
            hide mc normala at left2 with dissolve
            scene bg_rutnoeve with dissolve

            $ askAlex = True
            $ askedPerson += 1
            if askedPerson < 4:
                call screen guyChoice
    label aTimur:
        if askTimur == False:
            scene bg_classroom_blur with dissolve
            show jenya normala at right2 with dissolve
            show mc normala at left2 with dissolve

            j "Я пыталась заговорить с ним, но на всё получала односложные ответы. Лучше уж не говорить совсем, чем говорить так."

            j "Но, мне кажется, он этого и добивается. Хоть имя узнала — Тимур. В общем, какой-то он пугающий и мрачный…"

            n "Это же мой сосед в общаге. Ну, теперь хоть имя его знаю. Значит, он не только со мной такой необщительный."

            "Самое удивительное, что он пришёл в вуз раньше меня. И, как и во все наши предыдущие встречи, всё так же спал."

            "Хоть я и не мог разглядеть лица Тимура, всё равно можно было заметить помятый вид парня. Возможно, он, как и я, собирался впопыхах, но почему-то мне казалось, что он и не старался выглядеть иначе."

            hide jenya normala at right2 with dissolve
            hide mc normala at left2 with dissolve
            scene bg_rutnoeve with dissolve
            $ askTimur = True
            $ askedPerson += 1
            if askedPerson < 4:
                call screen guyChoice
    label aMargo:
        if askMargo == False:
            scene bg_classroom_blur with dissolve
            show jenya smile at right2 with dissolve
            show mc normala at left2 with dissolve

            j "Такая забавная! Глаза сияют при виде Шнурка, а тот дурак дураком: вроде умный, а ничего не понимает."

            show jenya normala at right2 with dissolve
            n "И действительно, светловолосая девушка часто кидала смущённые взгляды на парня с первого ряда."

            "Но, кажется, его это волновало меньше всего. Или он просто не замечал?"
            hide jenya normala at right2 with dissolve
            hide mc normala at left2 with dissolve
            scene bg_rutnoeve with dissolve

            $ askMargo = True
            $ askedPerson += 1
            if askedPerson < 4:
                call screen guyChoice

    play sound door

    "И вот наконец-то в аудитории появляется преподаватель. Он, не извинившись за своё опоздание, вальяжно направился к своему месту."

    show jenya normala at right2 with dissolve

    j "Ну вот… я уж думала, пары сегодня не будет."

    show mc smile crosseda at left2

    mc "Наверное, препод, как и я, потерялся в этом корпусе."

    show jenya smilea at right2

    j "Ой, так давай я тебе после пар экскурсию проведу! Я тут всё знаю!"

    menu:

        "Согласиться":

            mc "Давай, а то я снова заблужусь, как сегодня."

            show jenya smilea at right2

            j "Будет весело!"

            n "С каким же светлым и улыбчивым человеком я познакомился! Я точно сделал правильный выбор. Интересно, у неё вообще бывает плохое настроение?"

            $ relate_jenya += 5
            hide jenya smilea
            hide mc normala

        "Отказаться":

            $ excursion = True

            mc "Прости, сегодня не смогу."

            show jenya angrya at right2

            j "Ну и ладно. Если снова потеряешься, то сам виноват."

            "В памяти всплыли бесконечные лабиринты коридоров. Возможно, я ещё пожалею о своём выборе."
            $ relate_jenya -= 5
            hide jenya angrya at right2
            hide mc normala

    show cj_mc_jenya with dissolve

    $ persistent.poster1 = True

    if cookie:
        "Следующая часть пары прошла незаметно. Мы с Женей болтали и ели печенье. Как оказалось, Женя сама испекла его."

    else:
        "Следующая часть пары прошла незаметно. Мы с Женей болтали о том о сём и совсем не слушали преподавателя."

    "Сегодня я испытал невероятной степени уровень страдания. Отсидел три пары."

    "Моим первым мучителем была преподаватель английского. Она была маленького роста, с забавным акцентом."

    "Существуют такие преподаватели, у которых будто бы раздвоение личности. На перемене они улыбаются тебе, смеются над твоими шутками, активно отвечают на вопросы."

    "Но, когда начинается пара, ты сразу оказываешься в ледяной пещере. Ты больше не друг, а совершенно чужой человек."

    "Возможно, это хорошо. Субординация, все дела. Но всё-таки это те ещё эмоциональные качели!"

    "Вторая пара была с печальным и уставшим преподом. Его глаза были наполнены какой-то тоской."

    "Материал он рассказывал очень отвлечённо, будто смотрел в пустоту."

    "Множество смешков было сделано в его сторону разной степени тяжести. Каждый посчитал своим долгом что-то да сказать у него за спиной."

    "Только спустя время мы узнали, что от него ушла жена. Сказать, что было неловко и стыдно — ничего не сказать."

    "Никто больше его не обзывал и не оскорблял."

    "Третья пара была с преподавательницей, которая имела в себе черты препода по английскому. Но если на первой паре мы столкнулись с дилетантской сменой характера, то тут была профессиональная изобретательность."

    "Она улыбалась, шутила, кидала комплименты направо и налево во время пары."

    "Но вместе с тем, когда ей что-то не нравилось, было видно, что она может ругать с той же силой, что и хвалить."

    "Это была ювелирная работа кнута и пряника. Съедобный кнут, ядовитый пряник. Наверное, это и есть верх педагогики."

    "Что касается самих пар, войти и втянуться в процесс, честно сказать, было тяжеловато. Не из-за сложности материала, а из-за противостояния весёлого окружающего мира и скучного мира знаний."

    scene cj_window with dissolve

    "За окном целый мир с птичками, берёзами, проезжающими машинами всех цветов радуги."

    "Школьники, несмотря на тяжесть рюкзаков, вприпрыжку бегут домой. А милые бабушки с собачками не спеша прогуливаются вдоль дороги. Только одно это целиком и полностью манило мой взгляд и мысли."

    "И не одного меня. Женя тоже глядела в окно и часто, я так думаю, даже пыталась угадать, на что конкретно я сейчас смотрю и о чём думаю."

    scene cj_mc_jenya with dissolve

    "На перерывах же я открывал для себя новый мир — её внутренний. Послушал о том, как она случайно сожгла заброшенный дом в 14 лет, о том, какой она сейчас сериал смотрит, и о том, в чём отличие хоррора от триллера."

    "Одна из одногруппниц даже вступила вместе с ней в дискуссию по этому поводу."

    "В конце концов, вместе мы выжили. Пожалуй, ходить на много тяжёлых пар стоит хотя бы ради чувства свободы перед открытием дверей на улицу в конце дня. Запах свободы ударяет в голову. И всё, на что ты смотрел из окна, теперь можешь потрогать руками."

    if excursion:

            #Музыка очень приглушенная

            scene bg_classroom with dissolve

            show jenya grina at right2 with dissolve
            show mc normala at left2 with dissolve

            j "Ну как тебе первый день?"

            show mc smile crosseda at left2

            mc "Довольно неплохо."

            j "Кстати, а где ты живёшь?"

            show mc normala at left2

            mc "В 3 общаге."

            show jenya smilea at right2 with dissolve

            j "Ой, так я тоже! Пошли вместе!"

            stop music fadeout 2.5
            play background city
            scene black with dissolve
            scene bg_street_night_winter with dissolve

            "Не дожидаясь моего ответа, Женя взяла меня под руку и повела в сторону общежития."

            "Что ж, первый день прошёл не так уж и плохо, как я думал поначалу…"

            pause 1
            scene black with dissolve

    if excursion == False:

        scene bg_classroom with dissolve
        show jenya smilea at right2 with dissolve
        show mc normala at left2 with dissolve

        j "Ну что, готов к экскурсии от непревзойденной меня?"

        show mc smile crosseda at left2

        mc "Конечно!"

        show jenya normala at right2 with dissolve

        hide screen scr_over
        hide screen scr_hider

        show jenya normala at right2 with dissolve
        j "Тогда куда первым делом направимся?"
        jump ChoiceExcursion

        label ChoiceExcursion:
            if skolko_mest_na_excursion < 3:
                menu:
                    "Столовая" if visitCanteen:
                        $ skolko_mest_na_excursion += 1
                        $ visitCanteen = False
                        jump Canteen #находится в скрипте places_excursion.rpy
                    "Парк" if visitPark:
                        $ visitPark = False
                        $ skolko_mest_na_excursion += 1
                        jump Park #находится в скрипте places_excursion.rpy
                    "Библиотека" if visitLibrary:
                        $ visitLibrary = False
                        $ skolko_mest_na_excursion += 1
                        jump Library #находится в скрипте places_excursion.rpy

        #Музыка спокойная, средняя по звучанию
        stop background
        stop music fadeout 2.0
        scene black with dissolve
        pause 1
        play background city
        play music sincerely
        scene cj_aftertalk with dissolve

        $ persistent.poster2 = True

        j "Ну, самое главное я тебе показала, можно и по домам. Ты, кстати, где живёшь?"

        mc "В 3 общаге."

        j "Ой, так я тоже! Пошли вместе!"

        "Не дожидаясь моего ответа, Женя взяла меня под руку и повела в сторону общежития."

        "Что ж, первый день прошёл не так уж и плохо, как я думал поначалу."

        "Даже успел познакомиться с одногруппницей. Может, оно и к лучшему..."

        pause 1

        scene black with dissolve

    stop background fadeout 1.0
    scene bg_room_evening with dissolve
    play sound door

    if persistent.jenya_meet != True:
        $ renpy.notify("В дневнике появилась новая запись!")
    $ persistent.jenya_meet = True

    "Домой я пришёл обессилевший, и поэтому сразу лёг спать."

    "Утро вечера мудренее..."
    stop music fadeout 2.0

    pause 1

    scene black with off

    play background wind fadein 3.0
    pause 1
    show snow1
    show snow2
    with dissolve

    un "Снова ты?"

    "Из темноты раздался уже знакомый голос. Казалось, что со мной говорила сама темнота."

    mc "Снова я. Я не знаю, как сюда попал."

    #Спрайт черный силуэт человека

    "За пеленой снегопада я разглядел приближающийся силуэт. Теперь я был точно уверен, что мой собеседник — девушка, но очертаний её лица мне было не разглядеть."

    "Я будто оказался в мире двойственностей. Мне было хорошо и легко, но в то же время тревожно и непонятно.{w} Мне было всё интересно, но и абсолютно всё равно."

    "Я был свободен, свободнее любой птицы в небе, но в то же время я был прикован к земле, к деревьям вокруг, к девушке, стоящей передо мной."

    "Мы с ней, казалось, были на одной волне, и это одновременно успокаивало меня и пугало, невероятно пугало."
    "Наконец она уничтожила тишину задумчивым…."

    un "Наверное, в парке сейчас так красиво…"

    if visitPark != True:

        mc "Да, там очень красиво."

    else:

        mc "Я там ещё не был."

        un "Тебе стоит туда сходить."

        #Спрайт черного силуэта

    "Между нами повисла холодная тишина, лишь ветер осмеливался её нарушить."

    "Возможно, если прислушаться, можно было услышать сообщение, которое он пытался передать."

    un "Жаль, я не увидела, как цветут яблони в парке."

    "Голос незнакомки всегда звучал неожиданно и резко. Словно холодная горсть снега, что внезапно попала за шиворот."

    mc "Что… что ты имеешь в виду?"

    #Спрайт черного силуэта

    un "Я…"

    play music ambulance

    "Её ответ был будто проигран задом наперёд. Но, что удивительно, я почти догадался, что она имеет в виду. Возможно, я бы понял, что она ответила, если бы не громкий звук сирены в моей голове."

    "Голову словно кто-то сжимал. Я надавил на свои виски, и вся двойственность кончилась. Осталась только боль. Жгучая, как удар скорпиона, и продолжительная, как свежее клеймо."

    "Я не слышал больше ничего, кроме этой сирены, постепенно погружаясь во тьму. И, чем темнее становилось вокруг, тем тише был звук сирены."

    stop music fadeout 2.0
    stop background
    hide snow1 with dissolve
    hide snow2 with dissolve
    scene black with off
    pause 1

    "И вот, когда я, казалось, достиг дна этой темноты, я проснулся, и цвет, что я видел, сменился на белый — цвет потолка моей комнаты в общаге."

    scene bg_room_morning_blur with onn
    play background room

    "Голова чуть болела, но, в целом, я чувствовал себя как обычно."

    scene bg_room_morning with dissolve #at pan

    "С трудом повернувшись, я посмотрел в окно на дорогу за общагой."

    scene cj_room_window with dissolve

    play sound ambulance2

    "Уборщик подметал мусор, мужчина в костюме шёл по своим, наверняка очень важным, делам, а за поворотом исчезала из виду машина скорой помощи с тем же звуком, что недавно, казалось бы, разрывал мою голову на несколько частей."

    "Жизнь идёт своим чередом. Я выдохнул и попытался поспать ещё раз, но, хоть убей, больше не хотелось."
    if persistent.jenya_dreamcontinue != True:
        $ renpy.notify("В дневнике появилась новая запись!")
    $ persistent.jenya_dreamcontinue = True

    "Забросив идею со сном, я решил хоть немного взбодриться и направился в ванную комнату."

    "Это решение показалось мне разумным, потому что во время школы этот метод всегда помогал мне растрястись и настроиться на нужный лад."

    play sound steps
    scene black with dissolve
    scene cj_nocockroach with dissolve

    play background shower fadein 1.0

    "Открыв кран, я несколько раз умыл лицо холодной водой. Она быстро взбодрила моё сознание и тело."

    "Вместе с утекающей водой исчезали и мысли о странном сне."

    "Теперь я был достаточно бодр, чтобы начать свой новый день!"

    #Скример таракана

    scene cj_cockroach_screamer1 at zoomin

    play sound screamer

    pause 1

    scene cj_cockroach_screamer2 at tremble

    pause 1

    "Какие же неожиданные гады! Какая мерзость! Неужели я когда-то смогу к этому привыкнуть?"

    scene cj_nocockroach with dissolve

    "И куда скрылся этот таракашка?"

    "Ой, фу, не важно. Надеюсь, он убежал и больше мы с ним не пересечемся."

    stop background
    play sound steps
    scene black with dissolve
    scene bg_room_morning with dissolve
    play background room

    "После я вернулся в комнату. Она вызывала у меня чувство комфорта, и я ощущал даже некий уют. Отсутствие учебных задач и откровенная лень поставили меня перед извечным выбором: чем же теперь заняться?.."

    menu:

        "Пойти на кухню":

            mc "Блин, я же ещё не ел… надо что-то сварганить. Жаль, что я не слушался маму, когда она пыталась научить меня готовить."

            "Благо моя комната недалеко от кухни."

            play music home
            scene black with dissolve
            scene bg_hallway_light with dissolve

            "Я прошёл через коридор общаги, уже ставший мне привычным, и вошёл в место, где будут готовиться мои «кулинарные шедевры»."

            scene bg_kitchen_evening with dissolve

            "Кухня была оснащена несколькими электроплитами, микроволновками, мойками для посуды и общими холодильниками."

            "Я взял свои продукты и подошёл к плите в надежде, что не испорчу еду, которую трудно было испортить."

            "У плиты стояла моя новая знакомая — Женя. От запаха еды у меня ещё больше разыгрался аппетит."

            show mc normal homea at left2 with dissolve

            mc "О, доброе утро."

            show jenya normal homea at right2 with dissolve

            j "Что-то ты неважно выглядишь, у тебя всё хорошо?"

            mc "Да не, всё нормально."

            n "Я решил, что пельменей будет достаточно для начала дня."

            "Открыв упаковку пельменей, я хотел было приступить к «чуду кулинарии», но…"

            show jenya surprise homea at right2 with dissolve

            j "Ты действительно будешь это есть?!"

            j "Сейчас же только утро, а ты пельмени есть собрался…"

            mc "Ну… ничего нормального всё равно нет, так что придётся есть это."

            show jenya angry homea at right2 with dissolve

            n "Не понимаю, чем это было вызвано, но выражение лица Жени резко сменилось. Оно приняло недоуменный и слегка осуждающий вид. Немного подумав, она подуспокоилась и спокойно спросила…"

            show jenya normal homea at right2 with dissolve

            j "Слушай, а какой у тебя номер комнаты?"

            mc "Ну 205, а тебе зачем?"

            mc "В гости хочешь заглянуть?"

            j "Да так…"

            mc "Ну ты это, заходи, если что. Всё равно с соседом нормально не поболтать."
            show jenya smile2 homea at right2 with dissolve

            j "Возьму на заметку."

            hide jenya smile2 homea at right2 with dissolve
            hide mc normal homea at left2 with dissolve

            "К этому моменту мой завтрак был готов. Однако блюдо определённо получилось съедобным. Это меня порадовало, и я принялся уплетать свой, по мнению Жени, «недозавтрак»."

            "Женя села рядом. Мы обсудили нашу учебу, поговорили о том, какой я безнадёжный повар, и о гирляндах, которыми Женя собралась завесить свою комнату."

            "Женя спросила меня о моих планах на день. Я же поинтересовался у неё насчёт дедлайнов по некоторым предметам. В общем, беседа вышла весьма забавная."

            "Когда мы закончили с едой и помыли за собой посуду, я направился в своё логово."

            "Поначалу я хотел проводить Женю до её комнаты, но она отказалась. Сказала, что у неё ещё есть дела на кухне."

            "Что ж, её право."

            $ relate_jenya += 5
            $ eda = True
            scene bg_room_morning with dissolve
            play background room

            stop music fadeout 2.5
        "Разобрать вещи":

            play music sincerely

            "Пора бы уже разобрать вещи из своего чемодана."

            "Я начал тихо раскладывать свои вещи, стараясь не шуметь, чтобы не мешать соседу, который до сих пор спал. Однако мои усилия, казалось, были напрасными, потому что из-за моих шевелений вещами шума было не избежать."

            show timur angry homea with dissolve

            t "Эй, ну ты можешь не шуметь с утра пораньше?!"

            "Мне было искренне стыдно перед ним. Нет ничего хуже, чем когда тебя будят ранним утром. Тем более, по сути, абсолютный незнакомец."

            hide timur angry homea with dissolve

            "В целом, я уже знаю дальнейшее развитие событий. Варианта всего два:"

            "В первом варианте мы становимся закадычными друзьями и живём будто братья. Второй вариант: мы остаёмся пассивными знакомыми."

            "Кажется, мои шумы были критическими — больше он не сомкнул глаз. Достал свои чёрные беспроводные наушники и стал что-то смотреть."

            "Краем глаза я заметил у него в телефоне фотографию Теда Банди. Видимо, он любит тру-крайм. В худшем случае Теда Банди. Прям в очень худшем случае."

            "Может, почитать википедию про какого-нибудь маньяка и попытаться найти с ним общий язык? Дожили. Хочу почитать про серийные убийства ради того, чтобы пообщаться с соседом по комнате."

            "За всё время моего пребывания здесь мы толком и не поговорили. Сказали друг другу всякие мелочи и всё."

            "С ним разговаривать — это как будто собственными руками вытаскивать из воды якорь. Ну, если якорь, конечно, состоит из пассивной агрессии, меланхоличной тяги к одиночеству и желанию выбить из меня все миллиард мыслей о том, как с ним заговорить."

            "А может, мне только так кажется, и он как шалтай-болтай. Бледный снаружи, золотой внутри."

            "Однако долго это продолжаться не может. Я не хочу быть просто знакомым. Мне нужно попробовать сломать лёд между нами любой ценой."

            "Может, мне стоит попробовать с ним поговорить? Как-никак нам ещё долго предстоит жить вместе."

            menu:
                "Поговорить":

                    show mc normal homea at left2 with dissolve
                    mc "Давай нормально познакомимся? Нам всё-таки с тобой несколько лет жить вместе. Откуда ты?"

                    "Молчание. Упорное, наглое молчание."

                    n "Он просто игнорирует меня. Даже не мычит. Он полностью окунулся в яркий мир какого-то аниме, что смотрел в своём телефоне."

                    "Я попытался ещё пару раз неловко что-то сказать. Даже с агрессией. Ничего не помогало. Я даже попытался узнать, что за аниме он смотрит, но он повернул экран так, чтобы я ничего не видел."

                    show mc normal homea at left2 with dissolve

                    "Уверен, он сейчас хочет быть как Робинзон Крузо. Один на острове. И я этого хочу."

                    "Возможно, что даже волейбольный мяч был бы лучшей компанией, чем мой сосед."

                    mc "Вот и поговорили."
                    hide mc normal homea at left2 with dissolve
                    "Заканчивать с разбором вещей из чемодана пришлось в полной тишине и с назойливым чувством вины, сидящим на спине. Я чувствовал, как на душе стало тяжелее после разговора с Тимуром."

                    "Ну и ладно. Чего я так переживаю? Не получилось наладить контакт сейчас, значит, получится потом. Когда-нибудь…"

                    "Однако с самым важным заданием на сегодня я справился – разобрал вещи."

                "Не разговаривать":

                    "Он снова не настроен на разговоры… Видимо, так и будем жить."

                    "Зачем я вообще переживаю по этому поводу? Многие так живут годами – не общаются, хотя живут вместе. И ничего… справляются."

                    "Ключевое слово «справляются»."

                    "Так или иначе, но со своими вещами я разобрался. Даже быстрее, чем я ожидал."
    stop music fadeout 2.5

    "Я снова оказался на перепутье под названием «Чем бы мне сейчас заняться?»"

    "Заданий по учёбе нет. Уборка виделась чем-то жутко энергозатратным. К сериалам и прочему досугу в последнее время я подостыл."

    "Так и выглядит взросление? Или оно приходит, когда у тебя, наоборот, нет свободной минуты для размышлений?"

    "Как бы то ни было, я не нашёл для себя ничего лучше, чем лечь ненадолго вздремнуть. Быть может, так этот день пройдёт быстрее, а в голову придёт какая-нибудь идея."

    "Однако сразу провалиться в сон не получилось. Я то отвлекался на звуки за окном, то вспоминал о незнакомке, что снилась мне сегодня ночью."

    "Признаться честно, меня пугала перспектива повторной встречи с ней. Почему она вообще мне снится? И кто она такая?"

    "И ведь странно то, что она начала мне сниться именно после переезда в общагу. Связано ли это как-то? А может, я просто навыдумывал всякого из-за стресса?"

    "Наверное, это покажет только время."
    stop background
    pause 2
    scene black with dissolve

    if eda:

        play sound stuk
        play background room fadein 0.5
        "Меня разбудил стук в дверь."

        "Кто бы это мог быть? Вроде бы я никаких гостей не ждал. Да и Тимур, кажется, собирался провести этот день в одиночестве."

        scene bg_room_dawn #at pan
        with dissolve

        "Может, коменда? Ладно, выбора нет."

        play sound door

        "За дверью никого не оказалось, но на полу лежала тарелка, обёрнутая в фольгу."

        play music sunshine fadein 1.0

        "Я полагал, что это какой-то розыгрыш, но когда открыл тарелку, то увидел там свежий завтрак."

        "Запах омлета с сыром и помидорами заполнял комнату. Кажется, даже Тимур оживился и поглядывал на меня."

        "Только один человек мог сделать для меня такой сюрприз — Женя."

        "Я почувствовал тепло и любовь от этого жеста и с удовольствием принялся за второй завтрак."

        if persistent.jenya_endchap1 != True:
            $ renpy.notify("В дневнике появилась новая запись!")
        $ persistent.jenya_endchap1 = True

        "В этот момент я понял, что познакомиться с Женей было самым верным решением."

    scene black with dissolve

    stop music fadeout 2.0
    stop background fadeout 1.0
    pause 1.0

    jump jenya_cp2
