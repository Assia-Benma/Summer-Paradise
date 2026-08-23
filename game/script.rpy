# Vous pouvez placer le script de votre jeu dans ce fichier.

label start:

    stop music fadeout 5.0

    $ protag_name = renpy.input("Qui es-tu ?", default="Moi").strip()
    
    # Set a default name if the player leaves it blank
    if not protag_name:
        $ protag_name = "Moi"
        
    protag "Salut salut je suis [protag_name]!"

    "Choisis maintenant tes pronoms !"

    menu:
        "Il/lui":
            $ pronoms1 = "Il"
            $ pronoms2 = "Lui"
        "Elle/la":
            $ pronoms1 = "Elle"
            $ pronoms2 = "la"
        "Garder l'écriture inclusif":
            pass
        #Donner le choix de garder le texte en inclusif 

    ## début du jeu selon le script d'alissa

    window hide

    play sound "sfx/new_day.wav"

    call afficheJour(1)

    scene entree_camping

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

    scene cabane

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

    menu:
        "Fouiller":
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

    show NoaBasic
    with dissolve

    noa "Salut, t’es la nouvelle employée je crois. C’est moi qui doit t’aider à prendre tes marques."
    
    $ noa_name = "Noa"
    show screen loveMeter("Noa")

    menu:
        "Ah oui ! Tu es Noa.":
            $ AF["Noa"] += 5
            
            hide NoaBasic
            show NoaBasic2
            noa "Exactement. Content de voir que tu me connais."
            hide NoaBasic2
        "Ah oui ! Noé, c’est ça ?":
            hide NoaBasic
            show NoaNeutre
            noa "Presque, c’est Noa en fait."
            hide NoaNeutre
    
    show NoaBasic2
    protag "M.Thomas m’a parlé de toi."
    
    noa "Viens, je vais te donner tout ce dont tu as besoin."
    
    protag_pensee "On se dirige vers un grand terrain d’accrobranche où se trouve un local. Il pose sa caisse au sol puis récupère un talkie-walkie. Il allume et règle la fréquence radio."
    
    hide NoaBasic2
    show NoaBasic
    noa "Tiens. Tu auras besoin de ça pour communiquer dans tout le camp. Je vais te faire visiter tout le lieu mais je vais quand même te donner une carte au cas où."

    protag_pensee "Je prends tout ça et range tout dans ma banane."

    protag "Et pour le t-shirt du camping ?"

    noa "Je te le donnerais ce soir avant que tu ailles au bar. Maintenant, tu vas m’aider à tout préparer pour le feu de camp de ce soir."

    protag "Ok, je te suis."

    scene feu

    protag_pensee "On arrive face à des vestiges d’une ancienne fête. Des déchets partout, des cendres d’un feu, des miettes de gâteaux et de chips."
    
    protag_pensee "Même les troncs qui faisaient office de sièges semblent avoir été déplacés."

    protag "Wow. Vous avez fêté quelque chose hier soir ? Quel bazar. Je croyais que les arrivées étaient aujourd’hui."

    protag_pensee "Noa se gratte la nuque clairement gêné."

    hide NoaBasic
    show NoaPense
    noa "Ouais… On a eu une semaine de pause entre les deux séjours des clients."

    noa "Disons qu’on s’est tous défoulé avant la remise au boulot. Et maintenant, je dois tout ranger."

    protag "M.Thomas vous a laissé faire ?"

    noa "Pour être honnête, c’est un secret. Garde ça pour toi surtout. Je te le revaudrais."

    menu: 
        "C’est franchement pas malin. Et vous m'impliquez dans vos bêtises en plus. Je dois débarrasser à votre place":
            $ AF["Noa"] -= 5
            play sound "sfx/bad_choice.wav"
            hide NoaPense
            show NoaNeutre
            noa "Désolé, c’était pas voulu. On aurait peut-être pas dû, c’est vrai."
            hide NoaNeutre

        "Dommage, j’aurais aimé être là. Si j’avais su, je serais venu un jour plus tôt.":
            $ AF["Noa"] += 5
            hide NoaPense
            show NoaBasic2
            noa "J’aurais aimé aussi. Tu aurais pu connaître tout le monde dans une bonne ambiance."
            noa "Mais désolé que tu doive ranger ce bordel avec moi."
            hide NoaBasic2

    show NoaBasic with dissolve
    protag_pensee "Je m’arme d’un sac poubelle et ramasse les déchets. Noa réarrange le feu de camp pour ce soir en replaçant correctement les roches."
    hide NoaBasic

    window auto

    call screen ramasseDechets

    label finDechets:

        protag_pensee "J’en finis avec les déchets. Ce fut plus long et répugnant que prévu."

        protag_pensee "J’ai trouvé des choses que je souhaiterais {size=*2}oublier{/size}. Noa s’occupe des troncs, essayant de les pousser seul."

        menu:
            "L'aider":
                hide NoaBasic 
                show NoaBasic2
                noa "Merci, c’est gentil."
                protag_pensee "Je pousse le tronc de toutes mes forces."
                protag_pensee "C’est plus lourd que prévu mais on arrive à le remettre correctement face au feu éteint."
                noa "Tu es plus costaud que moi, je suis presque jaloux."
                protag "Prends en de la graine."
                protag_pensee "On rit ensemble."
                protag_pensee "Je suis contente d’avoir pu me rapprocher si vite de lui. Ce nouveau job devient moins stressant avec quelqu’un de sympa aux alentours."
                hide NoaBasic2

            "Le laisser faire":
                protag_pensee "Noa arrive à se débrouiller seul. Il est légèrement essoufflé mais il se relève plein d’énergie."
                hide NoaBasic 

        show NoaNeutre    
        noa "Bon. Le bar fermera plus tôt. Comme tu l’as compris, ce soir c’est histoires d’horreurs et marshmallows au coin du feu."
        
        hide NoaNeutre
        show NoaBasic
        noa "Si jamais tu as besoin, normalement tu ne seras pas seul(e)."

        protag "Oui je sais, le patron me l’a dit."

        noa "Je te fais faire le tour. Tu connais la forêt avec le club enfant, l’entrée du camping. Tu as vu le cabanon des animateurs ?"

        protag "Oui j’y ai déposé ma valise."

        noa "Bien, ce sera court alors. Par ici, le lac n’est pas loin."

        scene lac

        protag_pensee "Une grande étendue d’eau se présente devant mes yeux. Les reflets du soleil se promènent à la surface. Et les canards cancanent joyeusement, plongeant leurs têtes sous l’eau."

        protag_pensee "Un petit local près d’un ponton se situe à quelques mètres de nous."

        noa "Sincèrement, quand je meurs de chaud et que c'est une journée au lac pour les enfants, je me sens béni."

        protag "Je pourrais passer des jours au lac moi aussi ?"

        hide NoaBasic
        show NoaBasic2
        noa "Faut voir si le boss te met avec moi. Je prie pour toi."

        protag "Génial..."

        protag_pensee "Je sens déjà le soleil brûler ma peau avec la crème solaire sur mon visage. Sans oublier la sueur sous mes vêtements. De quoi rendre l’été insupportable."
        protag_pensee "J’aurais peut-être dû passer le BAFA et me présenter comme animatrice."

        noa "On passe à la suite."

        protag_pensee "Il me sourit gentiment et reprend la visite guidée."

        scene bar 

        protag_pensee "On se retrouve dans une sorte de place pleine de plantes et de fleurs. Les tables rondes et rectangulaires sont mises un peu partout face à une scène."
        protag_pensee "Le bar est de l’autre côté. Il semble assez spacieux et diversifié en alcool."

        protag "Je vois une scène basique. Faire des shows est aussi dans ton contrat ?"

        noa "C’est le cas. Figure toi que je vais égayer tes soirées ici."

        protag "Hâte de voir ça. J’imagine les mêmes choses que dans les autres campings."

        noa "Tu imagines très bien. Des karaokés, blind tests, etcetera."

        protag "Quel programme original."

        hide NoaBasic2
        show NoaNeutre
        noa "Je crois que c’est l’heure du déjeuner"

        protag "Génial, je meurs de faim."

        scene cabane 

        protag_pensee "On retourne au cabanon, se partageant la cuisine."
        protag_pensee "Je fais avec ce que je trouve et finis avec un sandwich simple. Noa me laisse pour manger, préférant finir ce qu’il faisait au club enfant."
        
        hide NoaNeutre
        hide screen loveMeter with dissolve
        
        protag_pensee "Une fois l’estomac rempli, je décide d’aller au bar pour me familiariser."

        scene bar

        protag_pensee "C’est bien spacieux. Les verres sont soigneusement posés sur les étagères. Des caisses fraîches d’alcools attendent d’être alignées également. Le menu des boissons est affiché sur le mur de pierres."

        protag "Qu’avons nous là. Mojito, Piña Colada, Sex on the beach et le Cosmopolitan. Des propositions classiques on dirait. Tiens, des mocktails aussi: Virgin mojito et Virgin Piña Colada. Ils ne sont vraiment pas allés chercher bien loin."

        protag_pensee "Le comptoir est poussiéreux j’ai l’impression. Je prends un chiffon dans le lavabo et l’humidifie. Je le glisse sur la surface lisse, le nettoyant vite fait."
        protag_pensee "Brusquement, le bruit d’un verre se brisant me fait sursauter. Je me retourne. Les débris sont dispersés au sol."

        protag "Merde. Comment c’est tombé…"

        protag_pensee "Je ramasse les plus gros morceaux dans ma main. Ensuite je les jette prudemment à la poubelle. Avec le balai, je récupère le reste."
        protag_pensee "Et là, boum ! Une ampoule explose. Je sursaute à nouveau et me protège la tête d’un réflexe." with vpunch
        protag_pensee "Un silence puis un rire au loin. C’est une voix féminine. Je regarde autour de moi. Mais personne."

        menu:
            "Voir s’il y a quelqu’un.":
                
                $ courage += 5
                jump voir_quelquun

            "Appeler le patron avec le talkie-walkie.":
                jump appeler_thomas

        label voir_quelquun:

            protag_pensee "Je quitte le bar mais ne vois rien vers les tables ni la scène. C’est désert. Je suis seul(e). Tout ça m’empêche de réfléchir. J’ai comme appuyé sur le bouton automatique de mon corps. Ma bouche s’ouvre sans que j’y fasse quoi que ce soit."

            protag "Hé ! Il y a quelqu’un d’assez débile pour casser des trucs pour effrayer les gens ?"

            protag_pensee "Insulter est la meilleure façon pour moi de surmonter ma peur on dirait."

            jump retour_cabanon

        label appeler_thomas:

            protag_pensee "Je prends mon talkie-walkie à ma ceinture et l’allume. J’ai une légère boule au ventre et je pense à tous les scénarios possibles. J’entends le grésillement de la radio. J’appuie sur le bouton pour parler."

            protag "Allo ?"

            thomas "Je suis là. Un problème ?"

            protag_pensee "Je sursaute pour la troisième fois. Je reconnais la voix de mon patron et pivote. Le soulagement me fait soupirer discrètement."

            protag "Excusez moi monsieur. On a un souci d’ampoule."

            protag_pensee "Je pointe l’ampoule au-dessus du bar. Le boss souffle sûrement pour la énième fois aujourd’hui."

            thomas "On va s’en occuper. Laissez. Vous reviendrez ce soir sans faute."

            protag "Bien monsieur."

        label retour_cabanon:

        scene cabane

        protag_pensee "Je pars et retourne au cabanon pour défaire ma valise. J’essaie d’oublier ce que j’ai entendu. Je suis peut-être folle de fatigue tout simplement. Même si je ne me sens pas fatigué(e)."

        scene bar2

        protag_pensee "La nuit est bien tombée et le bar est rempli de nouveaux arrivants. Mon t-shirt du camping est un peu trop grand mais ça va."
        protag_pensee " Je prépare un virgin mojito pour une femme enceinte. Et mon collègue est à la caisse. J’ai eu une petite formation rapide pour me mettre dans le bain avant le début."

        $ habilete += 5

        protag_pensee "Je sers le mocktail à la dame avec un sourire chaleureux. J’aime bien mettre les gens à l’aise."

        protag_pensee "Au loin, [noa_name] passe pour rejoindre la forêt avec sa lampe torche. Il a les bras plein de paquets de marshmallows. Je comprends tout de suite et l’eau monte à ma bouche."

        protag_pensee "[noa_name] me fait un signe de main et en me montrant les bonbons. Je rends son coucou puis prépare un nouveau cocktail."

        protag_pensee "Un jeune homme approche et s’affale sur le tabouret face au bar. Il met ses écouteurs et lance un podcast. Je le regarde. Il parait frustré ou lassé. Il regarde dans le vide sans vraiment écouter."

        protag "Tu veux quelque chose ?"

        protag_pensee "Le jeune homme relève les yeux vers moi, les sourcils levés. Comme s’il était surpris que je lui adresse la parole. Son regard se détourne et il répond doucement."

        show ChrisBasic
        show screen loveMeter("Chris")
        with dissolve

        chris "Euh…quoi ?"

        protag "Tu veux boire…?"

        hide ChrisBasic
        show ChrisTimide 
        protag_pensee "Il ne semble pas trop savoir quoi faire. Il consulte rapidement la carte, cherchant rapidement."

        chris "Un simple shot de vodka s’il te plait."

        protag "Ok, ça arrive tout de suite."

        protag_pensee "Je prends un verre à shooter et y verse de la vodka délicatement. Ce serait préférable de ne rien renverser. Je le glisse ensuite sous son nez."

        hide ChrisTimide
        show ChrisPetitSourire
        chris "Merci…"

        hide ChrisPetitSourire
        show ChrisEffraye
        protag_pensee "Il boit son verre d’une traite. Et ce n’était pas une bonne idée dans son cas. Il s’étouffe légèrement et tousse, tapant sur sa poitrine." with vpunch 

        protag "Oula. T’as bu de travers. Tout va bien ?"

        chris "Ouais…ça va. Désolé."

        protag_pensee "Le silence s’installe. Il ne sait plus où se mettre, se contentant de boire. Son podcast est toujours dans sa main. Je peux lire le titre: “Faits divers”."

        menu:
            "Faire la conversation":
                
                $ curiosite += 5
                $ AF["Chris"] += 5
                jump conversation_chris

            "Le laisser tranquille.":
                jump laisser_chris

        label conversation_chris:
            hide ChrisEffraye
            show ChrisBasic

            protag "“Fait divers” ? De quoi parle ton podcast exactement ?"

            chris "Hum…des meurtres, des histoires paranormales, ce genre de trucs."

            protag "Cool. Et tu es tout seul ici pour t’isoler avec tes écouteurs ?"

            chris "Non, je suis avec ma famille. Mais j’avais pas vraiment envie de venir pour être honnête."

            protag_pensee "Tout ça me fait presque de la peine. Ce serait dommage que son séjour se déroule comme ça: écouteurs + shots de vodka."

            protag "C’est quoi ton nom ?"
            hide ChrisBasic
            show ChrisTimide
            chris "Chris. Pourquoi ?"

            $ chris_name = "Chris"

            protag "Et bien, [chris_name], sache qu’il y a une soirée histoires d’horreur devant le feu de camp. Cela pourrait te plaire."

            hide ChrisTimide
            show ChrisPetitSourire
            protag_pensee "Il hoche simplement la tête, réfléchissant sérieusement à la question."
            jump fin_bar_nuit

        label laisser_chris:
            hide ChrisEffraye
            show ChrisBasic
            protag_pensee "Je préfère le laisser tranquille. Il ne veut probablement pas discuter avec moi. Il remet tout simplement ses écouteurs, ne faisant plus attention à moi."

        label fin_bar_nuit:
            $ chris_name = "Chris"
            hide screen loveMeter
            hide ChrisPetitSourire
            hide ChrisBasic 
            with dissolve

            protag_pensee "L’heure sonne la fin de cette soirée au bar. Tout le monde commence à partir en direction du feu de camp."
            protag_pensee "Le jeune homme de tout à l’heure et sa famille aussi. Je ferme tout avec mon collègue puis me dirige moi aussi vers cet after."

            scene feu2

            protag_pensee "Le feu est flamboyant cette nuit et sa chaleur reste supportable dans la fraicheur. [noa_name] installe les gens sur les troncs. Les petits sont assis au sol et des chaises sont à disposition au cas où."

            protag_pensee "J’apporte des bouts de bois pour garder le feu lumineux. [noa_name], lui, ouvre les paquets de marshmallows et les plantes sur des branches. Il n’hésite pas à en manger un ou deux au passage."

            protag_pensee "Je l’aide à distribuer les brochettes puis m’installe sur une chaise face au feu. [noa_name] me rejoint, s’asseyant à côté de moi. Il me laisse le reste des marshamallows."

            show NoaBasic 
            show screen loveMeter("Noa")
            with dissolve

            noa "Salut tout le monde. Je suis [noa_name], l’animateur du club enfant. Certains parents m’ont rencontré cette après-midi pour l’inscription."

            protag_pensee "Les mamans le reconnaissent immédiatement et une petite fille lui fait un signe enthousiaste."

            noa "Ce soir, devant le feu, nous allons nous conter des histoires d’horreurs. Vous avez la responsabilité de vos enfants, je vous préviens."

            hide NoaBasic
            show NoaBasic2
            protag_pensee "Il le dit avec un petit rire et les autres le suivent dans sa blague."

            noa "Qui veut commencer ?"

            protag_pensee "Personne ne veut prendre la parole. Le crépitement du feu à lui seul brise le silence. Dans un coin, je vois les parents essayer de pousser leur fils à se lancer."

            "Les parents" "Aller [chris_name]. Tu écoutes littéralement des histoires d’épouvantes toute la journée."

            protag_pensee "Il refuse catégoriquement voulant faire taire ses parents. Je décide d’intervenir."

            protag "Vas-y toi. [chris_name], il me semble."

            protag_pensee "Chris se fige immédiatement en entendant son nom. On aurait dit que son corps se refermait face à tous ces regards sur lui maintenant."

        hide screen loveMeter
        show NoaBasic2 at left
        with move

        show ChrisTimide at right
        with dissolve

        chris "Euh…Je préfère pas, merci."

        menu:
            "Insister":
                $ AF["Chris"] -= 10
                $ AF["Noa"] -= 5
        
                jump insister_chris

            "Le laisser":
                $ AF["Chris"] += 5
                jump laisser_chris2

        label insister_chris:

            protag "Aller [chris_name]. On veut entendre ton histoire."

            protag_pensee "Chris reste silencieux, paralysé. Sa pomme d’Adam bouge alors qu’il déglutit de stresse."

            play sound "sfx/bad_choice.wav"

            jump suite_feu_camp

        label laisser_chris2:

            protag "D’accord, c’est pas grave."

        label suite_feu_camp:

        hide ChrisTimide with dissolve

        show screen loveMeter("Noa")
        show NoaBasic2 at center
        with move

        noa "C’est bon. Je vais démarrer avec mon histoire. Connaissez-vous Jane Doe ?"

        hide NoaBasic2
        show NoaBasic

        protag_pensee "L’activité passe très vite. Tout le monde a pris du plaisir malgré la peur. [chris_name] était plus fasciné qu’effrayé par ces histoires. Et [noa_name] racontait étonnament bien les contes horrifiques. J’ai senti quelques frissons aux moments angoissants mais c’était amusant malgré tout."

        protag_pensee "Les gens partent au fur à mesure vers leurs bungalows. Certains récupèrent les branches de brochettes et [noa_name] ramasse les déchets à jeter."

        protag_pensee "Ils finirent par me laisser eux aussi. Il ne reste que [noa_name]."

        hide NoaBasic
        show NoaNeutre
        noa "Tu ne vas pas dormir ?"

        protag "Je vais rester un peu. J’éteindrais le feu."

        noa "Ok. Merci."

        hide NoaNeutre 
        hide screen loveMeter
        with dissolve

        protag_pensee "[noa_name] part, je suis seul(e). La brise légère est agréable et le feu apaisant. Cela fait du bien, même si ce n’est que la première journée."

        protag_pensee "Soudain, un vent fort et noir complet. Je regarde alors le feu et il est éteint. Je sors immédiatement ma lampe torche de ma banane et éclaire autour de moi. L’ambiance est brutalement plus froide et malaisante."

        protag_pensee "J’ai cette horrible impression qu’on me regarde. Mais je ne sais pas d’où ça vient. C’est comme si c’était partout et nulle part à la fois. Je me retourne finalement très lentement. Je le sens au fond de moi. Cette chose est là."

        show JaneFlip with dissolve

        JaneDoe "Bouh !" with hpunch

        protag "AAAAAAHH !!!" with vpunch

        protag_pensee "C’est un putain de fantôme ! Bordel de merde ! Sans plus attendre, je prends mes jambes à mon cou. Faisant gaffe où je posais mes pieds. Ce serait stupide de me fracasser en pleine fuite."

        hide JaneFlip

        scene foret2
        with dissolve

        protag_pensee "Je finis dans la forêt et dans la panique, je me perds au milieu des arbres."

        protag "Tout se ressemble ici ! Merde !"

        protag_pensee "Je tourne pour trouver un chemin. Et là, ce fantôme apparait de nouveau et brusquement devant moi."

        show JaneFlip with dissolve

        protag "AAAAHH ! Laisse moi ! T’es mort ! Tu pouvais pas rester sous terre !" with vpunch

        protag_pensee "Je tombe sur mes fesses et ferme les yeux par réflexe. Comme si cela allait me protéger. Puis, rien. Il ne se passe rien." with hpunch

        hide JaneFlip
        show JaneRizz with dissolve
        protag_pensee "Et là…j’entend un rire. Le même rire féminin au bar. J’ouvre doucement les yeux. Je distingue un peu mieux les traits de ce fantôme. C’est une jeune femme."

        protag_pensee "Elle rit à chaudes larmes. Enfin, si ça peut pleurer. Je me détends. Malgré la détermination claire qu’elle a eue à m'effrayer, elle ne semble pas dangereuse."

        protag "Qui es tu ?"
        hide JaneRizz
        show JaneNeutre with dissolve

        protag_pensee "La miss fantôme ne dit rien. Elle me regarde un instant avant de disparaitre d’un seul coup. Je reste un moment sous le choc toujours au sol. Mais je finis par me relever lentement puis retourne au cabanon."

        hide JaneNeutre with dissolve

        show cabane

        jump j2
