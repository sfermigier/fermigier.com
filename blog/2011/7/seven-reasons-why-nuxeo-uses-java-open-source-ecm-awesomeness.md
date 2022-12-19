---
title: "Seven reasons why Nuxeo uses Java for open source ECM awesomeness"
date: 2011-07-07
path: /blog/2011/7/seven-reasons-why-nuxeo-uses-java-open-source-ecm-awesomeness
summary: "So today's the 7th of July (7/7), and also, not so coincidentally, the day Oracle has chosen as the official day to launch Java 7."
tags: ['Nuxeo', 'Java', 'Eclipse', 'Apache', 'OW2', 'Linux']
---

<img style="float: right; margin-left: 5px;" title="Openjdk_logo200-630c77e7df4e6b4f" src="/images/6a010536291c30970b014e89accf05970d-800wi.png"/> 
So today's the 7th of July (7/7), and also, not so coincidentally, the day Oracle has chosen as the official day to launch <a href="http://www.theregister.co.uk/2011/07/07/oracle_java_seven_announcement/">Java 7</a>.

We weren't invited to the party, but let's take a break anyway from our <a href="/blog/2011/07/introducing-2011-tour-nuxeo/">Tour de Nuxeo series</a> to look at the 7 reasons why we're happy to be using Java (Java 6, actually, we're in no rush to adopt Java 7) for the <a href="http://www.nuxeo.com/en/products/ep">Nuxeo Enterprise Content Management Platform</a>.

<!-- more -->

<h2>7. Write once, run anywhere: it's not a myth</h2>

<p>We develop <a href="http://www.nuxeo.com/en/products/make-it-your-own">Nuxeo applications</a> with confidence that the application will run on Linux, Windows and Mac OS. </p>

<p>Of course, we run integration tests on all three platforms just to be sure.</p>

<h2>6. It's fast and robust</h2>

<p>It's not the 90's anymore. The JVM, with the integration of the <a href="http://en.wikipedia.org/wiki/HotSpot">HotSpot</a> technology ten years ago, is now on par (i.e. only 10% to 2x slower on most benchmarks) with the fastest languages, usually C and C++.</p>

<p>And, as a managed runtime, it also has many advantages over pure C or C++: no segmentation faults or buffer overflows, and a garbage collector that prevents most of the memory allocation mistakes that plague lower level programming languages.</p>

<h2>5. OSGi</h2>

<p>Java has <a href="http://community.nuxeo.com/static/book-draft/osgi2.html">OSGi</a>, a module system and service platform that allows developers to create software as independent components that can be wired together at runtime, allowing for cleaner (more decoupled) architectures and real software reuse.</p>

<h2>4. It has tools</h2>

<p>There are many open source tools (and a few proprietary ones) that help you be more efficient when working in Java.</p>

<p>Dependency management is much easier with Java (thanks to Maven, Ivy, Gradle and other similar tools) than with most other programming languages.</p>

<p>With Eclipse, for instance, one has a modern IDE that really helps developers (from the most junior to the most experienced) be efficient in what they do, that detects many errors even before the program is run, and that has support for refactoring to make sure your code base is always as cleanly architected as possible. </p>

<h2>3. It has, by far, the largest open source ecosystem</h2>

<p>Java has not one, but three major open source communities (all of which we are, in one way or another, members): the <a href="http://www.nuxeo.com/en/about/news/nuxeo-initiates-contribution-of-cmis-enabled-content-repository-to-eclipse-foundation">Apache Foundation</a>, the <a href="http://www.infoq.com/news/2011/02/nuxeo-core">Eclipse Foundation</a> and the <a href="http://blogs.nuxeo.com/fermigier/2011/04/nuxeo-now-incubated-ow2-project.html">OW2 Consortium</a>.</p>

<h2>2. It has a large set of quality open source libraries</h2>

<p>As a consequence of the previous point, there are thousands of mature open source libraries that one can use to write modern enterprise application software, out of which we can choose those we think are best-of-breed and useful to make our software.</p>

<h2>1. It also has the biggest business ecosystem</h2>

<p>We're not in this open source business just for the fun of it, but more importantly, to do serious projects for serious customers with serious partners.</p>

<p>And, surprise, all of them (customers and partners) are always happy to hear that we use Java, because they have developers who know Java and sysadmins who know how to manage Java applications.</p>

<p>So, no need to train developers on basic technologies, just (sometimes) on the subtleties of <a href="/blog/2011/07/why-manage-content/">Enterprise Content Management</a> and on the Nuxeo API, and they can start working on a project.</p>

<p>This is also the same for most other software companies we work with: most of them are using Java making it easy to integrate their applications -- for those who don't, we provide many web services APIs so that's not an issue either ;).</p>

