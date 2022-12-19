---
title: "Portages d'applications sous Linux"
date: 1998-11-02
path: /blog/1998/11/portages-applications-sous-linux
summary: "Malgré les dénégations véhémentes d'il y a quelques mois, on vient d'apprendre que Lotus allait porter sur Linux deux de ses logiciels phares, la suite bureautique SmartSuite et le logiciel de groupware Notes/Domino à l'horizon 1999."
tags: ['Linux', 'Unix', 'Microsoft']
---

<P>
Malgré les dénégations véhémentes d'il y a
quelques mois, on vient d'apprendre que Lotus <A HREF="http://www.infoworld.com/cgi-bin/displayStory.pl?981031.ehlotus.htm">allait porter sur Linux</A> deux de ses logiciels phares, la suite
bureautique SmartSuite et le logiciel de <EM>groupware</EM> Notes/Domino
à l'horizon 1999.
</P>

<P>
Dans ce cas, le portage est d'autant plus aisé que des portages sur UNIX
existent déjà. (``Il suffit de taper make'', selon les paroles historiques
de Pierre Ficheux.)
</P>

<P>
Pour les logiciels qui n'existent actuellement qu'en version Windows,
un récent <A HREF="http://lwn.net/daily/corel.html">message du chef
du développement Linux chez Corel</A> démontre la viabilité d'une
possibilité technique très intéressante, l'utilisation de la bibliothèque
de compatibilité <A HREF="http://www.winehq.com/">Wine</A>.
</P>

<P>
Il faut savoir que le projet (libre) Wine s'attaques à deux objectifs
séparés: d'une part un émulateur Win3.x et Win32 au dessus de X11
et d'Unix, et d'autre part une bibliothèque permettant le portage
d'application Windows sous Linux.
</P>

<P>
A mon avis, la réalisation d'un système capable d'émuler Windows à 100%
(autrement dit, avec les bugs et les API cachées) est un projet très
délicat, dans la mesure où celà signifie se soumettre aux règles du
jeu imposées par Microsoft. En revanche, avec une bibliothèque de
compatibilité pour développeurs, on peut réduire considérablement le
travail de portage, tout en gardant le contrôle sur ce qui se passe.
</P>

<P>
L'annonce de Corel d'utiliser le projet Wine pour le portage de ses
applications bureautiques, et surtout de contribuer en retour à son
développement, est donc une très bonne nouvelle.
</P>


