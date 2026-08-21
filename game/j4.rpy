label j4:

    window hide

    play sound "sfx/new_day.wav"

    show text "{font=fonts/Karla-VariableFont_wght.ttf}{cps=2}{size=*2}Jour 4{/cps}" with Pause(3.0):
        xpos 950
        ypos 350

    scene black
    with dissolve

    window show

    # Décor : Forêt

    protag_pensee "Le jour vient se lever. Je n’ai pas oublié
    ma batte au cas où. Appuyé(e) contre un arbre, je tape du pied sur
    le sol. Il prend son temps."

    protag_pensee "Il arrive en courant vers moi avec
    plusieurs appareils. Son souffle est court."

    show ChrisTimide
    show screen loveMeter("Chris")
    with dissolve

    chris "Désolé, je suis un peu en retard."

    protag "T’as pris tout ce qu’il faut ?"

    hide ChrisTimide
    show ChrisHeureux

    chris "Oui ! J’ai le détecteur de champ magnétique et le dictaphone
    pour toi. J'ai aussi amené un thermomètre si jamais il y a une
    baisse de température à cause d’un esprit."

    chris "Comme c’est le matin,
    j’ai pas pris la caméra infrarouge, c’est inutile mais ça marche super
    bien. Oh ! Et si j’avais su, j'aurais emporté de chez moi des boîtiers
    à diodes pour surveiller un périmètre et détecter le moindre
    mouvement. Et…"

    protag "Chris, respire."

    hide ChrisHeureux
    show ChrisTimide

    chris "Ah…oui…je parle trop je sais."

    menu:
        "Le complimenter":
            $ AF["Chris"] += 5
            jump complimentChris
        "Le ramener sur la mission ":
            $ habilete += 5
            protag "On a un fantôme à trouver. Allons-y."
            jump suite_foret
            

    label complimentChris:

        protag "C’est formidable tous ces trucs. T’es vraiment un expert en
        paranormal."

        hide ChrisTimide
        show ChrisHeureux

        chris "Oh…merci. Je pensais pas que ça t'intéresserait autant."

        protag_pensee "Le rose à ses joues est tellement
        adorable."

        protag "J’imagine que tu t’attendais pas non plus à voir un fantôme."

        chris "Tu peux le dire."

        protag_pensee " Nous rions légèrement face à cette
        situation improbable."

        protag "Je suis sûr(e) qu’on pourra l’attraper grâce à toi."


    label suite_foret:
        hide ChrisHeureux 
        protag_pensee "On s’enfonce dans la forêt, dépassant
        presque la limite du camping."

        show ChrisBasic
        with dissolve

        chris "On s’éloigne pas un peu trop ?"

        protag "Ne t’inquiète pas Chris. On est tous les deux ensemble."

        hide ChrisBasic
        show ChrisEffraye
        chris "Et les spectres ne peuvent pas nous faire de mal."

        protag "Voilà. C’est une bonne façon de voir les choses."

        protag_pensee "Soudain, au pied d’un chêne, un
        scintillement attire mon attention."
    
    protag "T’as vu ça ?"

    chris "De quoi ?"

    protag_pensee "Il se détache de son détecteur, regardant
    dans la direction que je pointe."

    hide ChrisEffraye
    show ChrisBasic
    chris "Qu’est ce que c’est ?"

    protag_pensee "Il approche et récupère une sorte de
    collier canin."

    hide ChrisBasic
    show ChrisTimide
    chris "Un collier pour chien ? C’est écrit… Cerbère."

    protag "Il appartient à ton beagle fantôme tu crois ?"

    chris "J’en sais rien."

    hide ChrisTimide
    hide screen loveMeter
    with dissolve

    play sound "sfx/CuteDog.wav"
    protag_pensee "Brusquement, des aboiements surgissent
    derrière nous. Dans un sursaut, Chris se cache dans mon dos." with vpunch

    menu:
        "S'écarter":
            $ AF["Chris"] -= 5
            play sound "sfx/bad_choice.wav"
            protag_pensee "En le voyant faire, je m’écarte rapidement
            dans la panique."
            protag "Qu’est ce que tu fais ?! Je suis pas un bouclier !"
            chris "Mais tu es armé !"

        "Le protéger":
            $ AF["Chris"] += 5
            $ courage += 5
            protag "Reste derrière moi Chris."
            protag_pensee "Je lève ma batte, prêt(e) à nous défendre."
            chris "N’hésite pas à frapper !"

    show Cerbere at right
    with dissolve

    protag_pensee "Chris tend son dictaphone pour enregistrer
    les sons. C'est là qu'apparaît l’esprit du beagle de Chris. Le chien
    court autour de nous et saute dans tous les sens."

    protag "Chris…appelle son nom."

    show ChrisEffraye
    show screen loveMeter("Chris")
    with dissolve

    chris "Moi ?"

    protag "Oui. c’est ton fantôme."

    chris "Ok…Cerbère ?"

    play sound "sfx/CuteDog.wav"
    protag_pensee "Le beagle semble se reconnaître. Il aboie
    et se redresse face à Chris."

    hide ChrisEffraye

    show ChrisPetitSourire
    with dissolve

    chris "Cerbère. C’est ton nom mon grand ?"

    protag_pensee "Chris tente de s’approcher du sien. Il a
    retrouvé confiance, on dirait."

    protag_pensee "Le grésillement de mon talkie-walkie
    retentit. Cerbère s’enfuit alors, s'évaporant entre les arbres. La voix
    de mon boss s’élève."

    hide Cerbere with moveinright

    hide ChrisPetitSourire

    show ChrisPetitSourire at right
    with move
    show thomas at left with dissolve

    thomas "Où es tu [protag_name] ! Je t’attends depuis 1h déjà."

    protag_pensee "Merde ! J’ai oublié l’inventaire."

    protag "Excusez moi monsieur. Je n’ai pas vu l’heure. Cela ne se
    reproduira plus."

    thomas "J’espère bien. On a dû se débrouiller sans toi. Pour la
    peine, tu iras aider Noa au lac pour l’activité de cet après-midi."

    hide thomas
    with dissolve

    show ChrisPetitSourire at center
    with move

    protag_pensee "Cette punition est pile ce que j’attendais. Il
    fait tellement chaud. Moi qui pensait que je ne pourrais jamais
    profiter du lac."

    hide ChrisPetitSourire

    show ChrisTimide

    chris "Désolé. c’est ma faute si tu t’ai fait sermonner."

    protag "Non. C’est moi qui n’a pas su s’en souvenir. Et puis, crois
    moi, j’ai jamais été aussi heureuse d’être punie."

    chris "Tant mieux alors…je crois ?"

    hide ChrisTimide
    hide screen loveMeter
    with dissolve

    # Décor : Lac

    protag_pensee "Les enfants sont déjà là, en maillot,
    attendant devant le local."

    show NoaBasic
    show screen loveMeter("Noa")
    with dissolve

    noa "Ok, les enfants, les jeux gonflables ont été installés dans
    l’eau. Je vais vous distribuer les gilets puis quand je vous le dirais
    vous pourrez y aller."

    noa "Personne ne doit passer sous les jeux dans
    l’eau, avec les gilets ça peut être dangereux. Et pour vous hisser
    vous avez des poignets sur les côtés. Vous avez écouté ?"

    "Enfants" "Oui, monsieur Noa."

    noa "Bien. Vous pourrez faire les fous sans problèmes si vous
    suivez ces règles."

    "Enfants" "Ouais !!!"

    protag "Je suis là, Noa."

    hide NoaBasic
    show NoaTimide

    noa "Génial. Tu m’aide à leur donner des gilets à leur taille."

    protag "Ouaip."

    noa "N’hésite pas à bien leur serrer."

    hide NoaTimide

    protag_pensee "J’équipe une partie des enfants, tirant sur
    les sangles pour la tenu."

    protag_pensee "Noa laisse ensuite les enfants s’élancer
    dans les jeux."

    show NoaBasic
    with dissolve

    noa "T'as un maillot ?"

    protag "Oui, sous mon t-shirt."

    noa "Parfait, si jamais ils ont besoin, on est là."

    menu:
        "Lui parler des enfants":
            $ AF["Noa"] += 5

            protag "Tu t’entends bien avec eux, non ?"
            hide NoaBasic
            show NoaBasic2
            noa "J’ai réussi à leur gratter l’amitié, ouais. Ils sont mignons les
            gamins. On a même fait une photo de groupe sur mon téléphone, tu
            veux voir ?"
            protag "Grave."
            protag_pensee "Il ouvre son téléphone à clapet et ouvre
            l’image. Il est au milieu et les gosses font des grimaces."
            protag "Vous êtes trop chou. Et leurs têtes, hilarantes."
            noa "Ils sont doués pour ça."

        "Lui parler des fantômes":
            $ curiosite += 5

            protag "Dis moi…tu aurais vu quelque chose d’étrange dernièrement
            ? Un bruit, une voix ou une silhouette mystérieuse ?"
            hide NoaBasic
            show NoaPense
            noa "A part que je perds tout ici. Non pas spécialement."
            protag "T’es sûr ?"
            noa "Ouais. Pourquoi ?"
            protag "Rien."
            hide NoaPense
            show NoaBasic
            protag_pensee "Je soupire, frustré(e). Heureusement qu’il
            y a Chris, sinon j’aurais pu croire être folle."

    protag_pensee "Tout d’un coup, une petite fille vient nous
    voir trempée et en pleurs. Je m’accroupis pour être à sa hauteur."

    hide NoaBasic
    hide NoaBasic2

    protag "Qu'y a t-il ma belle ?"

    "Petite fille" "J’ai…J’ai…J’ai perdu mon collier sous l’eau."

    show NoaPense
    with dissolve
    noa "Vers où ?"

    "Petite fille" "Au début du jeu."

    protag "C’est pas trop profond vers là, non ?"

    noa "Non ça va."

    protag "Je vais y aller. Tu vas retrouver ton bijou, petite."

    "Petite fille" "Merci beaucoup."

    hide NoaPense
    hide screen loveMeter

    protag_pensee "J’enfile des lunettes de plongée puis
    rentre dans le lac. C'est légèrement trouble à cause de la terre mais
    je vois le fond."

    protag_pensee "Je perçois un pendentif doré en forme de lune et
    l’attrape. Mais à quelques centimètres, je trouve également un
    bracelet personnalisé. Je le prends aussi puis remonte."

    protag_pensee "Je rends le collier à la fillette qui repart aux
    jeux."

    protag "Noa."

    show NoaBasic
    show screen loveMeter("Noa")
    with dissolve

    noa "Quoi ?"

    protag "J’ai aussi trouvé ça."

    protag_pensee "Le bracelet argenté porte un prénom,
    Jane. Jane la fantôme ?"

    hide NoaBasic
    show NoaPense

    noa "Hum…Je ne connais aucune Jane ici."

    protag "Tu penses que c’était dans le lac depuis longtemps ?
    Peut-être des années ?"

    hide NoaPense
    show NoaNeutre

    noa "J’en sais rien. C’est possible."

    protag_pensee "Est-ce que c’est ici ? Qu’elle est
    devenue…un esprit ? Je garde le bracelet dans ma poche."

    hide NoaNeutre

    protag_pensee "L’activité est finie, les enfants retournent
    avec leurs parents. Je range les gilets quand j'entends un splash.
    Je vais voir immédiatement." with hpunch

    protag "Noa ? Qu’est ce que tu fais à l’eau ?"

    show NoaPense
    with dissolve

    noa "Je ne sais pas ce qu’il s’est passé. J’ai eu l’impression qu’on
    m’a poussé."

    protag "Mais on est seul."

    noa "Je sais bien."

    show JaneRizz at right 
    with dissolve
    protag_pensee "Je scrute les alentours. Jane est là, riant.
    Au loin à l’entrée de la forêt. Cerbère court vers elle. Elle m’énerve.
    C’est vraiment qu’une gamine immature."

    hide JaneRizz with dissolve
    
    protag_pensee "Noa se hisse hors de l’eau."

    hide NoaPense
    show NoaBasic2
    noa "Je me suis rafraîchie au moins."

    protag_pensee "Je devrais lui en parler, des fantômes. Il
    faut qu’il sache que ce n’est pas sa faute. Il n’est pas juste
    maladroit."

    hide NoaBasic2
    hide screen loveMeter
    with dissolve

    # Décor : Bar soir

    protag_pensee "Je sers des shorts comme tous les soirs.
    Cette fois, Noa m’aide au comptoir. Je lui jette plusieurs coups d'œil
    et mordille ma lèvre. Je lui dis ou pas ?"

    protag_pensee " Je cherche Chris parmi les campeurs. Je
    vois sa famille mais pas lui. C’est bizarre. Où est-il ? Pitié, qu’il ne
    soit pas parti en expédition tout seul."

    "Homme" "Salut ma/mon joli(e)."

    protag "Qu’est ce que je vous sers ?"

    "Homme" "Un Sex on the beach."

    protag "Ok."

    "Homme" "Tu es drôlement jeune dis donc. Tu as quel âge ?"

    protag "Je préfère ne pas répondre, désolé(e)."

    "Homme" "[protag_name], c’est écrit sur ton badge. Je t’offre un
    verre pour te détendre ?"

    protag "Je suis en plein service et je ne vous ai pas permis de me
    tutoyer. Le respect ça va dans les deux sens."

    "Homme" "Oula, un(e) coincé(e)."

    protag_pensee "Un claquement de langue m’échappe. Si
    je n’étais pas au travail, je lui aurais servi une droite. Il m’en aurait
    dit des nouvelles."

    show NoaNRV
    show screen loveMeter("Noa")
    with dissolve

    noa "Monsieur, je vous demanderais de considérer les employés ici
    ou je n’hésiterais pas à appeler quelqu’un. Entendu ?"

    protag_pensee "L’homme récupère son cocktail et quitte le
    bar, marmonnant dans sa barbe."

    menu:
        "Le remercier":
            $ AF["Noa"] += 5

            protag "Merci. Il était vraiment lourd."
            hide NoaNRV
            show NoaTimide

            noa "Ouais, t’es pas la première malheureusement. J’irais en parler
            à M.Thomas."
            protag "J’espère qu’il fera quelque chose."
            noa "Quel répondant en tout cas. C’est cool."
            protag "Merci."

        "Se plaindre":
            $ AF["Noa"] -= 5
            play sound "sfx/bad_choice.wav"

            protag "Je sais me défendre tout(e) seul(e) tu sais. Occupe toi de tes
            affaires la prochaine fois."
            noa "Wow…ok."

            hide NoaNRV

            protag "Il m’a mis(e) sur les nerfs."

    protag_pensee "Quand il n’y a plus personne, je tire Noa à
    part."

    protag "Il faut que je te dise un truc."

    hide NoaTimide
    show NoaBasic
    with dissolve

    noa "Dis moi."

    protag "Tu vois… mes questions sur les spectres tout ça."

    noa "Ouais, tu devrais pas t’en inquiéter."

    protag "En fait, si. Enfin, ils ont pas l'air dangereux ou quoi mais…"

    hide NoaBasic
    show NoaPense
    noa "Quoi ? Toi aussi tu vois les fantômes ?"

    protag "C’est ça."

    noa "Hein ? Si c’est une blague, on me l’a déjà fait."
    hide NoaPense
    show NoaBasic2

    protag "Je rigole pas Noa. Le collier de Jane que j’ai trouvé, il
    appartient à une fille fantôme que j’ai vu."

    hide NoaBasic2
    show NoaPense
    noa "Hum…tu dors la nuit ?"

    protag "J’hallucine pas ! Un campeur en a vu un aussi. C’est Chris,
    sauf que c’était un beagle, Cerbère."

    noa "Hum…Va te reposer. Je continue ici."

    protag "Quoi ? Mais non !"

    hide NoaPense
    show NoaBasic 
    noa "Vas y."

    hide NoaBasic
    hide screen loveMeter
    with dissolve

    protag_pensee "Il ne me croit pas. Évidemment. Je soupire
    de frustration et quitte le bar."

    # Décor : Forêt nuit

    protag_pensee "Cette dernière discussion m’a insufflé une
    incroyable détermination. J’illumine le chemin avec ma lampe
    torche. Où est-elle ?"

    protag "Jane ! T’es là ?"

    protag_pensee "C’est si silencieux. Forêt + nuit = angoisse
    même quand tu traques du paranormal volontairement."

    JaneDoe "On me demande ?"

    protag_pensee "Un soubresaut me secoue." with hpunch

    protag "Merde ! Tu m’as fait peur, nom de dieu."

    show JaneBasic
    show screen loveMeter("Jane")
    with dissolve

    JaneDoe "Tu as peur facilement dis donc." 

    protag "C’est à cause de ta tête."

    hide JaneBasic

    show JaneRizz
    with dissolve

    JaneDoe "Du coup ? Tu me kiffes finalement ?" 

    protag "Rien à voir. Mais ce sera aussi fun pour toi."

    hide JaneRizz

    show JaneBasic
    with dissolve

    JaneDoe "Hum ? Cela m’intéresse." 

    protag "J’ai…besoin de toi. Noa ne me croit pas sur votre existence.
    On doit lui prouver que si."

    hide JaneBasic
    show JaneFlip
    with dissolve
    JaneDoe "Ouh…ça sent le piège. Je suis chaude. Quand tu veux. Je
    vais lui faire une frayeur qu'il ne se relèvera pas." 

    hide JaneFlip
    show JaneNeutre
    with dissolve

    protag "Évite le risque comme le pousser dans le lac par exemple."

    JaneDoe "Techniquement, c’était Cerbère, pas moi." 

    menu:
        "Lui montrer le bracelet":
            $ AF["Jane"] += 5
            $ curiosite += 5

            protag "Jane…Soyons sérieux deux minutes. J’ai trouvé ça au fond
            de l’eau tout à l’heure."

            hide JaneBasic
            show JaneChock
            with dissolve

            JaneDoe "C’est…mon bracelet. Comment ?"
            protag "Est ce que…difficile de demander ça mais…tu es morte
            là-bas ?"
            protag_pensee "Aucun mot ne sort de ses lèvres. Elle fixe
            le bijou avec, ce qui semble, une envie de pleurer."
            JaneDoe "Wow…je n’aurais jamais cru le retrouver un jour. Un vestige
            de ma vie. Il faudrait le placer au musée."
            protag "Désolé(e). Ma question est indiscrète."
            hide janeChockbar
            show JaneChock
            with dissolve
            JaneDoe "C’est bon. C’était il y a des années. Je me suis juste…noyée
            en tombant d’un petit bateau. Si on ne sait pas nager, dur de
            remonter." 
            protag "Qu’est ce que tu faisais au lac si tu ne sais pas nager ?"
            JaneDoe "Je…je suis juste débile, c’est tout. Débarrasse-toi de ça s’il te
            plait."

            hide JaneChock

            show JaneBasic
            with dissolve

            protag_pensee "Je range le bijou dans ma poche. N’en
            parlons plus pour l’instant. Elle simule une profonde inspiration et
            son sourire revient."
            
            hide JaneNeutre
            hide JaneBasic

        "Ne rien faire":
            protag_pensee "Vaut mieux ne pas y penser pour le
            moment."
            hide JaneNeutre

    
    show JaneRizz with dissolve
    protag "Tu es toute seule avec Cerbère ?"

    JaneDoe "Non ! On est un vrai gang de fantômes." 

    protag "Vraiment ? Combien ?"

    hide JaneRizz

    show JanePense
    with dissolve
    
    JaneDoe "Je sais pas, je compte pas." 

    protag "Ils sont plus discrets."

    hide JanePense

    show JaneBasic
    with dissolve
    
    JaneDoe "Cerbère et moi on adore attirer l’attention. Mais tu en as déjà
    fait l’expérience." 

    protag "Et pas que moi."
    
    JaneDoe "Bref. Pour quand l’opération terreur pour Noa ?" 

    protag "Demain soir au test de courage."
    
    hide JaneBasic
    show JaneRizz
    with dissolve
    JaneDoe "Ouh…L’ambiance sera folle." 

    protag "Ne fais plus de bêtises en attendant."
    
    JaneDoe "Je ne promets rien." 

    hide JaneRizz
    hide screen loveMeter
    with dissolve

    jump j5












    




    




