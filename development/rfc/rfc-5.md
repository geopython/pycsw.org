---
layout: default
title: RFC5 - GM03 Support
description: This RFC describes the pycsw implementation of the GM03 Swiss Metadata Model
keywords: rfc,rfc-5,gm03,outputschema
active_page: rfc-5
---

# RFC 5: GM03 Support

- date: 2015-11-11
- author: Tom Kralidis
- contact: tomkralidis@gmail.com
- status: draft
- modified: 2015-11-11

## Overview

This RFC describes the pycsw implementation of the [GM03 Core Swiss Metadata Model](http://www.geocat.ch/internet/geocat/en/home/documentation/gm03.html).

The metadata model GM03 is a Swiss standard SNV 612050. GM03 is a profile of the international metadata standard ISO 19115.  The metadata model GM03 is a Swiss standard SNV 612050.

## Proposed Solution

Similar to pycsw's FGDC, Atom, and DIF support, GM03 Core will be implemented as a core outputschema plugin which:

* ingests GM03 via `Harvest`, `Transaction`, the pycsw API (`pycsw.core.admin`) and `pycsw-admin.py`
* exports GM03 supports (full document for native GM03 format)
* transforms non-native GM03 metadata into GM03 Core

## Implementation

### Activating the feature

GM03 will be enabled by default. `GetRecords` and `GetRecordById` requests must be specified with `outputschema=http://www.interlis.ch/INTERLIS2.3` for proper export.

### Files affected

* `pycsw/core/config.py` (hooks)
* `pycsw/core/metadata.py` (ingest)
* `pycsw/oaipmh.py`
* `pycsw/plugins/outputschemas/__init__.py`
* `pycsw/plugins/outputschemas/gm03.py` (export [new])
* `pycsw/plugins/profiles/profile.py`
* `docs` (docs)
* `tests/suites/gm03` (testsuite)

### Backwards Compatibility Issues

None expected, new functionality. Unit tests will all succeed. CITE tests will be 100% successful.

### Internal Interface changes

None

### Performance Implications

None

### Related Bug Fixes

None

### Restrictions

None

### Documentation

GM03 information document will be added to the main documentation as required.

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/384](https://github.com/geopython/pycsw/issues/384)

### Pull Request

TBD

### Voting History

TBD

### Status

TBD
