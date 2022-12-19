---
title: "coverage.py, profile and hotshot support in Zope's testrunner"
date: 2005-08-21
path: /blog/2005/8/coverage-py-profile-hotshot-support-zope-testrunner
summary: "I have added support for coverage analysis using coverage.py from Gareth Rees and Ned Batchelder, as well as support for profiling using either the profile or hotshot modules from the Python standard library, to Zope 2's test runner test.py."
tags: ['Python', 'Zope']
---

I have added support for coverage analysis using <a href="http://www.nedbatchelder.com/code/modules/coverage.html">coverage.py</a>
from <a href="http://www.garethrees.org/2001/12/04/python-coverage/">Gareth
Rees</a> and <a href="http://www.nedbatchelder.com/">Ned Batchelder</a>, as well as support for profiling using either the <a href="http://docs.python.org/lib/profile.html">profile</a> or <a href="http://docs.python.org/lib/module-hotshot.html">hotshot</a> modules
from the <a href="http://effbot.org/zone/librarybook-index.htm">Python
standard library</a>, to Zope 2's test runner test.py.

See the <a href="/assets/code/test.py">attached file</a>.


