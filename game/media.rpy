# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

image thomas = "sprites/mrthomas-sprite.png"

#Sprite Noa 
image NoaBasic = "sprites/Noa/noa-basic.png"
image NoaBasicBis = "sprites/Noa/noa-basic-bis.png"
image NoaBasic2 = "sprites/Noa/noa-basic2.png"
image NoaEffraye = "sprites/Noa/noa-effray.png"
image NoaPense = "sprites/Noa/noa-penseur.png"
image NoaTimide = "sprites/Noa/noa-timide.png"
image NoaNRV = "sprites/Noa/noa-vener.png"
image NoaNeutre = "sprites/Noa/noa-neutral.png"

#Sprite Chris
image ChrisBasic = "sprites/Chris/chris-basic.png"
image ChrisEffraye = "sprites/Chris/chris-effray.png"
image ChrisHeureux = "sprites/Chris/chris-heureux.png"
image ChrisPetitSourire = "sprites/Chris/chris-petitsourire.png"
image ChrisNRV = "sprites/Chris/chris-vener.png"
image ChrisTimide = "sprites/Chris/chris-timide.png"

#Sprite JaneDoe
image JaneBasic = "sprites/JaneDoe/joe-sprite.png"
image JaneRizz = "sprites/JaneDoe/janeRizz.png"
image JanePense = "sprites/JaneDoe/janePense.png"
image JaneNRV = "sprites/JaneDoe/janeNRV.png"
image JaneChock = "sprites/JaneDoe/janeChockbar.png"
image JaneFlip = "sprites/JaneDoe/janeFlippant.png"
image JaneNeutre = "sprites/JaneDoe/jane-neutral.png"
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