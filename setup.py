import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ufmtrends-sdk',
    version='0.0.3',
    author='Jose Alvarez',
    author_email='jose@tecuntecs.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK',
    project_urls = {
        "Bug Tracker": "https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK/issues"
    },
    license='cc.license',
    packages=['ufmtrends_sdk'],
    install_requires=['requests'],
)