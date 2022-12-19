---
title: "Tour de Nuxeo, Stage 3: The Nuxeo architecture"
date: 2011-07-07
path: /blog/2011/7/nuxeo-architecture
summary: "As we've seen in stage 1 of this Tour de Nuxeo, Nuxeo EP is a platform that implements all the major services that are expected nowadays to manage content at an enterprise scale."
tags: ['Nuxeo', 'Java', 'Eclipse', 'Open Source']
---

<img class="asset asset-image at-xid-6a010536291c30970b0154338b67f6970c" style="float: right; margin-left: 5px;" title="Photo source: http://www.flickr.com/photos/nakedcharlton/" src="/images/6a010536291c30970b0154338b67f6970c-800wi.png"> 
As we've seen in <a href="/blog/2011/07/why-manage-content/">stage 1</a> of this <a href="/blog/2011/07/introducing-2011-tour-nuxeo/">Tour de Nuxeo</a>, Nuxeo EP is a platform that implements all the major services that are expected nowadays to manage content at an enterprise scale.

In today's stage, we're going to dive deeper into the technology that powers the <a href="http://www.nuxeo.com/en/products/enterprise-platform">Nuxeo platform</a>, and show how its architecture was carefully chosen to answer the common needs of our customers and user community.

However, since Thierry Delprat, our fearless CTO, has already written extensively <a href="http://doc.nuxeo.com/display/NXDOC/Overview+and+Architecture">about the Nuxeo EP architecture</a>, let me focus here on the points that I think need to be highlighted and refer you to his writings and slides (see below) for more details.

<!-- more -->

<h2>Overview</h2>

<p>Nuxeo EP is an open source Java platform that provides building blocks to create sophisticated and robust ECM applications:</p>

<ul>

<li><p><em>Core ECM services</em>, such as: storage, lifecycle, security, audit, metadata, etc.</p></li>

<li><p><em>High level ECM services</em>, such as workflow, search, document transformation / rendering, collaboration, etc.</p></li>

<li><p><em>Interfaces</em>, especially web user interfaces.</p></li>

</ul>

<p>To make it possible, and easy, for developers and systems integrators to create their applications, we have chosen an architecture where the building blocks are extremely decoupled, and can be easily assembled to address the specific needs of each project.</p>

<h2>The Nuxeo runtime and component framework</h2>

<p>How does it work in practice? Each of the independent services that comprises the platform is implemented as a set of Java classes and supporting files (e.g. config and templates), bundled together in a JAR file, which is a physical manifestation of what is generally called a "component", and in our case, a "bundle".</p>

<p>When the application server (such as JBoss) or web container (such as Tomcat or Jetty) starts, it scans the JARs that it has access to and starts up the services that are contained in these JARs. Upon activation, these components can register information in several registries, in other words, "extend" existing components. They can also define ways they can be extended by other components, using what we call "extension points".</p>

<p>This way, for the application developer, an important part of his work is already covered just by choosing the services he needs from the generic "off the shelf" components that are provided by the platform, or available as add-ons on the <a href="https://connect.nuxeo.com/nuxeo/site/marketplace/product/all">Nuxeo Marketplace</a>. </p>

<p>If you are familiar with modern Java technologies, you might have recognized here the principles of the <a href="http://en.wikipedia.org/wiki/OSGi">OSGi</a> module system and service platform, and Eclipse's <a href="http://wiki.eclipse.org/FAQ_What_are_extensions_and_extension_points%3F">extension points</a>.</p>

<p>As an example, a new OCR service (whose role would be to extract text from images) could be added to a platform and then register itself into the transformation engines registry. This way, an application that manages documents scanned from paper copies can be configured <em>with no specific code</em> to leverage this OCR service to index the full text content of these documents, as extracted by the OCR service.</p>

<p>As another example, a JAR can be comprised of only configuration files for the various services that the Nuxeo platform provides, to enable customization (or overriding) of the default parameters of a standard application built on top of <a href="http://www.nuxeo.com/en/products/enterprise-platform">Nuxeo EP</a> (for instance, Nuxeo DM for <a href="http://www.nuxeo.com/en/products/document-management">Document Management</a>), with customer-specific document types, life cycles, metadata, indexes, actions, or look and feel. </p>

<p><em>More info</em>: <a href="http://community.nuxeo.com/static/book-draft/osgi2.html">OSGi Bundles, Components &amp; Extension Points</a> from the Nuxeo Tutorial.</p>

<h2>Pre-built applications</h2>

<p>The end-game of our development effort is to create great applications that answer the needs of real users. </p>

<p>Providing great building blocks and an assembly manual to create these applications is a way to achieve this goal, but it would be time consuming to build an application from scratch using a bottom-up approach.</p>

