'''
'''

import pandas as pd
import datetime

today_timestamp = datetime.datetime.today().strftime('%Y-%m-%d')

## TODO to add more event sections just update this list
event_files = [
    ('Fall 2019', 'events_2019_fall.csv'),
    ('Spring 2019', 'events_2019_spring.csv'),
    ('Fall 2018', 'events_2018_fall.csv'),
    ]

main_item_template_str = \
"""
    <div class="row row-striped">
        <div class="d-none d-sm-block col-sm-2 text-left">
            <h2 class="pb-0 mb-0">{{MONTH_NAME}}</h2>
            <h1 class="pt-0 mt-0 display-4">
            <span class="badge badge-secondary">
                {{DAY_OF}}
            </span>
            </h1>
        </div>
        <div class="col-12 col-sm-10">
            <h3 class="mw-100">
            <a href="{{URL}}">
                <strong>
                    {{TYPE}}: {{TITLE}}
                </strong>
            </a>
            </h3>
            <ul class="list-inline mw-100">
                <li class="list-inline-item"><i class="fa fa-calendar-o" aria-hidden="true"></i> {{DATE}} </li>
                <li class="list-inline-item"><i class="fa fa-clock-o" aria-hidden="true"></i> {{TIME_STR}} </li>
                <li class="list-inline-item"><i class="fa fa-location-arrow" aria-hidden="true"></i> {{LOCATION}} </li>
                <li class="list-inline-item">
                    <button type="button" class="btn btn-primary btn-xs"
                        onclick="
                            d=new Date('{{YEAR}}-{{MONTH_NUM}}-{{DAY_OF}}T{{TIME24_STR}}');
                            downloadICS('{{TITLE}}','{{LOCATION}}',d,60);">
                    Download .ics
                    </button>
                </li>
            </ul>
            <p>
            Speaker: {{SPEAKER}}
            </p>
        </div>
    </div>
\n"""



out_md_str = "Title: Events\nDate: %s\nsave_as: events.html" % (
    today_timestamp)

out_md_str += (
"""\n
<!-- THIS PAGE SRC IS AUTO GENERATED. At terminal: $ make events -->

We keep a short list of special events on campus or nearby relevant to machine learning here.

For the latest information about these events, click the links below or see the primary source: <a href="https://engineering.tufts.edu/cs/events">Tufts CS Events Webpage</a>

<b>Reading group</b>: Interested research students are also invited to our machine learning reading group (we meet once a week). For details, please contact a faculty member.

\n""")



for title, fpath in event_files:

    csv_df = pd.read_csv(fpath, dtype={'DAY_OF':'str', 'MONTH_NUM':'str'})
    csv_df = csv_df.fillna('') # Fill missing values with blanks
    assert csv_df.shape[0] > 0

    anchor = title.lower().replace(' ', '-')
    out_md_str += "\n<a name='%s'></a>" % (anchor)
    out_md_str += "\n<h2>Events: %s</h2>" % (title)

    ## Main team names, images, + links
    out_md_str += '\n\n\n<div class="container">'
    for item_id, (row_id, row_df) in enumerate(csv_df.iterrows()):
        row_dict = row_df.to_dict()
        item_str = main_item_template_str + ""
        for key, val in row_dict.items():
            if key == 'URL':
                default_val = "#"
            else:
                default_val = ""
            cur_val = str(val)
            if len(cur_val) == '' or cur_val == 'nan':
                cur_val = default_val
            item_str = item_str.replace("{{%s}}" % str(key), cur_val)
        out_md_str += item_str
    out_md_str += "</div>\n"

with open("../pages/events.md", 'w') as f:
    f.write(out_md_str)
