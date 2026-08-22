default habilete = 0
default curiosite = 0
default courage = 0

default noa_name= "???"
default chris_name = "???"
default JaneDoe_name = "???"

default noa_main_proposee = Null
default KnowDirty = False
default drinkDirty = False
default ChoixDate = Null

default dechetsRamasses = 0

default AF = {
    "Noa": 0,
    "Chris": 0,
    "Jane": 0
}

define love_max = {
    "Noa": 120,
    "Chris": 110,
    "Jane": 90
}

define bonus_seuil = {
    "bonus_habilite": 45,
    "bonus_curiosite": 50,
    "bonus_courage": 40
}

default chosenDate = ""

init python:
    def get_love_level(character):
        """Calcule le niveau (1 à 8) de la lovemeter pour un personnage donné."""
        value = AF[character]
        max_value = love_max[character]
        ratio = value / float(max_value) #je te ratio Inès bleeeeeeh

        stade = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3]
        for i, t in enumerate(stade):
            if ratio >= t:
                return 8 - i
        return 1

    def ajout_bonus(habi, cour,curio):
        if habi >= bonus_seuil["bonus_habilite"]:
            AF["Noa"] += 5
        elif cour >= bonus_seuil["bonus_courage"]:
            AF["Jane"] += 5
        elif curio >= bonus_seuil["bonus_curiosite"]:
            AF["Chris"] += 5
        return


label afficheJour(jour):

    show text "{font=fonts/Karla-VariableFont_wght.ttf}{cps=2}{size=*4}Jour [jour]{/size}{/cps}{/font}":
        xpos 950
        ypos 450

    with dissolve
    pause 3.0

    hide text
    with dissolve

    scene black
    with dissolve

    window show

    return

screen loveMeter(character):
    $ level = get_love_level(character)
    add "Ui/lovemeter[level].png" xpos 1700 ypos 250

