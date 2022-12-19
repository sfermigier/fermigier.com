---
title: "Debian and Ubuntu packages available for Nuxeo DM 5.3.2 (stable)"
date: 2010-07-20
path: /blog/2010/7/debian-ubuntu-packages-available-nuxeo-dm-5-3-2-stable
summary: "With Nuxeo DM 5.3.2 released just a few minutes ago, I'm happy to report that we now have stable packages for Debian Lenny (4.0) and Ubuntu Lucid Lynx (10.4 LTS)."
tags: ['Nuxeo', 'Debian', 'Ubuntu']
---

<p>With Nuxeo DM 5.3.2 released just <a href="http://blogs.nuxeo.com/dev/2010/07/nuxeo-dm-532-is-available.html">a few minutes ago</a>, I'm happy to report that we now have stable packages for Debian Lenny (4.0) and Ubuntu Lucid Lynx (10.4 LTS).</p>

<p>To enjoy these packages using APT or Aptitude, just add the following lines to your /etc/apt/sources.list:</p>

<pre><code>deb http://archive.canonical.com/ lucid partner
deb http://apt.nuxeo.org/ lucid releases
</code></pre>

<p>Then run:</p>

<pre><code>apt-get install nuxeo-dm-tomcat # (or nuxeo-dm-jboss)
</code></pre>

<p>See <a href="http://blogs.nuxeo.com/fermigier/2010/06/new-experimental-ubuntu-packages-for-nuxeo-dm-and-dam.html">my previous blog post on the same subject</a> to learn how to report issues, ask for feature or contribute to the packaging code.</p>

<p><strong>Updated 2010/12/13</strong>: with the 5.4.0 release of Nuxeo DM, the package name for Nuxeo DM to use in your <code>apt-get install</code> command is now just: <code>nuxeo-dm</code>.</p>
 

