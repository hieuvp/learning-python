#!/usr/bin/env bash

set -eoux pipefail

flake8 learn-the-basics/variables-and-types/exercise.py

# optional arguments:
#
#  --append-config APPEND_CONFIG
#                        Provide extra config files to parse in addition to the files found by Flake8 by default. These files are the last ones read and so
#                        they take the highest precedence when multiple files provide the same option.
#  --config CONFIG       Path to the config file that will be the authoritative config source. This will cause Flake8 to ignore all other configuration
#                        files.
#  --isolated            Ignore all configuration files.
#  --version             show program's version number and exit
#  -q, --quiet           Report only file names, or nothing. This option is repeatable.
#  --count               Print total number of errors and warnings to standard error and set the exit code to 1 if total is not empty.
#  --diff                Report changes only within line number ranges in the unified diff provided on standard in by the user.
#  --exclude patterns    Comma-separated list of files or directories to exclude. (Default: ['.svn', 'CVS', '.bzr', '.hg', '.git', '__pycache__', '.tox',
#                        '.eggs', '*.egg'])
#  --extend-exclude patterns
#                        Comma-separated list of files or directories to add to the list of excluded ones.
#  --filename patterns   Only check for filenames matching the patterns in this comma-separated list. (Default: ['*.py'])
#  --stdin-display-name STDIN_DISPLAY_NAME
#                        The name used when reporting errors from code passed via stdin. This is useful for editors piping the file contents to flake8.
#                        (Default: stdin)
#  --format format       Format errors according to the chosen formatter.
#  --hang-closing        Hang closing bracket instead of matching indentation of opening bracket's line.
#  --ignore errors       Comma-separated list of errors and warnings to ignore (or skip). For example, ``--ignore=E4,E51,W234``. (Default: ['E123', 'W503',
#                        'E226', 'E704', 'E121', 'W504', 'E126', 'E24'])
#  --extend-ignore errors
#                        Comma-separated list of errors and warnings to add to the list of ignored ones. For example, ``--extend-ignore=E4,E51,W234``.
#  --per-file-ignores PER_FILE_IGNORES
#                        A pairing of filenames and violation codes that defines which violations to ignore in a particular file. The filenames can be
#                        specified in a manner similar to the ``--exclude`` option and the violations work similarly to the ``--ignore`` and ``--select``
#                        options.
#  --max-line-length n   Maximum allowed line length for the entirety of this run. (Default: 79)
#  --max-doc-length n    Maximum allowed doc line length for the entirety of this run. (Default: None)
#  --select errors       Comma-separated list of errors and warnings to enable. For example, ``--select=E4,E51,W234``. (Default: ['E', 'F', 'W', 'C90'])
#  --disable-noqa        Disable the effect of "# noqa". This will report errors on lines with "# noqa" at the end.
#  --show-source         Show the source generate each error or warning.
#  --statistics          Count errors and warnings.
#  --enable-extensions ENABLE_EXTENSIONS
#                        Enable plugins and extensions that are otherwise disabled by default
#  --exit-zero           Exit with status code "0" even if there are errors.
#  --install-hook {git,mercurial}
#                        Install a hook that is run prior to a commit for the supported version control system.
#  -j JOBS, --jobs JOBS  Number of subprocesses to use to run checks in parallel. This is ignored on Windows. The default, "auto", will auto-detect the
#                        number of processors available to use. (Default: auto)
#  --tee                 Write to stdout and output-file.
#  --benchmark           Print benchmark information about this run of Flake8
#  --bug-report          Print information necessary when preparing a bug report
#
# mccabe:
#  --max-complexity MAX_COMPLEXITY
#                        McCabe complexity threshold
#
# pyflakes:
#  --builtins BUILTINS   define more built-ins, comma separated
#  --doctests            also check syntax of the doctests
#  --include-in-doctest INCLUDE_IN_DOCTEST
#                        Run doctests only on these files
#  --exclude-from-doctest EXCLUDE_FROM_DOCTEST
#                        Skip these files when running doctests

# pylint learn-the-basics/variables-and-types/exercise.py

