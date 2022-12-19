---
title: "Packaging CPS"
date: 2006-04-12
path: /blog/2006/4/packaging-cps
summary: "Packaging CPS is important for ease of installation."
tags: ['Python', 'Zope', 'CPS', 'Linux', 'Debian', 'Ubuntu', 'Mandriva']
---

<p>
Packaging CPS is important for ease of installation. Unfortunately, it is also a great deal of effort, but an effort that can be distributed between the original software developers and third-party packagers.
</p><p>
The situation so far for CPS is that we have:
</p><ul><li>
the "<a href="http://www.cps-project.org/sections/downloads/.cps_download?url=/static/src/CPS-3.4.0-1.tar.gz">big tarball</a>", that installs itself on a fresh Zope 2.9 instance, made by the CPS dev. team.
</li>

<li>
the <a href="http://www.cps-project.org/sections/downloads/.cps_download?url=/static/windows/CPS-3.4.0-3.exe">Windows installer</a>, which installs Python + Zope + CPS + additional librairies + additional software (converters), made by <a href="/sections/blogs/ruslan_spivak">Ruslan</a>.
</li>

<li>
the <a href="http://packages.qa.debian.org/z/zope-cps.html">Debian/Ubuntu packages</a>, made by the <a href="http://qa.debian.org/developer.php?package=zope-cps">Debian Zope Packaging Team</a>, and specially <a href="http://www.kobold.it/">Fabio Tranchitella</a> 
</li>

<li>
Gerardo Puerta has made an <a href="http://bugs.gentoo.org/show_bug.cgi?id=127395">ebuild for Gentoo</a>.
</li>

</ul><p>
There are some areas were would benefit from some external help, though:
</p><ul><li>
We are still working on the Mac OS X installer, for which some <a href="http://svn.nuxeo.org/trac/pub/browser/CPS3/trunk/Installers/MacOSX/">preliminary code</a> has been written, but I have been told that the current approach is a dead-end and we need to start afresh with a new approach.
</li>

<li>
There are still not satisfactory RPM packages for common distributions like Fedora, Mandriva or OpenSuse.
</li>

</ul><p>
Packaging Zope and Zope applications under Linux is challenging, because you have to accomodate both people who just want "one click install" (using apt-get / yum / urpmi), but also provide the basis for rock-solid, possibly multi-instances, Zope server management (including easy instance creation / deletion, log rotation, service initialisations, etc.) without compromising security. The Debian Zope team seems to have done a lot of work to streamline this process for Zope.
</p><p>
Regarding CPS, any help in improving the existing packages, or in making new packages kinds available, would be really appreciated. If you feel in a packaging mood, join the <a href="">cps-devel</a> mailing list and let's start working together.
</p> 

