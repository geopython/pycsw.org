---
layout: default
title: RFC8 - Move to pytest testing tool
description: This RFC describes the replacement of pycsw's custom testing tools with pytest
keywords: rfc,rfc-8,pytest,test
active_page: rfc-8
---

# RFC 8: Move to pytest testing tool

- date: 2016-05-17
- author: Ricardo Garcia Silva
- contact: ricardo.garcia.silva@gmail.com
- status: draft
- modified: 2016-12-23

## Overview

This RFC describes the replacement of pycsw's custom testing tools with pytest.

Pycsw's current testing tool is not using any standard testing framework, it
has been developed specifically for pycsw. It is usable and provides effective
testing for pycsw. However, it has a number of weak areas that make its
usage a bit cumbersome. Specifically:

- It is not possible to run individual tests, only sets of suites;
- It is not possible to hide the output of passing tests. This makes it
  harder to focus on tests that fail;
- Running tests have side effects, creating new files in the code 
  directories. These files hold the output of failed tests, presumably to 
  provide an easier way to focus on problems;
- Local tests depend on the availability of a previously setup pycsw instance. 
  This previous step is currently automated in the `pavement.py` file, but
  it is perhaps not ideal that test setup be dependent on additional tooling.
- Running tests with multiple python versions and multiple repository backends
  is not straightfoward and requires a lot of manual tweaking and switching;

