---
layout: default
title: Features
description: features
keywords: features, 
active_page: features
---

# Features <span class="glyphicon glyphicon-ok-circle"> </span>

- certified OGC [Compliant](http://www.opengeospatial.org/resource/products/details/?pid=1374) and OGC Reference Implementation
- harvesting support for WMS, WFS, WCS, WPS, WAF, CSW, SOS
- implements [INSPIRE Discovery Services 3.0](http://inspire.jrc.ec.europa.eu/documents/Network_Services/TechnicalGuidance_DiscoveryServices_v3.0.pdf)
- implements [ISO Metadata Application Profile 1.0.0](http://portal.opengeospatial.org/files/?artifact_id=21460)
- implements [FGDC CSDGM Application Profile for CSW 2.0](http://portal.opengeospatial.org/files/?artifact_id=16936)
- implements the Search/Retrieval via URL ([SRU](http://www.loc.gov/standards/sru/)) search protocol
- implements [OpenSearch](http://opensearch.org)
- supports ISO, Dublin Core, DIF, FGDC and Atom metadata models
- CGI or WSGI deployment
- simple configuration
- transactional capabilities (CSW-T)
- flexible repository configuration
- [GeoNode](http://geonode.org) connectivity
- [Open Data Catalog](https://github.com/azavea/Open-Data-Catalog/) connectivity
- [CKAN](http://ckan.org) connectivity
- federated catalogue distributed searching
- realtime XML Schema validation
- extensible plugin architecture

## Standards Support

- [OGC CSW](http://www.opengeospatial.org/standards/cat) 2.0.2
- [OGC Filter](http://www.opengeospatial.org/standards/filter) 1.1.0
- [OGC OWS Common](http://www.opengeospatial.org/standards/common) 1.0.0
- [OGC GML](http://www.opengeospatial.org/standards/gml) 3.1.1
- [OGC SFSQL](http://www.opengeospatial.org/standards/sfs) 1.2.1
- [Dublin Core](http://www.dublincore.org/) 1.1
- [SOAP](http://www.w3.org/TR/soap/) 1.2
- [ISO 19115](http://www.iso.org/iso/catalogue_detail.htm?csnumber=26020) 2003
- [ISO 19139](http://www.iso.org/iso/catalogue_detail.htm?csnumber=32557) 2007
- [ISO 19119](http://www.iso.org/iso/iso_catalogue/catalogue_tc/catalogue_detail.htm?csnumber=39890) 2005
- [NASA DIF](http://gcmd.gsfc.nasa.gov/add/difguide/index.html) 9.7
- [FGDC CSDGM](http://www.fgdc.gov/metadata/csdgm) 1998
- [SRU](http://www.loc.gov/standards/sru/) 1.1
- [A9 OpenSearch](http://www.opensearch.org/Home) 1.1

## Supported Operations

|Request          |Optionality|Supported|HTTP method binding(s)       |
|-----------------|-----------|---------|-----------------------------|
|GetCapabilities  |mandatory  |yes      |GET (KVP) / POST (XML) / SOAP|
|DescribeRecord   |mandatory  |yes      |GET (KVP) / POST (XML) / SOAP|
|GetRecords       |mandatory  |yes      |GET (KVP) / POST (XML) / SOAP|
|GetRecordById    |optional   |yes      |GET (KVP) / POST (XML) / SOAP|
|GetRepositoryItem|optional   |yes      |GET (KVP)|
|GetDomain        |optional   |yes      |GET (KVP) / POST (XML) / SOAP|
|Harvest          |optional   |yes      |GET (KVP) / POST (XML) / SOAP|
|Transaction      |optional   |yes      |POST (XML) / SOAP|

**Note: Asynchronous processing supported for GetRecords and Harvest requests (via ``csw:ResponseHandler``)**

## Supported Output Formats

- XML (default)
- JSON

## Supported Output Schemas

- Dublin Core
- ISO 19139
- FGDC CSDGM
- NASA DIF
- Atom

## Supported Sorting Functionality

- ogc:SortBy
- ascending or descending
- aspatial (queryable properties)
- spatial (geometric area)

## Supported Filters

### Full Text

- csw:AnyText

### Geometry Operands

- gml:Point
- gml:LineString
- gml:Polygon
- gml:Envelope

**Note: Coordinate transformations are supported**

### Spatial Operators

- BBOX
- Beyond
- Contains
- Crosses
- Disjoint
- DWithin
- Equals
- Intersects
- Overlaps
- Touches
- Within

### Logical Operators

- Between
- EqualTo
- LessThanEqualTo
- GreaterThan
- Like
- LessThan
- GreaterThanEqualTo
- NotEqualTo
- NullCheck

### Functions
- length
- lower
- ltrim
- rtrim
- trim
- upper

