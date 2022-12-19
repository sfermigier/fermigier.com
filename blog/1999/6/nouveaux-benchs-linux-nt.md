---
title: "Nouveaux benchs Linux / NT"
date: 1999-06-30
path: /blog/1999/6/nouveaux-benchs-linux-nt
summary: "On se souvient des tests complètement fantaisistes de Mindcraft (société financée par Microsoft) qui il y a deux mois concluaient que NT était de 2.5 a 3.7 fois plus performant que Linux."
tags: ['Apache', 'Linux', 'Microsoft']
---

<P>
On se souvient des tests complètement fantaisistes de Mindcraft (société
financée par Microsoft) qui il y a deux mois concluaient que
NT était de 2.5 a 3.7 fois plus performant que Linux.
</P>

<P>
Les conditions dans lesquelles s'était déroulée cette première série
de tests étant par trop irrégulières, une deuxième série a eu lieu
plus récemment qui conclut encore a la supériorité de NT, mais par un
écart infiniment plus faible (40 a 50 %). Evidemment, Microsoft pavoise
et la partie de la presse la moins réputée pour son sens critique (<A HREF="http://www.zdnet.fr/cgi-bin/a_actu.pl?File_ini=a_actu.zd&amp;ID=9889">Ziff
Davis</A> pour ne pas les nommer) s'en fait l'écho.
</P>

<P>
Pourtant il n'y a vraiment pas de quoi se vanter, tout simplement
parce que les conditions dans lesquelles les tests ont été réalisés
sont totalement étrangères aux conditions réelles d'utilisation d'un
gros serveur.  Un test beaucoup plus sérieux réalisé par le magazine
allemand C't (<A HREF="http://www.heise.de/ct/english//99/13/186-1/">Mixed
Double: Linux and NT as Web Server on the Test Bed</A>, texte en anglais)
explique clairement la situation: Linux ne sait actuellement pas tirer
pleinement partie de la multiplication des cartes réseau (Ethernet
100 Mbits), et le test de Mindcraft utilisait un serveur avec 4 cartes
réseau. Dans les autres cas (une seule carte), les tests conduits par
C't montrent une supériorité nette voire très nette de Linux.
</P>

<P>
Citons la conclusion de l'article:
</P>

<BLOCKQUOTE>
In the web server areas most relevant for practical use, Linux and Apache
are already ahead by at least one nose. If the pages don't come directly
from the system's main memory, the situation is even reverted to favour
Linux and Apache: Here, the OpenSource movement's prime products leave
their commercial competitors from Redmond way behind.
</BLOCKQUOTE>
<P>
Et aussi ce passage:
</P>

<BLOCKQUOTE>
Relevant for practical use is Mindcraft's critical assessment of Linux and
Apache tuning tips being difficult to come by. True enough, professional
Linux support structures are still in development. However, Apache and
Linux developers have been extremely helpful. While Microsoft needed
more than a week to come up with the ListenBackLog hint, our questions
regarding Linux and Apache problems were answered with helpful hints and
tips within hours.  Emails to the respective mailing lists even resulted
in special kernel patches which significantly increased performance. We
have, on the other hand, never heard of an NT support contract supplying
NT kernels specially designed for customer problems.
</BLOCKQUOTE>


