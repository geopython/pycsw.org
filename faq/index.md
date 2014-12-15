---
layout: default
title: FAQ
description: frequently asked questions
keywords: faq, questions, problems, solutions
active_page: faq
---

# FAQ <span class="glyphicon glyphicon-question-sign"> </span>

[Can I use pycsw within my WSGI application?](#can-i-use-pycsw-within-my-wsgi-application)

[How do I export my repository?](#how-do-i-export-my-repository)

[How do I add a custom metadata format?](#how-do-i-add-a-custom-metadata-format)

[How can I catalogue 'sets' of metadata?](#how-can-i-catalogue-sets-of-metadata)

[How can I handle transactions safely?](#how-can-i-handle-transactions-safely)

[How can I make CSW POST XML requests?](#how-can-i-make-csw-post-xml-requests)

[Does pycsw have a GUI/webapp/interface?](#does-pycsw-have-a-guiwebappinterface)

[I have 2147 metadata records.  How do I add them?](#i-have-2147-metadata-records--how-do-i-add-them)

[How do I add metadata from a WAF?](#how-do-i-add-metadata-from-a-waf)

[How do I harvest huge OGC services without getting HTTP timeout errors?](#how-do-i-harvest-huge-ogc-services-without-getting-http-timeouts)

[Why am I getting a 'Connection refused' error when connecting pycsw?](#why-am-i-getting-a-connection-refused-error-when-connecting-to-pycsw)

Can I use pycsw within my WSGI application?
-------------------------------------------

Yes.  pycsw can be deployed as both via traditional CGI or WSGI.  You can also integrate pycsw via [Django](https://www.djangoproject.com/) views, [Pylons](http://www.pylonsproject.org/) controllers or [Flask](http://flask.pocoo.org/) routes.

How do I export my repository?
-------------------------------

Use the `pycsw-admin.py` utility to dump the records as XML documents to a directory:

{% highlight bash %}
$ pycsw-admin.py -c export_records -f default.cfg -p /path/to/output_dir
{% endhighlight %}

How do I add a custom metadata format?
--------------------------------------

pycsw provides a plugin framework in which you can implement a custom profile (see [Profile Plugins](http://docs.pycsw.org/en/latest/profiles.html#profiles))

How can I catalogue 'sets' of metadata?
---------------------------------------

Create a 'parent' metadata record from which all relevant metadata records (imagery, features) derive from via the same `dc:source` element of Dublin Core or `apiso:parentIdentifier` element of ISO 19139:2007.  Then, do a `GetRecords` request, filtering on the identifier of the parent metadata record.  Sample request:

{% highlight xml %}
<?xml version="1.0" encoding="ISO-8859-1" standalone="no"?>
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" xmlns:ogc="http://www.opengis.net/ogc" service="CSW" version="2.0.2" resultType="results" startPosition="1" maxRecords="5" outputFormat="application/xml" outputSchema="http://www.opengis.net/cat/csw/2.0.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/cat/csw/2.0.2 http://schemas.opengis.net/csw/2.0.2/CSW-discovery.xsd" xmlns:gml="http://www.opengis.net/gml" xmlns:gmd="http://www.isotc211.org/2005/gmd" xmlns:apiso="http://www.opengis.net/cat/csw/apiso/1.0">
  <csw:Query typeNames="csw:Record">
    <csw:ElementSetName>brief</csw:ElementSetName>
    <csw:Constraint version="1.1.0">
      <ogc:Filter>
        <ogc:And>
          <ogc:PropertyIsEqualTo>
            <ogc:PropertyName>apiso:parentIdentifier</ogc:PropertyName>
            <ogc:PropertyName>$identifier</ogc:PropertyName>
          </ogc:PropertyIsEqualTo>
          <ogc:BBOX>
            <ogc:PropertyName>ows:BoundingBox</ogc:PropertyName>
            <gml:Envelope>
              <gml:lowerCorner>47 -5</gml:lowerCorner>
              <gml:upperCorner>55 20</gml:upperCorner>
            </gml:Envelope>
          </ogc:BBOX>
        </ogc:And>
      </ogc:Filter>
    </csw:Constraint>
  </csw:Query>
</csw:GetRecords>
{% endhighlight %}

The above query will search for all metadata records of the same `apiso:parentIdentifier` (identified by `$identifier`) within a given area of interest.  The equivalent query can be done against `dc:source` with the same design pattern.

How can I handle transactions safely?
-------------------------------------

Transactions are handled by an IP-based authentication list which can be set in pycsw's [configuration](http://docs.pycsw.org/en/latest/configuration.html#configuration) (in `manager.allowed_ips`).  Supported notations includes traditional IP address, wildcard, and CIDR.

How can I make CSW POST XML requests?
-------------------------------------

HTTP POST requests with XML are a bit different then the traditional HTTP POST appraoch (key=value).  An HTTP client opens a connection to the server and sends XML directly.  CSW implements HTTP POST in this manner with XML requests.

There are numerous ways to make this type of request, but here are a few:

Python
{% highlight python %}
import requests
requests.post('http://demo.pycsw.org/cite/csw', data=open('/path/to/request.xml').read()).text

from owslib.util import http_post
# see owslib.util.http_post in https://github.com/geopython/OWSLib/blob/master/owslib/util.py
response = http_post('http://demo.pycsw.org/cite/csw', request=open('/path/to/request.xml').read())
{% endhighlight %}

Command line tools:
{% highlight bash %}
# pycsw-admin.py utility
pycsw-admin.py -c post_xml -u http://demo.pycsw.org/cite/csw -x /path/to/request.xml

# curl
curl -X POST -d @/path/to/request.xml http://demo.pycsw.org/cite/csw

# lwp-request
cat /path/to/request.xml | POST http://demo.pycsw.org/cite/csw

# wget
wget http://demo.pycsw.org/cite/csw --post-file=/path/to/request.xml

{% endhighlight %}

Does pycsw have a GUI/webapp/interface?
---------------------------------------

No.  pycsw is a headless metadata catalog.  [Administration](http://docs.pycsw.org/en/latest/administration.html) is via command line.  For full metadata management, applications like [CKAN](http://ckan.org), [GeoNode](http://geonode.org)  and [Open Data Catalog](http://commons.codeforamerica.org/apps/open-data-catalog) are built with pycsw inside and provide functionality to manage metadata via a GUI.

I have 2147 metadata records.  How do I add them?
-------------------------------------------------

Add metadata using `pycsw-admin.py`:

{% highlight bash %}
# read a directory of metadata files
pycsw-admin.py -c load_records -f /path/to/default.cfg -p /path/to/records

# read a directory of metadata files, recursively
pycsw-admin.py -c load_records -f /path/to/default.cfg -p /path/to/records -r

{% endhighlight %}

See [Loading Records](http://docs.pycsw.org/en/latest/administration.html#loading-records) in the documentation.

How do I add metadata from a WAF?
---------------------------------

Use the `pycsw-admin.py` [utility](http://docs.pycsw.org/en/latest/administration.html) and CSW's `Harvest` operation against your own server:

{% highlight bash %}
pycsw-admin.py -c post_xml -u http://localhost/csw -x /path/to/harvest-waf.xml
{% endhighlight %}

`harvest-waf.xml`:
{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<Harvest xmlns="http://www.opengis.net/cat/csw/2.0.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/cat/csw/2.0.2 http://schemas.opengis.net/csw/2.0.2/CSW-publication.xsd" service="CSW" version="2.0.2">
  <Source>http://demo.pycsw.org/waf</Source>
  <ResourceType>urn:geoss:waf</ResourceType>
</Harvest>
{% endhighlight %}

How do I harvest huge OGC services without getting HTTP timeouts?
-----------------------------------------------------------------

The CSW `Harvest` operation supports asynchronous processing via the `ResponseHandler` parameter.  When specified, this parameter allows the request to continue while
returning the response to the client.  The client will then be notified of completion via URI value of the `ResponseHandler` parameter being sent.

pycsw supports both FTP and SMTP-based `ResponseHandler` processing:

FTP (result gets pushed to `ftp://host/result.xml`):
{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<Harvest xmlns="http://www.opengis.net/cat/csw/2.0.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/cat/csw/2.0.2 http://schemas.opengis.net/csw/2.0.2/CSW-publication.xsd" service="CSW" version="2.0.2">
  <Source>http://demo.pycsw.org/waf</Source>
  <ResourceType>urn:geoss:waf</ResourceType>
  <ResponseHandler>ftp://host/result.xml</ResponseHandler>
</Harvest>
{% endhighlight %}

SMTP (result gets emailed to `you@example.com`.  See [the docs](http://docs.pycsw.org/en/latest/configuration.html) for more information on configuring `server.smtp_host`):
{% highlight xml %}
<?xml version="1.0" encoding="UTF-8"?>
<Harvest xmlns="http://www.opengis.net/cat/csw/2.0.2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.opengis.net/cat/csw/2.0.2 http://schemas.opengis.net/csw/2.0.2/CSW-publication.xsd" service="CSW" version="2.0.2">
  <Source>http://demo.pycsw.org/waf</Source>
  <ResourceType>urn:geoss:waf</ResourceType>
  <ResponseHandler>mailto:you@example.com</ResponseHandler>
</Harvest>
{% endhighlight %}


Why am I getting a 'Connection refused' error when connecting to pycsw?
-----------------------------------------------------------------------

Most CSW client tools (e.g. [QGIS MetaSearch](https://hub.qgis.org/projects/MetaSearch), [OWSLib](http://geopython.github.io/OWSLib), etc.) derive the CSW URL from the `GetCapabilities` reponse XML, as opposed to using directly the URL you provide.  Ensure that the `server.url` configuration value is set to ensure the URL to be advertised in the CSW Capabilities XML.
