# Déclarez les personnages utilisés dans le jeu.

init python:
    main_speaking = False

    def callback(event, **kwargs):
        global main_speaking

        if event == "show":
            renpy.music.play("sfx/talking_typewriting.wav", channel='sound', loop=True)
            main_speaking = True

        elif event == "slow_done":
            renpy.music.stop(channel='sound')

        elif event == "end":
            main_speaking = False

    ## définitions animations
    def animate_mouth_dynamic(st, at, sprite):
        if main_speaking:
            return "{}.png".format(sprite), None

        if int(st / 0.2) % 2 == 0:
            frame = "{}.png".format(sprite)
        else:
            frame = "{}-bis.png".format(sprite)
        return frame, 0.2

    def animate_mouth(sprite):
        return DynamicDisplayable(animate_mouth_dynamic, sprite=sprite)
            

define protag = Character("[protag_name]", color="#ea7602", callback=callback, what_italic=False)
define protag_pensee= Character("[protag_name]", color="#ea7602", callback=callback, what_italic=True)

define noa = Character("[noa_name]", color="#32a36b")

define thomas = Character("M. Thomas", color="#987d67")

define chris = Character("[chris_name]", color="#6fb7dc")

define JaneDoe = Character("[JaneDoe_name]", color="#ecf8ff")

