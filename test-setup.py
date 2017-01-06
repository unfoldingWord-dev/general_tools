from setuptools import setup

setup(
    name="uw_tools",
    version="0.0.6",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Unit test setup file.",
    keywords="",
    url="https://github.org/unfoldingWord-dev/uw_tools",
    packages=['general_tools', 'uw'],
    long_description='Unit test setup file',
    classifiers=[],
    requires=['pygithub', 'pyparsing'],
    test_suite='tests'
)
