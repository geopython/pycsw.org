---
layout: default
title: RFC4 - CSW 3.0 support
description: This RFC describes the pycsw implementation of the OGC Catalogue Services 3.0 Specification - HTTP Protocol Binding (OGC 12-176r5)
keywords: rfc,rfc-4,csw3,3.0
active_page: rfc-4
---

# RFC 4: CSW 3.0 support

- date: 2015-06-28
- author: Tom Kralidis, Angelos Tzotsos
- contact: tomkralidis@gmail.com, tzotsos@gmail.com
- status: draft
- modified: 2015-06-28

## Overview

This RFC describes the pycsw implementation of the OGC Catalogue Services 3.0 Specification - HTTP Protocol Binding ([OGC 12-176r5](https://portal.opengeospatial.org/files/?artifact_id=61521&version=1)).

CSW 3.0 provides major features and improvements over CSW 2.0.2 as part of the evolution of OGC Catalogue Services, including Open Search Geo and Time Extensions, OpenSearch 1.1, and the Atom Syndication Format.  Other enhancements include:

- features advertised as conformance classes
- simpler KVP API
- enhanced distributed searching functionality
- raw metadata response for GetRecordById
- proper use of HTTP status codes
- proper use of HTTP request/response headers
- `UnHarvest` operation
- use of temporal predicates for query and presentation.

Catalogue Services 3.0 - General Model ([OGC 12-168r5](https://portal.opengeospatial.org/files/?artifact_id=61522&version=1)) encompasses numerous changes (hence the major version change) to Catalogue Services overall.  This RFC (and pycsw) focuses exclusively on the HTTP Protocol Binding.

## Proposed Solution

Given the major changes in CSW 3.0, pycsw requires significant refactoring to support multiple verisons of numerous specifications (CSW, Filter Encoding, OWS Common, GML, etc.).  A high level design pattern includes:

- specifications implemented outside of the core server
- generic dispatcher (`pycsw.server.Csw`)
- version detection / negotiation determines code path

## Implementation

### Activating the feature

CSW 3.0 support will be enabled by default. The default version will be CSW 3.0 in accordance with the specification.  For backwards compatibility, there *may* implement a configuration directive which forces CSW 2.0.2 first.

### Files affected

- codebase: this RFC affects the entire codebase
- tests: a `csw3` test suite will be added
- docs: the documentation will be augmented to advertise support and describe changes and default version behaviour

### Backwards Compatibility Issues

This RFC represents breaking backwards compatibility in terms of default version.  For downstream applications, `pycsw.server.Csw` will continue to exist, and will accept a `version` argument to force CSW 2.0.2 behaviour if desired.  Unit tests will continue to succeed with a new `csw30` test suite added.  In addition, CITE tests will be 100% successful.

### Internal Interface changes

`pycsw.server.Csw` will continue to exist, and will accept a `version` argument to force CSW 2.0.2 behaviour if desired.

### Performance Implications

None expected.

### Related Bug Fixes

None

### Restrictions

None

### Documentation

Documentation will be augmented to advertise support and describe changes and default version behaviour.

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/149](https://github.com/geopython/pycsw/issues/149)

### Pull Request

None yet.  [csw3](https://github.com/geopython/pycsw/tree/csw3) branch in progress.

### Voting History

TBD

### Status

Proposed on 2015-06-28
