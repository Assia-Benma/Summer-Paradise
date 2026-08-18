label j5:

    window hide

    play sound "sfx/new_day.wav"

    show text "{font=fonts/Karla-VariableFont_wght.ttf}{cps=2}{size=*2}Jour 5{/cps}" with Pause(3.0):
        xpos 950
        ypos 350

    scene black
    with dissolve

    window show

    #Cabanon

    protag_pensee "Je quitte le cabanon quand je vois Chris m’attendre avec Cerbère."

    show ChrisBasic

    protag "Chris ! Pourquoi t’es là avec Cerbère ?"

    protag "On va le voir."

    chris "Je pense que c’est le dernier de leur souci aux fantômes."

    protag "Allons ailleurs."


    #Forêt

    protag "Pourquoi es-tu venu me voir ?"

    chris "Ben…tu es ma/mon seul(e) confident(e) pour tout ça."

    menu:
        "Être compréhensif(ve)":
            $ chrisAF += 5

            protag "Ouais, je comprends. C’est pareil pour moi, tu es le seul à qui je peux vraiment en parler."
            protag "Et tu es plutôt un bon partenaire de paranormal."

            chris "Vraiment ? Tu es doué(e) aussi. Plus courageux(se) et fort(e)."

            protag "Tu es aussi brave que moi, Chris. Tu n'hésites jamais pour enquêter."
            protag "Et je suis sûr(e) que c’est une habitude."

            chris "Ça m'arrive oui. Je fais un peu d’urbex quand j’ai le temps."

            protag "C’est trop cool !"

            chris "Merci. On pourrait en faire tous les deux un jour."

            protag "J’aimerais bien."

        "Le redescendre":
            $ chrisAF -= 5

            play sound "sfx/bad_choice.wav"

            protag "De base c’est pas mon truc après. C’est à cause des esprits que j’ai eu besoin de toi."

            chris "Au moins…tu es honnête."

            protag "Mais tu es sympa Chris. Tu es devenu un ami, je t’assure."

            chris "Cool alors."

    protag_pensee "Le chien saute et court partout. Il est très excité aujourd’hui."

    chris "Cerbère me lâche plus depuis que je l’ai trouvé. Je crois qu’il m’aime bien."

    protag "Tu l’aime bien également."

    chris "C’est vrai."

    protag "Tu penses…qu’il est mort comment ?"

    chris "Hum…vu où était le collier…abandonné sûrement. En fait, j’y suis retourné hier soir."
    chris "Il y avait une corde accrochée à l’arbre."

    protag "Mon dieu…pauvre Cerbère."

    chris "Je préfère ne pas y réfléchir. Et puis, il a l’air heureux en fantôme."

    protag_pensee "Chris ramasse un bâton et l’agite sous le nez du chien."
    protag_pensee "Il le jette ensuite au loin, Cerbère tente de l’attraper."
    protag_pensee "Bien évidemment, ça passe au travers. Le beagle essaye tout de même de saisir le bâton entre ses crocs mais rien y fait."

    chris "J’aurais dû m'y attendre."

    protag "Il va falloir que j’y aille. Je voudrais pas me faire engueuler…encore."

    chris "Ouais, je voudrais pas non plus."

    protag "Bye, Chris."

    hide ChrisBasic with dissolve

    #Bar

    protag_pensee "Cela fait trois fois que je repasse le chiffon. Je crois que M.Thomas m’en veut encore."
    protag_pensee "Il a compris que le lac n’était pas une vraie punition."

    protag_pensee "Un verre manque soudainement de tomber et je le rattrape."

    show JaneBasic with fade

    JaneDoe "Bon réflexe dis donc."

    protag "Tu peux arrêter de faire ça ? Comment fais-tu fais d’ailleurs ?"

    JaneDoe "J’ai pas besoin d’être matériel pour créer une force suffisante pour agir."
    JaneDoe "On est des esprits, certes, mais on est fait d’énergie pour exister. Une histoire avec l’âme."

    protag "Ouais ben cesse tes conneries quand même."

    protag_pensee "Jane regarde la carte des cocktails avec attention. Qu’est ce qu’elle a encore ?"

    JaneDoe "Tu sais, quand j’étais en vie, j’étais une grande buveuse d’alcool."

    protag "Une alcoolo en gros."

    JaneDoe "Ouais ! J’ai visité tellement de bars. Une championne en marathon."

    menu:
        "La rembarrer":
            $ JaneDoeAF -= 10

            play sound "sfx/bad_choice.wav"

            protag "Ne me raconte pas ta vie, merci. J’ai du travail là."

            JaneDoe "Pff. T’es qu’une rabat joie."

            protag_pensee "Elle disparaît aussi vite qu’elle est arrivée."

        "L’écouter":
            $ JaneDoeAF += 10
            $ curiosite += 5

            JaneDoe "J’ai carrément une liste pour mes cocktails préférés."

            protag "C’est lequel ton numéro 1 ?"

            JaneDoe "Hum…tu me poses une colle, attends."

            protag "Prends ton temps."

            JaneDoe "Le Dirty Shirley."

            protag "Rapide la réponse. C’est quoi ça ?"

            JaneDoe "Tu connais pas ? C’est super simple à faire. Note ça."

            protag "Que je note ?"

            JaneDoe "Ouais, ça t'apprend une nouvelle recette."

            protag "Ok."

            protag_pensee "Je récupère un stylo et un vieux reçu où écrire."

            JaneDoe "Alors, il te faut 6cl de Vodka, 3cl de sirop de grenadine et 18cl de soda citron-citron vert."
            JaneDoe "Tu mélange d’abord le sirop et la vodka légèrement avant d’ajouter le soda citron."
            JaneDoe "Et j’adore quand ils mettent la cerise."

            protag "J’avoue que ça me tente."

            JaneDoe "Tu vois."

            protag "Tu es du genre fêtarde, non ?"

            JaneDoe "Tu penses bien."

            protag "J’aurais dû m’en douter."

            JaneDoe "En parlant de fête, j’ai des farces à faire."

            protag "Pff…ok mais laisse Noa tranquille cette fois."

            JaneDoe "Ok, ok. Je vais me trouver quelqu’un d’autre."

            protag "Merci, à ce soir."

    hide JaneBasic with fade
    #Feu de camp nuit

    protag_pensee "La soirée débute enfin. Je suis un peu nerveuse."
    protag_pensee "J’aimerais éviter de traumatiser à vie Noa. Pitié que Jane ne soit pas trop méchante."

    show NoaBasic with dissolve

    noa "Tu es là. On prépare le goûter pour la fin de l’épreuve."

    protag "C’est bien prudent ? Les animaux risquent de manger notre nourriture, non ?"

    noa "Non t’inquiète, ça restera pas sans surveillance."

    protag "Ok."

    protag_pensee "Alors que je pose les snacks sur la table, les gens arrivent."
    protag_pensee "Ils semblent tous surexcités à commencer. J’avoue que moi aussi j’ai hâte."

    noa "Alors tout le monde, on va démarrer avec des explications."
    noa "Nous allons faire un test de courage. Cela s’inspire du concept du Kimodameshi au Japon."
    noa "Vous allez devoir parcourir les bois 1h dans le noir."
    noa "Si vous avez la frousse et venez vous réfugier au feu de camp, c’est perdu."
    noa "Mon collègue va rester ici en attendant."

    protag "Vous êtes prêts ? C’est parti."


    #Forêt nuit

    protag_pensee "Les gens s’enfoncent dans la forêt enthousiastes."
    protag_pensee "Je vois également Chris avec son détecteur. Il tremblote légèrement mais n’hésite pas à y aller."

    noa "On y va ?"

    protag "Nous aussi ?"

    noa "Ouais c’est pas interdit."

    protag "Oh. Ok."

    noa "Cache ta joie."

    protag_pensee "Je lui donne un coup de coude et on rit légèrement."

    menu:
        "Si tu as peur, je t’autorise à me tenir la main.":
            $ noaAF += 5
            $ courage += 5
            $ noa_main_proposee = True

            noa "Pour qui me prends-tu ? Mais c’est gentil, tu me donnes une excuse pour le faire."

        "Ne rien dire":
            $ noa_main_proposee = False

    protag_pensee "On ne voit vraiment rien ici. Les gens sont loin de nous."
    protag_pensee "C’est comme si on était seul au monde. Tout à coup, un bruit dans un buisson attire notre attention."

    noa "C’est quoi ça ?"

    protag "Juste un animal peut-être."

    protag_pensee "Est-ce que c’est Jane ? Elle est déjà là ?"

    protag_pensee "Un sanglier en sort et court devant nous." with hpunch

    hide NoaBasic
    show NoaEffraye
    protag_pensee "Noa sursaute et saisit ma main. Mon cœur rate un battement en sentant sa main dans la mienne."

    menu:
        "Retirer sa main":
            if noa_main_proposee:

                $ noaAF -= 5

                play sound "sfx/bad_choice.wav"

                noa "Désolé…je croyais que je pouvais."

                protag "C’était qu’une blague, Noa."

            else:

                noa "Désolé. Je me suis emballé."

                protag "Pas grave. T’inquiète pas."

        "Garder sa main":
            $ noaAF += 10

            if noa_main_proposee:

                noa "C’était pas une excuse finalement."

                protag "T’as vraiment eu peur ? Je suis sûre que tu as fait exprès."

                noa "Très drôle. Rien que pour ça, je te lâche plus."

                protag_pensee "Il serre ma main. C’est chaud et apaisant."
                protag_pensee "Un remède efficace contre la peur."

            else:

                protag "Tu as eu si peur que ça ?"

                noa "Ouais, désolé."

                protag "C’est bon, laisse."

                protag_pensee "Je serre sa main chaude et apaisante. Un remède efficace contre la peur."


    protag_pensee "L’ambiance change entre temps. Un épais brouillard se manifeste autour de nous."
    protag_pensee "Une forte brise nous frappe de plein fouet."

    noa "Que se passe-t-il ?"

    protag_pensee "Les silhouettes translucides apparaissent l’un après les autres entre les arbres."
    protag_pensee "Je vois également Jane ainsi que Cerbère qui aboie."
    protag_pensee "Noa se tend et se place devant moi pour me protéger."
    protag_pensee "Il ne bouge plus et me chuchote."

    noa "Ok…je te propose de faire demi-tour très lentement."

    protag "On va perdre si on y retourne."

    noa "Je rigole pas."

    protag "Noa…du calme. Tu ne risques rien."

    show NoaEffraye at left 
    show JaneRizz at right with fade
    protag_pensee "Jane s’approche le sourire aux lèvres."
    
    JaneDoe "Il n’y a rien à craindre mec. On ne va pas te manger, on ne peut pas se nourrir tout court."

    noa "Je deviens fou."

    protag "Tu te souviens quand je te parlais des fantômes."

    noa "C’était pas des histoires finalement."

    protag "Mais ça veut pas dire que c’est dangereux."

    noa "Ok…ok…je te fais confiance."

    protag_pensee "Les autres fantômes semblent hilares face à la confusion de Noa."
    protag_pensee "Cerbère s’élance derrière nous joyeusement et aboyant."

    chris "Salut mon grand. Toi aussi tu m’as manqué."

    protag "Chris ? Comment tu nous as trouvé ?"

    show ChrisHeureux at center with dissolve

    chris "Grâce au détecteur."

    protag "Ton truc est incroyable."

    JaneDoe "Toute la bande est présente je crois."

    chris "Wow…c’est elle ton fantôme ?"
    hide ChrisHeureux
    show ChrisBasic at center

    protag "Oui, voici Jane."

    chris "Comme Jane Doe ?"

    hide NoaEffraye
    show NoaPense at left 
    noa "C’était juste une histoire."

    JaneDoe "Mais si ça t’amuse de le croire."
    hide JaneRizz
    show JaneBasic at right 

    protag_pensee "Chris s’écarte un peu, se rapprochant de Cerbère comme gardien."
    protag_pensee "Mais il sort son appareil photo et un flash illumine les bois."

    protag "On voit quelque chose ?"

    chris "Non…"

    noa "Peut-être qu'ils ne sont pas visibles comme les vampires."

    JaneDoe "On est des vampires-fantômes, ouh…"

    protag "Arrête ça."

    hide NoaPense
    show NoaBasic at left 
    noa "Ravi de, tous, vous rencontrer…j’imagine."

    JaneDoe "De même."

    protag "Pas trop traumatiser."

    hide NoaBasic
    show NoaTimide at left 
    noa "Ça va…ils ont l’air…sympathiques ?"

    JaneDoe "Nous le sommes."
    hide NoaTimide
    show NoaBasic at left

    chris "Tu peux pas être plus effrayé que moi, je pense."

    noa "On ferait mieux d’y aller. L’épreuve se finit bientôt et j’ai besoin de temps pour digérer ça."

    chris "Compréhensible. Ma famille doit aussi me chercher."

    protag "On y va alors."

    JaneDoe "Salut. Si jamais vous sentez une présence derrière vous, c’est moi."
    hide JaneBasic with dissolve

    hide ChrisBasic
    show ChrisEffraye at center 
    chris "C’est rassurant…"

    hide ChrisEffraye
    hide NoaBasic 
    with dissolve

    #Feu de camp

    protag_pensee "Quand on arrive au feu de camp, la plupart des campeurs sont déjà là et se servent à table."

    menu:
        "Aller voir Noa":
            $ noaAF += 5

            show NoaEffraye with dissolve
            protag "Hey…pas trop dure à encaisser ?"

            noa "Ben…je réalise à quel point j’ai été aveugle. Et toutes tes questions prennent maintenant du sens."

            protag "Ouais, j’ai pas chercher à être discrète. Je suis là si jamais tu en as besoin."

            hide NoaEffraye
            show NoaTimide
            noa "Merci. Je peux compter sur toi. Tu me l’a prouvé un nombre incalculable de fois."

            protag "Toutes les fois où tu perdais quelque chose ou encore quand tu es tombé à l’eau."
            protag "C’était à cause de Jane. Elle y voyait une forme d’amusement."

            noa "J’ai fini par comprendre, ouais. Elle m’aura fait tourner en bourrique."

            protag "Elle adore ça, crois moi."

            noa "On ferait mieux de tout nettoyer maintenant."

            hide NoaTimide with dissolve

        "Aller voir Chris":
            $ chrisAF += 5

            show ChrisHeureux
            chris "Je m’attendais pas à voir autant de fantômes. Mon détecteur a surchauffé carrément."

            protag "J’imagine bien. Mais tu as géré comme un chef. Malgré ta peur, tu explores et traque le paranormal."

            chris "J’essaie de m’y faire mais c’est plus fort que moi."

            protag "Je suis fier(ère) de toi, Chris."

            hide ChrisHeureux
            show ChrisPetitSourire
            chris "Merci. Mais sûrement pas aussi fier que moi de t’avoir comme partenaire."

            protag "Comme les Ghostbusters mais en moins équipé et stylé."

            hide ChrisPetitSourire
            show ChrisHeureux
            chris "Moins équipé ? Tu n’as pas encore vu tout ce que je cache chez moi."

            protag "Ça promet dis donc."

            chris "Noa te fait signe pour ranger."

            protag "J’y vais alors. A plus tard."

            hide ChrisHeureux with dissolve

        "Aller voir Jane":
            $ JaneDoeAF += 5

            show JanePense with dissolve
            protag_pensee "J’aperçois Jane cachée derrière un pin. Je la rejoins discrètement."

            protag "Tu prépares un autre coup ?"

            hide JanePense
            show JaneRizz
            JaneDoe "Peut-être bien. C’est un secret."

            protag "Merci pour aujourd’hui. Je ne sais pas si vous faites l’effort de vous cacher ou non."
            protag "Mais merci d’avoir bien voulu vous montrer à Noa."

            JaneDoe "Ben, on a pas peur que vous le partagiez avec tout le monde. Qui vous croirez ?"
            JaneDoe "On peut pas être pris en photos en plus."

            protag "Fantômes 1, humains 0."

            JaneDoe "Enfin, si on compte toutes mes farces depuis le début…Je dirais un bon fantômes 10, humains 0."

            protag "Ne prends pas la grosse tête."

            JaneDoe "Si, si. Je vais le faire."

            protag "Bon, faut que j’y aille. A plus."

            hide JaneRizz with dissolve


    show NoaBasic2 with dissolve
    noa "Bien joué tout le monde pour votre courage, j’espère que cette soirée vous a plu."
    noa "Je vous souhaite une bonne nuit messieurs dames."

    protag_pensee "Les gens s’en vont vers les bungalow comme Chris et sa famille."
    protag_pensee "Je finis de tout ranger avec Noa. Ensuite j’éteins le feu et vais dormir au cabanon, repensant à cette journée."
    hide NoaBasic2 with dissolve
    
    jump j6