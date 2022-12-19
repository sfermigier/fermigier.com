---
title: "Philip Eby on Java+XML vs. Python and the sin of overengineering"
date: 2005-08-16
path: /blog/2005/8/philip-eby-java-xml-vs-python-sin-overengineering
summary: "Philip Eby has some comments on the Chandler development team recent decision to drop its XML-based \"parcel\" (parcels are components in Chandler) description format in favor of a pure-Python solution."
tags: ['Python', 'Java']
---

Philip Eby has <a href="http://dirtsimple.org/2005/08/chandler-begins-recovery-from-xml.html">some
comments</a> on the Chandler development team recent decision to drop its
XML-based "parcel" (parcels are components in Chandler) description format
in favor of a pure-Python solution.

There are two interesting lessons in his<a href="http://dirtsimple.org/2005/08/chandler-begins-recovery-from-xml.html">post:</a>

<blockquote>
Of course, the <span style="font-style: italic;">real</span> sin here was
not so much XML per se, as overengineering in advance of requirements. If
you're not developing the feature now, it's best not to make a bunch of
other design decisions based on what you <span style="font-style: italic;">think</span> the feature will need. A little
thing like choosing to put data in XML form can result in a wide variety of
additional costs like:<br><ul><li>Designing the XML format</li>

<li>Implementing a parser</li>

<li>Documenting the format</li>

<li>Developing a bunch of stuff in the format</li>

<li>Evolving and fixing the parser to handle more and more complex use
cases that weren't thought of previously</li>

<li>Productivity losses versus what it would've been with Python<br></li>

<li>Converting all the data once you decide it was a bad idea, or else
paying the ongoing marketing and education costs to get third-party
developers over the hump, or the cost of not getting those developers on
board</li>
</ul>
</blockquote>

And:

<blockquote>
I've certainly worked for organizations where the reverse is true, though,
including one that threw away <span style="font-style: italic;">tens of
millions of dollars</span> trying to replace a small, well-designed Python
application with an expensive piece of "enterprise" crapware. Ah, the
things I could've done with that budget! Well, probably I just would've
given everybody raises and maybe hired a few more people. Or maybe spun off
my group as a company that would sell the software to other companies.
Heck, we could've used it to buy <span style="font-style: italic;">free
sodas for life</span> for everybody working in the company and got more
value for the investors than what was actually done with the money!
</blockquote> 

