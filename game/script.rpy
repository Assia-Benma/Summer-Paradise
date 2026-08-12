# Vous pouvez placer le script de votre jeu dans ce fichier.

default habilete = 0

label start:

    $ protag_name = renpy.input("Qui es-tu ?", default="Moi").strip()
    
    # Set a default name if the player leaves it blank
    if not protag_name:
        $ protag_name = "Moi"
        
    protag "Salut salut je suis [protag_name]!"

    ## début du jeu selon le script d'alissa

    protag_pensee "Je descends enfin du car après 1h de trajet.
    Je ne voyais que des déserts de verdure à l’horizon.
    Ma tête tourne encore."

    protag_pensee "J’inspire à fond l’air frais et pur.
    Je retire mes écouteurs et lance mon sac sur le dos.
    Le coffre du car s’ouvre, j'agrippe la poignée et sors ma lourde valise.
    Ma mère m’adit de ne pas trop la remplir mais je tiens tellement à mes affaires."

    protag_pensee "L’insigne du camping indique “SummerParadise”. Je fixe l’entrée soupirante. Mon premier travail…
    c’est moins excitant que ce que je pensais. J’espère que mes collègues seront sympas."

    protag_pensee "Je vois le patron s’approcher. Il semble pressé, peut-être un peu sur les nerfs.
    Pourtant, il affiche un sourire accueillant. Cela me rassure étrangement."

    show thomas
    with dissolve

    thomas "Vous devez être [protag_name], c’est bien ça ?"

    protag "Oui. Bonjour mon-"

    hide thomas
    with dissolve

    protag_pensee " Je n’ai même pas le temps de répondre qu’il repart déjà. Je suis un peu prise de court mais je presse le pas, le suivant à distance respectueuse.
    Il ne se retourne pas pour vérifier que je le suis."

    protag_pensee "Je tire tant bien que mal ma grosse valise. Heureusement que ça roule bien sur ces chemins de terre."

    protag_pensee "Nous arrivons face à un cabanon plutôt grand. Une pancarte dit “staff only”. Je redresse mon bagage, sentant déjà mon muscle du bras forcer. Je suis soulagé(e) de ce
    poids en moins."

    protag_pensee "J’imagine que je vais dormir ici. Par la fenêtre, je vois plusieurs lits et des affaires éparpillés partout. Oh non… cela
    veut dire que l’on dort tous ensemble dans la même pièce. L’angoisse totale. Pitié que personne ne ronfle."

    show thomas
    with dissolve

    thomas "Bon, étant donné que Camille n’a pas renouvelé son contrat pour ce mois, vous serez au bar principalement le soir.
    Vous avez suivi une formation en mixologie ?"

    menu:

        "Hum…pas vraiment. Mais j’apprends vite.":
            pass

        "Non pas exactement. J’ai un oncle qui tient un bar, j’ai appris sur le tas.":
            $ habilete += 10

    thomas "Cela fera l’affaire, quelqu’un sera toujours avec vous. Pour la journée, vous serez un peu partout pour aider, je préfère ne
    pas vous laisser seul(e)."

    protag_pensee "Son talkie-walkie se met soudain à s’allumer."

    "Staff" "Monsieur ? Les portes des cabines du sanitaire sont encore toutes bloquées et l’eau ne coule plus dans une des douches."

    thomas "Quoi ? Encore ?! Cela fait 4 fois ce mois-ci."

    protag_pensee " Il se frotte les yeux lassé puis soupire longuement.
    J’ai presque de la peine pour lui. Surtout pour la personne qui devra réparer tout ça.
    Les heures supplémentaires…les pires inventions au monde."

    thomas "Bon, je vais devoir vous abandonner. Mais Noa va vous aider. Il doit être dans la forêt à s’occuper du matos pour l'accrobranche."

    hide thomas
    with dissolve

    protag_pensee "Le patron disparaît rapidement. Je suis un peu intimidé(e) ici, je ne connais pas encore très bien les lieux.
    On est entouré que de forêt, cela va être difficile de trouver."
    
    protag_pensee "Je vois au loin une flèche montrant le club enfant. 
    On va commencer par là je pense. Mais avant ça, je vais me débarrasser de mes affaires."

    protag_pensee "Je rentre dans le bungalow étonnamment spacieux. Un petit salon assez cosy, je suis agréablement surprise de voir une télé face au sofa. La cuisine semble avoir tout le
    nécessaire pour préparer les repas. Et il y a une clim ! Le bonheur."

    protag_pensee "Je suis sûr(e) de passer un bon été avec ça. Maintenant, l’endroit le
    plus important: la chambre."

    protag_pensee "J’ouvre la seule porte qui reste. Des lits alignés, certains défaits, d’autres arrangés. Des vêtements éparpillés, d’autres rangés. Puis des bibelots par ci par là. Je
    n’aurais jamais cru que l’ordre et le chaos pouvaient cohabiter."

    protag_pensee "Je rejoins le seul lit inoccupé et y laisse ma valise et mon sac."
    
return
