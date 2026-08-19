default habilete = 0
default curiosite = 0
default courage = 0

default noa_name= "???"
default chris_name = "???"
default JaneDoe_name = "???"

default AF = {
    "Noa" : 0,
    "Chris" : 0,
    "Jane" : 0
}
screen loveMeter(character):

    $ loveValue = AF[character]

    if loveValue >= 80:
        $ level = 8
    elif loveValue >= 70:
        $ level = 7
    elif loveValue >= 60:
        $ level = 6
    elif loveValue >= 40:
        $ level = 5
    elif loveValue >= 20:
        $ level = 4
    elif loveValue >= 10:
        $ level = 3
    elif loveValue >= 5:
        $ level = 2
    else:
        $ level = 1
    add "Ui/lovemeter[level].jpg" xpos 1700 ypos 250


$ noa_main_proposee = null
define KnowDirty = False
define drinkDirty = False