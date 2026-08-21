default dechets = [False, False, False, False]

define coordinates = [
    (0.05, 0.2),
    (0.3, 0.7),
    (0.6, 0.1),
    (0.8, 0.6)
]

screen ramasseDechets():

    text "Déchets ramassés : [dechetsRamasses] / [len(dechets)]"

    for i in range(len(dechets)):

        if not dechets[i]:

            imagebutton:
                xpos coordinates[i][0]
                ypos coordinates[i][1]

                idle "dechet{}".format(i + 1) # le truc de fdp jpp

                activate_sound "sfx/onclick.wav"
                hover_sound "sfx/hover.wav"

                action [
                    IncrementVariable("dechetsRamasses", 1),
                    SetDict(dechets, i, True)
                ]

    if all(dechets):
        timer 0.01 action Jump("finDechets")
