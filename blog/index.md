---
layout: default
title: Blog
description: project blog and news
keywords: blog, development, announcements
active_page: blog
---

# Archive [![RSS]({{site.baseurl}}/img/rss.png)]({{site.baseurl}}/blog/feed.xml)

<ul>
  {% for post in site.posts %}
    <li>{{ post.date | date_to_long_string }} - <a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
