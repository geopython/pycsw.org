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
- modified: 2016-05-17

## Overview

This RFC describes the replacement of pycsw's custom testing tools with pytest.

Pycsw's current testing tool is not using any standard testing framework, nor 
Python's `unittest` package. It has been developed specifically for pycsw. 
It is usable and provides effective testing for pycsw. However, it has a 
number of weak areas that make its usage a bit cumbersome. Specifically:

- It is not possible to run individual tests, only sets of suites;
- It is not possible to hide the output of passing tests. This makes it 
  harder to focus on tests that fail;
- Running tests have side effects, creating new files in the code 
  directories. These files hold the output of failed tests, presumably to 
  provide an easier way to focus on problems;
- Local tests depend on the availability of a previously setup pycsw instance. 
  This previous step is currently automated in the `pavement.py` file, but
  it is perhaps not ideal that test setup be dependent on additional tooling.

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
  output, saving test results into new files is not needed anymore. 
  Alternatively, if preferred, pytest's test functions can save files 
  in temporary directories (outside of the source code tree) and it manages 
  the names of these files, so that they don't clash between consecutive test 
  runs;
- Pytest has a very flexible way of configuring setup and tear down of test
  resources, making it possible to start and stop pycsw instances in an
  integrated way, as part of the testing framework.

In addition to the mentioned improvements, pytest brings some additional
benefits:

- It is widely used in the Python community, which can potentially make new 
  devs more comfortable with running pycsw's tests
- It has lots of useful plugins, which can be used to improve code quality
  further, such as code linting with flake8, generation of HTML reports, 
  distributing tests over multiple CPUs, etc.

## Proposed Solution

Pytest will be added as an extra requirement for pycsw development. This 
should not be problematic, as pytest is easily installable using pip and
it is available on all platforms targeted by pycsw.

The existing testing tool will be refactored in order to remove the custom
test runner code, replacing it with the pytest test runner. No modification 
should be needed in the actual test suites, as they are mostly data files.
The new testing framework will not remove any of the currently available 
features.

Pytest tests will be generated in a similar way to the current implementation:

- Based on the names of the tests or suites to run, a new database is 
  configured with testing data
- A pytest configuration function scans the available suite files and 
  automatically parametrizes a generic test class, creating individual tests
  for each POST or GET request in the available suites

Running of tests will be performed by using the `py.test` tool, which is 
available with pytest's installation.

## Implementation

Pytest provides flexible mechanisms for configuration and parametrization of 
tests:

-  The [pytest_generate_tests](http://pytest.org/latest/parametrize.html#basic-pytest-generate-tests-example)
   function will be used to automatically generate individual test cases for each
   request in the existing `tests/suites` directory. The name of each test
   will combine the name of the suite with the identifier of each request, making
   it trivial to select subsets of tests to run, using 
   `py.test -k "expression"` syntax;

- The addition of extra [command-line parameters](http://pytest.org/latest/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options) to pytest's runner will provide a way to specify the 
  necessary configuration of tests. It will be possible to specify the same
  configuration parameters as with the current tool. These parameters can 
  also be picked up from configuration files or specified as 
  environment variables, which can be used effectively in pycsw's continuous
  integration builds;

- The definition of [fixtures](http://pytest.org/latest/fixture.html#fixture). 
  These are used to start, configure and stop local pycsw instances for each 
  suite. This means that it is not necessary to resort to an external tool for
  configuring and running tests. A technical detail that is possible with this
  kind of unification is the _a priori_ definition of a server's 
  configuration file, meaning that it is not necessary to use the `config` 
  KVP parameter in test calls as in the current implementation.

### Activating the feature

Since this RFC is about replacing the current testing tool with a new one, 
the new testing tool will active by default and becomes the only choice for 
running pycsw's tests.

### Files affected

- docs - Relevant documentation will be updated to include information on how 
  to run tests and also on how to add new tests
- `tests/run_tests.py` - To be deleted.
- `tests/gen_html.py` - To be deleted. Pytest's `pytest-html` plugin will be 
   used to provide similar functionality
- `pavement.py` - The paver tasks that relate to testing will be deleted. Pytest's 
  `py.test` tool will be used for running tests
- `tests/conftest.py` - This is a new file that holds fixtures and parametrization
  instructions for setting up the tests;
- `tests/test_suites.py` - This is a new file that contains the tests to be run
- `requirements-dev.txt` - To include pytest and additional plugins as 
  dependencies
- `.travis.yml` - To be refactored with the new commands to run tests

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
- It becomes possible to inspect running times for each test

### Internal Interface changes

TBD

### Performance Implications

None

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

Pull request has not been issued yet. Implementation is ongoing at:

[https://github.com/ricardogsilva/pycsw/tree/issue#428](https://github.com/ricardogsilva/pycsw/tree/issue%23428)

### Voting History

TBD

### Status

TBD
