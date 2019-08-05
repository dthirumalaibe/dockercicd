# Module 5 - Getting Familiar with DevOps Processes and Tools
This directory builds on the Module 4 code which includes several
Docker-related and CRM-app related content. The additions are
discussed below. Note that the `install/` directory has been
removed as it is assumed that Docker and `docker-compose` are
still installed from the previous module.

## Tests
This module introduced linting, unit tests, and system tests.
  * `.pylintrc`: The configuration file used by `pylint`, a Python
    syntax and styling checker.
  * `src/test_unit.py`: Set of unit tests to evaluate the `Database`
    class `balance()` and `owes_money()` methods. This latter method
    was added using test-driven development (TDD).
  * `src/test_system.py`: Set of system tests which uses `docker-compose`
    to set up several containers then uses Python `requests` to test
    the complete functionality of all running containers.

## Test Pipeline
The course demonstrated Travis CI at a high-level to illustrate how
all the pieces fit together. The `.travis.yml` file contains the "script"
that Travis will follow upon every `git push` or pull request (PR)
operation.
