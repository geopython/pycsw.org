
[![Build Status](https://github.com/geopython/pycsw.org/workflows/build%20%E2%9A%99%EF%B8%8F/badge.svg)](https://github.com/geopython/pycsw.org/actions)

# pycsw.org

This is the setup for https://pycsw.org

## Setting up website environment locally

```bash
# setup virtualenv
virtualenv pycsw.org && cd $_
. bin/activate
# get the repo
git clone git@github.com:geopython/pycsw.org.git && cd pycsw.org
# set Ruby environment variables
. setenv-ruby-gem
# install Jekyll
gem install jekyll link-checker jekyll-mentions jekyll-sitemap github-pages
```

## Workflow

```bash
# edit content
jekyll build
jekyll serve  # default port is 4000, set explicitly with -P 
# check links
check-links _site
# view at http://localhost:4000
# commit changes
git commit -m 'my change' ...
# publish to live site
git push origin gh-pages
# update live deployment map
# content is managed at https://github.com/geopython/pycsw/wiki/Live-Deployments
python to_geojson.py live_deployments
git commit -m 'update live deployment map' live-deployments.geojson
git push origin gh-pages
# adding blogposts
cd _drafts
vi newpost.md
# make sure to set the following YAML front matter:
# layout: post
# title: Some Title
# author: Firstname Lastname
# author_url: URL to link to the author (Twitter, GitHub, etc.)
# preview with `make drafts` and draft will show up as latest post
# when you are ready to publish:
# - rename the file as per the current YYYY-MM-DD
git mv _drafts/newpost.md _posts/YYYY-MM-DD-newpost.md
vi _posts/YYYY-MM-DD-newpost.md
# update the publish_date YAML front matter
# commit and push
git commit -m 'publish article'
git push origin gh-pages
```

For a [Sphinx](https://www.sphinx-doc.org/) feel, there's a `Makefile` with
the familiar targets:

```bash
make html
make linkcheck
make clean
make drafts
```
