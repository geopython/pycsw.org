---
layout: default
title: RFC3 - OAI-PMH Support
description: This RFC describes the pycsw implementation of the The Open Archives Initiative Protocol for Metadata Harvesting
keywords: rfc,rfc-3,oai,oai-pmh,harvesting
active_page: rfc-3
---

# RFC 3: OAI-PMH Support

- date: 2014-07-18
- author: Tom Kralidis
- contact: tomkralidis@gmail.com
- status: draft
- modified: 2014-07-18

## Overview

This RFC describes the pycsw implementation of the `The Open Archives Initiative Protocol for Metadata Harvesting`_.

The Open Archives Initiative Protocol for Metadata Harvesting (referred to as the OAI-PMH in the remainder of this document) provides an application-independent interoperability framework based on metadata harvesting.

The OAI-PMH standard provides a straightforward API for listing metadata records.  Temporal query of metadata modificatoin dates is supported.  OAI-PMH does not support spatial, attribute or freetext searching.

## Proposed Solution

Similar to pycsw's `SRU`_ support, a simple wrapper will be implemented to:

- intercept OAI-PMH requests
- transform into the equivalent CSW request
- transform CSW response into OAI-PMH response

## Implementation

### Activating the feature

OAI-PMH support will be enabled by default. HTTP requests must be specified with `mode=oaipmh` in the base URL for OAI-PMH requests.

### Files affected

* `pycsw/oaipmh.py` (implementation)
* `pycsw/server.py` (hooks)
* `tests/suites/oaipmh` (testsuite)
* `docs/oaipmh.rst` (docs)

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

The `docs/oaipmh.rst` document will be created and added to the main documentation.

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/199](https://github.com/geopython/pycsw/issues/199)

### Pull Request

Current branch (pull request forthcoming)

[https://github.com/tomkralidis/pycsw/compare/issue-199](https://github.com/tomkralidis/pycsw/compare/issue-199)

### Voting History

None yet

### Status

Proposed on 2014-07-18.

.. _`The Open Archives Initiative Protocol for Metadata Harvesting`: http://www.openarchives.org/OAI/openarchivesprotocol.html
.. _`SRU`: http://docs.pycsw.org/en/latest/sru.html
