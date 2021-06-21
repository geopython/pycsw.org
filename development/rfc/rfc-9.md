---
layout: default
title: RFC9 - OGC API - Records support
description: This RFC describes the pycsw implementation of the OGC API - Records - Part 1: Core Specification (OGC 20-004)
keywords: rfc,rfc-9,OARec,ogcapi,records
active_page: rfc-9
---

# RFC 9: OGC API - Records support

- date: 2021-06-14
- author: Tom Kralidis, Angelos Tzotsos
- contact: tomkralidis@gmail.com, tzotsos@gmail.com
- status: draft
- modified: 2021-06-21

## Overview

This RFC describes the pycsw implementation of the OGC API - Records - Part 1: Core Specification ([OGC 20-004][1]).

OGC API - Records (i.e. OARec) is part of the overall [OGC API][2] to modernize
API specifications in support of lowering the barrier to implementation,
leveraging more native web patterns, as well as modern web technologies.  The
OGC API effort represents a clean break from first generation OGC web services.

Notable enhancements include:

- native use of HTTP methods (GET, POST, etc.)
- removal of HTTP as a tunnel
- JSON as a key representation/format
- HTML as a key representation/format
- use of GeoJSON as a baseline for data/metadata formats
- developer friendly
- OpenAPI as the API description language
- very simply query API patterns
- core and extension concepts for functionality, allowing for iterative development and implementation

## Proposed Solution

Given the pycsw architecture, the approach will be to leverage the existing
pycsw configuration and backend metadata repository management via the pycsw
native Python API.  OARec will be implemented on top of

Given the major changes in OARec, the following technical strategies are
put forth:

- use of [Flask][3] for front end routing and WSGI capability
  via `pycsw.wsgi_flask` to optionally serve all supported pycsw APIs
  (OARec, CSW 2/3, OAI-PMH, OpenSearch, SRU)
- use of [pygeofilter][4] as the abstract CQL/filter parser
- use of [Jinja2][5] for HTML templating
- introduction of `pycsw.ogc.api.records` for core OARec support
- introduction of `pycsw.ogc.api.oapi` for OpenAPI support
- introduction of `requirements-oarec.txt` for OARec specific requirements

## Implementation

### Activating the feature

OARec support is enabled by default and is exposed by deploying
`pycsw.wsgi_flask` via WSGI.  The default Docker implementation will
be updated to use `pycsw.wsgi_flask` thereby supporting all pycsw APIs.

The `pycsw.wsgi_flask` WSGI deployment provides updated routes as follows:

- `/`: OARec
- `/csw`: CSW 2/3
- `/oaipmh`: OAI-PMH
- `/opensearch`: OpenSearch
- `/sru`: SRU

Existing functionality will stil exist via the `pycsw.wsgi` WSGI deployment.

### Files affected

- codebase: introduction of `pycsw.ogc.api`
- tests: `oarec` unit tests will be added
- docs: documentation will be updated to describe OARec support

### Backwards Compatibility Issues

None.

### Internal Interface changes

None

### Performance Implications

None expected.

### Related Bug Fixes

None

### Restrictions

None

### Documentation

Documentation will be updated to describe OARec support and features.  A
migration guide will also be provided for users wishing to upgrade to OARec
and the Flask deployment strategy.

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/670](https://github.com/geopython/pycsw/issues/670)

### Pull Request

[https://github.com/geopython/pycsw/pull/686](https://github.com/geopython/pycsw/pull/686)

### Voting History

+1 from @capooti, @kalxas, @tomkralidis

### Status

Adopted.


[1]: https://docs.ogc.org/DRAFTS/20-004.html
[2]: https://ogcapi.ogc.org
[3]: https://flask.palletsprojects.com
[4]: https://github.com/geopython/pygeofilter
[5]: https://jinja.palletsprojects.com
