---
title: "CPS4/Z3ECM sprint, day 3, short report"
date: 2006-04-21
path: /blog/2006/4/cps4-z3ecm-sprint-day-3-short-report
summary: "Yesterday was the third day of the Z3ECM / CPS4 sprint."
tags: ['Nuxeo', 'Zope', 'CPS']
---

<p>
Yesterday was the third day of the <a href="http://www.z3lab.org/">Z3ECM</a> / <a href="http://blogs.nuxeo.com/sections/blogs/fermigier/2006_04_13_cps4-project-officially-started">CPS4</a> sprint.
</p><p>
Florent and Dario are now able to create complex Zope3 schemas from the
JackRabbit schemas. There is now a <a href="http://svn.nuxeo.org/trac/pub/browser/nuxeo.capsule/trunk/">nuxeo.capsule</a> package that contains just
base classes and a <a href="http://svn.nuxeo.org/trac/pub/browser/nuxeo.jcr/trunk/">nuxeo.jcr</a> package that contains the parser.  The next steps
are to create new node types in the JCR, export them at startup, and have
Zope to parse them as interfaces and schemas. Then we have to find out how
to exactly use them.
</p><p>
Jean-Marc took the upcoming Zope 2.10 branch (w/ Philipp's and Jim's branches)
and get all the ZCML files parsed and the utilities registered, etc.  Then he
started to look at Jim's refactoring of local utilities to use the same API.
He is now half-way in getting something that works. The next step is to
register these utilities in Zope 2.
</p><p>
Michael got the Zope 3 publisher to work in Zope 2 for ZServer.You can now
use all the 4 combinations of Zope 2 publisher vs. Zope 3 publisher, and
ZServer vs. Twisted.
</p><p>
Tarek has worked on a <a href="http://svn.nuxeo.org/trac/pub/browser/CPSResourceLibrary/trunk/">CPSResourceLibrary</a>, similar to <a href="http://svn.zope.org/zc.resourcelibrary/trunk/">zc.resourcelibrary</a>.  It's
now finished. Joachim has used it on some portlets. Tomorow Tarek is going to
look into the use cases of the <a href="http://svn.nuxeo.org/trac/pub/browser/nuxeo.javascript/trunk/">JS library</a> packaged on monday in CPS 3.4.
</p> 

