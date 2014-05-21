---
layout: default
title: Project Steering Committee (PSC)
description: Project Steering Committee (PSC)
keywords: psc,project steering committee,process
active_page: psc
---

# Project Steering Committee

In accordance with [RFC1](http://pycsw.org/development/rfc/rfc-1.html),
the authoritative and current PSC membership list is maintained at
[http://pycsw.org/community/psc.html](http://pycsw.org/community/psc.html)

Members are (in alphabetical order):

<ul>
{% for member in site.data.psc_members %}
  {% if member[2] == 'PSC' %}
  <li><a title="{{ member[0]  }}" href="https://github.com/{{ member[1] }}">{{ member[0] }}</a></li>
  {% elsif member[2] == 'PSC Chair' %}
  <li><a title="{{ member[0]  }}" href="https://github.com/{{ member[1] }}">{{ member[0] }}</a> (Chair)</li>
  {% endif %}
{% endfor %}
<ul>

<script src="https://embed.github.com/view/geojson/geopython/pycsw.org/master/live-deployments.geojson"></script>