<p>This is the reason why we also provide ready-to-use content applications, such as <a href="http://www.nuxeo.com/en/products/document-management">Nuxeo DM</a> (for document management) or <a href="http://www.nuxeo.com/en/products/dam">Nuxeo DAM</a> (for digital asset management), which cover most, if not all, the needs for basic document management and digital asset management with no customization at all.</p>

<p>But wait, it gets even better! Since these applications are based on the modular Nuxeo EP platform, they are easy to customize using just configuration files (no code), or by using <a href="http://www.nuxeo.com/en/products/studio">Nuxeo Studio</a>, our configuration "IDE" that is available as a service to our customers, that spits out the config file from high-level descriptions that can be modeled graphically by business consultants.</p>

<h2>Why did we choose this model?</h2>

<p>This model is great but comes with a price (mostly for us, developers of the platform): developing software as decoupled components imposes the need to be extra careful in the way software is developed, in order to isolate the different functionalities in different components and ensure that all the components can work together in every combination that makes sense.</p>

<p>Most of our competitors (including the big vendors in the Gartner magic quadrant) don't make this effort, or have a technology that is too old and inflexible to move into this direction: they are happy to provide products as big monolithic pieces of software that look ok out of the box, but that are so impervious to change beyond the basic configuration that they offer that it can take 10 times longer (when it's possible at all) to adapt their software to real-life customer needs.</p>

<p>Integration costs skyrocket, while the architecture of the end result looks more like a plate of spaghetti than a cleanly layered cake. </p>

<p>Worse, when a new version comes out, all the customization has to be thrown away and restarted from scratch. </p>

<p>With our model, on the other hand, you can cleanly isolate your customization and extensions into independent components, and be sure that the cost for upgrading to a new version stays very reasonable.</p>

<h2>Open source Java</h2>

<p>Nuxeo is an open source Java project. As such, we try to leverage as much as possible existing open source Java technologies, as long as they have licenses compatible with our project's license, and to focus our efforts on the parts that are not already served by the open source Java ecosystem.</p>

<p>It takes a lot of discipline to do so: we need to carefully assess each of the external libraries we are using, for license compatibility, of course, but also for their quality and long-term viability.</p>

<p>As good citizens of the open source Java ecosystem, accustomed to working within our own open source project, we also work with the communities or companies that develop the open source libraries we are using, when we find they need fixes or enhancements.</p>

<h2>Further information</h2>

<h3>Presentations</h3>

<div style="width:425px" id="__ss_6079337"> <strong style="display:block;margin:12px 0 4px"><a href="https://www.slideshare.net/nuxeo/lessons-learned-building-nuxeo-ep-componentbase-open-source-ecm-platform" title="Lessons learned Building Nuxeo EP - Component-based, open source ECM platform" target="_blank">Lessons learned Building Nuxeo EP - Component-based, open source ECM platform</a></strong> <iframe src="https://www.slideshare.net/slideshow/embed_code/6079337" width="425" height="355" frameborder="0" marginwidth="0" marginheight="0" scrolling="no"></iframe> <div style="padding:5px 0 12px"> View more presentations from <a href="https://www.slideshare.net/nuxeo" target="_blank">Nuxeo - Open Source ECM</a> </div> </div>

<div style="width:425px" id="__ss_8531495"><strong style="display:block;margin:12px 0 4px"><a href="https://www.slideshare.net/nuxeo/nuxeo-ecm-platform-technical-overview" title="Nuxeo ECM Platform - Technical Overview">Nuxeo ECM Platform - Technical Overview</a></strong><object id="__sse8531495" width="425" height="355"><param name="movie" value="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=nuxeo-ep-technical-overview-110707052815-phpapp01&stripped_title=nuxeo-ecm-platform-technical-overview&userName=nuxeo" /><param name="allowFullScreen" value="true"/><param name="allowScriptAccess" value="always"/><embed name="__sse8531495" src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=nuxeo-ep-technical-overview-110707052815-phpapp01&stripped_title=nuxeo-ecm-platform-technical-overview&userName=nuxeo" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="355"></embed></object><div style="padding:5px 0 12px">View more presentations from <a href="https://www.slideshare.net/nuxeo">Nuxeo - Open Source ECM</a>.</div></div>

<h3>Article and white papers</h3>

<ul>

<li><a href="/blog/2010/12/software-engineering-paper-lessons-learned-developing-nuxeo-ep-open-source-component-based-ecm-platform/">Lessons learned developing the Nuxeo EP open source, component-based, ECM platform</a>, a research paper that was presented during the ICSSEA 2010 conference.</li>

<li><a href="/assets/pdf/ovum-audit-nuxeo-5.3.pdf">Technology Audit of Nuxeo EP</a> by Ovum Research (2010).</li>

<li><a href="http://doc.nuxeo.com/display/NXDOC/Overview+and+Architecture">Overview and Architecture</a> on the Nuxeo Documentation site.</li>

</ul>