# $ pylint --help
#
#   Master:
#     --init-hook=<code>  Python code to execute, usually for sys.path
#                         manipulation such as pygtk.require().
#     -E, --errors-only   In error mode, checkers without error messages are
#                         disabled and for others, only the ERROR messages are
#                         displayed, and no reports are done by default.
#     --py3k              In Python 3 porting mode, all checkers will be
#                         disabled and only messages emitted by the porting
#                         checker will be displayed.
#     --ignore=<file>[,<file>...]
#                         Add files or directories to the blacklist. They should
#                         be base names, not paths. [current: CVS]
#     --ignore-patterns=<pattern>[,<pattern>...]
#                         Add files or directories matching the regex patterns
#                         to the blacklist. The regex matches against base
#                         names, not paths. [current: none]
#     --persistent=<y_or_n>
#                         Pickle collected data for later comparisons. [current:
#                         yes]
#     --load-plugins=<modules>
#                         List of plugins (as comma separated values of python
#                         module names) to load, usually to register additional
#                         checkers. [current: none]
#     --fail-under=<score>
#                         Specify a score threshold to be exceeded before
#                         program exits with error. [current: 10]
#     -j <n-processes>, --jobs=<n-processes>
#                         Use multiple processes to speed up Pylint. Specifying
#                         0 will auto-detect the number of processors available
#                         to use. [current: 1]
#     --limit-inference-results=<number-of-results>
#                         Control the amount of potential inferred values when
#                         inferring a single object. This can help the
#                         performance when dealing with large functions or
#                         complex, nested conditions.  [current: 100]
#     --extension-pkg-whitelist=<pkg[,pkg]>
#                         A comma-separated list of package or module names from
#                         where C extensions may be loaded. Extensions are
#                         loading into the active Python interpreter and may run
#                         arbitrary code. [current: none]
#     --suggestion-mode=<yn>
#                         When enabled, pylint would attempt to guess common
#                         misconfiguration and emit user-friendly hints instead
#                         of false-positive error messages. [current: yes]
#     --exit-zero         Always return a 0 (non-error) status code, even if
#                         lint errors are found. This is primarily useful in
#                         continuous integration scripts.
#     --from-stdin        Interpret the stdin as a python script, whose filename
#                         needs to be passed as the module_or_package argument.
#
#   Commands:
#     --rcfile=<file>     Specify a configuration file to load.
#     --help-msg=<msg-id>
#                         Display a help message for the given message id and
#                         exit. The value may be a comma separated list of
#                         message ids.
#     --list-msgs         Generate pylint's messages.
#     --list-msgs-enabled
#                         Display a list of what messages are enabled and
#                         disabled with the given configuration.
#     --list-groups       List pylint's message groups.
#     --list-conf-levels  Generate pylint's confidence levels.
#     --list-extensions   List available extensions.
#     --full-documentation
#                         Generate pylint's full documentation.
#     --generate-rcfile   Generate a sample configuration file according to the
#                         current configuration. You can put other options
#                         before this one to get them in the generated
#                         configuration.
#
#   Messages control:
#     --confidence=<levels>
#                         Only show warnings with the listed confidence levels.
#                         Leave empty to show all. Valid levels: HIGH,
#                         INFERENCE, INFERENCE_FAILURE, UNDEFINED. [current:
#                         none]
#     -e <msg ids>, --enable=<msg ids>
#                         Enable the message, report, category or checker with
#                         the given id(s). You can either give multiple
#                         identifier separated by comma (,) or put this option
#                         multiple time (only on the command line, not in the
#                         configuration file where it should appear only once).
#                         See also the "--disable" option for examples.
#     -d <msg ids>, --disable=<msg ids>
#                         Disable the message, report, category or checker with
#                         the given id(s). You can either give multiple
#                         identifiers separated by comma (,) or put this option
#                         multiple times (only on the command line, not in the
#                         configuration file where it should appear only once).
#                         You can also use "--disable=all" to disable everything
#                         first and then reenable specific checks. For example,
#                         if you want to run only the similarities checker, you
#                         can use "--disable=all --enable=similarities". If you
#                         want to run only the classes checker, but have no
#                         Warning level messages displayed, use "--disable=all
#                         --enable=classes --disable=W".
#
#   Reports:
#     -f <format>, --output-format=<format>
#                         Set the output format. Available formats are text,
#                         parseable, colorized, json and msvs (visual studio).
#                         You can also give a reporter class, e.g.
#                         mypackage.mymodule.MyReporterClass. [current: text]
#     -r <y_or_n>, --reports=<y_or_n>
#                         Tells whether to display a full report or only the
#                         messages. [current: no]
#     --evaluation=<python_expression>
#                         Python expression which should return a score less
#                         than or equal to 10. You have access to the variables
#                         'error', 'warning', 'refactor', and 'convention' which
#                         contain the number of messages in each category, as
#                         well as 'statement' which is the total number of
#                         statements analyzed. This score is used by the global
#                         evaluation report (RP0004). [current: 10.0 - ((float(5
#                         * error + warning + refactor + convention) /
#                         statement) * 10)]
#     -s <y_or_n>, --score=<y_or_n>
#                         Activate the evaluation score. [current: yes]
#     --msg-template=<template>
#                         Template used to display messages. This is a python
#                         new-style format string used to format the message
#                         information. See doc for all details.
