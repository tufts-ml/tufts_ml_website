# Tufts ML Research Group Website

Source code for the Tufts ML research group website from 2018-present.

Serving the groups of Prof. Liping Liu and Prof. Mike Hughes.

## Quick links

How to:
* [Add an event to the events page](#add-events)
* [Add a person to the people page](#add-people)
* [Add a course to the courses page](#add-course)
* [Build website from source](#how-to-build-website-from-source)
* [Install dependencies](#install-dependencies)


## Add events

1) Add a row to the appropriate CSV file

2) Then do `make html` to rebuild from source.

Event files:

* [events_2018_fall.csv](./content/events/events_2018_fall.csv)


## Add people

1) Edit by hand the file: [people.md](./content/pages/people.md)

2) The do `make html` to rebuild from source

## Add course

0) New semester? Add a new CSV file and update the list at the top of [make_page__courses.py](./content/courses/make_page__courses.py)

1) Add a row to the appropriate CSV file

2) Then do `make html` to rebuild from source.

Course files:

* [courses_2018_fall.csv](./content/courses/courses_2018_fall.csv)
* [courses_2018_spring.csv](./content/courses/courses_2018_spring.csv)



## How to build website from source
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
* Pandas (for reading/writing csv files)

#### Installing dependencies with conda (recommended)

```
$ conda install -c conda-forge pelican
$ conda install markdown
$ conda install pandas
```