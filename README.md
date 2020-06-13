# Site connectivity checker
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/massicer/Site-Connectivity-Checker/branch/master/graph/badge.svg)](https://codecov.io/gh/massicer/Site-Connectivity-Checker) 
[![Build Status](https://travis-ci.org/massicer/Site-Connectivity-Checker.svg?branch=master)](https://travis-ci.org/massicer/Site-Connectivity-Checker)

Checks periodically a site connection availability and reports downtimes.

## How to use it
Install the package:
```
make install-dev
```
Run the script
```python
poetry run start_service --number_of_request=20 --url_protocol=http --service_port=80 --service_url=www.google.com --check_time=5s
```
Check the logs

### check_time Options
You can specify your check time using the syntax of the library: [PyTime_converter](https://github.com/massicer/PyTime-Converter)


## Useful commands
- `make install-dev`
- `make test`
- `make lint`
- `make fix-lint`
