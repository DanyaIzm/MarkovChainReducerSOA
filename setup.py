try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = "1.0.2"
DESCRIPTION = "Reduce Markov's chains"

setup(
    name="markov_chain_reducer_soa",
    version=VERSION,
    author="StackCanary",
    description=DESCRIPTION,
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=[
        "markov_chain_reducer_soa",
    ],
)
