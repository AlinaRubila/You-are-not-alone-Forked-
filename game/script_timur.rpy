# Начало рута Тимура

label timur:

    if persistent.ending1 and persistent.ending122:
         scene bg_rut
    else:
        scene bg_rutnoeve

    "Мой сосед по комнате не обратил на меня внимание. Как он добрался быстрее меня, если я встал раньше?.."

    "Не хочу знать."

    scene bg_rutscreen

call screen rutChoice
