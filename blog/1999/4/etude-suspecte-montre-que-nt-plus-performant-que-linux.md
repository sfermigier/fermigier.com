---
title: "Une étude suspecte montre que NT est plus performant que Linux"
date: 1999-04-14
path: /blog/1999/4/etude-suspecte-montre-que-nt-plus-performant-que-linux
summary: "Un laboratoire de test ``indépendant'' vient de publier une étude qui montre que NT Server serait 2.5 fois plus rapide que Linux 5.2 (avec noyau 2.2) comme serveur SMB et 3.5 fois plus rapide avec IIS comme serveur Web que Linux avec Apache."
tags: ['Apache', 'Linux', 'Microsoft']
---

<P>
Un laboratoire de test ``indépendant'' vient de publier une
<A HREF="http://www.mindcraft.com/whitepapers/nts4rhlinux.html">étude</A>
qui montre que NT Server serait 2.5 fois plus rapide que Linux 5.2 (avec
noyau 2.2) comme serveur SMB et 3.5 fois plus rapide avec IIS comme
serveur Web que Linux avec Apache.
</P>

<P>
Les conditions de ce test, qui contredit l'expérience de
nombreux administrateurs systèmes, sont mises en doute dans le
<A HREF="http://linuxtoday.com/stories/4932_flat.html">forum de
LinuxToday</A> qui suit l'annonce. On peut notamment noter que cette
étude a été <B>commanditée par Microsoft</B> (<EM>Mindcraft, Inc.
conducted the performance tests described in this report between March
10 and March 13, 1999. Microsoft Corporation sponsored the testing
reported herein.</EM>).
</P>

<P>
Voir notamment cette réponse de Jeremy Allison, <EM>Team Leader</EM>
de l'équipe <A HREF="http://www.samba.org/">Samba</A>:
</P>

<BLOCKQUOTE>
<P>It's not really suprising. They did *no* tuning on the Linux server at all. I can well
imagine these results being accurate without modifying the bdflush and file system
cache parameters on a Linux 2.2.x kernel. You get a factor of 2 performance
improvement with Linux and Samba when you set these correctly.</P>

<P>The server itself was a Dell PowerEdge with 4Gb of Ram, but in the Linux section of their
report it states :</P>

<P>"The Linux kernel limited itself to use only 960 MB of RAM"</P>

<P>This in itself will kill the Linux performance compared to the NT performance. When I did
the PC Week benchmark using the VA Research box Linux was using the full amount
of server RAM.</P>

<P>Note as well that they did the benchmark with RAID *Zero* on the box. The PC
Week/VA Research benchmark was done with RAID 5. This makes a *big* difference
:-).</P>

<P>There are other tricks that they used (as I've been benchmarking with NT and
Samba/Linux for a while I know quite a few of 'em). One is to test with Windows 95/98
clients. To be completely honest Samba/Linux doesn't serve Windows 95/98 clients as
well as NT does. However, Windows NT is *terrible* when serving NT clients.</P>

<P>Note they don't mention the client OS type anywhere in the document :-). There are a
few other tricks that can skew performance also (the Samba "read raw/write raw"
prameters make a difference when used against Win9x clients for example).</P>

<P>At least this shows that we're starting to seriously annoy them :-) :-). I'm quite flattered
really.</P>

</BLOCKQUOTE>
<P>
<B>Mise à jour importante:</B>: <EM>Linux Weekly News</EM> a mis en place
une <A HREF="http://lwn.net/1999/features/MindCraft.phtml">page spéciale</A>
pour rapporter les différentes critiques qu'on peut adresser à cette
étude. On y trouve par exemple la <A HREF="http://www.novell.com/advantage/nw5/nw5-mindcraftcheck.html">réponse de Novell</A> à un test similaire.
</P>

<P>
<B>Deuxième mise à jour:</B>: Eric Lee Green,
de Linux Hardware Solutions, a également écrit un <A HREF="http://www.linux-hw.com/~eric/mindcraft.html">commentaire</A>
sur la crédibilité de ce rapport.
</P>


