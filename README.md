# Heroku-Streamlit-Setup (hss)

This is a symple library to help you put your streamlit webapp in production

### Documentation
<pre>
$ hss --help


Usage:
    get_requirements.py [options] [&lt;appname&gt;] [&lt;path&gt;] [&lt;email&gt;]

Arguments:
    &lt;appname&gt;             The app filename (with or without .py).
    &lt;path&gt;                The path to the directory containing the application
                          files for which a requirements file should be
                          generated (defaults to the current working
                          directory).
    &lt;email&gt;               The email associated with your Heroku account.

Options:
    --no-reqs             Don't make a requirements file
    --no-setup            Don't make a setup.sh file
    --no-proc             Don't make a Procfile
    --force               Substitute the current requirements.txt.
</pre>
