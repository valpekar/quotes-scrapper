from setuptools import setup, find_packages

setup(
    name="quotes_scraper",
    version="0.1.0",
    description="A clean-architecture quote scraper for quotes.toscrape.com",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    python_requires=">=3.7",
) 