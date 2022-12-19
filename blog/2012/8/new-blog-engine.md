---
title: "New blog engine"
date: 2012-08-09
path: /blog/2012/8/new-blog-engine
summary: "This blog has a new blog engine, the fifth one since I've started blogging in 1997."
tags: ['Nuxeo', 'Python', 'CPS', 'Flask', 'Java']
---

This blog has a new blog engine, the fifth one since I've started blogging in 1997.

## 1997-1999: Homebrewed Python engine

I wrote my first blog engine in Python. IIRC, it was a client-server system using some kind of remote calling protocol (probably homebrewed too) that generated static HTML content. The editor for the posts was VI.

Needless to say, it was a bit painful to use, and this was one of the reasons I stopped posting in 1999.

## 2005-2009: CPSBlog

Someone at Nuxeo (I think it was [Ruslan Spivak](http://ruslanspivak.com/), if I'm wrong please correct me) wrote a blog engine on top of [CPS](/blog/categories/cps). We used it for quite a while, but let it rot after we switched to Java and Ruslan left the company.

## 2009-2011: Typepad

We decided to use Typepad as our corporate blog engine, for two main reasons:

- we didn't have to host it ourselves
- it was multiuser / multiblog.

In retrospect, this was an unfortunate decision, since Typepad was already loosing steam against Wordpress at the time, but Wordpress wasn't really multiblog so that was not an option.

## Jan-Aug 2012: Octopress

Back to square one, I migrated all my existing content to [Octopress](http://octopress.org/), a static blog and website generator itself based on [Jekyll](http://jekyllrb.com/).

It was relatively OK, but for some reason it didn't really invite me to start producing content again.

## Aug 2012: New homebrewed Python-based dynamic engine

I've spent the last couple of days writing a new blog engine based on [Flask](http://flask.pocoo.org/) and a [new project I'm currently working on](http://signup.yaka.biz/).

It should be in a state where it's already OK to post some content (using [Marsedit](http://www.red-sweater.com/marsedit/) as a client, using XML-RPC as the transport). 

I've also taken some time to adapt (and tweak) a cool Octopress theme by [Alessandro Melandri](http://melandri.net/2012/07/23/darkstripes-octopress-theme-released/).

More technical details about the new platform (including its source code) in a couple of weeks.
