---
title: "Paris Zope3/ECM/Five sprint: the wrap-up"
date: 2005-03-18
path: /blog/2005/3/paris-zope3-ecm-five-sprint-wrap-up
summary: "Here is the wrap up for the sprint that just happened in Nuxeo's premises in Paris this week."
tags: ['Nuxeo', 'Zope', 'CPS', 'SQL']
---

<p>Here is the wrap up for the sprint that just happened in Nuxeo's
premises in Paris this week.</p>

<p>As you can see, a lot has been achieved, though what has been done is
slightly different from what was envisionned in the first place.<br></p>

<p>The good news is that we now have a better understanding of how we're
going to gradually and non-disruptively shift from Zope2 to Zope3, thanks
to Five and the upcoming Zope 2.8 release.</p>

<hr size="2" width="100%">

## Status of the different projects:

<ul><li>
<p>Five/2.8 integration:</p>

<p>Martijn: A release (pr1) should be available soon on Codespeak with
2.8 + Five + ZX3.0.</p>

<p>This is the result of the work of many people.</p>

<p>We will followup on zope-dev mailling list.</p>

<p>We haven't solved the release management issues (coordination with
Andreas Jung and Zope Corp).</p>

<p>We'd like to release 2.8 by mid-april, but it is not sure if it's
going to happen.</p>

<p>Stefan: all tests (5459 of them!) pass for Zope 2.8 + Five.</p>
</li>
<li>
<p>RDF:</p>

<p>Michel: Tarek has added a bunch of test cases to Zemantic.</p>

<p>We've added text indexing to the litteral object values by backporting
Zope 3.1 text indexes.</p>

<p>I'me going to do a 0.5 release as a result from the sprint.</p>

<p>Tarek: I've integrated Zemantic in our webmail. At this time it is
used to replace a regular ZCatalog for search in body and headers, but
the next step will be to set up more complex relations like : "give me
the mails from bob written in the foo list about this subject" and
zemantic has now everithing needeed to do so. It now deals with thinking
about a efficient UI.<br></p>
</li>
<li>
<p>Repository/versions:</p>

<p>We've chatted about this between Zope, CPS, Silva and Plone hackers.
That's all - not enough for a press release :).</p>
</li>
<li>
<p>CPSSkins:</p>

<p>Currently, I have implemented global portlets that can be dragged and
dropped.</p>

<p>Only dummy portlets have been created. This is very simple to do.</p>

<p>Rendering (without any optimisations) is much faster than Zope 2.</p>
</li>
<li>
<p>Workflow</p>

<p>Julien: I have checked the WfMC engine made by Jim Fulton in a branch
of the Subversion.</p>

<p>I have started implementing something on the third day of the sprint.
I have created a utility that maps between documents and process
instances.</p>

<p>The advantage of this model is that we could have something as simple
as DCWorkflow for modeling the process definition. But we can also use
all the power of the activity-based workflow for complex business
applications with relations between different content objects.</p>

<p>I'm going to write a more complete description for what I have done
and send it to the zope3-dev mailing list for comments.</p>
</li>
<li>
<p>Directories:</p>

<p>Florent: directories are a model for what an LDAP or a SQL directory
is.</p>

<p>I've checked-in into the ParisSprint repository some code. There is no
UI yet but I'm working on it.</p>
</li>
<li>
<p>Forms:</p>

<p>Sidnei: I've made a prototype to convert AT schemas to Z3.</p>

<p>There are local utilities in Five.<br><br>
All of the CMF and Plone tests pass with 2.8 after some fixes.<br>
A new release of CMF (1.4.8) has been made.</p>
</li>
</ul><ul><li>
<p class="first">i18n:</p>

<p>Martijn: we've discussed some use cases.</p>
</li>
</ul><p><strong>The branching situation is now:</strong></p>

<ul class="simple"><li>Five has two branches: trunk (must stay compatible with 2.7) and Zope
2.8 integration<br><br></li>
<li>We're doing a preview or an alpha today and our goal is to have a 2.8
release in 1 month.</li>
</ul>


