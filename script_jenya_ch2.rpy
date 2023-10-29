# Начало второй главы рута Жени

label jenya_cp2:

    "Начало второй главы."
    "Наступила зима. [mcname] рассказывает, что произошло за это время."
    "[mcname] идёт в вуз."
    "По пути [mcname] задумывается и чуть не попадает в аварию. Женя спасает его, оттянув за капюшон от дороги."
    "У Жени звонит телефон. Начинает говорить с родителями, и мы видим, что всё плачевно."
    "[mcname] замечает, что Женя что-то рисует. Затем она выбрасывает рисунок."
    menu:
        "Может, там что-то интересное?"
        "Полезть в мусорку":
            "[mcname] увидел свой портрет."
            $ relate_jenya += 5
        "Не лезть в мусорку":
            "И зачем ему лезть в чужую жизнь?"
    "[mcname] и Женя приходят на сбор, организованный Шнурком."
    menu:
        "Слушать":
            "[mcname] пожалел, что вообще согласился на это мероприятие."
        "Не слушать":
            "[mcname] замечает влюблённый взгляд одной из одногруппниц."
    "[mcname] и Женя идут в общагу и по пути разговаривают про снег в своих родных городах. Выясняется, что Женя с юга."
    "Ночью на него будет смотреть Ева."
    "[mcname] побежит за Евой и в результате окажется возле её комнаты."
    "Следующий день..."
    "[mcname] просыпается и обнаруживает открытую в комнату дверь. Чует с кухни какой-то запах."
    "Идёт на кухню и встречает там Женю."
    "Женя спрашивает про знак зодиака."
    menu:
        "Козерог":
            "О, козерог!"
        "Водолей":
            "Водолей - так водолей."
        "Рыбы":
            "Рыбы? Здорово..."
        "Овен":
            "Можно про друга-овена рассказать..."
        "Телец":
            "Хороший знак!"
        "Близнецы":
            "А где второй близнец?"
        "Рак":
            "Тоже неплохо!"
        "Лев":
            "Да ну?"
        "Дева":
            "Почему-то я догадывалась..."
        "Весы":
            "Есть в этом что-то."
        "Скорпион":
            "Опа, огненный знак!"
        "Стрелец":
            "Боже упаси!"
    "Женя предлагает пойти в парк."
    menu:
        "Согласиться?"
        "Да":
            $ relate_jenya += 5
            "[mcname] получит свой смешной портрет от Жени."
            "Возможно мини-игра."
            "[mcname] случайно забирает вещь у Жени и рассматривает её дома."
        "Нет":
            $ relate_jenya -= 10
            "[mcname] вспоминает про сон и идёт за Евой."
            "Он оказывается возле двери."
            menu:
                "Постучать":
                    "Скример глаз из-за двери."
            "[mcname] по ошибке получит какую-то книгу. Внутри неё - что-то значимое по типу номера телефона."
            "[mcname] рассматривает книгу у себя в комнате."
    "Ночью от сильного порыва ветра открывается окно. [mcname] встаёт, чтобы его закрыть."
    "Посреди пустой дороги он видит Еву, которая смотрит прямо ему в душу."
    "Утром пойдёт к комнате Жени"
    "Его встречает сонная Женя, но услышав про призрака быстро приводит себя в порядок"
    "Затягивает [mcname] в комнату, забывая про беспорядок"
    "[mcname] вызывается помочь Жени собрать вещи для гадания"
    "далее идет мини-игра в зависимости от баллов"
    if relate_jenya>relate_eve:
        "при гадании карты скажут что-то связанное с Женей"
        return
    if relate_eve>relate_jenya:
        "при гадании карты скажут что-то связанное с Eвой"
        return


    if relate_jenya>0:
        r "Женя даёт [mcname] оберег(с баночкой или камушком)"
        return
    if relate_jenya=0:
        r "У Жени заурчит живот. Женя и [mcname] вместе готовят обед)"
        return

    return