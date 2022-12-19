---
title: "First Release of Nuxeo WebEngine"
date: 2008-07-11
path: /blog/2008/7/first-release-nuxeo-webengine
summary: "WebEngine is a lightweight, versatile, content-centric, open source web framework to quickly build and deliver next generation content-oriented web applications."
tags: ['Nuxeo', 'Python', 'Java']
---

<p><em>WebEngine is a lightweight, versatile, content-centric, open source web framework to quickly build and deliver next generation content-oriented web applications.</em></p>

<p>WebEngine relies on the <a href="http://www.nuxeo.org/">Nuxeo content infrastructure</a> (OSGi runtime, component architecture, document repository, ECM services, etc.) to provide a component-based programing model and a web development model for building componentized content-centric applications (such as wikis, blogs, content-oriented websites, etc.).</p>

<p><a href="http://doc.nuxeo.com/display/NXDOC/WebEngine+(JAX-RS)"><img norder="0" src="http://www.nuxeo.org/static/images/webengine-screenshot-small.png"></a></p>

<p>WebEngine relies heavily on the REST paradigm: URLs are mapped to the hierarchical content repository, content is accessed using GETs, user actions are GETs and POSTs, etc. Hence it&#8217;s very easy and straightforward to write RESTful apps using WebEngine.</p>

<p>WebEngine is fully extensible and componentized, thanks to OSGi (all components are OSGi bundles) and Nuxeo Runtime&#8217;s extension points.</p>

<p>WebEngine can run either standalone (with startup time &lt;4s) using the Nuxeo Runtime launcher and the embedded <a href="http://www.mortbay.org/jetty-6/">Jetty 6</a>, or in a full-blown Java EE app server such as <a href="http://www.jboss.org/">JBoss</a>. WebEngine can also be connected to any Nuxeo EP instance (and Nuxeo Core repository) and be used to expose / publish its content to the web.</p>

<div style="width:425px;text-align:left" id="__ss_496662"><object style="margin:0px" width="425" height="355"><param name="movie" value="http://static.slideshare.net/swf/ssplayer2.swf?doc=nuxeowebenginetechnicalbriefing-1215039688940196-9"><param name="allowFullScreen" value="true"><param name="allowScriptAccess" value="always"><embed src="http://static.slideshare.net/swf/ssplayer2.swf?doc=nuxeowebenginetechnicalbriefing-1215039688940196-9" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="355"></embed></object><div style="font-size:11px;font-family:tahoma,arial;height:26px;padding-top:2px;"><a href="https://www.slideshare.net/?src=embed"><img src="http://static.slideshare.net/swf/logo_embd.png" style="border:0px none;margin-bottom:-5px" alt="SlideShare"></a> | <a href="https://www.slideshare.net/ebarroca/nuxeo-webengine-unveiled-496662?src=embed" title="View Nuxeo WebEngine unveiled on SlideShare">View</a> | <a href="https://www.slideshare.net/upload?src=embed">Upload your own</a></div></div>

## Features highlights

<ul><li><p>Scripting (Groovy, JavaScript, Ruby, Python&#8230;) or Java code for business logic</p></li>
<li><p>Advanced content model</p></li>
<li><p>Leverage Nuxeo Platform&#8217;s ECM services</p></li>
<li><p>Smart URLs management</p></li>
<li><p>Powerful templating (based on the <a href="http://freemarker.sourceforge.net/">FreeMarker</a> engine)</p></li>
<li><p>Wikitext renderer (using <a href="http://code.google.com/p/wikimodel">Wikimodel</a>)</p></li>
<li><p>Open source under the LGPL license</p></li>
</ul>

## Join the community!

<ul>
<li><p><a href="http://www.nuxeo.org/webengine/Download">Download</a> it and give it a try</p></li>
<li><p>Check out the <a href="https://www.slideshare.net/ebarroca/nuxeo-webengine-unveiled-496662">presentation on SlideShare</a></p></li>
<li><p>Read the <a href="http://doc.nuxeo.com/display/NXDOC/WebEngine+(JAX-RS)">reference documentation</a></p></li>
<li><p><a href="http://www.nuxeo.org/discussions/">Join the discussion</a> to get help and give feedback on the forums</p></li>
<li><p>Learn how WebEngine fits in the overall Nuxeo <a href="http://www.nuxeo.org/sections/about/roadmap/">roadmap</a></p></li>
<li><p>and&#8230; <a href="http://jira.nuxeo.org/browse/WEB">Contribute</a>]! :-)</p></li>
</ul>

