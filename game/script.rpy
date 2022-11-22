# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Босс', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bossoffice night

    show friend smile at center:
        zoom 0.75

    e "Здарова, я босс, если что."

    return
