label timur_good_end:
    scene bg_room_after_repair with dissolve

    "Весь день я клеил обои, стараясь делать это как можно аккуратнее. Мне действительно очень помогли советы, которые недавно давал мне Тимур. Я не хотел подвести друга и пытался сделать всё в лучшем виде."

    if persistent.timur_good != True:
        $ renpy.notify("В дневнике появилась новая запись!")
    $ persistent.timur_good = True

    "Вечером, когда я лёг спать, мне снова приснилась та девушка. Она стояла в комнате, полной света, улыбаясь мне и будто благодаря за что-то. Интересно, за что?"

    scene black with dissolve
    stop music fadeout 2.0
    stop background fadeout 2.0
    pause 1.0

    play music home fadein 1.0

    #нужна фоновая музыка (возможно, этим займусь уже я, но, если вдруг есть идея по поводу музыки - вперёд!)
    $ persistent.poster8 = True

    scene cj_timur_good_ending with dissolve

    "Дисциплинарка миновала! Комендант похвалила нас за ремонт. Тимур был очень благодарен мне."

    "Из-за скандала в начале я всё же уговорил его вместе сходить к психологу, а после он, не без моей поддержки, решился пойти к специалисту один. Ему было тяжело, но он знал, что рядом есть человек, который работал с психологом и всегда сможет поддержать его. И этот человек — я."

    "Я всё ещё чувствую чьё-то присутствие, но оно меня больше не пугает."

    pause 2.0
    stop music fadeout 2.5
    $ persistent.ending3 = True
    $ set_quick_menu(False)

    scene black with dissolve
    play background audio.wind
    centered "{size=+24}{color=#ffffff}Кому-то ещё нужна твоя помощь"
    stop background fadeout 1.0

return
