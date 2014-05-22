---
layout: post
title: pycsw 1.8.0 released
author: Angelos Tzotsos
author_url: http://users.ntua.gr/tzotsos/
publish_date: 2014-03-20 17:57:00 -0400
---

The pycsw team proudly announces the release of pycsw 1.8.0 codenamed "data.gov".
 
This release powers the [Geoplatform.gov](http://geoplatform.gov) and [Data.gov](http://data.gov) CSW endpoints [http://catalog.data.gov/csw](http://catalog.data.gov/csw) and [http://catalog.data.gov/csw-all](http://catalog.data.gov/csw-all).

[![Data.gov]({{site.baseurl}}/img/data-gov.png)](http://www.fgdc.gov/fgdc-news/geospatial-platform-catalog-api)
[![Geoplatform.gov](http://www.geoplatform.gov/sites/all/themes/geo/logo.png)](http://www.geoplatform.gov/announcements/announcing-availability-geoplatformgov-datagov-catalog)

Data.gov is the home of the U.S. Government's open data.
 
The 1.8.0 release brings significant features, enhancements and fixes to the codebase, including:
 
* support for PostgreSQL Full Text Search
* support for [repository filtering](http://docs.pycsw.org/en/1.8.0/repofilters.html)
* support for PostgreSQL schemas other than 'public'
* implement database connection pooling for WSGI
* more robust native model
* fix csw:AnyText population to be finer grained for OGC data services
* fix UTF-8 handling in configuration
 
The full list of enhancements and bug fixes is available at [https://github.com/geopython/pycsw/issues?milestone=9&state=closed](https://github.com/geopython/pycsw/issues?milestone=9&state=closed)
 
pycsw is an OGC CSW server implementation written in Python.
 
pycsw fully implements the OpenGIS Catalogue Service Implementation Specification (Catalogue Service for the Web). Initial development started in 2010 (more formally announced in 2011). The project is certified OGC Compliant, and is an OGC Reference Implementation.
 
pycsw allows for the publishing and discovery of geospatial metadata. Existing repositories of geospatial metadata can also be exposed via OGC:CSW 2.0.2, providing a standards-based metadata and catalogue component of spatial data infrastructures.
 
pycsw is Open Source, released under an MIT license, and runs on all major platforms (Windows, Linux, Mac OS X).
 
Source and binary downloads:
--------------------------------------------
The source code is available at:
[http://pycsw.org/download](http://pycsw.org/download)
 
Testers and developers are welcome.
 
The pycsw developer team.
[http://pycsw.org/](http://pycsw.org/)
