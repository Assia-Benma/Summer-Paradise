label j7:

    call afficheJour(7)

    scene cabane

    protag_pensee "Le matin se lève. Je sors du cabanon encore à moitié endormi. 
    Quelqu’un semble m’attendre appuyé contre le mur."

    if ChoixDate == "Chris":
        jump dateChris
    elif ChoixDate == "Noa":
        jump dateNoa
    elif ChoixDate == "Jane":
        jump dateJane

    label dateNoa:
        show NoaBasic2
        show screen loveMeter(ChoixDate)
        with dissolve

        noa "Salut. Tu as pris ton temps pour te lever dis donc."

        protag "Mon corps est fait pour les grasses mat."

        noa "Évite quand même de faire ça tous les matins. Sauf si un 
        nouveau sermon du boss te tente. "

        protag "Comment tu sais ? "

        hide NoaBasic2
        show NoaPense
        noa "On est connu pour avoir des commères parmi les employés."

        protag "Il faudra que tu me dise lesquels."

        hide NoaPense
        show NoaBasic
        noa "Je préfère ne pas avoir de fantômes en plus, merci."

        protag "Sinon, pourquoi tu m’attendais ?"

        noa "Ça te dit une balade ? "

        protag "Si tu veux."

        scene foret

        hide NoaBasic
        show NoaTimide
        noa "Tu sais...ça fait un moment qu’on passe le plus clair de notre 
        temps ensemble. Et je me disais qu’on s’était vraiment bien 
        rapprochés."

        protag "C’est vrai."

        noa "Du coup...je disais qu’on pourrait devenir encore plus proche 
        que ça."

        protag_pensee "J’ai tout de suite compris où il voulait en 
        venir. Je sens mon coeur battre à toute vitesse. Oh la la, qu’il le 
        dise clairement, que je ne confonds pas les signes. "

        protag "C'est-à-dire ?"

        noa "Tu sais, arrête."

        protag "Non je sais pas."

        hide NoaTimide
        show NoaBasic2
        noa "Ok, très bien...Tu me plais beaucoup. Je dirais même que tu 
        m’attires depuis le début. "

        hide NoaBasic2
        show NoaTimide
        protag_pensee "Oh. Mon. Dieu. Les mots résonnent dans 
        ma tête. Pitié que je ne sois pas juste dans mon lit en train de 
        dormir."

        protag "Je..."

        hide NoaTimide
        show NoaBasic
        noa "Pas obligé de me répondre immédiatement. J’attendrai ce 
        soir, à la fête."

        protag "D’accord"

        menu:
            "Lui prendre la main":
                $ courage += 5
                $ AF["Noa"] += 5
                hide NoaBasic
                show NoaTimide
                protag_pensee "Ma main glisse dans la sienne. Nos doigts 
                s’entrecroisent, serrés. Un petit sourire apparaît au coin de ses 
                lèvres. Je crois que je vais disjoncter."
                
            "Ne rien faire":
                pass
        
        hide NoaTimide
        hide NoaBasic
        with dissolve
        jump suite_boum

    label dateChris:
        show ChrisBasic
        show screen loveMeter("Chris")
        with dissolve

        chris "Hey. Ça va ?"

        protag "Chris ? Qu’y a-t-il ?"

        hide ChrisBasic
        show ChrisPetitSourire
        chris "Hum. Rien. Je voulais juste te proposer une balade dans la 
        forêt."

        hide ChrisPetitSourire
        show ChrisTimide
        protag "Tu es sûr ? Tu n’arrives même pas à me regarder dans les 
        yeux. Et tes joues sont rouges."

        chris "T’inquiète."

        protag "Ok."

        protag_pensee "Il est comme un livre ouvert. Son 
        embarras est bien visible et j’avoue que j’adore ça. "

        scene foret

        hide ChrisTimide
        show ChrisHeureux
        chris "Ce séjour au camping était plus passionnant que ce que 
        j’aurais cru."

        protag "Heureusement que les fantômes étaient là pour nous 
        distraire. "

        hide ChrisHeureux
        show ChrisPetitSourire
        chris "Et heureusement que tu étais là toi aussi."

        protag "Enfin, les fantômes sont plus intéressants." 
 
        chris "Pas du tout. Tu es nettement plus intéressant(e) à mes yeux. 
        Vraiment plus." 
        
        protag_pensee "Wow. Mes poils se dressent sur mes bras. 
        Quand il est direct comme ça, ça m’électrise. Plus efficace que du 
        paranormal."

        menu:
            "Tu es intéressant aussi, Chris.":
                $ AF["Chris"] += 5
                hide ChrisPetitSourire
                show ChrisTimide
                chris "Hum...merci."
            "Ne rien dire":
                pass
        
        hide ChrisTimide
        hide ChrisPetitSourire
        show ChrisBasic
        protag "Hum...du coup ? Tu voulais me dire quelque chose ?" 
        
        chris "Ouais...c’est un peu...compliqué à dire."
        
        protag "Je ne me moquerai pas de toi."
        
        hide ChrisBasic
        show ChrisTimide
        chris "J’espère bien... Ok, voilà, tu me plais..." 
        
        protag "Hein ?"
        
        chris "Tu...{size=*0.5}me plais...{/size}"

        protag_pensee "Oh. Mon. Dieu. Les mots résonnent dans 
        ma tête. Pitié que je ne sois pas juste dans mon lit en train de 
        dormir." 
        
        protag "Je..." 
        
        chris "Ne me réponds pas maintenant !" 
        
        protag "Oh. OK." 

        hide ChrisTimide
        show ChrisPetitSourire
        chris "Ce soir à la fête, je serais prêt à l’entendre." 
        
        protag_pensee "On dirait qu’il s’attend à un râteau. Le 
        pauvre. Il préfère se torturer jusqu’à ce soir." 
        
        protag "D’accord."

        menu: 
            "Lui prendre la main":
                $ AF["Chris"] += 10
                $ courage += 5
                hide ChrisPetitSourire
                show ChrisTimide
                protag "Ma main glisse dans la sienne. Nos doigts 
                s’entrecroisent, serrés. Il devient si rouge comme je ne l’ai jamais 
                vu. Je crois que je vais disjoncter."
            "Ne rien faire":
                pass
        
        hide ChrisTimide
        hide ChrisTimide
        jump suite_boum
    
    label dateJane:
        show JaneBasic
        show screen loveMeter("Jane")
        with dissolve

        JaneDoe "Coucou ma/mon belle/beau."
 
        protag "Jane ? Je t’ai manqué depuis hier ?" 
        
        hide JaneBasic
        show JaneRizz
        with dissolve
        JaneDoe "Si tu crois que je vais te le dire, tu te mets les doigts dans 
        l'œil." 
        
        protag "Tu veux quoi ?" 
        
        JaneDoe "Passer du temps avec ma/mon raleuse/raleur." 
        
        protag "Je savais bien que je te manquais." 
        
        hide JaneRizz
        show JaneBasic
        with dissolve
        JaneDoe "Allez. Viens."

        scene foret

        JaneDoe "Je suis heureuse tu sais. Ça fait tellement longtemps que je 
        n’ai pas parlé à des vivants." 
        
        protag "Pourtant, tu étais très à l’aise." 

        hide JaneBasic
        show JanePense
        with dissolve
        JaneDoe "Ouais. Je pense qu'inconsciemment j’avais envie qu’on me 
        remarque." 
        
        protag "Inconsciemment ? Sûre de ça ?" 
        
        hide JanePense
        show JaneRizz
        with dissolve
        JaneDoe "Fais pas genre. Tu comprends ce que je veux dire."

        menu: 
            "Sans mon fantôme préféré, ce séjour aurait été très ennuyeux.": 
                $ AF["Jane"] += 10
                JaneDoe "Et sans ma/mon vivante/vivant préféré(e) aussi." 
                protag  "Mais qui te dis que je parlais de toi ? Je faisais allusion à 
                Cerbère." 
                hide JaneRizz
                show JaneBasic
                JaneDoe "Ha. Ha. T’es bête. Presque aussi drôle que moi."
                hide JaneBasic
            "Ne rien dire":
                pass
        
        hide JaneRizz
        show JaneNeutre
        with dissolve
        protag "Bon, dis moi." 
 
        JaneDoe "Quoi ?" 
        
        protag "Ces mots brûlent tes lèvres carrément." 
        
        hide JaneNeutre
        show JanePense
        with dissolve
        JaneDoe "Je ne peux rien te cacher on dirait. Ok... Tu me plais." 
        
        protag_pensee "Oh. Mon. Dieu. Les mots résonnent dans 
        ma tête. Pitié que je ne sois pas juste dans mon lit en train de 
        dormir." 
        
        protag "Répète." 
        
        hide JanePense
        show JaneRizz
        with dissolve
        JaneDoe "Non. Fallait ouvrir grand ses oreilles." 
        
        protag "Allez !" 
        
        JaneDoe "Ok, ok. Tu me plais. C’est bon ?" 
        
        protag "Oui. Et tu sais quoi ? Je..." 
        
        hide JaneRizz
        show JaneBasic
        with dissolve
        JaneDoe "Non, tais toi !" 
        
        protag "Pourquoi ? T’as peur de ma réponse." 
        
        JaneDoe "Je préfère attendre ce soir, à la boum." 
        
        protag "Comme tu veux. C’est ton problème."  

        hide JaneBasic
        with dissolve

        menu: 
            "Lui prendre la main":
                $ courage += 5
                $ AF["Jane"] += 10
                protag_pensee "Mes doigts traversent sa main. Merde 
                c’est vrai. J’avais complètement oublié."
                show JaneRizz
                with dissolve
                JaneDoe "Hahaha ! Tu as essayé de me prendre la main ? C’est trop 
                mignon."
                protag_pensee "Mes joues s’échauffent de gêne. 
                J’aimerais pouvoir la tuer une deuxième fois."
                protag "Je... Ta gueule !" with vpunch
            "Ne rien faire":
                pass
        
        hide JaneRizz
        with dissolve

        jump suite_boum
        
    label suite_boum:
        $ ajout_bonus(habilete,courage,curiosite)

        scene feu

        hide screen loveMeter
        with dissolve

        show NoaNeutre 
        with dissolve

        protag "La préparation de la boum se fait dans un 
        silence plutôt apaisant pour cette fin de semaine. Noa installe les 
        guirlandes dans les arbres."

        protag "Et moi, je pose les encas sur les tables 
        dressées. Jane s’est également incrustée. Pas étonnant." 
        
        show NoaNeutre at right with moveinright
        show JaneBasic at center with dissolve
        JaneDoe "C’est quoi ces trucs ? Ça a l’air dégueu." 
        
        protag "C’est des verrines surgelées." 
        
        hide JaneBasic
        show JaneNeutre
        with dissolve
        JaneDoe "Ah. C’est pour ça." 
        
        protag "Mais ceci va te plaire." 
        
        hide JaneNeutre
        show JaneRizz
        JaneDoe "Oh. Du punch !"

        protag "Ce serait pas une soirée sinon." 

        hide JaneRizz
        show JaneBasic at left with dissolve
        show ChrisHeureux at center with dissolve
        hide NoaNeutre
        show NoaBasic at right
        noa "Salut Chris."  

        chris "Bonsoir tout le monde. Besoin d’aide ?" 
        
        noa "Ouaip. Tu peux brancher ce truc s’il te plait." 
        
        chris "No problemo." 
        
        hide JaneBasic
        show JaneRizz at left
        with dissolve
        JaneDoe "Woah. De véritables illuminations." 
        
        protag_pensee "Nous avons enfin terminé. On est épuisé 
        avant même que les choses sérieuses ne commencent. Je regarde 
        mes trois amis improbables avec une forme de soulagement. Si on 
        peut le dire. Je ne suis pas resté(e) seul(e) longtemps à ce boulot." 
        
        protag "Quelle bande étrange nous formons tous les 4." 
        
        hide NoaBasic
        show NoaBasic2 at right
        noa "Tu l’as dit" 
        
        hide ChrisHeureux
        show ChrisPetitSourire at center
        chris "J’aurais pas pu souhaiter de meilleures vacances." 
        
        JaneDoe "Tu l’as dit, le binoclard. Moi non plus." 
        
        protag "Mais tu es tout le temps en vacances toi, Jane." 
        
        JaneDoe "Ouais, j’en ai de la chance." 
        
        hide NoaBasic2
        show NoaBasic at right
        noa "La fête va bientôt démarrer. On va pouvoir se lâcher." 
        
        JaneDoe "D’ailleurs j’ai invité les autres." 
        
        protag "Qui ?" 

        hide JaneRizz
        show JaneBasic at left
        with dissolve
        JaneDoe "Les autres fantômes du camping." 
 
        noa "Pitié soyez discrets." 
        
        hide ChrisPetitSourire
        show ChrisEffraye at center
        chris "Vous allez faire peur aux gens." 
        
        JaneDoe "Ok, ok. Ça va." 
        
        protag "Allez. C’est parti." 
        
        hide ChrisEffraye
        hide JaneBasic
        hide NoaBasic
        with dissolve

        scene feu2
        
        protag_pensee "La fête bat son plein. Les fantômes 
        profitent, invisibles ou cachés derrière les arbres. ils connaissent la 
        discrétion. Ouf." 
        
        protag_pensee "Je veux m’amuser moi aussi. Prenons 
        l’initiative."

        menu: 
            "Danser avec Noa":
                $ AF["Noa"] += 5
                jump danse_noa
            "Danser avec Chris":
                $ AF["Chris"] += 5
                jump danse_chris
            "Danser avec Jane":
                $ AF["Jane"] += 5
                jump danse_jane
        
    label danse_noa:
        show NoaNeutre
        show screen loveMeter("Noa")
        with dissolve
        protag "Hey...Noa." 

        noa "Hum ?" 
        
        protag "Tu danses mon cher ?" 
        
        hide NoaNeutre
        show NoaBasic
        noa "Avec plaisir." 
        
        protag_pensee "Génial ! C’était pas trop difficile. La 
        musique est si énergique. Un amas de gens sautent et s’enjaillent 
        sur la piste de danse."

        protag_pensee "Noa et moi nous joignons à la foule. Le 
        rythme nous emporte dans des pas aléatoires et dynamiques. Je 
        me laisse porter par le beat."

        menu:
            "Se rapprocher":
                $ AF["Noa"] += 10
                hide NoaBasic
                show NoaTimide
                protag_pense "Je me rapproche de Noa 
                sans arrêter de me déhancher. On se colle presque, pressé l’un 
                contre l’autre. Ses mains se posent sur ma taille et accompagnent 
                mes mouvements." 
 
                protag_pensee "Le temps ralentit tout à 
                coup, mes yeux rivés sur les siens. Mon coeur est sur le point de 
                faire un infarctus. Et j’adore ça. J’espère que lui aussi."
                
            "Continuer à danser": 
                pass

        hide NoaTimide
        hide NoaBasic
        hide screen loveMeter
        with dissolve
        jump retour_boum  

    label danse_chris:
        show ChrisBasic
        show screen loveMeter("Chris")
        with dissolve
        protag "Hey...Chris." 
 
        chris "Oui ?" 
        
        protag "Tu danses avec moi ?" 
        
        hide ChrisBasic
        show ChrisTimide
        chris "Oh. Euh...oui. Bien sûr !" 
        
        protag_pensee "Génial ! C’était pas trop difficile. La 
        musique est si énergique. Un amas de gens sautent et s’enjaillent 
        sur la piste de danse."  
        
        hide ChrisTimide
        show ChrisHeureux
        protag_pensee "Chris et moi nous joignons à la foule. Le 
        rythme nous emporte dans des pas aléatoires et dynamiques. Chris 
        est légèrement maladroit dans ses gestes et pourtant ça le rend 
        encore plus attirant. Je me laisse porter par le beat, les yeux 
        fermés."

        menu:
            "Se rapprocher":
                hide ChrisHeureux
                show ChrisPetitSourire
                protag_pensee "Je me rapproche de Chris 
                sans arrêter de me déhancher. On se colle presque, pressé l’un 
                contre l’autre. Il est hésitant dans ses gestes, ne sachant pas 
                comment s’y prendre. Je saisis ses mains et les pose sur ma taille, 
                accompagnant mes mouvements." 
 
                protag_pensee "Le temps ralentit tout à 
                coup, mes yeux rivés sur les siens. Je le sens se laisser aller contre 
                moi. Mon coeur est sur le point de faire un infarctus. Et j’adore ça. 
                J’espère que lui aussi."
            "Continuer à danser":
                pass
        
        hide ChrisHeureux
        hide ChrisPetitSourire
        hide screen loveMeter
        with dissolve
        jump retour_boum

    label danse_jane:
        show JaneNeutre
        show screen loveMeter("Jane")
        with dissolve
        protag "Hey...Jane." 
 
        JaneDoe "Oui ma/mon belle/beau ?" 
        
        protag "Tu danses avec moi ?" 
        
        hide JaneNeutre
        show JaneBasic
        with dissolve
        JaneDoe "Hum ? On prend les devants on dirait. Amène toi." 
        
        protag_pensee "Génial ! C’était pas trop difficile. La 
        musique est si énergique. Un amas de gens sautent et s’enjaillent 
        sur la piste de danse. Mais, je rejoins Jane à l’écart du côté des 
        esprits." 
        
        protag_pensee "Jane et moi nous joignons aux spectres 
        entre les chênes. Le rythme nous emporte dans des pas aléatoires 
        et dynamiques. Jane exécute plusieurs figures dans les airs. C’est 
        l’avantage de pouvoir léviter. Je me laisse porter par le beat, les 
        yeux fermés."

        menu:
            "Se rapprocher":
                $ AF["Jane"] += 10
                jump disscusion_jane
            "Continuer à danser":
                hide JaneBasic
                hide screen loveMeter
                with dissolve
                jump retour_boum

        label disscusion_jane:
            hide JaneBasic
            show JaneRizz
            with dissolve
            protag_pensee "Je me rapproche de Jane 
            sans arrêter de me déhancher. Si seulement je pouvais la serrer 
            dans mes bras. Malheureusement, elle n’est pas physiquement là, 
            en vie." 
 
            protag_pensee "Cette réalité me frappe et 
            absorbe tout le plaisir de faire la fête. Le temps ralentit tout à coup, 
            mes yeux rivés sur les siens."  

            hide JaneRizz
            show JaneBasic
            with dissolve
            JaneDoe "Que se passe t-il chéri(e) ?" 

            protag "Je me rends compte...qu'il ne nous sera 
            jamais possible de nous toucher." 

            hide JaneBasic
            show JaneNeutre
            with dissolve
            protag_pensee "Elle arrête tout mouvement 
            et se rapproche de moi. Ses mains se placent sur les miennes, 
            simulant de me les tenir." 
 
            JaneDoe "Ferme les yeux." 
 
            protag "Quoi ? Je te parle d’un truc sérieux." 
 
            JaneDoe "Je suis tout aussi sérieuse." 
 
            protag "Ok." 

            hide JaneNeutre
            with dissolve

            show JanePense
            with dissolve

            JaneDoe "Imagine...la chaleur de mes mains, la texture 
            de ma peau, la pression de mes doigts. Et à quel point cela fait 
            battre ton cœur." 
 
            protag_pensee "Je me concentre sur sa 
            voix et l’illusion de son toucher. Mon coeur est sur le point de faire 
            un infarctus. Comme quoi, ça marche pour de vrai. J’adore ça."
 
            protag "Merci." 
 
            JaneDoe "J’aimerais autant que toi pouvoir le faire tu 
            sais." 
            hide JanePense
            hide screen loveMeter
            with dissolve
            jump retour_boum

    label retour_boum:

        scene feu2
        
        protag "La soirée finit par se tasser. Les campeurs 
        rentrent peu à peu à leur bungalow. Et la personne qui occupe mes 
        pensées s’assoit seule sur un tronc au coin du feu."

        menu:
            "C'est Noa" if get_love_level("Noa") >= 7:
                jump fin_noa
            "C'est Chris" if get_love_level("Chris") >= 7:
                jump fin_chris
            "C'est Jane" if get_love_level("Jane") >= 7:
                jump fin_janedoe
            "C'est personne":
                jump fin_seule
        
        label fin_seule:
            protag "Personne. Rien de très concluant sentimentalement. C’est 
            pas plus mal peut-être. Même si c’est dommage...Je n’aurais pas 
            pu mieux finir la soirée." 

            protag_pensee "Je rentre enfin chez moi. Valise rangée 
            dans le coffre, assise sur mon siège dans le car, je suis prête pour 
            les adieux." 
            
            protag_pensee "Ce job était de loin le meilleur: été, feu de 
            camp, canons, fantômes et, bien évidemment, le salaire." 
            
            protag "Quel été. On se refera ça !"

            return 






        
