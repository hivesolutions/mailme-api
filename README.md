# [Mailme API](http://mailme-api.hive.pt)

API Python client for the Mailme service.

## Configuration

* `MAILME_BASE_URL` (`str`) - The base URL for the Mailme API requests (defaults to `https://mailme.bemisc.com/api/`)
* `MAILME_KEY` (`str`) - The secret key to be used to authenticate API requests (defaults to `None`)

## Installation

```bash
pip install mailme_api
```

## Usage

```bash
RECEIVERS="receiver@domain.com" \
CONTENTS="Hello World" \
python -m mailme.scripts.sender
```

## License

Mailme API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/hivesolutions/mailme_api.svg?branch=master)](https://travis-ci.org/hivesolutions/mailme_api)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/mailme_api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/mailme_api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/mailme_api.svg)](https://pypi.python.org/pypi/mailme_api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
