
[![Build Status](https://travis-ci.org/geopython/pycsw.png?branch=website)](https://travis-ci.org/geopython/pycsw)

pycsw.org
=========

This is the setup for http://pycsw.org

Setting up website environment locally
--------------------------------------

    # setup virtualenv
    virtualenv pycsw-website && cd $_
    . bin/activate
    # get the website branch
    git clone git@github.com:geopython/pycsw.git -b website && cd pycsw
    # set Ruby environment variables
    . setenv-ruby-gem
    # install Jekyll
    gem install jekyll link-checker

Workflow
--------

    # edit content
    jekyll build
    jekyll serve  # default port is 4000, set explicitly with -P 
    # check links
    check-links _site
    # view at http://localhost:4000
    # publish to live
    ./publish.sh <username>
    # update live deployment map
    python to_geojson.py
    git commit -m 'update live deployment map' live-deployments.geojson
    git push origin website
    # adding blogposts
    cd _drafts
    vi newpost.md
    # make sure to set the following YAML front matter:
    # layout: post
    # title: Some Title
    # author: Firstname Lastname
    # author_url: URL to link to the author (Twitter, GitHub, etc.)
    # publish_date: YYYY-MM-DD HH:MM:SS [zone]
    # - examples:
    #  - 2013-09-23 11:11:11  # default timezone is UTC
    #  - 2013-09-23 11:11:11 -0400  # per http://asg.web.cmu.edu/rfc/rfc822.html#sec-5.1)
    #  - 2013-09-23 11:11:11 EST  # per http://asg.web.cmu.edu/rfc/rfc822.html#sec-5.1)
    # preview with `make drafts` and draft will show up as latest post
    # when you are ready to publish:
    # - rename the file as per the current YYYY-MM-DD
    git mv _drafts/newpost.md _posts/YYYY-MM-DD-newpost.md
    vi _posts/YYYY-MM-DD-newpost.md
    # update the publish_date YAML front matter
    # commit and push
    git commit -m 'publish article'
    git push origin website

For a [Sphinx](http://sphinx-doc.org/) feel, there's a `Makefile` with
the familiar targets:

    make html
    make linkcheck
    make clean
    make publish username=<username>
    make drafts
