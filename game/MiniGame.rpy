init python:
    choix_bouteille = []
    confirmation_ouverte = False

    recettes = {
        frozenset(["Cranberry", "Citron", "Vodka"]): "Cosmopolitain",
        frozenset(["Menthe", "Citron", "Eau gazeuse"]): "Virgin Mojito",
        frozenset(["Citron", "Grenadine", "Vodka"]): "Dirty Shirly",
        frozenset(["Menthe", "Citron", "Rhum"]): "Mojito",
    }

    def affiche_bouteille(nom):
        global choix_bouteille
        if nom in choix_bouteille:
            choix_bouteille.remove(nom)
        elif len(choix_bouteille) < 2:
            choix_bouteille.append(nom)

    def demander_confirmation():
        #Appelée au clic sur le shaker. Ouvre le panneau de confirmation.
        global confirmation_ouverte
        if len(choix_bouteille) != 3:
            renpy.notify("Il faut choisir 3 ingrédients !")
            return
        confirmation_ouverte = True

    def annuler_confirmation():
        #Appuyer sur 'Non'. Referme juste la frame.
        global confirmation_ouverte
        confirmation_ouverte = False

    def faire_cocktail(commande):
        #Appuyer sur 'Je suis sur' fait la commande
        global choix_bouteille, confirmation_ouverte

        resultat = recettes.get(frozenset(choix_bouteille), None)

        if resultat == "Dirty Shirley" and not KnowDirty:
            resultat = None

        choix_bouteille = []
        confirmation_ouverte = False

        if resultat == commande:
            return True
        else:
            return False


screen mini_game(commande, cache):

    add "bar"

    if not cache:
        text "Commande : [commande]":
            xalign 0.5 
            yalign 0.05 
            size 40
    else:
        text "Commande : ???":
            xalign 0.5 
            yalign 0.05 
            size 40

    text "Sélection : [', '.join(choix_bouteille)]":
        xalign 0.5 
        yalign 0.12 
        size 30

    imagebutton:
        idle "vodka"
        xpos 200 
        ypos 280
        action Function(affiche_bouteille, "Vodka")

    imagebutton:
        idle "petillant"
        xpos 600 
        ypos 280
        action Function(affiche_bouteille, "Eau gazeuse")

    imagebutton:
        idle "menthe"
        xpos 1000 
        ypos 330
        action Function(affiche_bouteille, "Menthe")

    imagebutton:
        idle "citron"
        xpos 1400 
        ypos 280
        action Function(affiche_bouteille, "Citron")

    imagebutton:
        idle "cranberries"
        xpos 1400 
        ypos 280
        action Function(affiche_bouteille, "Cranberry")
    
    imagebutton:
        idle "grenadine"
        xpos 1400 
        ypos 280
        action Function(affiche_bouteille, "Grenadine")

    imagebutton:
        idle "shaker"
        xpos 1700
        ypos 450
        action Function(demander_confirmation)

    #frame de confirmation
    if confirmation_ouverte:
        frame:
            xalign 0.5 
            yalign 0.5
            padding (40, 30)
            vbox:
                spacing 20
                xalign 0.5
                text "Es-tu sur de ce mélange ?" size 45
                hbox:
                    spacing 40
                    xalign 0.5
                    textbutton "Je suis sur !" action Function(faire_cocktail, commande)
                    textbutton "Non" action Function(annuler_confirmation)

label bar_minigame(commande, label):
    $ commande_du_jour = commande

    protag_pensee "Un client vient de commander un [commande_du_jour]. Je dois faire vite !"

    $ selected_bottles = [] 
    call screen mini_game(commande_du_jour, False)

    if _return:
        protag "Et voilà, un [commande_du_jour] comme demandé !"
        $ habilete += 10
    else:
        protag_pensee "Zut, je me suis trompé de mélange..."
        $ habilete -= 5 
    jump label
