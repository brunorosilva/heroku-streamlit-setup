from setuptools import setup
setup(
    name = 'heroku_streamlit_cli',
    version = '0.1.0',
    packages = ['hss'],
    entry_points = {
        'console_scripts': [
            'hss = hss.__main__:main'
        ]
    })