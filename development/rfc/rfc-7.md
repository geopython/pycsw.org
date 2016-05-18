---
layout: default
title: RFC7 - HHypermap Repository Plugin
description: This RFC describes adding the Harvard Hypermap application as a repository plugin
keywords: rfc,rfc-7,HHypermap,repository,plugin
active_page: rfc-7
---

# RFC 7: HHypermap Repository Plugin

- date: 2016-05-12
- author: Tom Kralidis
- contact: tomkralidis@gmail.com
- status: draft
- modified: 2016-05-12

## Overview

This RFC describes adding the Harvard Hypermap application as a repository plugin.

[HHypermap (Harvard Hypermap) Supervisor](https://github.com/cga-harvard/HHypermap) is an application that manages OWS, Esri REST, and other types of map service harvesting, and maintains uptime statistics for services and layers. HHypermap Supervisor will publish to HHypermap Search (based on Lucene) which provides a fast search and visualization environment for spatio-temporal materials. 

HHypermap uses CSW as a cataloguing mechanism to ingest, query and present geospatial metadata.

This RFC supports binding to an existing HHypermap repository for metadata query.

## Proposed Solution

Follows the same development approach as implemented for GeoNode/Open Data Catalog repository plugins.

## Implementation

### Activating the feature

pycsw is enabled and configured by default in HHypermap, so there are no additional steps required once HHypermap is setup.  See the ``PYCSW`` `settings/default.py entries`_ for customizing pycsw within HHypermap.


### Files affected

- `docs/hhypermap.rst` (docs)
- `docs/index.rst`
- `docs/introduction.rst` (features)
- `pycsw/ogc/csw/csw2.py` (abstractions for CSW-T against a non-default repository)
- `pycsw/ogc/csw/csw3.py` (abstractions for CSW-T against a non-default repository)
- `pycsw/plugins/repository/hhypermap/__init__.py`
- `pycsw/plugins/repository/hhypermap/hhypermap.py` (repository plugin)
- `pycsw/server.py` (repository hooks)
- `setup.py`

### Backwards Compatibility Issues

None expected, new functionality. Unit tests will all succeed. CITE tests will be 100% successful.

Given this RFC articulates a repository plugin, tests are rooted in the downstream application itself because of the specific use case / workflow.  In addition, this keeps pycsw testing light so as not to setup downstream applications in a test env/run.

### Internal Interface changes

None

### Performance Implications

None

### Related Bug Fixes

None

### Restrictions

None

### Documentation

Documentation will be updated as required.  

## Miscellaneous

### Issue Tracking ID

TBD, branch at [https://github.com/tomkralidis/pycsw/tree/HHypermap](https://github.com/tomkralidis/pycsw/tree/HHypermap)

### Pull Request

TBD

### Voting History

TBD

### Status

TBD
