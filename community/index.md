---
layout: default
title: Community
description: community participation
keywords: community, testing, mailing list, irc, chat, contributing, pull request
active_page: community
---

# Community <span class="glyphicon glyphicon-user"> </span>

pycsw is [used](https://github.com/geopython/pycsw/wiki/Live-Deployments) in government, academia and industry, both as a standalone and embedded component in geospatial data portal applications.

<script src="https://embed.github.com/view/geojson/geopython/pycsw.org/gh-pages/live-deployments.geojson"> </script>

<div class="pycsw-powered">
<a class="reference external image-reference" href="http://data.gov"><img alt="Data.gov" src="{{site.baseurl}}/img/data-gov.png"/></a>
<a class="reference external image-reference" href="http://ckan.org"><img alt="CKAN" src="{{site.baseurl}}/img/ckan.png"/></a>
<a class="reference external image-reference" href="http://cida.usgs.org"><img alt="USGS Center for Integrated Data Analytics" src="{{site.baseurl}}/img/usgs-cida.jpg"/></a>
<a class="reference external image-reference" href="http://geonode.org"><img alt="GeoNode" src="{{site.baseurl}}/img/geonode.jpg"/></a>
<a class="reference external image-reference" href="http://sopac.org"><img alt="Secretariat of the Pacific Community" src="{{site.baseurl}}/img/sopac.jpg"/></a>
<a class="reference external image-reference" href="http://insideidaho.org"><img alt="INSIDE Idaho" src="{{site.baseurl}}/img/inside-idaho.jpg"/></a>
<a class="reference external image-reference" href="http://www.opengeospatial.org/projects/initiatives/chisp"><img alt="OGC Climate-Hydrologic Information Sharing Pilot" src="{{site.baseurl}}/img/ogc-chisp.jpg"/></a>
<a class="reference external image-reference" href="http://commons.codeforamerica.org/apps/open-data-catalog"><img alt="Open Data Catalog, Code for America Brigade" src="{{site.baseurl}}/img/open-data-catalog.png"/></a>
<a class="reference external image-reference" href="http://crc806db.uni-koeln.de"><img alt="University of Cologne, Department of Geography, Collaborative Research Centre 806" src="{{site.baseurl}}/img/uni-koeln.png"/></a>
<a class="reference external image-reference" href="http://data.noaa.gov"><img alt="National Oceanic and Atmospheric Administration" src="{{site.baseurl}}/img/noaa.png"/></a>
<a class="reference external image-reference" href="http://geothermaldata.org"><img alt="National Geothermal Data System" src="{{site.baseurl}}/img/ngds.png"/></a>
</div>

There are numerous ways to interact with the pycsw community.

## Google+

pycsw exists as a [Google+ community](https://plus.google.com/communities/104084873011085696113). Join us there for pycsw news discussion, and more.

## FAQ

The [_FAQ_]({{site.baseurl}}/faq.html) provides answers to commonly asked questions about pycsw.

## Mailing List

The pycsw-devel mailing list enables users and developers to exchange ideas, discuss improvements / issues, and ask questions. To subscribe, visit <http://lists.osgeo.org/mailman/listinfo/pycsw-devel>.

Mailing list archives are available at <http://lists.osgeo.org/pipermail/pycsw-devel>.  The mailing list is also available/searchable via the OSGeo [Nabble](http://osgeo-org.1560.x6.nabble.com/pycsw-devel-f5055821.html) forum.

## IRC

Internet Relay Chat (IRC) allows for real-time communication and group discussion.  The [pycsw IRC channel](irc://irc.freenode.net/pycsw) can be found at:

- **Server**: `irc.freenode.net`
- **Channel**: `#pycsw` (or `#geopython`)
- **Port**: `6667`

pycsw developers can be found in the IRC channel.  Below are some suggested IRC clients:

- [Chatzilla](http://chatzilla.hacksrus.com/) (Firefox)
- [Colloquy](http://colloquy.info/) (Mac OS)
- [irssi](http://irssi.org/) (Terminal-based)

IRC logs can be found at [http://irclogs.geoapt.com/pycsw/](http://irclogs.geoapt.com/pycsw/)

## Service Providers

pycsw service providers (core development, support, training) can be found on the [OSGeo Service Provider Directory](http://www.osgeo.org/search_profile?SET=1&MUL_TECH[]=00107)

## GitHub (Wiki, Issues, Code)

The pycsw [wiki](https://github.com/geopython/pycsw/wiki) provides an area for supporting information that frequently changes and / or is outside the scope of the formal documentation.

pycsw's [issue tracker](https://github.com/geopython/pycsw/issues) is the place to report bugs or request enhancements.  To submit a [bug](https://github.com/geopython/pycsw/issues/) be sure to specify the version you are using, the appropriate component, a description of how to reproduce the bug, as well as what version of Python and platform.  For convenience, you can run `pycsw-admin.py -c get_sysprof` and copy/paste the output into your bug report.

GitHub provides the ability for users to issue [pull requests](https://help.github.com/articles/creating-a-pull-request), and is the preferred way to have your contributions added to pycsw, although patches and other mechanisms are welcome as well.  If you are submitting a patch, please add the `has-patch` label to the ticket (so tickets with patches can be easily filtered).  Also read the [_FAQ_]({{site.baseurl}}/faq.html) before submitting.

All pycsw [source code](https://github.com/geopython/pycsw) is managed on GitHub, which includes the latest (`master`) and other supported branches.

## Getting Involved

Users, developers and others are more than welcome!  There are plenty of ways to get involved:

- [Development](http://pycsw.org/development)
- [Project Steering Committee](psc.html)

__Developers__ (check [Contributing](http://docs.pycsw.org/en/latest/contributing.html) for more info)

- adding new functionality
- fixing issues
- adding unit tests

__Users__

- reporting bugs
- testing
- documentation

<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>
<script type="text/javascript">
  function makeSimpleSlideshow(container) {
    container.addClass('slideshow').hide().slideDown('slow');
    $('a', container).each(function() {
      $(this).attr('title', $('img', this).attr('alt'));
    }).clone().appendTo(container);
    var links = $('a', container).wrapAll('<div class=items></div>');
    var items = $('div.items', container);
    var firstLink = $(links[0]);
    var lastLink = $(links[links.length / 2 - 1]);
    var pixels = lastLink.offset().left - firstLink.offset().left + lastLink.width();

    function scroll() {
      items.animate({left: -pixels + 'px'}, pixels * 20, 'linear', function() {
        items.css('left', '0px');
        scroll();
      });
    }
    scroll();
  }

  $(document).ready(function() {
      var powered = $('div.pycsw-powered');
      if (powered.length > 0)
          makeSimpleSlideshow(powered);
  });
</script>
