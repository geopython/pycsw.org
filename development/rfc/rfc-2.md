---
layout: default
title: RFC2 - OGC OpenSearch Geo/Time support
description: This RFC describes the pycsw implementation of the OGC OpenSearch standard (10-032r8).
keywords: rfc,rfc-2,opensearch,ogc,geo,time
active_page: rfc-2
---

# RFC 2: OGC OpenSearch Geo/Time support

- date: 2014-05-10
- author: Angelos Tzotsos
- contact: tzotsos@gmail.com
- status: draft
- modified: 2014-05-10

## Overview

This RFC describes the pycsw implementation of OGC OpenSearch Geo and Time extensions standard (10-032r8)

The OGC OpenSearch standard is intended to provide a very simple way to make spatial and temporal queries to a repository of geospatial content that contains geographic and temporal properties and to allow simple syndication of repositories.

The OpenSearch standard originated in a community effort built around Amazon's A9.com. It was intended to allow syndication of search results that could then be aggregated by one large index. The OpenSearch specification is made available under the Creative Commons Attribution-Sharealike 2.5 license. In 2007, the geo and time extensions were proposed through http://OpenSearch.org.

OpenSearch is a collection of simple formats for the sharing of search results. The OpenSearch description document format can be used to describe a search engine so that it can be used by search client applications. The OpenSearch description format allows the use of extensions that allow search engines to request a specific and contextual query parameter from search clients.

The basic concept of OpenSearch is to specify how to query a web resource, and additional metadata to support syndicating the results. Search clients can use OpenSearch description documents to learn about the public interface of a search engine. These description documents contain parameterized URL templates that indicate how the search client should make search requests. Search engines can use the OpenSearch response elements to add search metadata to results in a variety of content formats. For example, if a web site allows search by the URL:
http://www.example.com?q=question

OpenSearch provides a way to define where that search term goes. Essentially it would look like: http:// www.example.com?q={searchTerms}, where `{searchTerms}` would be replaced by any general string. Using OpenSearch, aggregators and applications have a way to simply define a search service and let a user just type in their terms, but then search N search engines. For example, the Firefox search bar is powered by OpenSearch and allows the user to add new OpenSearch compliant site.

The Geo and Time Extensions specify a series of parameters that can be used to geographically constrain search results. In this RFC, the core GeoSpatial and Temporal conformance classes are supported, where provision is made to filter results by:

* A bounding box (`{geo:box}`)
* A start and end of a temporal extent (`{time:start}` and `{time:end}`)

## Proposed Solution

Since version 1.2.0, pycsw supports the A9 OpenSearch 1.1 implementation in support of aggregated searching. 

Core OpenSearch support is enabled by default. HTTP requests must be specified with `mode=opensearch` in the base URL for OpenSearch requests.

In order to support Geo and Time extensions, pycsw must accept `{geo:box}`, `{time:start}` and `{time:end}` OpenSearch tokens in the description document and accept the appropriate parameters (`bbox=minx,miny,maxx,maxy`) and (`time=YYYY-MM-DD/YYYY-MM-DD`) in the request URL.

Since pycsw already supports those queryables through the CSW specification (`ows:BoundingBox`, `dc:date`), it is proposed that the OpenSearch query parameters should be parsed, internally transformed into an OGC Filter XML and passed on to FES module to form the appropriate SQL query for the database.  Internally this transforms the OpenSearch query into a GetRecords with Filter query, and processing continues normally.

The default output schema will then be Atom.

## Implementation

### Activating the feature

The OGC Geo and Time extensions will be enabled by default.

In order to get the OpenSearch description document the client will need to add `mode=opensearch` in the GetCapabilities URL:

  http://localhost/pycsw/csw.py?mode=opensearch&service=CSW&version=2.0.2&request=GetCapabilities

This will return the Description document which can then be autodiscovered.

A search request can be issued in the form of:

  http://localhost/pycsw/csw.py?mode=opensearch&service=CSW&version=2.0.2&request=GetRecords&q=SearchTerm&bbox=xmin,ymin,xmax,ymax&time=YYYY-MM-DD/YYYY-MM-DD

All `q`, `bbox` and `time` parameters are optional, but in order to get a valid OpenSearch responce, at least one of them should be present in the request URL.

### Files affected

The main changes are in `pycsw/opensearch.py`. There a `kvp2filterxml` function is added to transform the incoming OpenSearch request to an OGC Filter. Then this Filter XML is returned to the `pycsw/server.py` and is set as `kvp['constraint']`.

In `pycsw/server.py` a small block of code will be added to identify OpenSearch requests that have the `q`, `bbox` or `time` parameter and redirect them to `pycsw/opensearch.py` for proper parsing.

* opensearch.py
* server.py

### Backwards Compatibility Issues

None expected, new functionality. Unit tests will all succeed. CITE tests will be 100% successful.

### Internal Interface changes

None

### Performance implications

The parsing of the extra parameters (`q`, `time`, `bbox`) will happen in `pycsw/server.py` the same way the other parameters are discovered.

The `kvp2filterxml` function call is the only overhead added and is not causing any performance issues since it is a simple lxml construction of Filter XML.

### Related Bug Fixes

None

### Restrictions

The Core GeoSpatial and Temporal conformance classes are implemented in the RFC.

### Documentation

The `docs/opensearch.rst` and `docs/introduction.rst` documents are going to be updated.

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/245](https://github.com/geopython/pycsw/issues/245)

### Pull Request

[https://github.com/geopython/pycsw/pull/247](https://github.com/geopython/pycsw/pull/247)

### Voting History

None yet

### Status

Proposed on 2014-05-10.
