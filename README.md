# Heroku-Streamlit-Setup (hss)

This is a symple cli (command line interface) library to help you put your streamlit webapp in production.

This lib will soon be hosted on pypi.org and I'll also write a article on Medium explaining it (:

If you have any problem with it, please open an issue and I'll get back to you.

### Why is this package important and what do I need to use it?
From what I've seen there's not lots of documentation about putting streamlit webapps into production, trust me I've suffered.

You just need a Free [Heroku](https://www.heroku.com/) Account, a Github account and a [Streamlit](https://www.streamlit.io/) webapp you want to share with the world.

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
