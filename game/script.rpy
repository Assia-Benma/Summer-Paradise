# Vous pouvez placer le script de votre jeu dans ce fichier.


label start:

    $ protag_name = renpy.input("Qui es-tu ?", default="Moi").strip()
    
    # Set a default name if the player leaves it blank
    if not protag_name:
        $ protag_name = "Moi"
        
    protag "Salut salut je suis [protag_name]!"
return
