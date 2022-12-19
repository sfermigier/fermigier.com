---
title: "CPS4/Z3ECM sprint, day 1, short report"
date: 2006-04-19
path: /blog/2006/4/cps4-z3ecm-sprint-day-1-short-report
summary: "The sprint has started yesterday with notable guests Jean-Marc and Dario from Chalmers, Joachim from AixtraWare, and Michael from OpenApp, and a bunch of Nuxeo guys."
tags: ['Nuxeo', 'Zope', 'CPS']
---

<p>
The <a href="http://www.z3lab.org/sections/news/zope-3-z3ecm-april">sprint</a> has started yesterday with notable guests Jean-Marc and Dario from <a href="http://www.chalmers.se/">Chalmers</a>, Joachim from <a href="http://www.aixtraware.de/">AixtraWare</a>, and Michael from <a href="http://www.openapp.biz/">OpenApp</a>, and a bunch of Nuxeo guys.
</p><p>
The goal is still to provide Zope3 ECM components for <a href="http://blogs.nuxeo.com/sections/blogs/fermigier/2006_04_13_cps4-project-officially-started">CPS4</a>
</p><p>
Yesterday morning was spent discussing the AJAX and JavaScript MVC features of CPSSkins v3 (more info in Jean-Marc's <a href="http://blog.gmane.org/gmane.comp.web.zope.zope3.ecm.general">numerous messages</a> in the mailing list, or on the <a href="http://www.z3lab.org/">z3lab</a> website).
</p><p>
Then we had a discussion about the JCR content model and the JCR schemas for documents (JackRabbit's <a href="http://jackrabbit.apache.org/doc/nodetype/cnd.html">CND</a>).
</p><p>
In the afternoon, work has proceeded in pairs or small groups.
</p><p>
Florent and Dario have investigated existing schemas sytems and are trying to find a common subset. Now, they will code and write an importer for the JCR schemas.
</p><p>
Lennart and Michael are looking on how to plug the Zope3, Twisted-based, publisher into Zope2.
</p><p>
Jean-Marc, Tarek and Joachim are working on AJAX and CPSSkins. They have created <a href="http://svn.nuxeo.org/trac/pub/browser/nuxeo.javascript/trunk/src/nuxeo/javascript/">small package</a> of all the ressources used by cpsskins so that they can be reused in CPS. The goal now is to instanciate de Zope 3 CPSSkins utilities in Zope 2, look for breakages, and fix them.
</p><p>
Bogdan is working on <a href="http://www.eclipse.org/proposals/apogee/">Apogee</a> integration through <a href="http://www.zeroc.com/">ICE</a>.
</p> 

