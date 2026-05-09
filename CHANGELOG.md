# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* Support for `MODE` configuration in the sender script
* Python 3.13 and 3.14 to the CI build matrix

### Changed

* Narrowed the `mode` field type to `Literal["markdown", "html", "auto"]`
* Bumped `actions/checkout` to v6 in CI workflows
* Switched the deploy workflow to build distributions with `python -m build`

### Fixed

*

## [0.2.2] - 2024-04-30

### Added

* Support for `style_css` in the `MessagePayload`

## [0.2.1] - 2024-04-30

### Changed

* Direct inclusion of pyi files in `setup.py`

## [0.2.0] - 2024-04-20

### Changed

* Sanitization of the code structure, making compliant with `black`
* Improved support for type hints
