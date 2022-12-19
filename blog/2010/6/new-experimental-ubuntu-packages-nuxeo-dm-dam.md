---
title: "New (experimental) Ubuntu packages for Nuxeo DM and DAM"
date: 2010-06-28
path: /blog/2010/6/new-experimental-ubuntu-packages-nuxeo-dm-dam
summary: "We've restarted work on Debian/Ubuntu packages."
tags: ['Nuxeo', 'Debian', 'Ubuntu']
---

<p>We've restarted work on Debian/Ubuntu packages.</p><p>To try the new packages on an Ubuntu Lucid (10.04) machine, you can add the following line at the end of your /etc/apt/sources.list :</p><pre><code>deb http://archive.canonical.com/ lucid partner
deb http://apt.nuxeo.org/ lucid snapshots
</code></pre><p>Then you can run:</p><pre><code>$ apt-get update
$ apt-get install nuxeo-dm-jboss
</code></pre><p><strong>OR</strong> (at this point you can't have both DM and DAM on the same server, at least not running at the same time, unless you change the ports of one of the servers):</p><pre><code>$ apt-get install nuxeo-dam-jboss
</code></pre><p>Currently only snapshots versions are provided, we need your help to test and make the system extra robust for when Nuxeo DM 5.3.2 will be released (in a few weeks).</p><p>We haven't tried (yet) the packages on other distros than Ubuntu Lucid, hopefully it will work without changes on a recent Debian and a few previous Ubuntu releases, but there might be some minor issues and we need your help to run the tests on other setups.</p><p>If you have bugs to fill, you can go to:</p><p><a href="https://jira.nuxeo.org/secure/IssueNavigator.jspa?reset=true&amp;mode=hide&amp;pid=10032&amp;sorter/order=DESC&amp;sorter/field=priority&amp;resolution=-1&amp;component=10622">https://jira.nuxeo.org/secure/IssueNavigator.jspa?reset=true&amp;mode=hide&amp;pid=10032&amp;sorter/order=DESC&amp;sorter/field=priority&amp;resolution=-1&amp;component=10622</a></p><p>If you want to help fine-tune the packages, you can fetch the build scripts using Mercurial this way:</p><pre><code>$ hg clone http://hg.nuxeo.org/tools/nuxeo-packaging/
</code></pre><p>Many thanks to Mathieu Guillaume and Julien Carsique for writing the new packaging scripts. There is some more work to do, but I'm sure the result will be great.</p><p>Please give us feedback, as this will keep us motivated to improve the packages!</p>
 

