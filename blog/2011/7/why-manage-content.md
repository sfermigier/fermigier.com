---
title: "Tour de Nuxeo, Stage 1 - Why manage content?"
date: 2011-07-04
path: /blog/2011/7/why-manage-content
summary: "This is stage 1 of the 2011 \"Tour de Nuxeo\"."
tags: ['Nuxeo', 'Java', 'Unix']
---

<img style="float: right; margin-left: 5px;" src="/images/6a010536291c30970b01543376aa03970c-800wi.png" alt="Photo credit: hada55 on Flickr"/>
<em>This is stage 1 of the 2011 "<a href="/blog/2011/07/introducing-2011-tour-nuxeo/">Tour de Nuxeo</a>". Follow the link for the list of other stages.</em>

Enterprises and organizations face tremendous pressure to deal with an increasing amount of content, in terms of sheer volume (petabytes and beyond), number of content items (millions to billions of documents), and number of interaction points with either human personnel (inside or outside the organization) or automated systems.

In today's *Tour de Nuxeo stage*, we will have a look at the main challenges that face organizations that need to manage their content. But first, let's start by answering a simple question: What is content?

<!-- more -->

<h2>What is content?</h2>

*Content is information transmitted through a medium, which conveys a meaning to its receiver.*

Web pages are content. Word documents are content. Images, movies, business forms, complex XML business documents, tweets (140 characters long text messages) are other examples of content.

According to Forrester, content falls into three categories:

<ul>

<li><p><em>transactional</em>: content that supports business transactions between an organization and its customers or suppliers,</p></li>

<li><p><em>persuasive</em>: content that aims at communicating a message that supports the organization's mission - for instance, marketing material that helps the organization sell its products or services, </p></li>

<li><p>and <em>collaborative</em>: everything else, including all the office automation documents (e.g. MS Word / Excel / Powerpoint, but also emails) that are used and shared everyday by the organization's personnel to support their activities.</p></li>

</ul>

<h2>What is Enterprise Content Management (ECM)?</h2>

According to AIIM, ECM is: “the strategies, methods and tools used to capture, manage, store, preserve, and deliver content and documents related to organizational processes. ECM tools and strategies allow the management of an organization's unstructured information, wherever that information exists.”

This means that ECM is not just a technical concept ("tools"), it's also an organizational challenge ("strategies"). Only by articulating technical innovation with change management to foster adoption by their employees can organizations really make their ECM projects a success.

An ECM system typically needs to address the following concerns:

<ul>

<li><p><em>Storage</em>: the system need to store content in a way that makes it available for the entire duration it is needed, as a "live" (i.e. editable) document, as well as a "dead" document (a non-editable record that needs to be preserved for compliance purposes). As with any business application, content storage needs to be <em>transactional</em>  For documents that need to be preserved over a period of time significantly longer than the obsolescence half-life of hardware and software technologies, provision must be taken to ensure that content can still be extracted from the system after a long period of time in a format that will be still meaningful by that time.</p></li>

<li><p><em>Lifecycle</em>: as we've hinted above, content can change state during its life, for instance from "draft" to "live" to "archived" to "destroyed". One of the fundamental functions of the system is to manage the state transitions of the content, which can be triggered either by human interaction (e.g. validation by one or several editors) or automatically (e.g. automatic expiration on a given date).</p></li>

<li><p><em>Security</em>: the system must enforce access rules so that only people authorized to access a given piece of content are allowed to do so. In the most sophisticated systems, it's even possible to specify rules that give visibility to parts of the content.</p></li>

<li><p><em>Audit</em>: with great power comes great responsibility, and it's important in an ECM system to be able to track users action (lifecycle changes, writes, sometimes even reads) so that everyone is held accountable for their actions.</p></li>

<li><p><em>Metadata</em>: raw content, represented by a raw file, is mostly useless. Only with additional <em>metadata</em> is it possible to do anything meaningful with it. A common set of metadata includes: its title, its author(s), several dates attached to its lifecycle (creation, validation, expiration). Also of importance is all the information necessary to classify the document (see below): categories, tags, references to or from other documents and real life concepts (project code, account number, etc.). This metadata needs to be stored and managed by the system, with the same (or specific) rules as applied to the raw content itself.</p></li>

<li><p><em>Efficient collaboration</em>: the system must enable people to efficiently collaborate (i.e. work together) on content, with functionalities such as versioning, check-in / check-out, locking, workflow or commenting systems.</p></li>

<li><p><em>Delivery</em>: content is usually useless if it sits in a repository without producing business value. This is the reason why an organization wants to be able to deliver the content needed by its personnel, customers or partners at the time they really need it, and in a form that is most convenient to them. These days, this includes delivery on the web (on a public website for persuasive content, on a intranet or a portal for transactional or business documents), on mobile devices, but also, more traditionally, in a form suitable for printing. </p></li>

