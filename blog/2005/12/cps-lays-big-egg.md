---
title: "CPS lays a (big) egg"
date: 2005-12-16
path: /blog/2005/12/cps-lays-big-egg
summary: "I'm experimenting with eggification of CPS, trying to have support in place for the upcoming CPS 3.4.0 release."
tags: ['Nuxeo', 'Python', 'Zope', 'CPS']
---

<p>I'm experimenting with eggification of CPS, trying to have support in
place for the upcoming CPS 3.4.0 release. I already have something basic
working, here is how to test it:<br></p><ol><li>Create a fresh Zope 2.8.4 instance (with Python 2.4).</li>

<li>Download the Basket product from <a href="http://www.plope.com/software/Basket/Basket">http://www.plope.com/software/Basket/Basket</a>
(I have tested with version 0.2)</li>

<li>Download the CPS egg from <a href="http://www.cps-project.org/static/eggs/">http://www.cps-project.org/static/eggs/</a></li>

<li>Create a lib/python directory in your instance, and put the egg
there</li>

<li>Start Zope and play with CPS</li>
</ol><br>
Remarks:<br><ol><li>If it doesn't work, you may checkout CPS3 from SVN from <a href="http://svn.nuxeo.org/pub/CPS3/trunk">http://svn.nuxeo.org/pub/CPS3/trunk</a>
and, type 'make' then 'make egg' and hack the setup.py until your egg is
working (well that's how I did it anyway). Then send me the patch or commit
your changes if you have SVN access.<br></li>

<li>The big egg will be broken into smaller eggs. I fact, that is the main
reasons to have eggs in the first place, because currently the installation
procedure is not simpler that with the normal tarball.<br></li>

<li>I hope the Basket product will be integrated soon into Zope, though I
understand it's already too late for Zope 2.9.</li>
</ol><p>BTW: kudos to <a href="http://www.plope.com/">chrism</a> for the Basket
product!</p> 

