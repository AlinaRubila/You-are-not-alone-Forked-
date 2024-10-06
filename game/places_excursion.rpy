label Canteen:

    #Музыка ритмичная, спокойная, средняя по звучанию

    stop music
    stop background

    play sound steps

    play background room

    scene black with dissolve

    scene bg_uni_day with dissolve

    show mc normala at left2 with dissolve

    mc "С моими навыками готовки, мне стоит ближе познакомиться со столовой."

    show jenya smilea at right2 with dissolve

    j "Что, все настолько плохо?"

    show mc talk crosseda at left2 with dissolve

    mc "Увы, да. Я однажды даже случайно спалил кухню. Но можешь считать, что я просто любитель вел-дан."

    hide mc talk crosseda with dissolve
    hide jenya smilea with dissolve

    n "Мы шли по бесчисленныму количеству и переплетений лестниц и их пролётов, заходили в, на первый взгляд, заброшенные части корпуса, проносились мимо полупустых аудиторий, будто бы я нахожусь в Хогвартсе. Но Женя как охотничья ищейка, стремительно и неумолимо неслась к столовой."

    "Я надеялся, что я почувствую приближение нашего конечного пункта своим носом. Почувствую запах супов, бутербродов с сервелатом, пюрешки с котлетками и подливом, и дешевого чая с тонной сахара."

    "Но всё это осталось где-то там. В той самой школьной столовке."

    scene black with dissolve

    scene bg_canteen with dissolve

    play music evening
    play background people

    "Университетская столовая была, как и взрослая жизнь, более холодной. За столами сидели не то подростки, не то взрослые. Сидели и что-то задумчиво писали в ноутбуках, попивая латте на кокосовом молоке."

    "Кухня была закрыта. Нельзя увидеть весь процесс готовки. Основным блюдом были сэндвичи спорного содержания, но были и салаты, и даже паста с морепродуктами."

    "А цены на эти сэндвичи, Боже мой! Мамы готовят детям бутерброды мало того, что дешевле, так ещё и вкуснее. Вся еда, что делают с любовью, вкуснее. Любви я тут не почувствовал, но Женя сказала…"

    show jenya normala at right2 with dissolve

    j "Ну, столовка, в принципе, нормальная, готовят вкусно. Иногда кто-то из студентов помогает поварам, и им за это разрешают выносить еду с собой. "

    j "Но я готовлю сама  в общаге, получается довольно вкусно."

    show mc smile crosseda at left2 with dissolve

    mc "Напрашиваешься на комплимент?"

    show jenya smilea at right2 with dissolve
    j "Возможно."

    if skolko_mest_na_excursion < 3:
        show jenya normala at right2 with dissolve
        j "Куда пойдём дальше?"
    jump ChoiceExcursion

label Park:

    show mc normala at left2 with dissolve

    mc "Я даже не обратил внимания, что рядом есть парк. Хотелось бы взглянуть."

    show jenya normala at right2 with dissolve

    j "Моё любимое место!"

    stop music fadeout 2.0
    stop background
    scene black with dissolve
    play sound steps
    pause 1
    play background park
    scene bg_park_winter with dissolve

    "Обнаружение новых парков в жилых районах это всегда как маленький праздник. Они отличаются от больших парков вроде Измайловского или Зарядья. "

    "Сюда ходят жители местных домов, самые обычные семьи. Туристы о таких парках никогда не узнают. Как и многие, между прочим, жители Москвы."

    "И я о нём мог не узнать, чего греха таить. Этот парк был сонливый, медлительный, и именно в этом он был великолепен."

    show jenya normal wintera at right2 with dissolve

    j "Ну, это обычный парк, но мне тут очень нравится, особенно осенью. Тут даже специально стоят столики для студентов, поэтому я иногда делаю тут домашку. А закат здесь просто закачаешься."

    if skolko_mest_na_excursion < 3:
        j "Куда пойдём дальше?"

    jump ChoiceExcursion

label Library:

    #Музыка очень тихая и очень спокойная
    show mc normala at left2 with dissolve
    show jenya normala at right2 with dissolve

    mc "Думаю, библиотека мне однажды может пригодиться."

    j "Возможно."

    hide mc normala at left2 with dissolve
    hide jenya normala at right2 with dissolve
    stop music
    stop background

    scene black with dissolve
    play sound steps
    pause 1
    play music chill
    scene bg_library with dissolve

    n "Библиотека была далека от Александрийской. Тут и там стояли кожаные пустующие диванчики, забитые различной (в основном профессиональной) литературой шкафы, и самое главное - почти никого нет."

    "В одной из комнат в углу сидел парень с ноутбуком и что-то печатал. В другой еле выглядывали из-за стола чьи-то светлые волосы. Это была библиотекарь, глубоко погруженная в рутинную работу за компьютером."

    "Также туда-сюда ходил мужчина преклонного возраста, который будто бы впитал в себя и в свою внешность всю тоску, тишину, но в то же время и мудрость этого места. А может быть, он её источал."

    "Вот эти три человека и мы с Женей - это абсолютно все, кто сейчас здесь находился. {w} Хотя, вру. Здесь, помимо нас, навсегда остались жить: Достоевский, Тургенев, Пушкин, Лермонтов, Ганди…"

    "Ну, если не навсегда, то, по крайней мере, до тех пор, пока кто-то любознательный не заберёт их книгу и не забудет вернуть. А такое случится. Непременно."

    show jenya thoughtfula at right2 with dissolve

    j "Если будешь мил с библиотекаршей, то она может подсказать много интересного, а ещё она ужасная сплетница. Сюда я хожу не часто, но порой хочется побыть в тишине."

    n "В глазах Жени промелькнула тоска. Даже такому яркому и весёлому человеку, кажется, было от чего прятаться в тишине библиотеки."

    show jenya normala at right2 with dissolve

    if skolko_mest_na_excursion < 3:
        j "Куда пойдём дальше?"

    jump ChoiceExcursion
