---
title: "Nuxeo + Ubuntu = open source ECM for the masses"
date: 2011-07-11
path: /blog/2011/7/nuxeo-ubuntu-open-source-ecm-masses
summary: "I'm happy that we announced today that: Our Nuxeo DM packages have been accepted in the Ubuntu \"Partner\" repository, so that it's even easier than before to install Nuxeo DM (and soon, other products from Nuxeo) on an Ubuntu Linux server."
tags: ['Nuxeo', 'Java', 'Linux', 'Debian', 'Ubuntu']
---

<img style="float: right; margin-left: 5px;" src="/images/6a010536291c30970b014e89c21699970d-150wi.png" />
I'm happy that we announced today that:</p>

<ul>

<li><p>Our Nuxeo DM packages have been accepted in the Ubuntu "Partner" repository, so that it's even easier than before to install Nuxeo DM (and soon, other products from Nuxeo) on an Ubuntu Linux server.</p></li>

<li><p>Nuxeo is now a part of Canonical's "Software Partner Programme" and listed as a "<a href="http://webapps.ubuntu.com/partners/software/">software partner</a>" on the Ubuntu site.</p></li>

<li><p>Canonical is now <a href="http://www.nuxeo.com/en/partners/partner-directory/canonical">listed as a partner</a> in our own <a href="http://www.nuxeo.com/en/partners/partner-directory/">partner directory</a>.</p></li>

<li><p>More than 1/2 of our developers are using Ubuntu Linux on their main development machine, and 100% of our production servers are using either Debian or Ubuntu Linux (OK, that part was not it the official announcement, but it's the truth ;).</p></li>

</ul>

<!-- more -->

<p>The <a href="http://www.nuxeo.com/en/about/news/nuxeo-releases-new-open-source-ecm-packages-for-ubuntu-server">official Nuxeo press release is here</a>, with a quote from a customer (<a href="http://blogs.nuxeo.com/marketing/2010/11/case-study-remote-delivery-of-content-by-jeppesen-a-boeing-subsidiary.html">Jeppesen</a>) who is also a happy Ubuntu user.</p>

<p>Details on <a href="https://doc.nuxeo.com/display/KB/Configuring+Nuxeo+Debian+or+Ubuntu+repositories">how to choose the best package for your Ubuntu or Debian distro are here</a>.</p>

<h2>FAQ</h2>



<h3>Why is Nuxeo DM only in <code>partner</code> and not in <code>main</code>, <code>universe</code> or <code>multiverse</code>?</h3>



<p>Debian and Ubuntu have strict rules on how packages have to be done if one wants them to be part of their main distributions. These rules are unfortunately <em>very</em> hard to follow when packaging Java applications, specially applications made using Maven, one of the standard tools for building enterprise Java applications. </p>



<p>For these reasons, we agreed with Canonical that the best and fastest way to move the partnership forward was to put the Nuxeo packages in the "partner" repository.</p>



<h3>Does this mean that Nuxeo DM is not open source?</h3>



<p>No, it doesn't. Nuxeo DM is open source, under the LGPL and LGPL-compatible licenses.</p>



<h3>I want to help improve the Nuxeo packages on Debian / Ubuntu</h3>



<p>You can help, indeed.</p>



<p>The source code for the packaging scripts lives here:

<a href="http://hg.nuxeo.org/tools/nuxeo-packaging/">http://hg.nuxeo.org/tools/nuxeo-packaging/</a> (in the <code>debian</code> directory).</p>



<p>You can also join the <code>nuxeo-isv</code> PPA on Launchpad: 

<a href="https://launchpad.net/~nuxeo-isv">https://launchpad.net/~nuxeo-isv</a></p>

