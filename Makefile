PY?=python
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content/
OUTPUTDIR=$(BASEDIR)/output/
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/pelicanconf.py

SSH_USER?=mhughes
SSH_HOST?=tuftscs
SSH_PORT?=22

SSH_TARGET_DIR?=/r/ml/public_html/

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '                                                                          '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '


html: courses_page events_page headshots
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif


ssh_upload: html
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: html
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude --exclude "**/*_raw/"

.PHONY: html help clean serve ssh_upload rsync_upload


## PEOPLE PAGE

headshots:
	cd $(INPUTDIR)/images/ && bash create_folder_of_square_crops.sh headshots_raw/ headshots_200x200/ 200

$(INPUTDIR)/pages/people.md: headshots
	cd $(INPUTDIR)/courses/ && touch people.md


## COURSES PAGE

course_logos:
	cd $(INPUTDIR)/images/ && bash create_folder_of_square_crops.sh course_logos/ course_logos_200x200/ 200

$(INPUTDIR)/pages/courses.md: course_logos $(INPUTDIR)/courses/*.csv $(INPUTDIR)/courses/make_page__courses.py
	cd $(INPUTDIR)/courses/ && python make_page__courses.py

courses_page: $(INPUTDIR)/pages/courses.md


## EVENTS PAGE

$(INPUTDIR)/pages/events.md: $(INPUTDIR)/events/make_page__events.py $(INPUTDIR)/events/*.csv
	cd $(INPUTDIR)/events/ && python make_page__events.py

events_page: $(INPUTDIR)/pages/events.md


