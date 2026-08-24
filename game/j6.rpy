label j6:

    define config.menu_include_disabled = True

    call afficheJour(6)

    scene cabane

    protag_pensee "Je n’ai pas arrêté de penser à hier. Le fait
    que l’on partage ce secret maintenant: Chris, Noa, Jane et moi. Et
    Cerbère, on peut dire."

    protag_pensee "Je pense surtout ầ cette personne.
    J’aurais jamais cru tomber sur quelqu’un comme ça à ce camping."

    protag_pensee "Je devrais lui proposer une rencontre au
    bar. J’ai une surprise."

    window auto

    call screen dateChoice

    label noaDate:

        $ AF["Noa"] += 10

        protag_pensee "Je vais voir Noa. Il a été un vrai guide et
        soutien, ici. C’est celui en qui j’ai le plus confiance."

        scene foret

        protag_pensee "Il s’occupe de la dernière activité de la
        semaine à l’accrobranche. Tous les enfants sont dans le parcours,
        bien accrochés."

        protag "Salut Noa."

        show NoaTimide
        show screen loveMeter("Noa")
        with dissolve

        noa "Salut, tu n’as rien à faire aujourd'hui ?"

        protag "Non, je suis libre. Alors, comment ça va depuis hier ?"

        hide NoaTimide

        show NoaPense
        with dissolve

        noa "Et bien…c’est encore assez déroutant. Mais je commence à
        m’y faire. En fait, je l’ai toujours su d’une certaine façon. Avec
        toutes ces histoires…Le déni j’imagine."

        protag "Je te comprends tu sais. Mais avec Jane qui apparaissait
        partout, je n'ai pas eu le temps de vraiment le digérer."


        noa "C’est sûr. C’est vraiment elle qui m’a poussé dans l’eau."

        protag "Techniquement non. Jane a poussé Cerbère à le faire."

        noa "Le chien ?"

        protag "Ouaip. Je t’ai jamais demandé…tu fais quoi en dehors du job
        au camping."

        hide NoaPense

        show NoaBasic
        with dissolve

        noa "Ben…là j’attends les résultats d’une formation, le DEES. On
        va voir si je suis diplômé."

        protag "Ah oui ? Je sais que tu vas réussir."

        menu:
            "Mais c’est quoi le DEES ?":
                $ AF["Noa"] += 5
                $ curiosite += 5

                noa "Le Diplôme d’Etat d’Educateur Spécialisé. Comme le
                nom l’indique, c’est pour être éducateur spécialisé. Ça ne doit pas
                être surprenant, je suis animateur."
                protag "Tu aimes beaucoup les enfants, hein ?"
                noa "Ouais. J’ai envie d’en faire mon métier."
                protag "Tu me diras pour les résultats."
                noa "Tu seras la/le deuxième à le savoir, après ma mère."

            "Je connais le DEES.":
                $ AF["Noa"] += 5

                protag "Tu veux être éducateur spécialisé ? Je te vois bien
                dans ce rôle."
                noa "Ah ouais ?"
                protag "Tu sais t’y prendre avec les petits et tu sais gérer les
                problèmes. Comme quand le garçon a été blessé, tu l’as guéri."
                noa "Merci de me dire ça."
                protag "Je le pense."
            
            "Ne rien dire.":
                pass
        
        protag "Je me demandais…ça te dirait de me rejoindre cet
        après-midi au bar."

        hide NoaBasic

        show NoaTimide
        with dissolve

        noa "Ouais. Pourquoi ?"

        protag "Surprise."
        
        noa "J’ai encore plus envie de venir maintenant."

        protag "Juste savoir que tu passerais du temps avec moi devrait te
        donner envie."
        
        noa "Mais je n’ai jamais dit le contraire."

        protag_pensee " Est ce qu’on flirte là ? Ouah. J’ai pas
        l’habitude. Je crois ? Il a ce sourire en coin qu’il le confirme en tout
        cas. Mon cœur s’emballe et je me sens surexcité(e). Vivement cet
        aprem."

        hide NoaTimide

        scene bar

        protag_pensee "Je prépare les ingrédients pour mon
        cadeau. Voyons voir la carte. Je vais l’impressionner avec mon
        talent en mixologie. Prions pour que j’en ai du talent."

        show NoaTimide
        with dissolve

        noa "Je suis là."

        protag_pensee "Il s’accoude au comptoir, légèrement
        penché vers moi. C’est assez perturbant."

        noa "Alors ?"

        protag "Hum…et bien…prépare toi à perdre la tête avec ma magie
        de barmaid."
        
        noa "De la magie ? A ce point ? Je m’attends à ce que ce soit léger,
        attention."

        call bar_minigame_crush("Virgin Mojito", "reussiNoaBoisson", "echecNoaBoisson")

        label reussiNoaBoisson: 
            $ AF["Noa"] += 5
            $ habilete += 5

            protag_pensee "Je fais comme je l’ai appris. Je
            mélange les ingrédients et les secoue au shaker. Je suis
            généreux(se) dans les doses puis verse le tout dans un verre à
            cocktail."
            protag "Voilà, mon cher Noa."
            noa "Lequel tu m’as servi ?"
            protag "Un Virgin Mojito, un classique."
            noa "Parfait, tu pouvais pas me faire rêver plus."
            protag "Régale toi."
            protag_pensee "Il le sirote avec plaisir dans ses
            yeux."
            noa "Tu as un vrai talent. Je suis presque jaloux."
            protag "Je t’apprendrais si tu veux."
            noa "Avec plaisir. Mais il va falloir que j’y aille. M.Tomas
            m’attend."
            protag "D’accord, bye."

            hide NoaTimide

            jump endDate
        
        label echecNoaBoisson:

            hide NoaTimide

            show NoaNRV
            with dissolve

            noa "Désolé mais je ne bois pas d’alcool. Je crois te l’avoir
            déjà dit."

            protag "Oh. Mince, excuse moi."

            noa "C’est pas grave. Je dois retourner bosser de toute
            façon."

            protag "D’accord, bye."

            hide NoaNRV

            protag_pensee "Il n’y a pas du tout touché. Je suis
            trop con(ne). Pourquoi je lui ai proposé de l’alcool ?!"

            jump endDate

    label endDate:
        hide screen loveMeter

        protag_pensee "Bon. Moi, je vais rester au bar jusqu’à ce
        soir. J’ai que ça à faire."

        jump finEpisode

    ### Date Chris

    label chrisDate:

        $ AF["Chris"] += 10

        protag_pensee "Je vais voir Chris. Mon partenaire de
        chasse au fantôme. Toute cette histoire nous a bien rapprochés et
        je ne vais pas m’en plaindre."

        scene feu

        protag_pensee "Quand j’arrive, Chris joue avec Cerbère. Il
        semble essayer de le dresser."

        show ChrisHeureux at left
        show Cerbere at right 
        show screen loveMeter("Chris")
        with dissolve

        chris "Allez Cerbère. Tu peux le faire. Assis !"

        protag_pensee "Le beagle se roule par terre, se remuant
        joyeusement."

        chris "Ok, bon, c’est un début."

        protag "Tu galères ?"

        hide ChrisHeureux
        show ChrisPetitSourire at left 
        with dissolve

        chris "Salut. Ouais, il ne comprend pas. Mais ce n'est pas grave
        mon grand."

        protag_pensee "On s’assoit côte à côte sur un tronc, nos
        épaules s’effleurent. J'en ai des frissons. Cerbère lévite au-dessus
        du feu de camp éteint."
        hide Cerbere with dissolve
        show ChrisPetitSourire at center with moveinright
        protag "Dis moi, Chris. Pourquoi tu enquête autant sur le paranormal
        si ça te fait aussi peur ?"

        chris "Oh…euh…je copie les Ghostbusters c’est tout. Je les ai
        toujours trouvé super cool et j’avais besoin de me sentir spécial
        comme eux."

        chris "Puis, plus je me plongeais dans cet univers, plus ces
        histoires étranges me fascinaient."

        protag "Je vois. Découvrir ces fantômes, c'est un rêve qui se réalise
        pour toi."

        hide ChrisPetitSourire

        show ChrisTimide
        with dissolve

        chris "Ouais. Je peux me considérer comme un vrai chasseur de
        fantômes maintenant. Enfin, j’imagine."

        menu:
            "C’est surtout moi qui ait fait la majorité du travail.":
                $ AF["Chris"] -= 5
                play sound "sfx/bad_choice.wav"
                hide ChrisTimide

                show ChrisNRV
                with dissolve

                chris "Oui, tu as raison. Désolé, je m’emporte un peu. Je ne
                suis pas un chasseur de fantômes. Tu l’es plus que moi."
                protag "Je…c’est pas ce que je voulais dire."
                chris "Oublie. On s’en fiche."

                hide ChrisNRV

            "Tu en es un. Je n'aurais jamais vu autant sans toi.":
                $ AF["Chris"] += 10

                hide ChrisTimide

                show ChrisHeureux
                with dissolve

                chris "Merci. Vraiment. Ça me soulage. Ce que tu penses
                de moi est important à mes yeux."
                protag "Je le pense, sois sûr."
                protag_pensee "Il me sourit. Il semble heureux et
                pleinement détendu. J’aime le voir comme ça."

                hide ChrisHeureux

        show ChrisBasic
        with dissolve

        protag "Je me demandais…ça te dirait de me rejoindre cet
        après-midi au bar."

        chris "Euh ouais. Ok ça marche."

        protag "J’ai une surprise."

        hide ChrisBasic

        show ChrisPetitSourire
        with dissolve

        chris "Sérieux ? Cool. Je serais là."

        protag "A toute. Je ne tolérerais aucun retard."

        chris "Ne t’inquiète pas."

        hide ChrisPetitSourire

        scene bar

        protag_pensee "Je prépare les ingrédients pour mon
        cadeau. Voyons voir la carte. Je vais l’impressionner avec mon
        talent en mixologie. Prions pour que j’en ai du talent."

        show ChrisPetitSourire
        with dissolve

        chris "Je suis pas en retard."

        protag "Je vois ça. Cerbère avec toi ?"

        chris "Non. Il est avec Jane. Du coup cette surprise ?"

        protag "Je vais te montrer mes talents de barmaid."

        chris "Impressionne moi. Quelque chose qui est à la carte."

        protag_pensee "Chris s’assoit correctement face à moi.
        Ses mains sont sur ses cuisses et me regarde sans rien dire."

    call bar_minigame_crush("Cosmopolitan","goodChris","badChris")

    label goodChris:
        $ AF["Chris"] += 10
        $ habilete += 5

        protag_pensee "Je fais comme je l’ai appris. Je
        mélange les ingrédients et les secoue au shaker. Je suis
        généreux(se) dans les doses puis verse le tout dans un verre à
        cocktail."

        protag "Voilà, mon cher Chris."

        hide ChrisPetitSourire

        show ChrisHeureux
        with dissolve

        chris "Génial ! Le Cosmopolitan est mon préféré."
        protag "Ah ouais ? C’est la première fois que je te le sers."
        chris "Je vais le savourer alors."
        protag_pensee "Il le sirote avec un certain plaisir
        dans ses yeux."
        chris "C’est le meilleur Cosmopolitan de ma vie."
        protag "Je veux un avis honnête, Chris."
        chris "Je ne te mentirais pas."
        protag "Ok, je te crois."
        chris "Il va falloir que je parte. Désolé. Mes parents veulent
        qu’on se retrouve au lac pour ce soir."
        protag "Pas de souci. Vas-y"

        hide ChrisHeureux

        jump endDate

    label badChris:
        $ AF["Chris"] -= 5
        play sound "sfx/bad_choice.wav"
        protag "Voilà, mon cher Chris."

        hide ChrisPetitSourire

        show ChrisBasic
        with dissolve

        play sound "sfx/bad_choice.wav"

        protag "Tu sembles déçu."
        chris "Ouais…hum…c’est pas mon truc haha... Mais
        tant pis. Je suis sûr que c’est bon."
        protag_pensee "Il boit le mocktail silencieusement,
        impossible de savoir ce qu'il pense."
        chris "Bon, il va falloir que je parte. Désolé. Mes parents
        veulent qu’on se retrouve au lac pour ce soir."
        protag "Quoi ? Déjà ?"
        chris "Ouais, désolé."
        protag "Pas de souci. Vas-y"

        hide ChrisBasic

        jump endDate


    ### Date Jane

    label janeDate:

        $ AF["Jane"] += 10

        default drinkDrity = False

        protag_pensee "Je vais voir Jane. Mon insupportable
        fantôme. Mais aussi la plus mignonne. Qui l’aurait cru. Pas moi. Et
        pourtant, je veux la voir. C’est ennuyant ici sans elle."

        scene foret

        protag_pensee "La journée aide à ne pas flipper dans cette
        forêt. Où est-elle ?"

        show JaneFlip
        show screen loveMeter("Jane")
        with dissolve

        JaneDoe "Bouh !" with vpunch

        protag "Oh ! Putain de merde ! Jane !"

        hide JaneFlip
        show JaneBasic
        with dissolve

        JaneDoe "Oui ma belle/mon beau ?"

        protag "Si je pouvais, je t'étranglerai."

        JaneDoe "Désolée mais ce n'est pas mon délire. Mais si tu kiffes le
        BDSM, je ne te juge pas."

        protag "Comment tu fais pour partir aussi loin ?"

        JaneDoe "J’ai beaucoup d’imagination. Sinon pourquoi tu me cherches?"

        protag "J’avais simplement envie de te voir."

        hide JaneBasic

        show JanePense
        with dissolve

        JaneDoe "Sérieux ?"

        protag "Je suis aussi choqué(e) que toi."

        hide JanePense

        show JaneRizz
        with dissolve

        JaneDoe "Cela ne me déplait pas pour autant. C’est adorable."

        protag "Tu es toute seule ?"

        hide JaneRizz

        show JaneBasic
        with dissolve

        JaneDoe "Ouais, Cerbère est avec Chris."

        protag "Vous êtes très proches, ce chien et toi."

        JaneDoe "Ouais. On se colle depuis qu’il est devenu un esprit."

        protag "Ah oui ?"

        hide JaneBasic

        show JanePense
        with dissolve

        JaneDoe "En fait…pour tout te dire…j’étais là à sa fin."

        protag "Oh."

        JaneDoe "Je l’ai aperçue, ce jour-là, tout seul attaché à cet arbre. Il
        aboyait et tentait de se libérer. Je suis restée près de lui les jours
        qui ont suivis. Il…il a fini par mourir de faim et de soif."

        protag "Quelle horreur. Mais comment se fait-il que personne ne l’ait
        retrouvé ?"

        JaneDoe "Le camping avait fermé après les vacances d’été. Il n’y avait
        donc plus personne sur place. Je l’ai accueillie quand il s’est
        transformé en fantôme et on ne s'est plus quittés depuis."

        hide JanePense

        show JaneBasic
        with dissolve

        protag "Je vois… Vous faites les 400 coups ensemble maintenant."

        JaneDoe "Ouais. Je veux que sa vie après la mort soit plus mémorable
        que sa vie tout court."

        protag "Il a de la chance de t’avoir."

        JaneDoe "Merci. Et Chris aussi d’ailleurs. Je pense que ça fait du bien à
        Cerbère d’avoir un vivant avec qui s’amuser."

        protag "Je veux te remonter le moral."

        JaneDoe "Oh tu sais, ça fait un moment que ça s’est passé."

        protag "Je m’en fiche."

        hide JaneBasic

        show JaneRizz
        with dissolve

        JaneDoe "D’accord ! C’est ton défi du jour. Redonne-moi le sourire."

        protag "Alors rendez-vous cette après-midi au bar."

        JaneDoe "Mon endroit préféré. Je serais là."

        hide JaneRizz

        scene bar

        protag_pensee "Je prépare les ingrédients pour mon
        cadeau. Voyons voir la carte. Je vais l’impressionner avec mon
        talent en mixologie. Prions pour que j’en ai du talent."

        show JaneRizz
        with dissolve

        JaneDoe "Présente !" with vpunch

        protag "Putain ! Tu m'as fait peur."

        hide JaneRizz

        show JaneBasic
        with dissolve

        JaneDoe "Pas désolée. Alors, ce remontant ?"

        protag "Je vais t’impressionner de mon savoir-faire."

        JaneDoe "Une démonstration en direct ? Quelle chance."

        protag "Jane lévite au-dessus de moi, me
        regardant performer."

        call bar_minigame_crush("Dirty Shirly", "goodJane", "badJane")

        label goodJane:
            $ AF["Jane"] += 10
            $ habilete += 5
            $ drinkDirty = True

            protag_pensee "Je fais comme je l’ai appris. Je
            mélange les ingrédients et les secoue au shaker. Je suis
            généreux(se) dans les doses puis verse le tout dans un verre à
            cocktail."

            protag "Voilà, ma chère Jane."

            hide JaneBasic

            show JaneRizz
            with dissolve

            JaneDoe "C’est pas vrai. Tu as vraiment appris la recette ?"
            protag "Évidemment. Et si tu as reconnu, ça veut dire que
            j’ai géré."
            JaneDoe "Ça me fait si plaisir."

            jump janeDrink

        label badJane:
            $ AF["Jane"] += 5
            $ habilete += 5

            protag_pensee "Je fais comme je l’ai appris. Je
            mélange les ingrédients et les secoue au shaker. Je suis
            généreux(se) dans les doses puis verse le tout dans un verre à
            cocktail."

            protag "Voilà, ma chère Jane."

            JaneDoe "Un classique, je vois."
            protag "C’est souvent les meilleurs."
            JaneDoe "J’approuve."

            jump janeDrink


        menu janeDrink:
            "Régale toi.":
                $ AF["Jane"] -= 5
                play sound "sfx/bad_choice.wav"

                show JaneNRV
                with dissolve

                JaneDoe "Euh… Allo… Je suis un fantôme.
                Si je pouvais boire, je serais saoule depuis un bail."
                protag "Ouais…J’ai oublié.
                Excuse-moi."
                JaneDoe "Pas grave."

                play sound "sfx/bad_choice.wav"

                hide JaneNRV

                jump suiteJane
                
            "Je bois en ton honneur.":
                $ AF["Jane"] += 5

                show JaneBasic
                with dissolve

                JaneDoe "Je suis flattée par tant
                d’attention."
                protag "Compte sur moi pour t’en
                donner."

                "" "..."

                JaneDoe "Alors ?"

                hide JaneBasic

                if drinkDirty == True:
                    jump dirtyJane
                jump drinkResultJane

        label dirtyJane:
            protag "C’est super bon !"

            show JaneRizz
            with dissolve

            JaneDoe "Tu vois pourquoi j’étais accro."
            protag "Oui clairement."

            hide JaneRizz

            jump suiteJane

        label drinkResultJane:

            show JaneBasic
            with dissolve

            protag "Je suis définitivement doué(e)."
            JaneDoe "Mais c’est qu’elle/il prend la grosse tête."
            protag "Pas du tout, c’est la vérité."

            hide JaneBasic

            jump suiteJane

        label suiteJane:

            show JaneBasic
            with dissolve

            JaneDoe "Bon, je vais disparaître."
            protag "Déjà ?"
            JaneDoe "Je suis peut-être un fantôme mais j’ai des choses à faire."
            protag "Encore des bêtises sûrement."
            JaneDoe "Exact."

            hide JaneBasic
            with dissolve

            jump endDate

    label finEpisode:

        scene bar2

        protag_pensee "Nouvelle animation pour cette soirée. Noa
        fait un blind test sur des musiques des années 80, 90 et 2000. Il
        s’amuse à chanter au micro."

        protag_pensee "Chris est là avec sa famille. C’est la
        première fois que je le vois participer aussi activement. Ça fait
        plaisir."

        protag_pensee "Jane est également ici. Cachée derrière
        un arbre, elle regarde le show avec Cerbère."

        protag_pensee "Je bosse comme d’habitude, rien de
        nouveau. Puis M.Thomas me rejoint au bar."

        show thomas
        with dissolve

        thomas "Tout se passe bien ?"

        menu:

            "Oui monsieur":
                $ habilete += 5
            
            "J’ai hâte que ça se termine.":
                pass

    
        thomas "Ok. Demain, changement de programme. La boum de
        fin de semaine se fera au feu de camp et non au bar."

        protag "Cool."

        thomas "Ça ne veut pas dire que tu ne travailleras pas. Avec
        Noa, vous vous assurez du bon déroulement."

        protag "Bien, c’est noté."

        hide thomas

        protag_pensee "La journée se termine. Hâte de demain
        soir."

    call bar_minigame("Mojito", "j7")