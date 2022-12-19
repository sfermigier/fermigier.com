---
title: "Sprint wrapup"
date: 2005-06-26
path: /blog/2005/6/sprint-wrapup
summary: "Jean-Marc Orliaguet: has ported (in fact totally rewrote) CPSSkins for Zope3."
tags: ['Zope']
---

<br><p><strong>Jean-Marc Orliaguet</strong>: has ported (in fact totally rewrote) <a href="http://www.medic.chalmers.se/%7Ejmo/CPS/">CPSSkins</a> for Zope3. The
 "main content area" (the place where the current document or folder is
 displayed) is now a portlet like all the other portlets.</p> 
 <p>Ph. von Weitershausen: we need a common vocabulary for portlets,
 pagelets, whatever. Otherwise it gets confusing.</p> 
 <p><strong>Tres Seavers</strong>: has worked on the <a href="http://codespeak.net/svn/z3/pipelines/trunk">pipeline</a> machinery.
 The point is to be able to define series of transformations that apply to an
 input. A pipeline is a list of callable objects. For example, a pipeline
 that converts an XML document to a DOM, then does something to the DOM like
 adding some elements, then converts it back to a string. The code for
 pipeline itself is not very interesting.</p> 
 <p><strong>Tarek Ziad&#233; / Godefroid Chappelle</strong>: AJAX development for Zope = <a href="http://svn.nuxeo.org/trac/pub/browser/z3lab/azax/trunk/">AZAX</a>. We
 have created a model where yuo creat .azax files that are combined with .pt
 files, and a preprocessor creates on the fly the JavaScript code that is
 included in the HTML page. Everything else is standard AJAX. The benefit for
 the developer is that he/she doesn't have to write complex JS code.</p> 
 <p><strong>Florent Guillaume</strong>: after I started coding a proxy model for Z3, I
 realized that the proxy model is too complex and that there are many risks
 associated. And I've decided to go back to a more traditional model with
 checkins/checkouts. I'll be presenting that at EuroPython tomorrow.</p> 

