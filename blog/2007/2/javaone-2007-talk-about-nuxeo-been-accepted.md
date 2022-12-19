---
title: "JavaOne 2007: our talk about Nuxeo has been accepted"
date: 2007-02-26
path: /blog/2007/2/javaone-2007-talk-about-nuxeo-been-accepted
summary: "I&#8217;m very happy (some would say \"ecstatic\" ;) ) to report that our talk proposal for the JavaOne conference has been accepted by the program committee."
tags: ['Nuxeo', 'Java', 'Eclipse']
---

<p>I&#8217;m very happy (some would say "ecstatic" ;) ) to report that our talk proposal for the <a href="http://java.sun.com/javaone/sf/">JavaOne conference</a> has been accepted by the program committee.</p><p>It will be called &#8220;Building an embeddable Enterprise Content Management core&#8221; and will be an in-depth overview of the <a href="http://www.nuxeo.org/sections/projects">Nuxeo 5</a> architecture, as proposed in our abstract:</p><blockquote>
  <p>This session describes the architecture and implementation of an embeddable, extensible Enterprise Content Management core for Java EE and simpler platforms.</p>
  
  <p>The presentation starts by describing the general architectural concepts that are used as building blocks:</p>
  
  <ul><li>a schema and document model, reusing XMLSchemas and making good use of XML namespaces, where documents types are build using a number facets,</li>
  <li>a repository model, using hierarchy and versioning, with JCR (JSR-170) being one of the possible backends,</li>
  <li>a query model, based on JPQL (JSR-220) and reusing the path-based concepts from JCR,</li>
  <li>a fine-grained security model, compatible with WebDAV concepts and designed to provide flexible security policies,</li>
  <li>an event model using synchronous and asynchronous events, allowing bridging through JMS (or other systems) to other event-enabled frameworks,</li>
  <li>a directory model, representing access to external data sources using the same concepts as for documents but taking advantage of the specificities of the data backends,</li>
  </ul><p>Suitable abstraction layers are put in place to provide the required level of flexibility. One of the main architectural tasks is to find commonalities in all the systems used (or whose use is planned in the future) to have a minimal number of concepts learned and used by the user of the framework. The result is a set of concepts that are fundamental to Enterprise Document Management and are usable through direct Java APIs, Java EE APIs or SOA. The presentation will show, for each of the main components, which challenges have been met and overcome when building a framework where all components are designed to be improved and replaced by different implementations in the future without sacrificing the backward compatibility with existing ones.</p>
  
  <p>The described implementation, <a href="http://www.nuxeo.org/sections/projects/core/">Nuxeo Core</a>, can be embedded in a basic Java framework based on OSGi (like Eclipse), or in one based on Java EE, according to the needs of the application using it. This means that the core has to function without relying on Java EE services but also has to take advantage of them when they are available (providing clustering, messaging, caching, remoting, and advanced deployment).</p>
  
  <p>The session includes a demo. Attendees should have intermediate knowledge of Java technology concepts and design patterns, and an understanding of the Content Management problem space.</p>
</blockquote> 

