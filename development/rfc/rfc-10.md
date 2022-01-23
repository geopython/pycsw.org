---
layout: default
title: RFC10 - OGC API - Records virtual collections support
description: This RFC describes the pycsw implementation of virtual collections as part of OGC API - Records support
keywords: rfc,rfc-10,OARec,ogcapi,records,virtual collections
active_page: rfc-10
---

# RFC 10: OGC API - Records virtual collections support

- date: 2021-12-24
- author: Tom Kralidis, Angelos Tzotsos
- contact: tomkralidis@gmail.com, tzotsos@gmail.com
- status: draft
- modified: 2022-01-23

## Overview

This RFC describes the pycsw implementation of virtual collections as part of OGC API - Records support ([OGC 20-004][1]).

The current pycsw implementation supports a single collection of metadata in both OGC:CSW and OARec modes.  OGC API - Records
differs from OGC:CSW in that multiple collections of metadata can be published and made available as disctinct endpoints.  Providing
multiple collections of metadata from a pycsw instance allows for finer grained discovery based on collections of metadata
(themes, projects, areas of interest, etc.).

Hierarchical metadata relationships are defined in both metadata and OGC standards:

- OGC API - Records
- IANA link relations
  - `collection`
  - `up` ([RFC8288][3])
- ISO 19115 `gmd:parentIdentifier`

pycsw implements parent/child relationships in the core metadata repository model, enabling clients
to discover metadata based on a specific collection.  This functionality is realized as follows:

- OGC:CSW: `GetRecords` and FES `parentIdentifier` filters
- OGC API - Records: `.../items` queries with `parentidentifier=` property query

It is also possible to use [repository filters][4] realize the above without requiring the user to specify
any query/filter syntax.  However, using repository filters would apply to the entire repository/deployment.

For OGC API - Records, there is an opportunity to expose the `parent` metadata as distinct collections,
to reduce the barrier for users querying on a specific collection, for multiple collections

## Proposed Solution

This functionality will be implemented in OGC API - Records only, given OGC:CSW does not support multiple
collections form a single endpoint.  Functionality will be implemented and triggered by the following
endpoints:

- `/collections`
  - detect all metadata records that have child, but no parent, metadata
  - emit each result as a collection.  Record identifier becomes the collection identifier (e.g. `virtual-collection-1`)
  - emit the `metadata:main` collection as normal
- `/collections/virtual-collection-1`
  - query for identifier, return collection metadata
- `/collections/virtual-collection-1/queryables`
  - return queryable properties as normal (straightforward given all metadata regardless of granularity have the same underlying model)
- `/collections/virtual-collection-1/items`
  - underlying query for records with `parentidentifier='virtual-collection-1`
  - return records accordingly
- `/collections/virtual-collection-1/items/{itemId}`
  - process as normal (query single identifier)

Note that `/collections/metadata:main/...` remains the "cross-collection" functionality.

## Implementation

### Activating the feature

This feature will enabled by default.

### Files affected

- codebase: `pycsw.ogc.api`
- tests: `oarec` unit tests will be added
- docs: documentation will be updated to describe the new feature

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

Documentation will be updated to describe the new feature (adding new page for virtual collections in OARec).

## Miscellaneous

### Issue Tracking ID

TBD

### Pull Request

https://github.com/geopython/pycsw/pull/726

### Voting History

TBD

### Status

Draft


[1]: https://docs.ogc.org/DRAFTS/20-004.html
[2]: https://ogcapi.ogc.org
[3]: https://www.rfc-editor.org/rfc/rfc8288.html
[4]: https://docs.pycsw.org/en/latest/repofilters.html
