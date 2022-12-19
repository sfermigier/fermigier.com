---
title: "New beta Nuxeo DM package for Debian / Ubuntu"
date: 2010-12-13
path: /blog/2010/12/new-beta-nuxeo-dm-package-debian-ubuntu
summary: "We have made a new .deb package of Nuxeo DM for Debian and Ubuntu."
tags: ['Nuxeo', 'SQL', 'Linux', 'Debian', 'Ubuntu', 'Mandriva', 'Red Hat']
---

<p>We have made a new .deb package of Nuxeo DM for Debian and Ubuntu. <a style="float: right; margin-left: 5px;" href="http://blogs.nuxeo.com/.a/6a010536291c30970b0147e0a34458970b-popup" onclick="window.open( this.href, '_blank', 'width=640,height=480,scrollbars=no,resizable=no,toolbar=no,directories=no,location=no,menubar=no,status=no,left=0,top=0' ); return false"><img class="asset  asset-image at-xid-6a010536291c30970b0147e0a34458970b" alt="Deb" title="Deb" src="/images/6a010536291c30970b0147e0a34458970b-800wi.png" border="0" style="margin: 0px 0px 5px 5px;"></a>  </p>

<p>It's available for Debian 5.0 "Lenny" (and probably works for Squeeze too), and for Ubuntu 10.04 LTS "Lucid" and 10.10 "Maverick".</p>

<!-- more -->

<p>There are a few major changes over the previous (5.3.2) packages:</p>

<ul><li><p>There is now only one package, instead of two, and it is now called "nuxeo-dm", not "nuxeo-dm-tomcat" or "nuxeo-dm-jboss". We choose to base it on Tomcat, and we won't do a JBoss-based .deb package in the foreseeable future (if you want to install Nuxeo on top of JBoss 5, you can still download it as an EAR from <a href="http://www.nuxeo.com/en/downloads/download-dm-form">nuxeo.com</a>).</p></li>
<li><p>The package is now able to set up a PostgreSQL 8.4 database, which is the open source database we use and recommend for production settings with the correct tuning and customization needed to make Nuxeo DM work with it. Alternatively, you can connect your Nuxeo DM instance to an existing PostgreSQL / MySQL / Oracle / MS-SQL instance, but you're on your own to set it up properly, using the information in our <a href="https://doc.nuxeo.com/display/KB/Installing+and+configuring+the+backend+database+software">Installing and configuring the backend database software</a> knowledge base entry. </p></li>
<li><p>Once the server is started, you can use the Nuxeo Admin Center to fine-tune the configuration, or to download (with the appropriate subscription) extensions from the <a href="http://marketplace.nuxeo.com/">Nuxeo Marketplace</a>.</p></li>
</ul><p>Since this is still a recent development, we ask those with a Debian or Ubuntu machine suitable for deploying test software to try to install the package and report any issue you might find.</p><p>To do so:</p><ul><li><p>Either add "deb http://apt.nuxeo.org/ lenny releases" to your /etc/apt/sources.list file (substitute "lucid" or "maverick" for "lenny" if you're using Ubuntu), then run "apt-get update" and "apt-get install nuxeo-dm" (or use a graphical package manager).</p></li>
<li><p>Or download the package from <a href="http://apt.nuxeo.org/pool/releases/nuxeo-dm_5.4.0.1-02_all.deb">http://apt.nuxeo.org/pool/releases/nuxeo-dm_5.4.0.1-02_all.deb</a>, install it with "dpkg -i" (and install the needed dependencies if it complains).</p></li>
</ul><p>Note that on Debian Lenny, you might need to enable the backports if you run into errors such as "nuxeo-dm: Depends: postgresql (&gt;= 8.4) but 8.3.12-0lenny1 is to be installed".</p><p>To do so, add "deb http://backports.debian.org/debian-backports lenny-backports main contrib non-free" to your /etc/apt/sources.list</p><p>Note that at this point, these packages come with absolutely NO WARRANTY. We can't promise that it won't break your system, erase your data, etc.</p><p>ALWAYS BACKUP YOUR DATA before running an install or an upgrade, and perform the install first on a test server before deploying it in production.</p><p>One last thing: we have, according to the logs of the apt.nuxeo.org server, at least 2000 deployed instances of Nuxeo on Debian or Ubuntu. With this new, much improved version, we hope to gain many more users in the Debian and Ubuntu communities and hope you will help us with the final QA steps needed to deliver production-grade packages.</p><p>For Linux users of other distributions than Debian and Ubuntu: I'm sure you are also interested in having RPMs for Red Hat / Fedora / CentOS / Mandriva / OpenSuSE. If you're willing to help us with the task of creating this or these packages, drop me an email. I'm sure that parts of the scripts that have been written for Debian / Ubuntu can be reused.</p><p>The source code for the installer lives in <a href="http://hg.nuxeo.org/tools/nuxeo-packaging/">http://hg.nuxeo.org/tools/nuxeo-packaging/</a> BTW.</p>
 

