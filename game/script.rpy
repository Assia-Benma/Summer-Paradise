# Vous pouvez placer le script de votre jeu dans ce fichier.


label start:

    $ protag_name = renpy.input("Qui es-tu ?", default="Moi").strip()
    
    # Set a default name if the player leaves it blank
    if not protag_name:
        $ protag_name = "Moi"
        
    protag "Salut salut je suis [protag_name]!"

    "Choisis maintenant tes pronons !"

    menu:
        "Il/lui":
            $ pronoms1 = "Il"
            $ pronoms2 = "Lui"
        "Elle/"

    ## début du jeu selon le script d'alissa

    protag_pensee "Je descends enfin du car après 1h de trajet.
    Je ne voyais que des déserts de verdure à l’horizon.
    Ma tête tourne encore."

    protag_pensee "J’inspire à fond l’air frais et pur.
    Je retire mes écouteurs et lance mon sac sur le dos.
    Le coffre du car s’ouvre, j'agrippe la poignée et sors ma lourde valise.
    Ma mère m’a dit de ne pas trop la remplir mais je tiens tellement à mes affaires."

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
            play sound "sfx/p5sfx.wav"
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

    menu:
        "Fouiller":
            play sound "sfx/p5sfx.wav"
            $ curiosite += 5
            jump fouille

        "Sortir":
            pass

    label fouille:

        protag_pensee "J’observe les aménagements des autres employés. Autant savoir avec quel genre de personne je vais vivre.
                        Une photo repose sur une table de nuit entre mon lit et un autre."

        protag_pensee "Je prends la photo, laissant ma curiosité prendre le dessus. Un jeune homme avec une femme plus âgée. Cela semble avoir été pris
        dans un jardin fleuri. Peut-être un des animateurs et sa mère."

        protag_pensee "Ils sont plutôt adorables. C’est presque touchant mais ce n’est pas la seule photo familiale que je vois ici.
        Au moins, ils sont tous proches de leur famille."  

    protag_pensee "Je finis par sortir. Je dois trouver ce fameux Noa. La flèche du club enfant montre un chemin vers la forêt."
    
    protag_pensee "Le chant des oiseaux et le bruissement des feuillages sont les seuls bruits que j’entends.
    Je suis la route espérant tomber sur mon futur guide. Me perdre est la dernière chose que je veux."

    protag_pensee "Je sors mon téléphone. Pas de réseaux.
    Evidemment, ce ne serait pas drôle sinon. Je souffle, commençant
    à angoisser. Puis un craquement se fait dans mon dos."

    protag_pensee " Je me retourne et vois une énorme caisse
    soulevée par quelqu’un. Il dévoile sa tête. Beau garçon dis donc."

    noa "Salut, t’es la nouvelle employée je crois. C’est moi qui doit t’aider à prendre tes marques."
    
    $ noa = "Noa"

    menu:
        "Ah oui ! Tu es Noa.":
            play sound "sfx/p5sfx.wav"
            noa "Exactement. Content de voir que tu me connais."
            $ noaAF += 5
        "Ah oui ! Noé, c’est ça ?":
            noa "Presque, c’est Noa en fait."
    
    protag "M.Thomas m’a parlé de toi."
    
    noa "Viens, je vais te donner tout ce dont tu as besoin."
    
    protag_pensee "On se dirige vers un grand terrain d’accrobranche où se trouve un local. Il pose sa caisse au sol puis récupère un talkie-walkie. Il allume et règle la fréquence radio."
    
    noa "Tiens. Tu auras besoin de ça pour communiquer dans tout le camp. Je vais te faire visiter tout le lieu mais je vais quand même te donner une carte au cas où."

    protag_pensee "Je prends tout ça et range tout dans ma banane."

    protag "Et pour le t-shirt du camping ?"

    protag "Je te le donnerais ce soir avant que tu ailles au bar. Maintenant, tu vas m’aider à tout préparer pour le feu de camp de ce soir."

    protag "Ok, je te suis."

    protag_pensee "On arrive face à des vestiges d’une ancienne fête. Des déchets partout, des cendres d’un feu, des miettes de gâteaux et de chips."
    
    protag_pensee "Même les troncs qui faisaient office de sièges semblent avoir été déplacés."

    protag "Wow. Vous avez fêté quelque chose hier soir ? Quel bazar. Je croyais que les arrivées étaient aujourd’hui."

    protag_pensee "Noa se gratte la nuque clairement gêné."

    noa "Ouais… On a eu une semaine de pause entre les deux séjours des clients."

    noa "Disons qu’on s’est tous défoulé avant la remise au boulot. Et maintenant, je dois tout ranger."

    protag "M.Thomas vous a laissé faire ?"

    noa "Pour être honnête, c’est un secret. Garde ça pour toi surtout. Je te le revaudrais."

    menu: 
        "C’est franchement pas malin. Et vous m'impliquez dans vos bêtises en plus. Je dois débarrasser à votre place":
            $ noaAF -= 5
            jump PasMalin
        "Dommage, j’aurais aimé être là. Si j’avais su, je serais venu un jour plus tôt.":
            $noaAF += 5
            jump EtreLa
        
    label PasMalin: 
        noa "Désolé, c’était pas voulu. On aurait peut-être pas dû, c’est vrai."
    label EtreLa:
        noa "J’aurais aimé aussi. Tu aurais pu connaître tout le monde dans une bonne ambiance."
        noa "Mais désolé que tu doive ranger ce bordel avec moi."

    protag_pensee "Je m’arme d’un sac poubelle et ramasse les déchets. Noa réarrange le feu de camp pour ce soir en replaçant correctement les roches."

    protag_pensee "J’en finis avec les déchets. Ce fut plus long et répugnant que prévu."

    prota_pensee "J’ai trouvé des choses que je souhaiterais oublier. Noa s’occupe des troncs, essayant de les pousser seul."

    menu:
        "L'aider":
            jump aider
        "Le laisser faire":
            jump poAider


    label aider:
        noa "Merci, c’est gentil."
        protag_pensee "Je pousse le tronc de toutes mes forces."
        prota_pensee "C’est plus lourd que prévu mais on arrive à le remettre correctement face au feu éteint."
        noa "Tu es plus costaud que moi, je suis presque jaloux."
        protag "Prends en de la graine."
        protag_pensee "On rit ensemble."
        protag_pensee "Je suis contente d’avoir pu me rapprocher si vite de lui. Ce nouveau job devient moins stressant avec quelqu’un de sympa aux alentours."

    label poAider:
        noa "Noa arrive à se débrouiller seul. Il est légèrement essoufflé mais il se relève plein d’énergie."

    noa "Bon. Le bar fermera plus tôt. Comme tu l’as compris, ce soir c’est histoires d’horreurs et marshmallows au coin du feu."
    
    noa "Si jamais tu as besoin, normalement tu ne seras pas seul(e)."

    protag "Oui je sais, le patron me l’a dit."

    noa "Je te fais faire le tour. Tu connais la forêt avec le club enfant, l’entrée du camping. Tu as vu le cabanon des animateurs ?"

    protag "Oui j’y ai déposé ma valise."

    noa "Bien, ce sera court alors. Par ici, le lac n’est pas loin."

    #Decors : Lac 

    protag "Une grande étendue d’eau se présente devant mes yeux. Les reflets du soleil se promènent à la surface. Et les canards cancanent joyeusement, plongeant leurs têtes sous l’eau."

    protag "Un petit local près d’un ponton se situe à quelques mètres de nous."
return
