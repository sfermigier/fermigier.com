---
title: "JSR 170 (Java Content Repository) and Zope 3 ECM"
date: 2005-06-25
path: /blog/2005/6/jsr-170-java-content-repository-zope-3-ecm
summary: "I&#39;m at the Z3ECM sprint in EuroPython 2005 and I&#39;ve spent yesterday trying to play with the JCR (Java Content Repository aka JSR-170) trying to understand how easy it would be to how a Zope content management system into a JCR (short answer: not easy - despite of claims of interoperability, JCR is a 100% Java technology)."
tags: ['Python', 'Zope', 'CPS', 'SQL', 'Java', 'Apache']
---

I&#39;m at the Z3ECM sprint in EuroPython 2005 and I&#39;ve spent yesterday trying
to play with the <a href="http://www.artima.com/lejava/articles/contentrepository.html">JCR</a> 
(Java Content Repository aka JSR-170) trying to understand

<ol>
<li>how easy it would be to how a Zope content management system into a JCR
(short answer: not easy - despite of claims of interoperability, JCR is a
100% Java technology).</li>
<li>if there are useful ideas in the JCR that could be put into the design
of the repository for Z3ECM (short answer: probably, yes)</li>
</ol>

<h4>Hooking Zope into a JCR</h4> 

After installing <a href="http://incubator.apache.org/jackrabbit/">Jackrabbit</a> (an open source implementation of the JCR made by the Apache project) and testing it 
with some Java examples, I've trying calling it from Python using the <a href="http://jpype.sourceforge.net/">JPype</a> Java&lt;-&gt;Python 
bridge.

Installing Jackrabbit is not that hard, it took me about one hour though 
since I haven't done any Java development since 1996 and didn't have all the 
right tools (including Maven and a dozen of libraries like xalan, xerces, 
log4j, etc.) from the Apache Java project installed. Not a big deal 
anyway.

Unfortunately, JPype is pretty much a work in progress, that would benefit 
from more users and developers. There are, seemingly, limitations that 
prevented me from login in the JCR so this experiment didn't succeed and my 
knowledge of Java is much to light to keep on the experiment.

If we succeed in hooking Python/Zope into a JCR (which is, overall, just a 
question of Java/JNI knowledge and grunt work), I think the most important 
question is how the to make Zope and Java transactions systems work well 
together (transactions are an optional JSR-170 feature, but I don't see how 
a repository without transactions would be useful at all).

<h4>Ideas from the JCR specs</h4> 

A JCR is a repository of nodes stored in whatever you want (flat files, SQL 
DB, object DB, XML DB...). Nodes are just collections of properties, so it's 
a very data-centric model that doesn't impose a programming model, and would 
work very well outside of Java. In practice, Nodes are the documents you're 
managing with you application. Nodes can be accessed from a path 
(hierarchical navigation, something Zope developers are very familiar 
with), or by UUID (unique identifiers). More interesting are:

<ol>
<li>Querying nodes, which is based on a simplified XPath query language,
or, optionally, a variant of SQL</li>
<li>XML import/export, which would provide interoperability between
repositories at list in the sense that you can import data from one
repository to another (no vendor lock-in)</li>
<li>Versionning</li>
<li>Events<br></li>
</ol> 

Overall, nothing very different from what we are already doing with the CPS 
Repository (from CPSCore), but it's interesting to try to dig a bit further 
in the specs and to keep then in our minds when designing the Z3ECM model 
for the repository, querying, and versionning.

<h4>Related standards</h4> 

The <a href="http://www.webdav.org/deltav/">WebDAV/DeltaV</a> standard for 
versionning and its JCP interpretation (<a href="http://jcp.org/aboutJava/communityprocess/review/jsr147/index.html">JSR-147</a>) are related to these specifications. 

