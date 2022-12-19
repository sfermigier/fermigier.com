---
title: "Un enjeu: la définition d'un Système Standard pour Linux"
date: 1998-05-20
path: /blog/1998/5/enjeu-definition-systeme-standard-linux
summary: "Sept ans après l'apparition du premier embryon du noyau Linux, son succès est tel qu'on le retrouve maintenant dans de multiples distributions: Slackware (en perte de vitesse semble-t-il), Debian GNU/Linux, RedHat Linux, Caldera Open Linux, Turbo Linux, SuSE, pour ne citer que les plus connues."
tags: ['Linux', 'GNU', 'Debian', 'Red Hat', 'GNOME', 'KDE', 'Unix', 'Open Source']
---

<P>
Sept ans après l'apparition du premier embryon du noyau Linux, son succès est
tel qu'on le retrouve maintenant dans de multiples distributions: Slackware (en
perte de vitesse semble-t-il), Debian GNU/Linux, RedHat Linux, Caldera Open
Linux, Turbo Linux, SuSE, pour ne citer que les plus connues.
</P>

<P>
Bien entenu, dans toutes ces distributions, on retrouve toujours un
dénominateur commun qu'est le noyau Linux, programme qui va tourner en
permanence sur votre machine: le coeur du système d'exploitation. Mais
finalement, ce petit programme éxécutable de quelques centaines de Ko
seulement - le fameux "/vmlinuz" - et ses quelques modules dynamiques
associés (pour les versions récentes de Linux) ne sont pas grand chose
sans toutes les dizaines de Mo qui constituent le reste d'une distribution
Linux: le système de fichiers, les fichiers de configuration, les scripts
d'initialisation, les utilitaires GNU, les interfaces graphiques... Or,
sur tous ces points, il existe des différences sensibles entre les
distributions (atténué par l'existence d'un standard, le FHS, qui définit
précisément la place de chaque fichier dans l'arborescence du système
de fichiers).
</P>

<P>
Sans toutefois être incompatibles, et possédant un air de famille
marqué, une Debian et une RedHat n'ont pas exactement la même structure
de fichiers, ni des scripts d'initialisation strictement identiques,
ni (et là c'est un peu plus gênant) le même système de "packages"
logiciels. Ceci est à l'image de ce que l'on rencontre dans les Unix
commerciaux classiques (à une différence près: ces derniers n'ont même
pas le même noyau en commun, et ne sont pas du tout compatibles au niveau
du format des programmes exécutables!).
</P>

<P>
Ainsi, avec la multiplication des distributions, se pose un problème:
comment garantir qu'un programme conçu pour Linux va véritablement
fonctionner sur n'importe quel système? Cette interrogation a poussé
quelques-uns à souhaiter que l'on définisse un ``Système de Base
Linux Standard''. De cette façon, on définirait un système de base
pour une distribution Linux, ce qui n'empêcherait pas forcément que
des fonctionalités plus avancées y soient ajoutées. Tous les détails
des propositions pour ce système de base sont disponibles sur <A HREF="http://slashdot.org/features/9804191033234.shtml">http://slashdot.org/features/9804191033234.shtml</A>.
</P>

<P>
Bruce Perens (qui a récemment quité Debian) est à l'origine de cette
initiative, soutenue par Linus Torvalds et par Linux International. Plusieurs
distributions importantes adhèrent déjà au projet comme Caldera Open
Linux, SuSE, et Turbo-Linux (Red Hat reserve pour l'instant son avis, en
souhaitant juger le projet sur sa valeur technique).
</P>

<P>
Les spécifications du ``Système de Base Linux Standard''
imposent que ses composants soient libres (ou ``<A HREF="http://www.opensource.org/osd.html">Open Source</A>'': GPL, Licence
BSD ou MIT ou Artistique, etc.).  Or il n'est pas clair à ce point si le
``Système de Base Linux Standard'' intègrera un environnement X et un
desktop-manager. Si c'était le cas, cette restriction risquerait de nuire
à l'épanouissement du Desktop Manager KDE qui, bien que sous licence GPL,
repose sur des bibliothèques graphiques (Qt) gratuites, mais non libres,
et ouvrirait en grand la porte à son concurrent direct - Gnome.
</P>

<P>
La question de la standardisation des interfaces graphiques, qui est
un enjeu essentiel pour le monde Unix, reste donc ouverte.
</P>


