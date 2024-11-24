label Kitchen:
    mc "Можете показать, где тут кухня?"

    od "Хорошо, пойдём."

    stop background
    stop music
    scene black with dissolve

    play sound steps

    play music room

    scene black with dissolve

    scene bg_kitchen_morning with dissolve
    play music home
    play background room

    "Кухня была прямо рядом с моей комнатой. Довольно выгодное расположение, так как не придется протаптывать целый коридор, чтобы просто поставить ужин в микроволновку."

    "А если она еще и окажется занята, то это вообще туши свет."

    "На самой кухне ещё висел в воздухе вкусный аромат: кто-то пожарил себе мясо. Сбоку была электрическая плита, местами запачканная."

    "Мне сказали, что убираются на кухне сами студенты, по дежурствам, четко по графику. Но судя по окружающим издержкам готовки, сегодня дежурства ещё не было."

    "Справа от плиты был стол с микроволновкой, между ними была забитая уже почти полностью мусорка. Мусор выкидывают тоже по дежурствам. "

    "Над микроволновкой для особо одаренных были правила по ее использованию. И, как ни странно, кто-то умудрялся их нарушать."

    "У другой стены были две раковины, большие как мойдодыр. В одной из них была только холодная вода, поэтому спрос на первую был в разы больше. Не повезло холодной воде, что она жир с трудом отмывает!"

    show comenda home normala at right2 with dissolve

    od "В холодильнике полки поделены между жильцами. Кстати, с плитой будь осторожнее, она долго разогревается."

    show mc normala at left2 with dissolve
    mc "Хорошо, я понял. Спасибо, что предупредили."

    if dormPlaces < 3:
        od "Что ещё тебе показать?"
    jump ChoiceDorm

label Dayroom:
    mc "У вас есть комната отдыха?"

    od "Да, она находится на втором этаже."

    stop background
    stop music
    scene black with dissolve

    play sound steps

    play background room

    scene bg_dayroom with dissolve

    "Комната отдыха располагалась недалеко. Завернув за угол сразу после входа и пройдя через комендантскую в дверь, расположенную в конце коридора, можно было дойти до неё."

    "Комната отдыха оказалась не такой захламленной, какой могла быть."

    "В центре стояли столы, рядом с ними были кресла-груши, а у стен стояли стулья, стеллажи с никому уже не нужными книгами и настольными играми, в которых уже отсутствовало большинство составляющих."

    "Единственным, что привлекало внимание были стены этой комнаты - покрытые фотографиями, рисунками, и парой плакатов с правилами дорожного движения и проживания в общежитии, на которых вместо привычных всем детишек и животных, был изображён персонаж какого-то аниме."

    "Видимо, автор этих художеств был фанатом японской мультипликации."
    show comenda home normala at right2 with dissolve

    od "В комнате отдыха нельзя мусорить. Сидеть ночью можно, но главное тихо."
    show mc smilea at left2 with dissolve

    mc "Ого. А здесь классно."

    if dormPlaces < 3:
        od "Что ещё тебе показать?"
    jump ChoiceDorm
label Laundry:
    mc "Где здесь можно постирать вещи?"

    od "На первом этаже у нас стоят стиральные машины."

    stop music
    stop background

    scene black with dissolve
    play sound steps

    play background room

    scene bg_laundry with dissolve

    "Ольга Дмитриевна провела меня по первому этажу нашего общежития."

    "Справа и слева двери, которые вели в комнаты живущих там студентов. На одной из дверей было написано “Постирочная”."

    "Комендант прошла со мной в комнату. В ней стояло несколько стиральных машин. Мне кажется, это довольно удобно. Жаль, конечно, что стиралка не в комнате, но то, что она хотя бы есть – не может не радовать."

    show comenda home normala at right2 with dissolve

    od "Тут вещи можно и постирать, и погладить. Не забывай после себя всё выключать. Стиральный порошок каждый покупает свой. Хранить его можно здесь."

    "Она указала на шкаф напротив."

    if dormPlaces < 3:
        od "Что ещё тебе показать?"
    jump ChoiceDorm
