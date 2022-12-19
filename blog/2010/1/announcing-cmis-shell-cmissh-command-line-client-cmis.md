---
title: "Announcing the CMIS Shell (cmissh) - command-line client for CMIS"
date: 2010-01-21
path: /blog/2010/1/announcing-cmis-shell-cmissh-command-line-client-cmis
summary: "We&#8217;ve been working recently on a CMIS command-line client, called &#8220;cmissh&#8221;, based on the Apache Chemistry client code."
tags: ['Nuxeo', 'Apache']
---

<p>We&#8217;ve been working recently on a CMIS command-line client, called
&#8220;cmissh&#8221;, based on the <a href="https://chemistry.apache.org/">Apache Chemistry</a>
client code.</p> 
<p>We have decided to donate the code to the Apache Chemistry project, as
there are no dependencies on Nuxeo code in it.</p> 
<p>cmissh can be used interactively (with a nice autocompletion console)
to explore and run CRUD operations on a CMIS server, or as a testing
tool. We&#8217;ve included, for instance, a test script in the distribution,
called &#8216;testscript&#8217;, that can be run against the Nuxeo demo server and
will fail on errors. I&#8217;ve also been able to use cmissh against the
Chemistry test server.</p> 
<p>If you are busy, you can download a binary distribution (built just
before the migration to Apache) from here:</p> 
<p><a href="http://www.nuxeo.org/static/cmis/cmissh-20100115.zip">http://www.nuxeo.org/static/cmis/cmissh-20100115.zip</a></p> 
<p>(or look for a later build here: <a href="http://www.nuxeo.org/static/cmis/">http://www.nuxeo.org/static/cmis/</a>).</p> 
<p>and test it against our public CMIS demo server (available here:
<a href="http://cmis.demo.nuxeo.org/">http://cmis.demo.nuxeo.org/</a>) using the &#8220;testscript&#8221; script included
in the distribution.</p> 
<p>Here is a sample session:</p> 

<pre><code class="prettyprint lang-text">SFs-macbook% cmissh
CMIS Shell by Nuxeo (www.nuxeo.com). Type 'help' for help.
|:&gt; help
Usage: help [command]

To get help of a specific command, type 'help name_of_command'.

List of available commands:

cat - Read the stream of the target document to the console
cd - Change working item
connect [open] - Open a new session
disconnect [close] - Close current session
dump [tree] - Dump a subtree
exit [bye|quit] - Exit
get [getstream] - Downloads the stream of the target document
help - Help
id - Identity of the specified entry
lcd - Change local working directory
lls [ll] - List local directory content
lpopd - Pop local directory stack
lpushd - Push local directory stack
lpwd - Print local working directory
ls - List entries in working directory
match - Fails if last command result doesn't match the pattern
mkdir - Create a folder given its name
mkfile [mkdoc] - Create a document of the given name
popd - Pop directory stack
propget - Print the value of the given property on the current context object
props - (Obsolete) Print the value of all the properties of the current context object
propset - Set the value of a property on the current context object
pushd - Push directory stack
put - Uploads the stream of the target document
pwd - Print working directory
rm [del] - Removes an object of the given name
setstream - Set the given file content as a stream on the current context object

|&gt; connect http://Administrator:Administrator@cmis.demo.nuxeo.org/nuxeo/site/cmis/repository

|&gt; ls
default

|&gt; cd default

|cmis.demo.nuxeo.org:default&gt; ls
default-domain

|cmis.demo.nuxeo.org:default&gt; cd default-domain

|cmis.demo.nuxeo.org:default-domain&gt; ls
workspaces
sections
templates

|cmis.demo.nuxeo.org:default-domain&gt; cd workspaces

|cmis.demo.nuxeo.org:workspaces&gt; ls
demo-workspace

|cmis.demo.nuxeo.org:workspaces&gt; cd demo-workspace

|cmis.demo.nuxeo.org:demo-workspace&gt; ls
pictures

|cmis.demo.nuxeo.org:demo-workspace&gt; cd pictures

|cmis.demo.nuxeo.org:pictures&gt; ls
pony-jpg
dog-jpg
cat-jpg

|cmis.demo.nuxeo.org:pictures&gt; put /Users/fermigier/Pictures/sf-square.jpg 

|cmis.demo.nuxeo.org:pictures&gt; ls
pony-jpg
dog-jpg
cat-jpg
sf-squared.jpg

|cmis.demo.nuxeo.org:pictures&gt; propget sf-square.jpg
cmis:baseTypeId = cmis:document
cmis:changeToken = [null]
cmis:checkinComment = [null]
cmis:contentStreamFileName = sf-square.jpg
cmis:contentStreamId = [null]
cmis:contentStreamLength = [null]
cmis:contentStreamMimeType = [null]
cmis:createdBy = Administrator
cmis:creationDate = GregorianCalendar(2010-01-21T16:14:05.000+01:00)
cmis:isLatestMajorVersion = false
cmis:isLatestVersion = true
cmis:isMajorVersion = false
cmis:isVersionSeriesCheckedOut = false
cmis:lastModificationDate = GregorianCalendar(2010-01-21T16:14:05.000+01:00)
cmis:lastModifiedBy = Administrator
cmis:name = sf-square.jpg
cmis:objectId = 01e009cc-11fd-4f84-a710-5af9cc12a97c
cmis:objectTypeId = File
cmis:versionLabel = [null]
cmis:versionSeriesCheckedOutBy = [null]
cmis:versionSeriesCheckedOutId = [null]
cmis:versionSeriesId = 01e009cc-11fd-4f84-a710-5af9cc12a97c
dc:contributors = [Ljava.lang.String;@555c07d8
dc:coverage = [null]
dc:description = [null]
dc:expired = [null]
dc:format = [null]
dc:issued = [null]
dc:language = [null]
dc:rights = [null]
dc:source = [null]
dc:subjects = [null]
dc:title = sf-square.jpg
dc:valid = [null]
filename = [null]
icon = /icons/file.gif
icon-expanded = [null]
major_version = 1
minor_version = 0
size = [null]
uid = [null]

|cmis.demo.nuxeo.org:pictures&gt; get sf-square.jpg
Object stream saved to local file: ./sf-square.jpg

|cmis.demo.nuxeo.org:pictures&gt; lls
sf-square.jpg

|cmis.demo.nuxeo.org:pictures&gt; id
Object 0a37ffea-fd65-4e78-b3bc-074168dd99f9 of type PictureBook

|cmis.demo.nuxeo.org:pictures&gt; quit
Bye
</code></pre> 
 

