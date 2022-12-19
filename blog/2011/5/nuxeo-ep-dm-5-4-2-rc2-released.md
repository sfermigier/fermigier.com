---
title: "Nuxeo EP/DM 5.4.2 RC2 released"
date: 2011-05-26
path: /blog/2011/5/nuxeo-ep-dm-5-4-2-rc2-released
summary: "We've done yesterday a second release candidate for Nuxeo EP and DM."
tags: ['Nuxeo', 'Debian', 'Ubuntu']
---

We've done yesterday a second release candidate for Nuxeo EP and DM.

You can download the packages (zip, windows installer, generic installer) here:

<a href="http://community.nuxeo.com/static/rc/nuxeo-5.4.2-RC2/">http://community.nuxeo.com/static/rc/nuxeo-5.4.2-RC2/</a>

<!-- more -->

If you are running Debian or Ubuntu, you can also test it by adding:

<pre><code>deb http://apt.nuxeo.org/ natty releases datebased 
</code></pre>

and running <code>apt-get install nuxeo-dm</code>.

(You may substitute `natty` with `maverick`, `squeeze`, etc. i.e. the nickname of your current Debian or Ubuntu release but it won't change anything for now).

<a href="https://jira.nuxeo.com/secure/IssueNavigator.jspa?reset=true&amp;jqlQuery=project+%3D+NXP+AND+fixVersion+%3D+%225.4.2-RC2%22+AND+status+%3D+Resolved+ORDER+BY+priority+DESC&amp;mode=hide">77 issues have been resolved</a> between RC1 and RC2:

Now we are focussed on delivering Nuxeo 5.4.2 final next week. We have a bug day <em>today</em> where we will try to crush as many bugs and outstanding issues (<a href="https://jira.nuxeo.com/secure/IssueNavigator.jspa?reset=true&amp;jqlQuery=project+%3D+NXP+AND+resolution+%3D+Unresolved+AND+fixVersion+%3D+11088+ORDER+BY+priority+DESC">there are currently 159 of them</a>):

If you'd like to help, please test the RC2 <em>today</em> if possible and submit new bugs to the Jira.

If you are into IRC, you can join to the #nuxeo channel on irc.freenode.net to participate in this endeavor.

NOTE: this is a <em>release candidate</em>, so don't deploy it to your production servers!

