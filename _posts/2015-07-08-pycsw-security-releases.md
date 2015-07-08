---
layout: post
title: pycsw Security Releases
author: Tom Kralidis
author_url: https://twitter.com/tomkralidis
publish_date: 2015-07-08 06:36:33 -0400
---

The pycsw team announces the release of pycsw 1.10.2 and 1.8.4.

This is a security release to mitigate an information disclosure issue
with libxml2 (versions older than 2.9, c.f.
https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2013-0339) which
can reveal any file accessible on the host system by passing a
specially crafted XML file. Although this is not an issue with
pycsw itself, the update blocks this vector of attack when pycsw
is using a version of libxml2 older than 2.9.

You are strongly recommended to update if your pycsw has libxml2
support and is using an unpatched version of libxml2 older than 2.8.

pycsw is an OGC CSW server implementation written in Python.

pycsw fully implements the OpenGIS Catalogue Service Implementation Specification (Catalogue Service for the Web). Initial development started in 2010 (more formally announced in 2011). The project is certified OGC Compliant, and is an OGC Reference Implementation.

pycsw allows for the publishing and discovery of geospatial metadata. Existing repositories of geospatial metadata can also be exposed via OGC:CSW 2.0.2, providing a standards-based metadata and catalogue component of spatial data infrastructures.

pycsw is Open Source, released under an MIT license, and runs on all major platforms (Windows, Linux, Mac OS X).

Source and binary downloads
---------------------------

The source code is available at: http://pycsw.org/download

Testers and developers are welcome.

The pycsw developer team.

http://pycsw.org/
