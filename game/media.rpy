# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

image thomas = "sprites/mrthomas-sprite.png"

#Sprite Noa 
image NoaBasic = animate_mouth("sprites/Noa/noa-basic")
image NoaBasic2 = animate_mouth("sprites/Noa/noa-basic2")
image NoaEffraye = animate_mouth("sprites/Noa/noa-effray")
image NoaPense = animate_mouth("sprites/Noa/noa-penseur")
image NoaTimide = animate_mouth("sprites/Noa/noa-timide")
image NoaNRV = animate_mouth("sprites/Noa/noa-vener")
image NoaNeutre = animate_mouth("sprites/Noa/noa-neutral")

#Sprite Chris
image ChrisBasic = animate_mouth("sprites/Chris/chris-basic")
image ChrisEffraye = animate_mouth("sprites/Chris/chris-effray")
image ChrisHeureux = animate_mouth("sprites/Chris/chris-heureux")
image ChrisPetitSourire = animate_mouth("sprites/Chris/chris-petitsourire")
image ChrisNRV = animate_mouth("sprites/Chris/chris-vener")
image ChrisTimide = animate_mouth("sprites/Chris/chris-timide")

#Sprite JaneDoe
image JaneBasic = animate_mouth("sprites/JaneDoe/joe-sprite")
image JaneRizz = animate_mouth("sprites/JaneDoe/janeRizz")
image JanePense = animate_mouth("sprites/JaneDoe/janePense")
image JaneNRV = animate_mouth("sprites/JaneDoe/janeNRV")
image JaneChock = animate_mouth("sprites/JaneDoe/janeChockbar")
image JaneFlip = animate_mouth("sprites/JaneDoe/janeFlippant")
image JaneNeutre = animate_mouth("sprites/JaneDoe/jane-neutral")
image Cerbere = "sprites/JaneDoe/jane-chien.png"

image mamanvener = "sprites/mamanvener.png"

# Déchêts (je perds du temps pour rien mais az)

image dechet1 = "sprites/dechets1.png"
image dechet2 = "sprites/dechets2.png"
image dechet3 = "sprites/dechets3.png"
image dechet4 = "sprites/dechets4.png"

# fonction pour resize les images pour les utiliser en boutons

init python:
    def resizeImg(img, width=800, height=900):
        return Transform(img, size=(width, height))