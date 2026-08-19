# Déclarez les personnages utilisés dans le jeu.

init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("sfx/talking_typewriting.wav", channel='sound', loop=True)
        elif event == "slow_done" or event == "done":
            renpy.music.stop(channel='sound')

define protag = Character("[protag_name]", color="#f29100", callback=callback, what_italic=False)
define protag_pensee= Character("[protag_name]", color="#f29100", callback=callback, what_italic=True)

define noa = Character("[noa_name]", color="#32a36b")

define thomas = Character("M. Thomas", color="#987d67")

define chris = Character("[chris_name]", color="#6fb7dc")

define JaneDoe = Character("[JaneDoe_name]", color="#ecf8ff")
