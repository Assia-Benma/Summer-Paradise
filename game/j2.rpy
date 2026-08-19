
label j2:

   window hide

   play sound "sfx/new_day.wav"

   show text "{font=fonts/digital-7.ttf}{cps=2}{size=*2}Jour 2{/cps}" with Pause(3.0):
      xpos 950
      ypos 350

   scene black
   with dissolve

   window show

   protag_pensee "Un vacarme infernal m’explose les tympans.
   J’éteins ce fichu réveil d’un coup brutal sans le vouloir.
   Mes yeux prennent le temps de s’ajuster à la lumière."

   protag_pensee "Cette fantôme hier soir…qui est-ce ? Elle est morte ici ? Au camping ? Comment et en quelle année ? Et puis
   depuis quand je peux voir des apparitions ? Depuis quand ça existe même ?"

   protag_pensee "J’ai une longue journée qui m’attends aujourd’hui. J’ai sûrement déliré avec la fatigue. Oui, c’est juste ça."

   protag_pensee " Heureusement, je suis de corvée au lac.
   Moi qui pensais que cet été serait un calvaire, je vais pouvoir en profiter."

   # Décor : Lac 

   protag_pensee " Le lac apparaît enfin devant mes yeux.
   Noa est là aussi. Il est accroupi au sol, cherchant quelque chose."
   protag "Il y a un souci ?"

   show NoaPense
   show screen loveMeter("Noa")
   with dissolve

   noa "Ah salut. Euh… j’ai perdu les clés du local. Je ne sais pas où
   elles ont pu tomber."

   protag_pensee " Ses sourcils sont froncés, son regard
   parcourt l’herbe rapidement. Son doigt tapote son genou. Un tic qui
   me partage toute son anxiété."

   menu:
      "L'aider à chercher":
         $ AF["Noa"] += 10
         $ habilete += 5
         jump aideNoa

      "Aller prendre le double des clés.":
         $ AF["Noa"] += 5
         $ habilete += 10

         hide NoaPense
         show NoaNeutre
         protag_pensee "Je retourne vite fait au cabanon, un des
         animateurs avait signalé un double sur la table sur le talkie-walkie."

         protag_pensee "Lorsque que je reviens, Noa fouille encore
         par terre."

         protag "Je les ai. Ne t’inquiète plus."
         hide NoaNeutre
   
   label aideNoa:

         protag "Attends, je vais t’aider."

         hide NoaPense

         protag_pensee "Il ne répond pas, trop concentré. Je fouille
         aux alentours, me rapprochant de la forêt. Et là, je vois un
         scintillement sous un arbre."

         protag "Je crois que je les ai repérés."

         noa "Où ça ?"

         protag_pensee "Il se lève immédiatement pour me
         rejoindre."

         show NoaPense
         with dissolve

         protag "C’est celles-là."

         protag_pensee "En tournant la tête, une silhouette lévite
         derrière les feuilles, fuyante."

   hide NoaPense

   show NoaBasic
   with dissolve

   protag_pensee "Ses épaules se détendent. Il les récupère
   et ouvre finalement le local."

   noa "Merci. Je me serais probablement fait sermonner par le patron
   sans toi."

   hide NoaBasic

   protag_pensee "Je suis Noa à l’intérieur. Mes pensées
   s’égarent sur la fantôme stupidement énervante et effrayante."
   
   protag_pensee "Si elle existe vraiment, c’est sûrement elle qui a brisé le verre et éclaté
   cette ampoule."

   protag_pensee "Dis moi. As-tu déjà entendu des rumeurs
   ou vu un je-ne-sais-quoi d’inhabituel ?"

   show NoaPense
   with dissolve

   noa "Ici ? Personnellement non. Mais des clients ont mentionné
   des voix et des objets qui se sont déplacés par le passé."

   noa "Une fois, quelqu’un a même dit avoir vu un fantôme une nuit.
   Son cerveau a dû s’imaginer des monstres dans le noir à mon avis."

   protag_pensee "Je hoche la tête, prenant toutes les
   informations en compte. Je n’ai pas déraillé(e) finalement."

   noa "Pourquoi ? Tu as vu quelque chose ?"

   protag "Non non."

   protag_pensee "Vaut mieux éviter d’être pris(e) pour un(e)
   folle/fou."

   hide NoaPense

   show NoaBasic
   with dissolve

   noa "Tu es attendu ailleurs je pense."

   protag "Quoi ? Je reste pas au lac avec toi ?"

   noa "Et non, désolé."

   protag "Super…"

   hide NoaBasic
   hide screen loveMeter
   with dissolve

   protag_pensee "Mes pieds traînent sur le sol alors que je
   m’éloigne. Plus loin, Chris se balade avec un détecteur de champ
   magnétique et d’autres outils dont je ne connais pas le nom. Un
   bidule paranormal a peut-être croisé sa route."

   # Décor : Forêt

   protag_pensee "Quand j’arrive derrière lui, il tressaille.
   D’un mouvement vif, il se retourne face à moi, appareil levé."

   show ChrisEffraye with vpunch
   show screen loveMeter("Chris")
   with dissolve

   protag "Tout va bien, ce n’est que moi ?"

   hide ChrisEffraye

   show ChrisBasic
   with dissolve

   chris "Oh… Salut."

   protag "Tu pars en expédition ?"

   chris "Fais pas attention. C’est juste des bêtises pour passer le
   temps."

   protag "Cool le matos. Tu as attrapé un fantôme avec ça ?"

   hide ChrisBasic

   show ChrisPetitSourire
   with dissolve

   chris "Non pas encore. Mais tu trouves mes machins cool ?
   Vraiment ?"

   protag "Ouais, ça m’intéresse. Ces trucs marchent au moins ?"

   hide ChrisPetitSourire

   show ChrisHeureux
   with dissolve

   chris "Évidemment, je ne me promène pas avec de la camelote.
   Mon détecteur de champ magnétique s’est déclenché pour la
   première fois ce matin. J’ai rien vu mais je sens qu’il y a quelque
   chose."

   protag "Ok. C’est bon à savoir."

   menu:
      "Essayer":
         $ AF["Chris"] += 10
         $ curiosite += 5
         jump essayer

      "Partir":
         protag_pensee "Sur ce, je lui fais signe d’au revoir et
         m’éloigne vers le cabanon des animateurs."

         jump suite_j2
   
   label essayer:

      protag "Je peux essayer ?"

      protag_pensee "Autant s’assurer que ça fonctionne pour
      de vrai. L’expression de Chris pétille en voyant mon intérêt. Une
      bonne vague d’excitation le prend."

      chris "Oh ! Oui bien sûr."

      protag_pensee "Il me donne en main le détecteur."

      chris "Alors. Pour commencer, les leds: quand c’est vert, tout est
      normal. Puis quand ça passe au jaune, une faible émanation est
      détecté. Plus on avance en couleur, plus la présence est proche."

      hide ChrisHeureux
      show ChrisBasic
      protag "D’accord."

      protag_pensee "Je me déplace, cherchant le moindre
      signe du fantôme. On s’oriente vers le cabanon désert."

      # Décor : Cabanon

      protag_pensee "On s’approche de la porte lentement. Et
      soudainement, un pic se produit sur le détecteur. Cela vire au
      rouge."

      hide ChrisBasic
      show ChrisHeureux
      chris "Regarde ! C’est rouge !"

      protag_pensee "Je fais attention autour de moi mais il n’y a
      rien. Nada. Aucune apparition, aucune silhouette, aucune voix
      lointaine."

      protag "C’est probablement des interférences."

      hide ChrisHeureux
      show ChrisNRV
      chris "Impossible. Un pic pareil ? Quelle machine ici pourrait faire
      ça ?"

      menu:
         "Insister":
            $ AF["Chris"] -= 5
            play sound "sfx/bad_choice.wav"

            protag "Puisque que je te dis que c’est des interférences,
            c’est logique."
            protag_pensee "Il récupère son détecteur
            sèchement."
            hide ChrisNRV
            show ChrisTimide
            chris "Si tu le dis."
            protag_pensee "Il me laisse là. Reprenant ses
            enquêtes ailleurs."
            hide ChrisTimide
            hide screen loveMeter
            with dissolve

         "Rester sceptique":
            hide ChrisNRV
            show ChrisBasic
            protag "Peut-être…j’en sais rien honnêtement."
            protag_pensee "Je lui rend son instrument et le
            laisse partir sur ses investigations."
            hide ChrisBasic
            hide screen loveMeter
            with dissolve

   label suite_j2:
   
      # Décor : Cabanon

      protag_pensee "Je vais dans la chambre pour me remettre
      de la crème solaire. Le soleil tape trop fort aujourd’hui."

      protag_pensee "Alors que je m’en étale sur le visage, un
      mouvement dans le coin de l'œil attire mon attention."

      show JaneNeutre
      show screen loveMeter("Jane")
      with dissolve

      protag_pensee " C’est elle, la fantôme. Figée, aucun son ne
      sort de ma bouche. Je fixe la silhouette féminine farfouiller dans
      nos affaires."

      protag_pensee "Pour m’assurer de la réalité, je me pince le
      bras aussi fort que possible."

      protag "Aie !" with vpunch

      hide JaneNeutre with dissolve
      protag_pensee "À ma douleur, elle se cache à toute
      vitesse. Mais c’est inutile, je l’ai vu."

      protag "Trop tard pour ça."

      show JaneBasic
      with dissolve
      JaneDoe "Mince alors."

      protag_pensee "Riant légèrement, elle porte un sourire qui
      m’irrite."

      protag "Je peux savoir ce que tu fais ? Et qui es tu d’abord ?"

      JaneDoe "Je me prénomme Jane, mademoiselle/damoiseau."

      $ JaneDoe_name = 'Jane'

      protag "Ne dis plus jamais ça."

      hide JaneBasic
      show JanePense
      with dissolve
      JaneDoe "J’ai été prise en flagrant délit on dirait. Miséricorde ! Je plaide
      coupable."

      protag_pensee "Jane tend les poignées comme prête à se
      faire passer les menottes. Son ton théâtrale me tape sur les nerfs."

      protag "T’as fini tes conneries ? Qui t’as permis de toucher à nos
      affaires ?"

      hide JanePense
      show JaneBasic
      with dissolve

      JaneDoe "C’est quoi ton nom à toi ?"

      protag_pensee "Je ressens un profond désir de la tabasser
      là, maintenant."

      menu:
         "Répondre à sa question":
            protag "C'est [protag_name]. Tu vas dégager maintenant ?"
            hide JaneBasic
            show JaneRizz
            with dissolve
            JaneDoe "Non."
            hide JaneRizz with dissolve

         "L'envoyer boulet":
            $ AF["Jane"] += 5
            protag "Si tu crois que je vais te le dire, tu rêves cocotte."
            hide JaneBasic
            show JaneFlip
            with dissolve
            JaneDoe "Tu veux jouer à ça. Ok, si tu ne me dis pas ton nom, je
            continuerai mes conneries jusqu'à ce que tu craques."
            protag "Tu le feras de toute façon."
            JaneDoe "Ah oui ! T’as raison."
            hide JaneFlip with dissolve

      show JaneBasic with dissolve

      protag_pensee "Je lève les yeux au ciel et croise les bras
      sous ma poitrine."

      protag "Tu peux m’expliquer pourquoi tu es là. Je veux dire en tant
      que revenante. Tu es la seule ?"

      JaneDoe "Oh ! Un polaroid."

      protag "Touche pas !"

      protag_pensee " Je m’élance vers elle en la voyant
      approcher des photos. Le visage rouge de gêne et de colère, je la
      traverse…logique. Elle se marre sans vergogne."

      hide JaneBasic
      show JaneRizz
      with dissolve
      JaneDoe "Oh mon dieu ! La gueule sur la photo."

      protag "On m'avait envoyé du gâteau au visage pour mon
      anniversaire !"

      JaneDoe "Pourquoi tu gardes ce dossier ? C’est hilarant."

      protag "Ma mère m’a donné une enveloppe pleine de photos avant
      de partir."

      JaneDoe "Oh mon dieu. Je ne pensais pas mourir une deuxième fois."

      protag "Je vais t’étriper !"

      hide JaneRizz
      hide screen loveMeter
      with dissolve

      protag_pensee "Malheureusement, ce maudit fantôme
      disparaît avant que je réagisse. Est ce que ça aurait servi ? Non.
      Mais je me serais défoulé(e)."

      # Décor : Bar (nuit)

      protag_pensee "Je me suis calmé un moment dans la
      chambre. Puis je suis allé(e) travailler au bar. L’animation joyeuse
      disperse Jane de mes pensées en ébullition."

      protag_pensee "Ce soir, Noa organise un karaoké. Après
      cette journée chargée, ça me surprend qu’il ne soit pas au lit. Les
      chansons s’enchaînent. Et je jure que la plupart des gens dans ce
      camping ne sont pas de grands chanteurs."

      protag_pensee "Les guirlandes de lumières clignotent
      au-dessus de ma tête. Un ricanement, que je connais trop bien,
      résonne."

      show ChrisTimide 
      show screen loveMeter("Chris")
      with dissolve

      protag_pensee "Je jette un coup d’oeil vers la table de
      Chris avec sa famille. Il a ses écouteurs à ses oreilles, toujours
      plongé dans le même podcast."

      protag_pensee "Chris se balance sur sa chaise, sans se
      douter une seconde de Jane à ses pieds. Que manigance cette
      foutue fantôme ? Elle me lance un regard plein de malice."

      menu:
         "Ne pas se mêler":
            $ AF["Jane"] += 5
            protag_pensee "Je préfère me détourner. Jane ne doit pas
            me perturber. Autant l’ignorer."
            hide ChrisTimide
            show ChrisEffraye
            play sound "sfx/MetalPipe.wav"
            chris "Ah !" with hpunch
            protag_pensee "Un fracas éclate dans mon dos. Chris est
            au sol attirant des regards. Il se hisse sur ses pieds sans attendre,
            rouge de gêne."
            hide ChrisEffraye

            jump suite_j2_2

         "Intervenir":
            $ AF["Chris"] += 5
            $ AF["Jane"] -= 5
            play sound "sfx/bad_choice.wav"

            jump intervention

      label intervention : 

         protag_pensee "Je sors immédiatement du bar, approchant
         de Chris. Je retiens son dossier d’une main avant qu’il ne tombe.
         Jane s’enfuit aussitôt, s’évaporant plus loin."

         hide ChrisTimide
         show ChrisPetitSourire
         chris "Merci. J’ai failli me couvrir de honte."

         protag "Y’a pas de quoi."

         hide ChrisPetitSourire
         hide screen loveMeter
         with dissolve

         protag_pensee " L’ambiance reprend, Noa délaisse la
         scène aux participants et s’appuie au comptoir."

         show NoaBasic
         show screen loveMeter("Noa")
         with dissolve

         protag "Tu prends enfin une pause ?"

         noa "Ouais. Je suis épuisé."

         menu:
            "Lui proposer un verre":
               $ AF["Noa"] += 5
               protag "Je t’offre un verre ?"

               hide NoaBasic
               show NoaBasic2
               noa "Oh oui, avec plaisir. Mais sans alcool s’il te plait."
               protag "Je hoche la tête et lui sers un Virgin
               Mojito."
               hide NoaBasic2
               show NoaTimide
               noa "Tu es doué(e)."
               hide NoaTimide

            "Ne rien faire":
               pass

      label suite_j2_2:
         show NoaBasic
         protag "Le boss est cruel de t’obliger à travailler même le soir avec
         tes journées."

         noa "Après, tu sais, je m’amuse dans mon boulot. Les enfants sont
         vraiment hilarants. Et j’adore savoir que je fais rire."

         protag "Quand même, tu te fais exploiter. Tu devrais demander une
         augmentation."

         hide NoaBasic
         show NoaBasic2
         noa "Je vais peut-être le faire. Tu t'inquiètes pour moi ?"

         menu :
            "Je suis simplement juste.":
               $ AF["Noa"] += 10
               $ courage += 5
            "Oui, c’est normal.":
               $ AF["Noa"] += 5
            "Non, je dis ça comme ça.":
               pass
            
         hide NoaBasic2
         show NoaNeutre
         protag_pensee "Un client nous interpelle dans notre
         discussion."

         "Client" "Mademoiselle/jeune homme, retournez travailler voulez
         vous. J’attends d’être servi depuis tout à l’heure."
         
         hide NoaNeutre
         show NoaBasic
         noa "C’est ma faute, je la monopolise. Salut."

         protag_pensee "Il remonte sur scène et moi je m’occupe
         du monsieur."
         hide NoaBasic
         hide screen loveMeter
         with dissolve

         jump j3













         