[pytest](http://pytest.org/latest/) is a mature, full-featured Python testing 
tool. It is widely used in the Python community. It is a robust tool, 
available for multiple Python versions and implementations. It is feature 
complete and also sports a number of extra plugins, allowing for a flexible 
usage.

Pytest can be used to replace pycsw's own testing tool. Its usage will improve
all of the aforementioned issues with the current tool:

- Tests can be selected using pytest markers or by filtering based on the name
  of each test. It becomes possible to run individual tests or even arbitrary
  groups of tests. Running all tests, or individual test suites remains 
  possible;

- Pytest suppresses the output of passing tests by default, making it easy to
  focus only on the output of failed tests. This behaviour is easily 
  configurable, and it is possible to show the full output of every test, if
  needed;

- Since it is easy to run individual tests and also to suppress unneeded 
  output, saving test results into new files is not needed anymore;

- Pytest has a very flexible way of configuring setup and tear down of test
  resources, making it possible to start and stop pycsw instances in an
  integrated way, as part of the testing framework.
  
- Integrating pytest and tox allows running tests in multiple isolated 
  environments with different python versions and database backends.

In addition to the mentioned improvements, pytest brings some additional
benefits:

- It is widely used in the Python community, which can potentially make new 
  devs more comfortable with running pycsw's tests
- It has lots of useful plugins, which can be used to improve code quality
  further, such as generating code coverage reports, code linting with flake8, 
  generation of HTML reports, distributing tests over multiple CPUs, etc.
  
In addition to pytest, it is very common in the python community to also use 
[tox](https://tox.readthedocs.io/) to test the same code base against multiple 
python versions and dependency combinations. Tox creates multiple virtual 
environments in a fully automatic way. It can be integrated with pytest
and also works well under continuous integration. This enables devs to test 
pycsw locally against multiple configurations, the same way as it is done on
pycsw's current CI tool, [travis](https://travis-ci.org/geopython/pycsw)

## Proposed Solution

Pytest will be added as an extra requirement for pycsw development. This 
should not be problematic, as pytest is easily installable using pip and
it is available on all platforms targeted by pycsw.

The existing testing tool will be refactored in order to remove the custom
test runner code, replacing it with the pytest test runner. Small modficiations
to the actual test suites will also be introduced, mostly in order to remove
unneeded parameters and moving expected results into their own suite's
directory.
The new testing framework will not remove any of the currently available
features.

Tox will also be setup to run pycsw's pytest tests against multiple Python 
versions. In the future, this can be extended to also run tests against 
multiple pycsw repository backends, such as `sqlite`, `postgresql` and `mysql`.

Pytest tests will be generated in a similar way to the current implementation:

- For each test suite, a new database is always created on each test session,
  and an individual pycsw instance is fed a test request; In contrast with the
  current implementation, pycsw will not be called through a web server, but 
  directly by importing `pycsw.core.server`. This allows collecting information
  on code coverage and also negates the need to spawn an extra process for the
  web server.

  Those suites wich do not require custom data, will still get a new database
  populated with data from the `cite` suite.
  
  Suites that do not specify a `data/` directory will get an empty database for
  testing, as is the case in the current implementation;

- A pytest configuration function scans the available suite files and
  automatically parametrizes a generic test class, creating individual tests
  for each POST or GET request in the available suites. Each test is named by
  combining three parameters:
  
  - The current suite's name;
  - The current HTTP method;
  - The current test's identifier
  
  This makes it easy to run only certain tests by using pytest's 
  `-k <test_expression>`

- Each test is basically an HTTP request that gets sent to the pycsw instance
  followed by a comparison of the received response with an expected result.
  The way in which tests are evaluated is the same as in the current 
  implementation;

Running of tests will be performed by using the `py.test` tool, which is 
available with pytest's installation.

## Implementation

Pytest provides flexible mechanisms for configuration and parametrization of 
tests:

-  The [pytest_generate_tests](http://pytest.org/latest/parametrize.html#basic-pytest-generate-tests-example)
   function will be used to automatically generate individual test cases for each
   request in the existing `tests/suites` directory. The name of each test
   will combine the name of the suite with the identifier of each request,
   making it trivial to select subsets of tests to run. For example:

       py.test -k "cite and get"

   The previous command can be used to run all tests from the `cite` suite that
   are made with an HTTP GET request;

- The addition of extra [command-line parameters](http://pytest.org/latest/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options) to pytest's runner will provide a way to specify the 
  necessary configuration of tests. It will be possible to specify the same
  configuration parameters as with the current tool;

- The definition of [fixtures](http://pytest.org/latest/fixture.html#fixture). 
  These are used to start, configure and stop local pycsw instances for each 
  suite. This means that it is not necessary to resort to an external tool for
  configuring and running tests. A technical detail that is possible with this
  kind of unification is the _a priori_ definition of a server's 
  configuration file, meaning that it is not necessary to use the `config` 
  KVP parameter in test calls as in the current implementation.
  
- Tox will be used as a frontend for running pytest tests in order to allow 
  quick testing against multiple python versions. It will also be used in the
  configuration of the Travis CI script, so that there is a consistent way to
  run tests, locally and on the CI server. Regardless of tox, pytest can also 
  be used standalone when hacking on pycsw's code to get some quick feedback
  on test execution;


### Activating the feature

Since this RFC is about replacing the current testing tool with a new one, 
the new testing tool will active by default and becomes the only choice for 
running pycsw's tests.

Tests will be run using the `py.test` command line utility that becomes
available after pytest has been installed. Some example usage:

    py.test -h  # outputs help on pytest usage
    py.test --verbose --exitfirst  # be more verbose and exit as soon as one test fails
    py.test --capture=no  # do not suppress test's stdout
    py.test -k cite  # only run tests that have 'cite' in their identifiers
    py.test -k "cite and post"  # only run tests that have 'cite' and 'post' in their identifiers
    
As mentioned previously, it will also be possible to use tox to test against
multiple python versions (the versions must be previously intalled somehow).
Some example usage:

    sudo pip install tox  # must be installed on the base system
    tox  # runs all tests in python versions 2.6, 2.7, 3.4 and 3.5
    tox -e py27-sqlite  # runs all tests only on python2.7
    tox -e py34-sqlite -- -k 'csw30'  # runs only tests from the csw30 suite and only on python 3.4
    

### Files affected

- docs - Relevant documentation will be updated to include information on how 
  to run tests and also on how to add new tests

- `tests/expected/suites_<suite-name>_<request-type>_<test-id>.xml` - All
  files will be moved to their suite's corresponding
  `tests/functionaltests/suites/<suite-name>/expected/` directory and each 
  file's name is simplified to `<request-type>_<test-id>.xml`

- `tests/suites/<suite-name>/get/request.txt` - The
  `PYCSW_SERVER?config=<path-to-config-file>` portion of each GET request will
  be deleted. This becomes unnecessary, as each suite is backed by a
  previously setup pycsw instance that is already configured with the
  appropriate configuration file.

- `tests/run_tests.py` - To be deleted. Pytest's `py.test` script becomes the
  new test runner

- `pavement.py` - The paver tasks that relate to testing will be deleted.

- `tests/conftest.py` - This is a new file that holds fixtures and
  parametrization instructions for setting up the tests;
  
- `tests/functionaltests/` - This is a new directory that will contain the 
  existing tests. In the future it will be possible to add a `unittests/`
  directory with new, smaller scoped tests;
  
- `tests/functionaltests/conftest.py` - This is a new file that holds the 
  pytest code to automatically generate the functional tests;

- `tests/functionaltests/test_suites_functional.py` - This is a new file that 
  contains the actual code for performing tests.

- `requirements-dev.txt` - To include pytest and additional plugins as 
  dependencies

- `.travis.yml` - To be refactored with the new commands to run tests on
  github's travis CI


### Backwards Compatibility Issues

The proposed change is backwards incompatible because the whole testing 
infrastructure will be replaced. However, this change will not affect any 
user facing functionality. It is strictly oriented towards improving 
developer experience. 
Even if the existing test infrastructure will be refactored, the actual 
subjects under test will not change in any way. The same test requests, 
same test data and same test suites will continue to be used. As such, 
all tests will continue to pass, including CITE tests.

Recap of major new functionalities:

- A new way of running tests, using the `py.test` command-line tool
- It becomes possible to select single tests or arbitrary subsets of tests
  to run
- It becomes possible to have code coverage information
- Integration with tox allows running tests in multiple python versions

### Internal Interface changes

Nothing will change on the actual `pycsw` code, this change affects only the
testing infrastructure.

### Performance Implications

As no change will be made to `pycsw`'s code, performance will not be altered in
any way. However, the performance of tests will be improved due to the 
following:

- Not saving test results to the filesystem anymore;
- Not spawining extra process to run pycsw server;
- (local) Reusing tox virtualenvs between test runs makes testing faster but 
  still isolated;
- (CI) Caching pip dependencies on travis makes test setup a lot faster, 
  specially due to not having to compile `lxml` all the time;

### Related Bug Fixes

TBD

### Restrictions

None

### Documentation

Documentation will be updated as required.  

## Miscellaneous

### Issue Tracking ID

[https://github.com/geopython/pycsw/issues/428](https://github.com/geopython/pycsw/issues/428)

### Pull Request

Pull request at:

[https://github.com/geopython/pycsw/pull/492](https://github.com/geopython/pycsw/pull/492)

### Voting History

TBD

### Status

TBD
