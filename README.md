# Tufts ML Research Group Website

Source code for the Tufts ML research group website from 2018-present.

Serving the groups of Prof. Liping Liu and Prof. Mike Hughes.

## Quick links

How to:
* [Add an event to the events page](#add-event)
* [Add a person to the people page](#add-people)
* [Add a course to the courses page](#add-course)
* [Build website from source](#build-website)
* [Install dependencies](#install-dependencies)



## How to build the website from source
```
$ make html         # Build static site on local machine, in output/ folder
$ make serve        # Serve website locally (runs in background). To view, point your favorite browser to: localhost:8000
```

To push any local changes to the real site, just do:
```
$ SSH_USER=____ SSH_HOST=____ SSH_TARGET_DIR=____  make rsync_upload 
```

This will upload the files to SSH_USER@SSH_HOST:SSH_TARGET_DIR via rsync.


## Install Dependencies

* Pelican: http://blog.getpelican.com/
* Markdown

#### Installing dependencies with conda (recommended)

$ conda install -c conda-forge pelican=3.7.0
$ conda install markdown

#### Installing with pip

$ pip install pelican
$ pip install markdown
