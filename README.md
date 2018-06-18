Systers Hyperkitty [![Build Status](https://travis-ci.org/systers/hyperkitty.svg?branch=develop)](https://travis-ci.org/systers/hyperkitty) [![Coverage Status](https://coveralls.io/repos/github/systers/hyperkitty/badge.svg?branch=develop)](https://coveralls.io/r/systers/hyperkitty?branch=develop)
========================

Systers Hyperkitty is a customized version of [mailman's v3 archiver, Hyperkitty](https://gitlab.com/mailman/hyperkitty)

Website: http://hyperkitty.systers.org

Project page: http://systers.github.io/hyperkitty/

Since this project is originally a clone of mailman's Hyperkitty, it important to check the [LEGACY README](https://github.com/systers/hyperkitty/blob/develop/LEGACY_README.rst) which reflects a general setup for the Hyperkitty project irrespective. Since the project is changing on both sides the live documents maintained by the mailman Hyperkitty may eventually become confusing to use for this repository. Hence we maintain basic setup instructions here **You should read the [LEGACY README](https://github.com/systers/hyperkitty/blob/develop/LEGACY_README.rst) first** as we are trying to always be in synchrony with the latest updates.


Setup for developers (Unix)
---------------------------

1. Create a virtual environment with Python 3 and install dependencies:

     ```bash
   virtualenv venv_name
   source venv_name/bin/activate
     ```

*That should be done preferably in a directory know as mailman where you can configure the rest of the tools in suite such as Postorius. Also `venv_name` can be anything you want a lot of developers simply always name their virtual environment venv that's if you keep the virtual environment in its project folders to avoid confusion*

1. Clone the repository 
    ```
    git clone https://gitlab.com/systers/hyperkitty.git
    cd hyperkitty
    python setup.py develop
    ```
1. As mentioned in the [hyperkitty live documation](http://hyperkitty.readthedocs.io/en/latest/development.html) : *You will also need to install the `Sass` CSS processor using your package manager or the project’s installation documentation. You can either use the default Ruby implementation or the C/C++ version, called `libsass` (the binary is `sassc`). The configuration file in `example_project/settings.py` defaults to the `sassc` version, but you just have to edit the COMPRESS_PRECOMPILERS mapping to switch to the Ruby implementation, whoose binary is called `sass`.*

Run `sudo apt-get install ruby-sass` to run the sass binary then update `example_project/settings.py` and change default `sassc` to `sass`. Take note, if you install sassc don't modify this part as specified.

```
COMPRESS_PRECOMPILERS = (
  ('text/x-scss', 'sass -t compressed {infile} {outfile}'),
  ('text/x-sass', 'sass -t compressed {infile} {outfile}'),
)
```


1. Run `python example_project/manage.py migrate` or `django-admin migrate --pythonpath example_project --settings settings` as specified in the live documentation to setup the database.

1. Run `python example_project/manage.py runserver` or `django-admin runserver --pythonpath example_project --settings settings` to start the server

*Please note, the [live documentation](http://hyperkitty.readthedocs.io/en/latest/development.html) contains many other details that are important but may not be required for a successful setup, you are strongly encouraged to visit the live documentation as well.*


If you face any issues while setting up Hyperkitty locally, have a look at issues labelled as [hyperkitty-setup](https://github.com/systers/portal/labels/hyperkitty-setup). We are on  slack you can make use of the [#hyperkitty and #questions](https://systers-opensource.slack.com/messages/C0FGYV50U/) channels.


Documentation
-------------

A more comprehensive documentation for Hyperkitty is generated using [Sphinx](http://sphinx-doc.org/)
and available online at http://hyperkitty.readthedocs.io/en/latest/development.html and the general Mailman suite (which includes Hyperkitty setup) at http://docs.mailman3.org/en/latest/prodsetup.html

To build the documentation locally run:
```bash
$ make -C doc html
```

The HTML files will be available in the `doc/_build/html` directory.

For more information on semantics and builds, please refer to the Sphinx
[official documentation](http://sphinx-doc.org/contents.html).
