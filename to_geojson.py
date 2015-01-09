# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#          Ryan Clark <ryan.clark@azgs.az.gov>
#
# Copyright (c) 2013 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import csv
import json
import sys
from StringIO import StringIO
import urllib2


def health_check_csw(url):
    """Do a terse check / smoke test on a live deployment CSW"""

    try:
        content = urllib2.urlopen(url).read()
        if 'Capabilities ' not in content:
            raise RuntimeError('Unexpected response: %s' % content)
    except urllib2.HTTPError as err:
        raise RuntimeError('HTTP problem with %s: %s' % (url, err))
    except urllib2.URLError as err:
        raise RuntimeError('URL problem with %s: %s' % (url, err))
    except Exception as err:
        raise RuntimeError('Cannot open %s: %s' % (url, err))


def build_live_deployments_geojson():
    """Convert Live Deployments wiki page to GeoJSON for GitHub to render"""

    errors = 0
    dep_url = 'https://raw.github.com/wiki/geopython/pycsw/Live-Deployments.md'
    geojson = {'type': 'FeatureCollection', 'features': []}

    # grab Markdown file of Live Deployments from GitHub
    content = urllib2.urlopen(dep_url).read()

    # serialize as GeoJSON
    dep_reader = csv.reader(StringIO(content), delimiter='|')
    next(dep_reader)  # skip fields row
    next(dep_reader)  # skip dashed line row
    for row in dep_reader:
        url = row[2].strip()
        if url != 'http://demo.pycsw.org/':
            try:
                health_check_csw(url)

                xycoords = row[3].split(',')

                feature = {
                    'type': 'Feature',
                    'properties': {
                        'url': '<a target="_blank" href="%s">%s</a>' %
                               (url, row[1].strip())
                    },
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [float(xycoords[1]), float(xycoords[0])]
                    }
                }
                geojson['features'].append(feature)
            except RuntimeError as rte:
                errors += 1
                print 'ERROR: %s' % rte

    with open('live-deployments.geojson', 'w') as output_file:
        output_file.write(json.dumps(geojson, indent=4))

    return errors


def build_psc_geojson():
    """Create GeoJSON of PSC membership for GitHub to render"""
    geojson = {'type': 'FeatureCollection', 'features': []}

    # serialize as GeoJSON
    psc_reader = csv.reader(open('community/psc.csv'))
    next(psc_reader)  # skip fields row
    for row in psc_reader:
        url = '<a target="_blank" href="https://github.com/%s">%s</a>' % \
              (row[1], row[0])

        feature = {
            'type': 'Feature',
            'properties': {
                'name': url,
                'role': row[2]
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [float(row[4]), float(row[3])]
            }
        }
        if row[2].startswith('PSC'):
            color = '0000FF'
        else:
            color = '00FF00'

        feature['properties']['marker-color'] = color

        geojson['features'].append(feature)

    with open('community/psc.geojson', 'w') as output_file:
        output_file.write(json.dumps(geojson, indent=4))

if __name__ == '__main__':
    USAGE = 'Usage: %s <live_deployments|psc>' % sys.argv[0]
    if len(sys.argv) < 2:
        print USAGE
        sys.exit(1)
    if sys.argv[1] not in ['live_deployments', 'psc']:
        print USAGE
        sys.exit(2)
    if sys.argv[1] == 'live_deployments':
        ERRORS = build_live_deployments_geojson()
        sys.exit(ERRORS)
    elif sys.argv[1] == 'psc':
        build_psc_geojson()