<li><p><em>Classification</em>: from the 19th century onwards, organizations have stored their business documents in file cabinets according to hierarchical, tree-like, taxonomies. This habit has lingered with the advent of electronic storage systems, with file plans with a rigid tree-like structure. Unconstrained from the physical worlds, it has appeared that it was possible to assign a document to not just one, but several categories. Eventually, fundamental new techniques have emerged less than 10 years ago, from Web 2.0 (tagging, folksonomies) and Web 3.0 (ontologies) applications, and are now gaining steam in enterprise applications. </p></li>

<li><p><em>Search</em>: full-text search is now the most popular way for people to find information on the public Web. It's not surprising that they expect the same approach to work also on their private document libraries. The problem may seem simpler, as a private content repository usually has several less orders of magnitude in terms of documents than the public web, but the structure of these repositories is also very different, and algorithms that are known to work well on the public Web (e.g. Google's PageRank) don't apply that well on a company's intranet.</p></li>

<li><p><em>Integration</em>: ECM it not just about managing documents anymore, it's about managing the content that supports all the business activities of an organization, <em>in relation</em> to the other systems that comprise its information system: the authentication and identity management system to compute access permissions on content, CRM and ERP applications that generate, and use, documents such as proposals, purchase orders or invoices, etc. Ease of integration with external systems is hence a critical capability of an ECM system, that only highly customizable and modular systems can provide.</p></li>

</ul>

<h2>What is a content application?</h2>

Content applications, also called CEVAs (Content Enabled Vertical Applications) or CCAs (Composite Content Applications), are business applications that primarily manipulate content.

Examples include:

<ul>

<li><p>An HR management application that focuses on keeping, and updating when needed, all the documents related to a person's employment in a given organization: resumés, diplomas, certificates, annual evaluation reports, disciplinary documents, termination documents, etc.</p></li>

<li><p>A news management system, where a news organization (press agency, press conglomerate) provides its writers and editors with the tools needed to efficiently produce and validate news-related content (text, pictures, videos, infographics..), to publish it in the appropriate form (HTML, PDF, etc.) on the appropriate channels, and to efficiently repurpose existing content when needed.</p></li>

</ul>

<h2>How is ECM different from traditional data management?</h2>

ECM shares some commonalities with two technologies that everyone in IT knows about: relational databases (RDBMS) and file systems (FS).

<ul>

<li><p>Filesystems provide a hierarchical view of documents, stored as <em>files</em> in a hierarchy of <em>folders</em> (also called <em>directories</em> in Unix and Unix-like systems). They provide access control, usually via user-level and group-level permissions, though usually not with the same granularity level as mandated by ECM applications. They also usually don't provide indexing and search (this can be done by external applications) or metadata management. Transactionality, lifecycle management, auditing, collaboration, etc. need to be added on top of the filesystem by the applications.</p></li>

<li><p>On the other hand, RDBMSes store information in tables, i.e. in a very flat manner. This is good for metadata management (you can add columns to your table to add pretty much any kind of metadata you need), and most modern RDMSes provide full search functionalities on textual content. Another nice thing is that they also have transactionality built-in. But, with their flat spaces, RDBMSes don't allow for hierarchical access control, and they also are more suited at managing structured data than semi-structured or unstructured data as is the most common way to look at content.</p></li>

</ul>

In the end, our view at Nuxeo is that both FSes and RDBMSes lack many functionalities that are crucial for ECM, but they provide several of the building blocks needed for it. This is the reason we chose to build our ECM platform using both these robust and proven technologies, and add the missing functionalities as part of the value added by our software.

<h2>Why use Nuxeo to manage your content?</h2>

There are many reasons why you would want to use Nuxeo EP as the basis of your next ECM project. We will come back to this subject later in much greater detail, but let me now list a few of them:

<ul>

<li>Nuxeo EP provides all the functionalities expected from a modern ECM platform.</li>

<li>Nuxeo EP is professionally developed and supported by a mature company.</li>

<li>Nuxeo EP is based on very standard enterprise Java technologies, so that it's easy to find personnel able to work with it.</li>

<li>Projects developed with Nuxeo EP are usually 2 to 10 times less expensive that projects developed with a proprietary ECM platform.</li>

</ul>

<h2>Additional resources</h2>

<ul>

<li><p><a href="http://doc.nuxeo.com/display/MAIN/Getting+started+with+Nuxeo+--+a+beginner%27s+page">Getting started with Nuxeo - a beginner's page</a> (Nuxeo Documentation).</p></li>

<li><p><a href="https://www.slideshare.net/norwiz/what-is-ecm-presentation">What is ECM?</a> (Atle Skjekkeland - AIIM).</p></li>

<li><p><a href="https://www.slideshare.net/jmancini77/8-reasons-you-need-a-strategy-for-managing-informationbefore-its-too-late">8 reasons you need a strategy for managing information...before it's too late</a> (John Mancini - AIIM).</p></li>

<li><p><a href="http://en.wikipedia.org/wiki/Enterprise_content_management">Enterprise Content Management</a> (Wikipedia).</p></li>

</ul>

<h2>Next stage</h2>

That's all for today. Join us again tomorrow for another Tour de Nuxeo stage: "What is Nuxeo?".


<h2>Comments? Questions?</h2>

<p>Did I forget something? Did I write something outrageously wrong? Use the comments below to make your voice heard.</p>

