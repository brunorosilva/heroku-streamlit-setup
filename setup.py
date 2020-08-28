from setuptools import setup
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name = 'hss',
    version = '0.0.2',
    author='Bruno Rodrigues Silva',
    author_email='rodriguessilvabruno@outlook.com',
    description="command line interface for setting up streamlit webapps on heroku",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/brunorosilva/heroku-streamlit-setup',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'hss = hss.__main__:main'
        ],
    },
    python_requires='>=3.6',
    install_requires=["pipreqs"]
)