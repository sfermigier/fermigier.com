---
title: "FAQ sur les forks de logiciels libres"
date: 2021-10-02
path: /blog/2021/10/forks-de-logiciels-libres
summary: "On m'a posé récemment quelques questions sur les forks de logiciels libre. Voici quelques éléments de réponse."
tags: ['Logiciel libre', 'Droit', 'Open Source']
---

On m'a posé récemment des questions sur les forks de logiciels libre. Voici quelques éléments de réponse.

> Prenons le cas d'un logiciel disponible en licence MIT ou Apache 2.0, qu'une entreprise prendrait comme base d'un produit ensuite commercialisé (le genre de cas qui ne plait pas toujours aux défenseurs du LL).

Déjà là il y a plusieurs distinctions à faire:

1) La plupart des défenseurs du LL ne sont pas choqués qu'un logiciel libre puisse être ["commercialisé"](https://cnll.fr/media/LivretBleu_ModelesEconomiques_GT-LogicielLibre_Systematic.pdf), sous certaines formes (et notamment lorsque cela reste un logiciel libre).

2) Ce qui peut déplaire à certains (mais pas à tous - certains trouvent cela au contraire totalement légitime, tant que c'est fait en accord avec la licence du projet), c'est une "propriétarisation" du logiciel (i.e. d'en passer, tout ou partie, sous une licence non libre, aussi appelée "propriétaire" ou "privative").

Cette propriétarisation peut prendre plusieurs aspects, dont:

a) L'utilisation du logiciel en tant que composant / bibliothèque d'un autre logiciel. C'est extrêmement courant (par ex, mes logiciels, dont quelques-uns ne sont pas open source, intègrent typiquement plus d'une centaine de composants tiers). C'est communément accepté, car le logiciel (composant) d'origine ne perd (*a priori*) pas sa valeur du fait de son utilisation dans un logiciel privateur et son développement peut même être renforcé du fait de cette utilisation.

b) L'ajout de surcouches propriétaires, par un mécanisme d'extension (*plugin*) à un logiciel libre. C'est communément accepté, mais peut-être un peu moins que a).

c) Le fork d'une base de code existante. Ça c'est souvent perçu avec réticence. Mais ça dépend aussi de l'état de la base de code initiale et de sa base utilisateurs. (*Cf. infra*).

Pour moi, le principe est simple: le projet au départ a une licence, qui a *a priori* été choisie pas le ou les auteurs du logiciel en connaissance de cause (mais pas toujours, ce qui peut être la source de malentendus), et si ce qu'on en fait est en accord avec la licence de départ, alors personne n'est en droit de se plaindre.

Les problèmes peuvent surgir, par exemple, si:

a) Les auteurs ont mal choisi la licence par rapport à leurs intentions initiales.

b) Le contexte stratégique et/ou les intentions des auteurs ont changé.

c) Une communauté s'est créée autour du logiciel qui ne partage pas les intentions des auteurs.


> Au fil de temps, l'entreprise transforme le code, n'ajoutant pas que des surcouches mais bien des modications majeures des fonctionnalités initiales. 
> Y a-t-il un moment où un logiciel, initialement en licence MIT ou Apache 2.0, peut être considéré comme un nouveau logiciel ? Y a-t-il un principe, un seuil (par exemple : X % du code modiié par rapport à l'original) qui permet à une entreprise d'individualiser son produit, voir de créer un nouveau projet open source ? 

Sur ces questions, comme partout en droit, il y a des pincettes à prendre. Le mieux est de lire [le bouquin de Pellegrini et Canevet](https://www.lgdj.fr/droit-des-logiciels-9782130626152.html) mais il fait 600 pages. Si on préfère éviter cet effort, il y a le ["livret bleu" sur les fondamentaux juridiques](https://cnll.fr/media/LivretBleu_Juridique-2eEdition_GT-LogicielLibre_Systematic_Nov2016_web.pdf) qui a été aussi relu par Pellegrini et qui est pas mal du tout.

Mais pour répondre brièvement et sous réserves de précisions à trouver dans les deux documents sus-mentionnés:

Si je modifie le code d'un logiciel, ça devient une "œuvre dérivée" et dans ce cas le droit des œuvres dérivées s'applique. Les conditions de réalisation, d'utilisation et de diffusion de cette œuvre dérivée doivent tenir compte de la licence d'origine, et peuvent en différer éventuellement si la licence d'origine le permet.

Enfin, oui, il arrive souvent qu'un nouveau projet soit forké à partir d'un projet existant. Cela peut se faire dans le calme ou dans le drame (il y a un exemple récent). Les cas légitimes me semblent être:

a) L'auteur ou les auteurs ont cessé de maintenir le projet, parfois même de répondre aux sollicitations.

b) Les nouveaux auteurs souhaitent emmener le projet dans une direction qui ne convient pas aux anciens auteurs.

c) Les auteurs ont décidé de faire don du logiciel à une "fondation" de logiciel libre (comme Apache ou Eclipse), qui impose le renommage et des modifications de la base de code pour suivre ses propres règles (ça m'est arrivé, c'est très pénible)

d) Une entreprise décide de propriétariser un logiciel libre (comme je le disais au début, ça peut être mal vu - ou pas - mais c'est légitime si la licence de départ le permet).
