---
layout: post
title: pycsw 2.4.0 released 
author: Tom Kralidis
author_url: https://twitter.com/tomkralidis
publish_date: 2019-05-17 13:34:41 -0500
---

The pycsw team announces the release of pycsw 2.4.0. 

The 2.4.0 release adds WMS 1.3.0 and WPS process harvesting as well as plugin support enhancements.

Note that though pycsw works with Python 2 and 3, we have turned
off Python 2 testing given the [Python 2 end of life](https://pythonclock.org)
scheduled for 01 January 2020.  Users are strongly encouraged to update
their deployments to Python 3 as soon as possible.

Source and binary downloads:
----------------------------

The source code is available at: 

[https://pycsw.org/download](https://pycsw.org/download)

PyPI packages are available at:

[https://pypi.org/project/pycsw](https://pypi.org/project/pycsw)

Version 2.4.0 (2019-05-17):
---------------------------

[Bulleted list of enhancements / bug fixes]

- fix CAT 3.0 schema locations
- fix to handle plugin loading across various operating systems
- bump of requirements
- new project logos
- safeguard WKT exceptions against newer versions of Shapely
- updated Chinese translations
- enhancements and fixes to large metadata harvesting workflows
- safeguard async naming for Python 3.7
- OpenSearch description document updates
- startposition fixes to for GetRecords workflows

Testers and developers are welcome.

We would like to thank [OSGeo](https://osgeo.org) and the [2019 Minneapolis Code Sprint](https://wiki.osgeo.org/wiki/OSGeo_Community_Sprint_2019) organizers and sponsors for their support.
 
The pycsw developer team.
[https://pycsw.org/](https://pycsw.org/)
