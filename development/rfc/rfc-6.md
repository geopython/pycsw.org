---
layout: default
title: RFC6 - JSON Improvements
description: This RFC describes improvements to pycsw's outputFormat JSON support
keywords: rfc,rfc-6,json,outputformat
active_page: rfc-6
---

# RFC 6: JSON Improvements

- date: 2016-01-13
- author: Tom Kralidis
- contact: tomkralidis@gmail.com
- status: draft
- modified: 2016-01-13

## Overview

This RFC describes improvements to pycsw's JSON support to provide a more natural, efficient approach to the current capability.

The [current approach](https://github.com/geopython/pycsw/blob/1.10/pycsw/util.py#L314-L332) takes an `lxml.etree.Element` object and converts it to a Python `dict` which is then converted to JSON by Python's default json implementation.  Below is a snippet of JSON output of a `GetRecords` request with `outputFormat=application/json` specified:

        {
          "tag": "csw30:SummaryRecord",
          "children": [
            {
              "text": "urn:uuid:19887a8a-f6b0-4a63-ae56-7fba0e17801f",
              "tag": "dc:identifier"
            },
            {
              "text": "Lorem ipsum",
              "tag": "dc:title"
            },
            {
              "text": "http:\/\/purl.org\/dc\/dcmitype\/Image",
              "tag": "dc:type"
            },
            {
              "text": "Tourism--Greece",
              "tag": "dc:subject"
            },
            {
              "text": "image\/svg+xml",
              "tag": "dc:format"
            },
            {
              "text": "Quisque lacus diam, placerat mollis, pharetra in, commodo sed, augue. Duis iaculis arcu vel arcu.",
              "tag": "dct:abstract"
            }
          ]
        }

## Proposed Solution

The [xmltodict](https://github.com/martinblech/xmltodict) Python module provides parsing/serialization support in a manner which provides a closer mapping to / from an XML content model.  For the pycsw JSON codepath this results in:

* more compact JSON output (~30% reduction in payload size)
* closer representation / better transformation of native XML
* easier for downstream applications to process

Below is the same snippet using xmltodict:

      "csw30:SummaryRecord": [
        {
          "dc:identifier": "urn:uuid:19887a8a-f6b0-4a63-ae56-7fba0e17801f",
          "dc:title": "Lorem ipsum",
          "dc:type": "http:\/\/purl.org\/dc\/dcmitype\/Image",
          "dc:subject": "Tourism--Greece",
          "dc:format": "image\/svg+xml",
          "dct:abstract": "Quisque lacus diam, placerat mollis, pharetra in, commodo sed, augue. Duis iaculis arcu vel arcu."
        }

As a Python module xmltodict has no further dependencies.  Debian/Ubuntu package development is required.

## Implementation

### Activating the feature

JSON support is enabled by default. All JSON output support will be generated using xmltodict.

### Files affected

* `pycsw/core/util.py` (`exml2dict` update)
* `pycsw/server.py` (minor refactoring)
* `docs` (docs)
* `tests/default/post/*-json.xml` (possibly adding more tests)

### Backwards Compatibility Issues

The update in the JSON format represents a compatability break and will only be implemented in master branch as part of the 2.0 release.  This functionality will not be backported to other branches.

Affected unit tests will be updated and CITE tests will be 100% successful.

### Internal Interface changes

None

### Performance Implications

None

### Related Bug Fixes

None

### Restrictions

Debian/Ubuntu package development is required.  Discussion and consensus is also required on dealing with downstream applications like GeoNode and CKAN.

### Documentation

Documentation will be updated as required.  

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/395](https://github.com/geopython/pycsw/issues/395)

### Pull Request

[https://github.com/geopython/pycsw/issues/396](https://github.com/geopython/pycsw/issues/396)

### Voting History

TBD

### Status

TBD
