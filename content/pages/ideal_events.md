title: Ideal template for Events
save_as: ideal_events.html


<div class="container">
<div class="row display-flex">

    <div class="row row-striped">
        <div class="col-xs-2 col-md-2 text-right">
            <h1 class="display-4"><span class="badge badge-secondary">
                23
            </span></h1>
            <h2>OCT</h2>
        </div>
        <div class="col-xs-10 col-md-10">
            <h3 class="text-uppercase"><strong>
                Ice Cream Social
            </strong></h3>
            <ul class="list-inline">
                <li class="list-inline-item"><i class="fa fa-calendar-o" aria-hidden="true"></i> Monday</li>
                <li class="list-inline-item"><i class="fa fa-clock-o" aria-hidden="true"></i> 12:30 PM - 2:00 PM</li>
                <li class="list-inline-item"><i class="fa fa-location-arrow" aria-hidden="true"></i> Cafe</li>
            </ul>
            <p>Lorem ipsum dolsit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
            <button type="button" class="btn btn-primary btn-xs"
                    onclick="
                    d=new Date('2018-10-03T12:00:00PM');
                    downloadICS('MyTitle', 'Halligan 102',d, 60);">
                Download .ICS
            </button>


        </div>

</div>
</div>

<!--
                onclick="my_alert('hello');">
                            onclick="downloadICS(
                            'MyTitle', 'Halligan 102',
                            new Date('2018/10/04 12:30', 60);">
-->

