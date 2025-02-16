label timur_cp3:
    $ quick_menu = False

    scene black with dissolve
    centered "{size=+24}{color=#ffffff}Глава 3"
    $ quick_menu = True
    #фон комнаты без обоев
    if helpedWithRepair == False:
        #стандартная музыка - Chill
        play music chill
        "Утро прошло стандартно настолько, насколько может пройти утро в общежитии. Проснулся-потянулся, отправился умываться. Я хотел поспрашивать соседей о призраке, однако мои планы нарушил Тимур, загнав меня в магазин, чтобы докупить оставшиеся материалы и обои."

        "Очень не вовремя."

        #фон строительного магазина (hardware_store)
        scene bg_hardware_store with dissolve
        #нужен фоновый звук для строительного магазина
        "Тимур, будучи профессионалом, бегал от полки к полке, шустро закидывая в тележку всё необходимое. И, только когда мы подошли к отделу с обоями, процесс начал затягивать и меня."

        "Я разглядывал разноцветные рулоны, представляя, какой может стать наша комната. Взгляд упал на обои, которые, как мне казалось, подошли бы идеально. Но Тимур опередил меня и одной «левой», в прямом и переносном смысле, закинул в тележку два рулона других обоев."

        #на диске в папке не вошло в игру (вроде) есть цг, где гг и Тимур спорят в строительном магазине. нам это надо
        scene cj_timur_argument with dissolve
        mc "Эй, а моё мнение тебя не интересует? Мне эти обои не нравятся!"

        t "И? Ты же у меня насчёт постера не спрашивал."

        "Я почувствовал злость, буквально закипал."

        mc "Тоже мне сравнил, маленький постер и обои на всю комнату."

        "Тимур, казалось, был готов разорваться от накатывающей злости."

        t "Забыл, из-за кого нам ремонт теперь нужно делать?"

        mc "А что я такого сделал? Это ведь ты во всём виноват!"
        #обратно фон строительного магазина
        scene bg_hardware_store with dissolve

        "Я ждал, пока злость Тимура достигнет предела, но он молчал. Молчал и смотрел на меня убийственным взглядом. Я нервничал. Всё же злой Тимур – не самое безопасное зрелище. В момент он выдохнул и отвел взгляд. Пронесло?"

        #спрайт Тимур немного раздраженный - зимняя одежда
        show timur angry winter at right2 with dissolve
        t "Ладно, давай так: обои берём мои, но клеить я их буду сам."

        #спрайт гг обычный - тоже зимний - помним о контексте событий!
        show mc normal winter at left2 with dissolve
        mc "Хорошо. Ты сам это предложил."

        #фон дорога к общежитию (день)
        scene bg_street_morning_winter with dissolve
        "До общежития мы шли молча, и, эта тишина даже резала мои уши. Тимур все покупки донёс бы и сам, но боль в ноге, как мне показалось, не позволяла этого."

        #фон комната без обоев (должна быть дневная вариация, но пока оставляем, как есть)
        scene bg_room_nowalls_day with dissolve
        "Стоило нам зайти в комнату, Тимур сразу же ушёл, ничего мне не сказав. Остаток дня я ходил по общаге и пытался что-то выяснить насчёт призрака, однако попытки мои остались безуспешны. Никто из попавшихся мне на глаза о нём не слышал."

        #тот же фон, но вечерняя вариация

        "Вечером вернулся Тимур и снова уткнулся в свой ноутбук. Вступать в коммуникацию не хотелось. Тимур просто продолжал копаться в ноутбуке. Мне же… Мне стало скучно, и я просто решил лечь спать."

        #фон пропадает с эффектом моргания и переходит в черноту, все звуки затихают
        scene black with dissolve
        stop music fadeout 1.0
        #небольшая пауза
        pause 1.0
        jump timur_bad_end

    else:
        #бодренько - Wholesome
        play music wholesome
        "Утро прошло стандартно настолько, насколько может пройти утро в общежитии. Проснулся-потянулся, отправился умываться."

        "Всё ещё не проснувшееся тело медленно передвигалось по комнате, словно я был роботом, чьё программное обеспечение ни разу не обновляли, как вдруг в незагрузившийся мозг поступил запрос от Тимура:"

        scene bg_room_nowalls with dissolve

        #спрайт гг обычный пижама
        show mc normal home at left2 with dissolve
        mc "Какие планы на сегодня?"

        #спрайт Тимур обычный пижама
        show timur normal home at right2 with dissolve
        t "Нужно в строительный магазин сходить."

        "Собрались мы достаточно быстро и вышли из общежития в хорошем настроении."

        #фон строительного магазина
        scene bg_hardware_store with dissolve

        "В магазине я шёл рядом с Тимуром, слушая его рассказы о его семье. За забавными рассказами о сёстрах моего соседа я и не заметил, как тележка заполнилась необходимыми товарами. Оставались только обои."

        "Я рассматривал стеллажи с рулонами и нашёл, как мне казалось, самый лучший вариант. Я хотел окликнуть Тимура, но заметил, что в тележке уже лежат рулоны других обоев."

        #спрайт гг удивленный зимняя одежда
        show mc surprise winter at left2 with dissolve
        mc "Тимур, что это?"

        #спрайт Тимур обычный зимняя одежда
        show timur normal winter at right2 with dissolve
        t "Обои."

        ##спрайт гг обычный зимняя одежда
        show mc normal winter at left2 with dissolve
        mc "Я вижу, что обои, но почему ты меня даже не спросил?"

        t "Так мы же вроде вчера решили, какие будем брать."

        mc "Ты серьезно взял обои под цвет карточек?!"

        t "Ну да."

        "И он замолчал, видимо поняв, что наши вчерашние приколы сегодня уже неактуальны. Кажется он немного смутился."

        t "М-да… Неловко вышло. А ты какие хотел?"

        "Я указал на те, что мне понравились."

        t "Эти обои не подходят. У них качество не очень. Я хорошие выбрал… Ну, по качеству."

        #спрайт гг возмущённый зимний  Игорь - его нет
        show mc normal winter at left2 with dissolve

        mc "Но мне они не нравятся!"

        "Тимур, кажется, начал заводиться, а потом посмотрел на ярко-красные обои в тележке и спокойно выдохнул:"

        t "Ладно, давай так. Мы подберём обои, которые устроят нас обоих. Ты, соответственно, выберешь цвет, а я отвечаю за качество. По рукам?"

        show mc normal winter at left2 with dissolve

        mc "По рукам."

        t "Отлично."

        scene bg_hardware_store with dissolve
        "В конечном итоге, обои мы всё же выбрали. Вроде бы хорошего качества, вроде бы приятного цвета. Да, они были не тем, чего мы оба изначально хотели, но это был компромисс, который говорил о том, что нам с Тимуром станет легче жить друг с другом."

        "Всё же договариваться без скандала мы уже научились."

        scene bg_street_morning_winter with dissolve
        "Выйдя из магазина, мы направились в сторону общежития. Тимур хотел нести всё сам, но я не мог ему это позволить. А он, собственно, и не возражал."

        #фон комната без обоев (должна быть дневная вариация, но пока оставляем, как есть)
        scene bg_room_nowalls_day with dissolve
        "Зайдя в комнату, Тимур тут же начал собираться, чтобы снова уйти."

        show timur normal winter at right2 with dissolve
        t "Слушай, мне уже бежать пора. Обои завтра поклею."

        show mc smile winter at left2 with dissolve
        mc "Хорошо. Успехов на работе!"

        hide timur normal winter with dissolve
        hide mc normal winter with dissolve
        "Тимур улыбнулся мне в ответ и ушёл. А я остался один."

        #возможно, затемнение, небольшая пауза и переход к ночному варианту фона без обоев (когда будет готов)
        scene black with dissolve
        pause 1.0
        scene bg_room_repair_night with dissolve
        stop music fadeout 1.0
        play background room
        "Весь оставшийся день прошёл как в тумане. Я прошёлся по общаге. На кухне меня даже угостила печеньем милая рыжая девушка, которую, кажется, звали Женя."

        "Вечером вернулся Тимур, и мы снова вместе пили чай и болтали, решив сделать это обязательным вечерним ритуалом. Однако сосед показался мне грустным и даже задумчивым."

        "Я не сдержался и спросил:"
        show mc normal home at left2 with dissolve

        mc "Что-то случилось?"
        play music sadness fadein 1.0

        show timur normal home at right2 with dissolve
        t "Да вроде нет. За пару часов, что меня не было, ничего особо не поменялось."

        mc "Просто, мне кажется, у тебя в жизни что-то не ладится."

        t "У всех студентов жизнь не ладится."

        mc "Да, но…"

        t "Прости, я не намерен обсуждать свои проблемы."

        mc "Не намерен со мной? Или не намерен в принципе?"

        t "Ни с кем."
        show mc smile homea at left2 with dissolve

        mc "Знаешь, иногда, чтобы стало легче, нужно выговориться."

        show timur sad homea at right2 with dissolve

        "Тимур замолчал и, кажется, глубоко задумался."

        mc "Необязательно мне. Можно сходить к психологу… как вариант."

        "Тимур снова промолчал."

        mc "Я могу сходить с тобой для моральной поддержки."

        t "Я подумаю."

        "Кажется, я помог ему встать на путь решения его ментальных проблем."

        mc "Давай спать. Кажется, завтра у нас трудный день."

        show timur smile homea at right2 with dissolve
        t "Да, по койкам!"
        hide timur smile homea at right2 with dissolve
        hide mc smile homea at left2 with dissolve
        pause 1.0

        "Пожелав друг другу спокойной ночи, мы уложились в кровати."

        "Я закрыл глаза и тут же погрузился в царство Морфея."

        scene black with off
        #небольшая пауза
        stop music fadeout 1.0
        pause 1.0
        #утренняя комната без обоев (когда появится), пока оставляем, какой уже есть - ночной
        scene bg_room_nowalls_morning with dissolve
        #звуки затихают

    if relate_timur < 20:
        "Утром, открыв глаза, я не обнаружил своего соседа в комнате, но заметил записку, лежавшую на столе. В ней было написано: «Мне надо уехать, клей обои сам, а то скоро дисциплинарка» и подпись «Тимур»."

        "Моему возмущению не было предела. Мало того, что мы купили эти ужасные обои, так ещё и сосед наверняка меня обманул. Наверняка гуляет с кем-то, а мне ещё с этими полотнищами мучаться."

        "Ну уж нет… У меня есть свои планы. Нужно продолжить расследование про призрака."

        "Похожу по общаге. Наверняка кто-то что-то, да знает. Раз уж призрак общажный, значит, он студент."

        "Я хотел было взять свой рюкзак, но нигде не мог его найти, как вдруг заметил его в куче с вещами Тимура. Видимо, он случайно положил рюкзак к себе, когда убирал вещи."

        "Пока я разгребал вещи Тимура, передо мной неожиданно оказался завёрнутый листок. Любопытство взяло верх. Развернув бумажку, я понял, что это фотография."

        play sound bumaga
        scene cj_photo with dissolve

        play music EvaMemories fadein 1.0

        "На ней был Тимур и ещё несколько человек, а на фоне красовалось слово 	«Посвят» и год 	«2023». Я хотел отложить фото, но тут вгляделся в лицо девушки рядом с Тимуром."

        "Это же она! Это тот призрак!"

        "Я был в шоке. Оказалось, что человек с ответами был прямо под моим носом. Осталось только дождаться его, если он вообще захочет говорить со мной…"

        scene bg_room_nowalls with dissolve
        "Я посмотрел на стены и понял, что всё-таки надо поклеить обои. Может, тогда он заговорит."

        #здесь должна быть мини-игра с неровными обоями, но мы её встроим потом, но на ней музыка уже не играет, только эмбиент комнаты
        stop music fadeout 1.0

        "Весь день я клеил эти чёртовы обои. Где-то они отклеивались, где-то наслаивались. У меня уже не оставалось сил."

        "В конечном итоге я махнул рукой и лёг спать."

        #фон комнаты уже с обоями исчезает с эффектом моргания и сменяется на чёрный фон
        scene black with off
        #небольшая пауза
        pause 0.5
        stop music fadeout 2.0
        stop background fadeout 2.0

        "Однако во сне призрак девушки вновь явился ко мне."

        "Она смотрела на меня самым что ни на есть суровым, холодно-осуждающим взглядом. Стоя в полной темноте, она погрозила мне пальцем, словно маленькому ребёнку."
        pause 1.0
        jump timur_bad_end
    else:
        play background room fadein 1.0
        scene bg_room_repair_night with dissolve
        "Утром, открыв глаза, я не обнаружил своего соседа в комнате, но, включив телефон я увидел сообщение от Тимура."
        nvl_narrator "{size=+8}{color=#000000}Тимур"

        t_nvl "Привет. Извини, мне срочно нужно уехать домой. Поклей обои без меня, а то скоро дисциплинарка."
        mc_nvl "Хорошо"

        nvl clear

        play background room fadein 1.0

        "Я испуганно осмотрел стены: как же мне справиться без Тимура? Но, взяв себя в руки, я решил начать."

        "Я достал из пакетов обои и остальные материалы. Мой взгляд упал на кровать Тимура. На ней лежал его блокнот, раскрытый блокнот. Глаз случайно упал на написанное на бумаге."

        scene cj_notebook with dissolve

        "Расписание Тимура…"

        "Я понял, что Тимур был на работе, как и в многие другие дни, когда он исчезал и возвращался только вечером. Мне стало его жаль, и я решительно настроился на поклейку обоев."

        #здесь должна быть мини-игра с ровными обоями
        #после игры фон вечерней комнаты, обои уже поклеены. Музыка - Home
        scene black with dissolve
        pause 2.0
        play music home fadein 1.0
        scene bg_room_after_repair with dissolve

        "Весь день я клеил обои, стараясь как можно аккуратнее. Мне действительно очень помогли советы, которые недавно давал мне Тимур. Я не хотел подвести друга и пытался сделать всё в лучшем виде."

        "Вечером, когда я лег спать, мне снова приснилась та девушка. Она стояла в комнате, полной света, улыбаясь мне и будто благодаря за что-то. Интересно за что?"

        scene black with dissolve
        stop music fadeout 2.0
        stop background fadeout 2.0
        pause 1.0

        jump timur_good_end
