---
layout: post
title: pycsw 2.6.0 released 
author: Tom Kralidis
author_url: https://twitter.com/tomkralidis
publish_date: 2020-12-05 08:47:00 -0500
---

The pycsw team announces the release of pycsw 2.6.0. 

This release brings various enhancements to OpenSearch temporal support, cloud
enhancements, and 12 factor support.  This release also drops all Python 2
support given the [Python 2 end of life](https://pythonclock.org) which occured
on 01 January 2020.  Users are strongly encouraged to update their deployments
to Python 3 as soon as possible.

Source and binary downloads:
----------------------------

The source code is available at: 

[https://pycsw.org/download](https://pycsw.org/download)

PyPI packages are available at:

[https://pypi.org/project/pycsw](https://pypi.org/project/pycsw)

Version 2.6.0 (2020-12-05):
---------------------------

[Bulleted list of enhancements / bug fixes]

- fix GetRecords startposition empty parameter fixes
- update OpenSearch temporal extent query support
- add 12 factor support
- support environment variables in configuration
- add kubernetes and helm configurations
- fix quoting for PostgreSQL backends
- add logging switch to pycsw-admin.py CLI to stdout
- safeguard XML as bytes to unicode
- update core model xml column to Unicode on repository creation
- handle different formats for CRS code input
- add test for invalid gml:posList geometry
- drop all Python 2 support

Testers and developers are welcome.

The pycsw developer team.
[https://pycsw.org](https://pycsw.org)
