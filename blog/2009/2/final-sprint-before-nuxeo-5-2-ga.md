---
title: "Final sprint before Nuxeo 5.2 (GA)"
date: 2009-02-18
path: /blog/2009/2/final-sprint-before-nuxeo-5-2-ga
summary: "The final (GA) release of Nuxeo EP 5.2 should be ready in less than a month now."
tags: ['Nuxeo', 'SQL', 'Java']
---

<p>The final (GA) release of Nuxeo EP 5.2 should be ready in less than a month now. Here are some notes on how we plan to proceed with the final sprint until the release:</p> 
 <ul><li><p>you will find below a list of the issues we&#8217;d like to address before the release (some of them might already have been addressed).</p></li>
<li><p>most of these issues have been affected to teams or developers, who are working on them during this sprint.</p></li>
<li><p>so next release, 5.2 RC, is scheduled in two weeks (Friday 27th) and hopefully will be feature-complete (and fairly stable).</p></li>
<li><p>the final release will happen after some testing and eventual bugfixing, hopefully less than a couple of weeks later.</p></li>
<li><p>the Jira (<a href="http://jira.nuxeo.org/browse/NXP">http://jira.nuxeo.org/browse/NXP</a>) has been updated accordingly (almost, it&#8217;s not completely in sync with the list below, we will try a slightly different system when we will start planning the next releases to ensure that the Jira state accurately reflects the products and release backlogs).</p></li>
</ul><h3>Task we must do before GA</h3> 
 <ul><li><p>Ensure Java 6 compatibility for webservices:</p>

<p>The build will remain in Java 5, but we will support deployment on a 1.6 JVM.</p></li>
<li><p>Events:</p>

<p>There are some errors in the logs while processing some events. This seems to only happend for specific events
(emptyDocumentModelCreated), but this still needs to be checked and fixed.
We should also unit test all async listeners since it&#8217;s now possible.</p></li>
<li><p>Data Migration:</p>

<p>We need to be able to migrate content from the JCR backend to the new VCS (SQL-based) backend. </p></li>
<li><p>WebServices:</p>

<p>We still have the &#8220;old&#8221; webservice based in JBossWS and JAX-RPC.</p>

<p>These needs to go away :</p>

<ul><li>there are issues with Java 6</li>
<li>looks like we can not run JBossWS and Metro in the same box</li>
</ul><p>=&gt; We will migrate the 3 WS (Audit, Core, IndexingGateway) to Metro.</p></li>
<li><p>Visible Content Store (aka VCS, aka Visible SQL, aka SQL repository):</p>

<ul><li>We will support H2, PostgreSQL, MySQL, Oracle, MS-SQL</li>
<li>All supported DBs must be tested in hudson.</li>
</ul></li>
<li><p>Workflow:</p>

<ul><li>Workflows needs to be plugged back to the event and notification services.</li>
</ul></li>
<li><p>Annotations:
It must be possible to delete an annotation.</p></li>
<li><p>Packaging cleanup:</p>

<p>We need to check the packaging :</p>

<ul><li>remove depracated/compat packages</li>
<li>remove cache packages</li>
</ul></li>
</ul><h3>Task we should do before GA</h3> 
 <ul><li><p>UI cleaup on JSF WebApp:</p>

<p>Some look &amp; feel work will be done by GUnit team.</p>

<p>We will also do some cleanup :</p>

<ul><li>review order of tabs and namming</li>
<li>fix / re-enable tooltips</li>
<li>re-enable D&amp;D inside the browser (it is only 50% usable in M4)</li>
<li>enable popup context menu on full rows</li>
<li>refactor summary screen</li>
</ul></li>
<li><p>More FileManager plugins:</p>

<ul><li>IO-Plugin</li>
<li>Bundle file mac</li>
<li>create mail addon</li>
</ul></li>
<li><p>Picture book:</p>

<ul><li>test, fix and package well</li>
</ul></li>
<li><p>Finish WebWorkspace</p></li>
<li><p>REST API:</p>

<ul><li>Check and document the existing REST API</li>
</ul></li>
<li><p>Update and align sample project on 5.2 GA</p></li>
<li><p>Complete / update the Nuxeo Book and the Nuxeo tutorials</p></li>
<li><p>Extend audits views:</p>

<p>We can easily provide for each workspace a timeline of what happends.
As a default implementation there will be no security filtring on event logs.</p></li>
</ul><h3>Nice to have</h3> 
 <ul><li><p>Show case for NXThemes and WebWidgets:</p>

<ul><li>it would be great to have a default usage for WebWidgets</li>
</ul><p>=&gt; use it for the default DashBoard</p></li>
<li><p>Mail Drop box:</p>

<p>The idea is to reuse the sceduled email fetcher to feed an InBox associated to each workspace</p>

<p>=&gt; Have an email adresse for each workspace</p>

<p>=&gt; Add a mailto link to workspace summary</p></li>
<li><p>NxWSS and MOSS:</p>

<p></p><p>Add a WSS URL to each workspace summary to enable direct access via WSS clients.</p></li>
</ul><h3>Dead for GA (will be done in 5.2.1)</h3> 
 <ul><li><p>GWT integration:</p>

<p>Search Center will be the showcase for GWT integration.</p></li>
<li><p>Flex:</p>

<p>We should release the connector and the samples, and communicate how to use them via some blogs.</p></li>
<li><p>DynSearch:</p>

<ul><li>Replaced by Search Center</li>
</ul></li>
<li><p>Thumbs management and nice web folder contents view</p></li>
<li><p>Smart Folder / Saved search</p></li>
<li><p>UserWorkspace improvements</p></li>
</ul>

