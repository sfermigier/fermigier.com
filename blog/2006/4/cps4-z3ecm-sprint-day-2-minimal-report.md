---
title: "CPS4/Z3ECM sprint, day 2, minimal report"
date: 2006-04-20
path: /blog/2006/4/cps4-z3ecm-sprint-day-2-minimal-report
summary: "Yesterday was the second day of the Z3ECM / CPS4 sprint."
tags: ['Zope']
---

<p>
Yesterday was the second day of the <a href="http://www.z3lab.org/">Z3ECM</a> / <a href="http://blogs.nuxeo.com/sections/blogs/fermigier/2006_04_13_cps4-project-officially-started">CPS4</a> sprint.
</p><p>
Michael and Lennart have got Zope 2 working on a Twisted server. They are using
the Zope 3 publisher now in Zope 2. No benchmarking has been done yet.  The
code lives in Sidnei's publication-refactor branch of Zope2 (Sidnei did most of
the work).
</p><p>
Tarek, Joachim and Jean-Marc have worked on CPSSkins integration. There
were many branches. They finally landed on a Philikon branch where Jean-Marc
did all the hard work. Tarek is now working on a "resource library"
for Zope 2. Joachim is trying to use the JS library package that was
created yesterday manually.
</p><p>
Florent and Dario have written an importer for JCR schemas expressed in CND
notation. They have a parser for that and are able to build a Zope 3 schema
from it. They are now stuck on the fact that the JCR can have children with the
same name.
</p> 

