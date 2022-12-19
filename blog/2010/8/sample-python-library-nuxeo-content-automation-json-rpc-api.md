---
title: "A sample Python library for the Nuxeo Content Automation JSON-RPC API"
date: 2010-08-10
path: /blog/2010/8/sample-python-library-nuxeo-content-automation-json-rpc-api
summary: "I have created a sample Python library to illustrate the use of the Content Automation JSON-RPC API (described here: https://doc.nuxeo.com/display/NXDOC/REST+API)."
tags: ['Nuxeo', 'Python']
---

I have created a sample Python library to illustrate the use of the
Content Automation JSON-RPC API (described here:
<a href="https://doc.nuxeo.com/display/NXDOC/REST+API">https://doc.nuxeo.com/display/NXDOC/REST+API</a>).

The project, which is only illustrative and not officially supported by
Nuxeo, lives here:

<a href="http://bitbucket.org/sfermigier/nuxeo-automation-clients/">http://bitbucket.org/sfermigier/nuxeo-automation-clients/</a>

Here are the functions that have been implemented so far:

<pre><code>def create(self, ref, type, name=None, properties=None):
def update(self, ref, properties=None):
def setProperty(self, ref, xpath, value):
def delete(self, ref):
def getChildren(self, ref):
def getParent(self, ref):
def lock(self, ref):
def unlock(self, ref):
def move(self, ref, target, name=None):
def copy(self, ref, target, name=None):
def fetch(self, ref):
def query(self, query, language=None):
def getBlob(self, ref):
def attachBlob(self, ref, blob):
</code></pre>

And here is a sample interactive session to illustrate its use:

<pre><code>% python
Python 2.6.5 (r265:79063, Jul 18 2010, 11:41:34)
[GCC 4.2.1 (Apple Inc. build 5659)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; URL = "http://localhost:8080/nuxeo/site/automation/"
&gt;&gt;&gt; LOGIN = 'Administrator'
&gt;&gt;&gt; PASSWD = 'Administrator'
&gt;&gt;&gt; from nuxeoautomation import Client
&gt;&gt;&gt; from pprint import pprint
&gt;&gt;&gt;
&gt;&gt;&gt; c = Client(URL)
&gt;&gt;&gt; s = c.getSession(LOGIN, PASSWD)
&gt;&gt;&gt; pprint(s.getChildren("/"))
{u'entity-type': u'documents',
 u'entries': [{u'entity-type': u'document',
               u'lastModified': u'2010-08-10T13:19:26Z',
               u'path': u'/default-domain',
               u'state': u'project',
               u'title': u'Default domain',
               u'type': u'Domain',
               u'uid': u'20a4bea1-e71a-47b6-86fd-c59e0a63d84d'}]}
&gt;&gt;&gt; pprint(s.getChildren("/default-domain"))
{u'entity-type': u'documents',
 u'entries': [{u'entity-type': u'document',
               u'lastModified': u'2010-08-10T13:19:26Z',
               u'path': u'/default-domain/workspaces',
               u'state': u'project',
               u'title': u'Workspaces',
               u'type': u'WorkspaceRoot',
               u'uid': u'bc56455a-5345-440d-aa4e-31eed166e949'},
              {u'entity-type': u'document',
               u'lastModified': u'2010-08-10T13:19:26Z',
               u'path': u'/default-domain/sections',
               u'state': u'project',
               u'title': u'Sections',
               u'type': u'SectionRoot',
               u'uid': u'f8f7c052-cbb5-407b-8d19-3f2ec9e43efd'},
              {u'entity-type': u'document',
               u'lastModified': u'2010-08-10T13:19:26Z',
               u'path': u'/default-domain/templates',
               u'state': u'project',
               u'title': u'Templates',
               u'type': u'TemplateRoot',
               u'uid': u'cf1edd5a-2781-4b6b-aae7-310954da15f0'}]}
&gt;&gt;&gt; pprint(s.create("/", "File", "First Doc"))
{u'entity-type': u'document',
 u'lastModified': u'2010-08-10T13:20:25Z',
 u'path': u'/First Doc',
 u'state': u'project',
 u'title': u'First Doc',
 u'type': u'File',
 u'uid': u'dafbf9c7-b870-4f39-830c-892469890072'}
&gt;&gt;&gt; pprint(s.delete("dafbf9c7-b870-4f39-830c-892469890072"))
None
</code></pre>
 

