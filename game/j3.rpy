label j3: 
    
    call afficheJour(3)

    #Cabanon de nuit 

    protag_pensee "Je suis allongé(e) dans mon lit essayant vainement de m’endormir. Mon corps se tourne et se retourne sans cesse."

    chris "AAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHH !" with vpunch 

    protag_pensee "Je bondis à ce cri lointain. C’est Chris, je le reconnais." with hpunch
    protag_pensee "On est encore au beau milieu de la nuit, il fait noir dehors. Personne n’est réveillé."
    protag_pensee "Je prends une lampe torche et m’arme d’une batte. C’est toujours mieux que rien."
    protag_pensee "Je quitte le cabanon me dirigeant prudemment vers le lieu du hurlement."
    $ courage += 10

    #Forêt de nuit 

    protag_pensee "Le silence m'étourdit. Dans le noir, tous les coins se ressemblent. 
    Ma vision m’illusionne d’ombres et de faux monstres. Mes muscles se tendent d’appréhension."
    protag_pensee "Brusquement, quelqu’un me fonce dessus. Ce poids lourd me plaque au sol sans que je puisse faire quoique ce soit."

    protag "Ah ! Dégage !" with vpunch
    protag_pensee "La batte m’échappe dans notre chute à quelques mètres. Je me débats dans l’obscurité. 
    Dans un réflexe inattendu, je donne un coup puissant entre les jambes de mon assaillant. Puis je me redresse debout."

    show ChrisEffraye
    show screen loveMeter("Chris")
    chris "Arg !" with vpunch

    protag "Chris ?"

    protag_pensee "Il se retourne sur le sol, se tenant l'entrejambe et gémissant de douleur."

    menu:
        "Le reprocher pour la frayeur.":
            $ AF["Chris"] -= 5
            play sound "sfx/bad_choice.wav"

            protag "Merde, Chris. J’ai failli avoir une crise cardiaque."
            hide ChrisEffraye
            show ChrisTimide
            chris "Désolé. Désolé vraiment."
            hide ChrisTimide

        "S’excuser":
            $ AF["Chris"] += 5
            protag "Mince, excuse moi. Je croyais qu’on m’attaquait."
            hide ChrisEffraye
            show ChrisBasic
            chris "C’est rien…J’espère seulement que ça marche encore en bas."
            hide ChrisBasic

    show ChrisEffraye
    protag_pensee "Il se relève difficilement. Je prends son bras pour l’aider."

    protag "Qu’est ce qui t’es arrivé ? Je t’ai entendu crier."

    chris "Je…Je pense…avoir vu un fantôme."

    protag_pensee "Bizarrement, cette nouvelle fut réjouissante. Je ne suis plus seul(e) dans cette galère."

    protag "Mais c’est génial !"

    hide ChrisEffraye
    show ChrisPetitSourire
    chris "Hein ? Oui…dans un sens. J’ai enfin pu en voir un."

    protag "Quel fantôme précisément ? Une jeune femme ?"

    hide ChrisPetitSourire
    show ChrisTimide
    chris "Euh…non. Cela ressemblait plutôt à un chien."

    protag "Un chien ?"

    hide ChrisTimide
    show ChrisBasic
    chris "Ouais."

    protag "Bon. On ferait mieux d’en reparler plus tard. Retournons dormir."

    protag_pensee "La forêt en pleine nuit fait trop flipper pour avoir une discussion sur le paranormal."

    hide ChrisBasic
    show ChrisEffraye
    chris "Tu as raison. C’est trop flippant ici."

    protag "On est d’accord."

    protag_pensee "Sur ce, on se quitte."
    hide ChrisEffraye 
    hide screen loveMeter
    with dissolve
    #Décor : Bar

    protag_pensee "Après ce sommeil mouvementé, je manque d’énergie pour aujourd’hui. J’ai entre les mains une caisse pleine de bouteilles pour ce soir."

    protag_pensee "Je pose délicatement la caisse sur le comptoir puis étire mon dos."

    menu:
        "Laisser les bouteilles dans la caisse jusqu’à la soirée.":
            jump laisser_caisse

        "Les ranger de suite":
            $ habilete += 5
            jump ranger_caisse

    label laisser_caisse:

        show thomas with dissolve

        thomas "Je peux savoir ce que tu fabriques ? Range moi ça." with vpunch

        protag "Oui…"

        protag_pensee "Je laisse échapper un râle silencieux alors que je place les alcools."

        jump suite_thomas

    label ranger_caisse:

        protag_pensee "J’entame ma corvée alors que M.Thomas arrive."

        show thomas with dissolve

    label suite_thomas:

    thomas "Bien. Demain matin à la première heure j’aurais besoin de toi pour l’inventaire du matériel sportif. On a de nouveaux équipements à caser."

    protag "Pas de problème."

    protag_pensee "Il s’éloigne enfin. Je suis nerveux(se) dès que le patron est à proximité."

    hide thomas with dissolve

    protag_pensee "D’un seul coup, la caisse s’ouvre brutalement. Je me cogne à l’étagère d’un sursaut."

    protag "Aie ! Putain !" with vpunch

    protag_pensee "Des pièces sont semées partout sur le sol. Jane se téléporte devant moi sans que je m’y attende. Elle garde ce sourire malicieux que je déteste peu à peu."

    show JaneRizz 
    show screen loveMeter("Jane")
    with dissolve

    protag "Encore toi ? T’as vraiment pas d’amis."

    hide JaneRizz
    show JaneBasic
    JaneDoe "De vivant et grincheux ? Non, c’est vrai, tu es la/le seul(e)."

    protag_pensee "Je lève les yeux au ciel, lassé(e) de son attitude."

    protag "T’as que ça à faire que d’emmerder les gens ?"

    JaneDoe "Pour le coup, oui."

    protag "Ouais. Question stupide."

    JaneDoe "Toujours rabat joie et râleuse ?"

    protag_pensee "Mes nerfs sont à vif, ça y est. Je serre les poings pour me calmer."

    protag "Et toi toujours fourbe et chiante ?"

    hide JaneBasic
    show JaneNRV

    JaneDoe "Oh ! wow ! Tu as dis fourbe ? Un nouveau mot dans ton vocabulaire, dommage que ça se suive d’un mot vulgaire. Tu ne risques pas de plaire comme ça."

    menu:
        "Abandonner et retourner travailler.":
            jump abandonner_jane

        "Répondre":
            $ AF["Jane"] += 5
            jump repondre_jane

    label abandonner_jane:

        protag_pensee "J’inspire à fond et ramasse les pièces au sol."
        hide JaneNRV
        show JaneRizz
        JaneDoe "Hé ! Tu as perdu ta langue ?"

        protag_pensee "Je ne lui accorde plus une seconde de mon attention. Vaut mieux l’ignorer."

        hide JaneRizz
        show JaneNeutre
        JaneDoe "Pff."

        jump fin_jane

    label repondre_jane:

        protag "J’en ai rien à faire de plaire ! Surtout pas à toi."
        hide JaneNRV
        show JanePense
        JaneDoe "Oh non ! Cela me blesse ce que tu dis."
        hide JanePense
        show JaneBasic
        protag_pensee "Je vais lui faire ravaler ce sourire."

        protag "Ce que tu as fait à Chris était vraiment idiot. Il aurait pu se faire très mal. Arrête d’embêter Noa. Il a stressé pour rien la dernière fois. Et ne casse plus rien. T’imagine le temps que tu nous fais perdre."

        hide JaneBasic
        show JanePense
        JaneDoe "Hum ? Tu disais ? Je n'ai pas vraiment écouté."

        protag "Les responsabilités c’est pas ton truc, hein ?"


    label fin_jane:

    protag_pensee "Je la chasse d’un geste de la main."

    protag "Allez, du balais."

    hide JanePense
    hide JaneNeutre
    hide screen loveMeter
    with dissolve

    #Décor : Forêt

    protag_pensee "Une fois ma tâche finit au bar. Je traverse le camping. Des pleurs attirent mon attention vers le club enfant."

    protag_pensee "En m’approchant, je trouve Noa en pleine dispute avec une maman et un petit garçon les larmes sèches."

    show mamanvener at right
    with dissolve

    show NoaEffraye at left
    show screen loveMeter("Noa")
    with dissolve

    "Maman" "Je peux savoir où vous étiez pendant que mon fils, paniqué dans la forêt, s’est blessé au genou ?!" with vpunch

    noa "Je suis vraiment désolée madame. J’ai beaucoup d'enfants à surveiller et vu que le terrain de la course est assez grand et fermé…"

    "Maman" "Je veux pas savoir."

    protag_pensee "La blessure du petit a été pansée. Noa l’a soigné. Il a fait ce qu’il devait faire et maintenant il se fait sermonner."

    menu:
        "Ne rien faire":
            jump rien_faire_noa

        "Prendre sa défense":
            $ AF["Noa"] += 10
            $ courage += 5
            jump defense_noa

        "Lui demander ce qu’il s’est passé":
            $ AF["Noa"] += 5
            $ curiosite += 5
            jump demander_noa

    label rien_faire_noa:

        noa "Oui je comprends. C’est ma faute, je prends la responsabilité. Je ferais plus attention la prochaine fois."

        "Maman" "J’espère bien."

        hide mamanvener

        show NoaEffraye at center
        with move

        hide NoaEffraye

        show NoaBasic

        protag_pensee "Me voilà seul(e) avec lui."

        protag "Hé…ça va ?"

        noa "Ouais t'inquiète."

        jump suite_noa_talkie

    label defense_noa:

        protag "Excusez moi madame mais Noa a très bien réagi. 
        Votre fils s’est blessé et Noa a pris soin de lui. De plus, il n'est pas surhumain, il n’a pas les yeux partout. 
        Et les jeunes faisaient une course d’orientation je vous rappelle. C’est ça ?"

        hide NoaEffraye
        show NoaNeutre at left 
        noa "Oui…"

        protag "Donc, il est normal qu’ils soient dispersés et impossible de tous les surveiller."

        "Maman" "Vous devriez avoir honte vous deux. Je ne reviendrais plus dans ce camping."

        protag "Ne vous gênez pas madame."

        hide mamanvener
        with dissolve

        show NoaNeutre at center
        with move

        hide NoaNeutre
        show NoaBasic

        protag_pensee "Me voilà seul(e) avec lui."

        noa "Merci d’avoir pris ma défense."

        protag "De rien. Ne te met pas la pression, ok ?"

        noa "Ouais…"
        
        hide NoaBasic
        jump suite_noa_talkie

    label demander_noa:

        hide mamanvener
        with dissolve

        protag_pensee "La mère et son fils s’éloignent finalement. Me voilà seul(e) avec lui."

        show NoaEffraye at center
        with move

        hide NoaEffraye

        show NoaNeutre

        protag "Tout va bien ? Qu’est ce que s’est passé ?"

        noa "Hum…Le garçon est tombé sur le terrain de la course d’orientation. Il avait perdu son coéquipier donc il s’est affolé. 
        Une fois trouvé, je l’ai immédiatement soigné mais cela n’a quand même pas plu à sa mère."

        protag "Elle n'aurait pas dû te parler comme ça. Tu as géré la situation comme il fallait."

        noa "Je la comprends après. J’aurais dû mieux veiller sur eux."

        protag "Ne te met pas la pression, ok ?"
        
        hide NoaNeutre
        show NoaTimide
        noa "Merci."
        hide NoaTimide

    label suite_noa_talkie:
        
        show NoaBasic

        protag "Bon sinon. Tu t'en tire pas trop mal ?"
        
        hide NoaBasic
        show NoaPense

        noa "Ben figure toi que j’ai encore perdu un truc."

        protag "Quoi ?"

        noa "Mon talkie-walkie. Bizarre d’ailleurs vu qu’il était accroché à ma ceinture."

        protag "Tu l’as probablement perdu durant l’activité. Je vais t’aider."

        hide NoaPense
        show NoaBasic2

        noa "Merci encore. Je ferais quoi sans toi."

        protag "Tu perdrais ta tête."

        protag_pensee "Il rit à ma remarque. Après ce qu’il s’est passé, ça me fait plaisir de voir son sourire. Moi-même, il apparaît sur mon visage."

        protag_pensee "Je retrouve son talkie-walkie près d’une racine. Je sais très bien comment il l’a perdu. Jane, toujours Jane."

        hide NoaBasic2 
        hide screen loveMeter
        with dissolve

        #Décor : Bar nuit

        protag_pensee "La soirée arrive enfin. Je manque de sommeil à cause de mon réveil à 4h du mat. Comment va Chris d’ailleurs ?"

        protag_pensee "Quand on parle du loup. Je prépare une Pina colada alors qu’il trébuche en voulant s'asseoir au bar."

        show ChrisBasic 
        show screen loveMeter("Chris")
        with dissolve

        chris "Euh…Salut."

        protag "Toujours entier ?"

        hide ChrisBasic
        show ChrisTimide

        chris "Ouais…"

        protag_pensee "Il se penche légèrement vers moi pour me chuchoter."

        chris "Je voulais te parler des fantômes."

        hide ChrisTimide
        show ChrisPetitSourire

        protag_pensee "En entendant ça, je sers rapidement le cocktail avant de lui faire face. Je chuchote également."

        protag "Dis moi."

        chris "Je vais essayer de capturer une image avec mon appareil photo à vision nocturne. J’ai aussi une caméra infrarouge. 
        Tu veux m’accompagner ? Tu pourras tenir mon dictaphone pour l’enregistrer."

        protag "Tu es vraiment bien équipé. J’accepte. Je veux venir."

        chris "Cool. Cool. Tu me rejoins demain matin à la forêt."

        protag "Quelle heure ?"

        chris "A l’aube."

        menu:
            "Lui poser des questions sur le spectre.":
                $ AF["Chris"] += 5
                $ curiosite += 5
                jump questions_spectre

            "Retourner travailler.":
                $ habilete += 5
                jump retour_travail

        label questions_spectre:

            protag "Il ressemble à quoi exactement ton fantôme ?"
            hide ChrisPetitSourire
            show ChrisTimide
            chris "Ben du coup, c’est un chien…un beagle je dirais. Il me surprend toujours, venant de nulle part."

            protag "Toujours ? Tu l’as aperçu plusieurs fois ?"

            chris "Ouais. Il me saute dessus et aboie. La sensation est trop étrange. On sent qu’il te traverse mais on peut pas le toucher."

            protag "Tu l’as vu aujourd’hui ?"
            hide ChrisTimide
            show ChrisBasic
            chris "Cet après-midi à mon bungalow."

            protag "Ok…"

            jump fin_jour3

        label retour_travail:
            protag_pensee "Je le laisse, retournant laver des verres."

        label fin_jour3:

        hide ChrisPetitSourire 
        hide ChrisBasic
        hide screen loveMeter
        with dissolve

        protag_pensee "Ma journée est enfin terminée, c’est l’heure de dodo."

    jump j4