'''
'''

import pandas as pd
import datetime

today_timestamp = datetime.datetime.today().strftime('%Y-%m-%d')

## TODO to add more event sections just update this list
event_files = [
    ('Fall 2018', 'events_2018_fall.csv')
    ]

main_item_template_str = \
"""
    <div class="row row-striped">
        <div class="col-2 text-right">
            <h1 class="display-4"><span class="badge badge-secondary">
                {{DAY_OF}}
            </span></h1>
            <h2>{{MONTH_NAME}}</h2>
        </div>
        <div class="col-10">
            <h3>
            <a href="{{URL}}">
                <strong>
                    {{TYPE}}: {{TITLE}}
                </strong>
            </a>
            </h3>
            <ul class="list-inline">
                <li class="list-inline-item"><i class="fa fa-calendar-o" aria-hidden="true"></i>{{DATE}}</li>
                <li class="list-inline-item"><i class="fa fa-clock-o" aria-hidden="true"></i> {{TIME}} </li>
                <li class="list-inline-item"><i class="fa fa-location-arrow" aria-hidden="true"></i>{{LOCATION}}</li>
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


We keep a short list of events relevant to machine learning here.

For the latest information about these events, click the links below or see the primary source: <a href="https://engineering.tufts.edu/cs/events">Tufts CS Events Webpage</a>

\n""")



for title, fpath in event_files:

    csv_df = pd.read_csv(fpath, dtype={'DAY_OF':'str'})
    csv_df = csv_df.fillna('') # Fill missing values with blanks
    assert csv_df.shape[0] > 0

    anchor = title.lower().replace(' ', '-')
    out_md_str += "\n<h2><a name='%s'>Events: %s</a></h2>" % (anchor, title)

    ## Main team names, images, + links
    out_md_str += '\n\n\n<div class="container">'
    for item_id, row_obj in enumerate(csv_df.itertuples()):
        row_dict = row_obj.__dict__
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