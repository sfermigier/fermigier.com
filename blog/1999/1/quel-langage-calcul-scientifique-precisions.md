---
title: "Quel langage pour le calcul scientifique? Des precisions"
date: 1999-01-08
path: /blog/1999/1/quel-langage-calcul-scientifique-precisions
summary: "[Au sujet de l'article récent OCAML arrive en tête d'une étude comparative de langages, Jérôme Kalifa, chercheur-doctorant en mathématiques appliquées à l'école polytechnique, m'a fait parvenir les précisions suivantes:] J'ai contacte David MacClain au sujet de son comparatif."
tags: ['Linux', 'GNU']
---

<P>
[Au sujet de l'article récent <A HREF="http://www.linux-center.org/news/#331">OCAML arrive en tête d'une étude comparative de langages</A>,
Jérôme Kalifa, chercheur-doctorant en mathématiques appliquées
à l'école polytechnique, m'a fait parvenir les précisions suivantes:]
</P>

<P>J'ai contacte David MacClain au sujet de son comparatif. Premierement,
les resultats un peu decevants de gcc/g++ s'expliquent en grande partie
par le fait qu'il soit reste avec les gcc et g++ "officiels" du projet GNU
et non avec ceux du projet <A HREF="http://www.cygnus.com/egcs/">egcs</A>,
qui incorporent enormement d'optimisations, et qui sont censes etre
beaucoup plus rapides. Et d'ailleurs, ils le sont effectivement.</P>

<P>Notez aussi que MacClain m'a signale que sur des benchmarks de plus
petite taille, gcc/g++ etait imbattable, alors que les resultats
s'effondrent curieusement sur les benchmarks de plus grande
taille. Inversement, le compilateur d'Intel dispose d'optimisations
remarquables sur les pipelines x86, qui lui permettent de briller sur
les gros benchmarks.</P>

<P>Pour en revenir a egcs, il vient de le recuperer, et semble avoir
l'intention de refaire tourner ces tests, mais n'a encore rien
installe pour l'instant. Notez qu'il utilise GNUWin32 sous NT 4. Je
pense qu'il serait peut-etre bon que l'ensemble de ces tests soient
repris dans un environnement Linux, y compris pour les langages
interpretes (Mathematica, etc...) dont les performances fluctuent
souvent de maniere significative selon les plateformes. Je n'ai pas le
temps de m'en occuper pour le moment (fin de these qui n'en finit
pas). Si quelqu'un a envie de s'en charger... sinon j'essaierai de le
faire des que j'aurai une occasion de souffler.</P>

<P>Il y a un certain nombre de choses a dire sur le calcul
scientifique. Premierement, des tests ont ete menes sur Mathematica, qui
se veut a la fois un outil de calcul formel et de calcul numerique. Dans
les faits, ses performances en utilisation reelle pour le calcul numerique
sont deplorables, comparees a d'autres langages environnements/dedies
tels que Matlab (la reference, le plus rapide en utilisation
reelle), <A HREF="http://www-rocq.inria.fr/scilab/">Scilab</A>
(tres bon logiciel libre Matlab-like de l'INRIA), et <A HREF="http://www.che.wisc.edu/octave/">Octave</A> (autre Matlab-like
libre, moins riche que Scilab, mais plus compatible avec Matlab). Je lui
ai donc suggere de tester Matlab/Scilab/Octave, mais il n'en a pas sous la
main et n'a pas apparement pas l'intention de trop fouiller. Je n'ai pas
assez insiste sur le fait qu'il obtiendrait des resultats tres diferents
avec ces trois-la qu'avec Mathematica. Il est apparement aussi branche sur
<A HREF="http://www.physics.berkeley.edu/computing/yorick/">Yorick</A>,
un nouveau langage des Livermore Labs.</P>

<P>
[A noter, ce qui n'a pas été signalé dans mon intervention précédente,
que la version 2.01 d'<A HREF="http://caml.inria.fr/">Objective Caml (OCAML)</A>
est sortie récemment, avec un modèle objet vraiment bien conçu, contrairement
à certain langage à la mode dont le nom commence par J.]
</P>


