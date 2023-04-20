![](../img/cover.png)

\pagebreak

# Welcome

We wish you a warm welcome to Padua for the 16th Annual International Biocuration Conference (Biocuration 2023): a forum
for curators, developers, and users of clinical and life sciences data, knowledge, and models to discuss their work,
promote collaboration, and foster the community around this active and growing area of research. We are delighted to see
participation from academia, government, and industry as well as diverse interest in the tools, methodology, and
philosophy of curation that will surely lead to memorable and forward-looking conversations and experiences at the
conference.

We would like to take this opportunity to thank our sponsors, who have been integral towards the execution of the
conference and many of its events. We thank the journal DATABASE for hosting a virtual issue corresponding to the
conference (https://academic.oup.com/database/pages/biocuration_virtual_issue). We thank F1000 researchers for providing
a platform for publishing posters and oral presentations (https://f1000research.com/collections/biocuration).

Finally, we would like to thank the International Society of Biocuration (ISB) for its support. The ISB is a non-profit
organization for curators, developers, and researchers with an interest in biocuration. The society promotes the field
of biocuration and provides a forum for information exchange through meetings and workshops.

We hope that by attending this meeting, you too will feel welcomed into our biocuration community.

Best wishes,
The Biocuration 2023 Organizing Committee

\pagebreak

# Organizers

Contact the organizers at any of:

- Email: <a href="mailto:biocuration2023@gmail.com">biocuration2023@gmail.com</a>
- Twitter: [@biocuration2023](https://twitter.com/biocuration2023)
- Mastodon: [@biocuration2023@genomic.social](https://genomic.social/@biocuration2023)

## Organizing Committee

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Affiliation</th>
        <th>ORCID</th>
        <th>Twitter</th>
    </tr>
</thead>
<tbody>
{% for person in organizers %}
<tr>
<th role="rowheader">{{ person.personLabel }}{% if person.note %}†{% endif %}</th>
<td>{{ person.employerLabel_ }}</td>
<td>
<a href="https://bioregistry.io/orcid:{{ person.orcid }}">
        {{ person.orcid }}
    </a>
</td>
<td>
{% if person.twitter %}
    <a href="https://twitter.com/{{ person.twitter }}" style="margin: 0 0.5rem;">
        @{{ person.twitter }}
    </a>
    {% endif %}
</td>
</tr>
{% endfor %}
</tbody>
</table>

† Committee Chair

## Scientific Program Committee

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Affiliation</th>
        <th>ORCID</th>
        <th>Twitter</th>
    </tr>
</thead>
<tbody>
{% for person in program_committee %}
<tr>
<th role="rowheader">{{ person.personLabel }}{% if person.note %}†{% endif %}</th>
<td>{{ person.employerLabel_ }}</td>
<td>
<a href="https://bioregistry.io/orcid:{{ person.orcid }}">
        {{ person.orcid }}
    </a>
</td>
<td>
{% if person.twitter %}
<a href="https://twitter.com/{{ person.twitter }}" style="margin: 0 0.5rem;">
    @{{ person.twitter }}
</a>
{% endif %}
</td>
</tr>
{% endfor %}
</tbody>
</table>

† Committee Chair

\pagebreak

# General Information

## Conference Badges

Please wear your name badges at all times to promote networking and to assist staff in identifying you.

## Social Media Policy

To encourage the open communication of science and biocuration, we would like to support the use of social media at this
year’s conference. Please use the conference hashtag #biocuration2023 either on Mastodon or Twitter. For poster
sessions, please check with the presenter to obtain permission for sharing their work.

## Poster Sessions

Two consecutive poster sessions will be held on Tuesday, April 25th. The first poster session from 16.00-17.00 will
feature even-numbered posters. The second poster session from 17.00-18.00 will feature odd-numbered posters. Abstracts
can be found at [https://biocuration2023.github.io/abstracts](https://biocuration2023.github.io/abstracts).

## Social Events

Please
visit [https://biocuration2023.github.io/social](https://biocuration2023.github.io/social) for more details.

## Ground Transportation

Please find a list of local taxi numbers below:

- RadioTaxi (+39 049.651333; https://www.taxipadova.it/services/radiotaxi/)
- AppTaxi (https://apptaxi.it/en/padua/)
- Padua Taxi (+39 049 4906001; https://padova-taxi.it/)

Note that Uber and Lyft are not available in Padua.

Bike riding is very common in Padua, and we recommend this bike sharing app:
[RideMovi](https://www.ridemovi.com/cities/)

Padua's tourism website has links to public transport info, as well as car sharing service and other bicycle
sharing/rental options. Please visit [Moving around Padua](https://www.turismopadova.it/en/getting-around-padua/) for
more details.

\pagebreak

# Sponsors

Biocuration 2023 is proudly sponsored by the following organizations. Additional information can be found
at https://biocuration2023.github.io/sponsors:

{% for record in sponsors %}

## {{ record.name }}

[{{ record.link }}]({{ record.link }})

![](../{{ record.image_local }})

{% if loop.index % 2 == 0 %}\pagebreak{% endif %}

{% endfor %}

\pagebreak

# Schedule

Additional information on the schedule can be found at https://biocuration2023.github.io/schedule.

{% for day in sessions %}

## Day {{ loop.index}}: {{ day.day }}, {{ day.date }}

{% for session in day.sessions %}

### {{ session.title }} ({{ session.start }}-{{ session.end }})

{%- if session.description %}{{ session.description }}{% endif %}

<dl>
{% if session.chairs %}
    <dt><strong>Chairs</strong></dt>
    <dd>
    {% for chair in session.chairs %}
    <a href="https://orcid.org/{{ chair.orcid }}">{{ chair.personLabel }}</a>{% if not loop.last %}, {% endif %}
    {% endfor %}
    </dd>
{% endif %}
{% if session.talks %}
{% for talk in session.talks %}
<dt></dt>
<dt>{{ talk.time_start }}-{{ talk.time_end }}</dt>
<dd>
<br/><strong>
{{ talk.title }}</strong><br/>
{{ talk.speaker }}
</dd>
{% endfor %}
{% endif %}
</dl>

{% endfor %}

{% if loop.index != 1 %}\pagebreak{% endif %}

{% endfor %}

# Workshops

{% for record in workshops %}

## {{ record.title | safe }}

<table>
<tr>
<td>Date</td>
<td>{{ record.date }} ({{ record.day }})</td>
</tr>
<tr>
<td>Time</td>
<td>{{ record.start }} - {{ record.end }} ({{ record.length }})</td>
</tr>
{% for organizer in record.organizers %}
<tr>
<td>Organizer</td>
<td>
    <a href="https://orcid.org/{{ organizer.orcid }}">{{ organizer.name }}</a>
    {%- if organizer.affiliation %}, {{ organizer.affiliation }}{% endif %}
</td>
</tr>
{% endfor %}
</table>

{{ record.abstract }}

\pagebreak

{% endfor %}

# Keynotes

{% for record in keynotes %}

## {{ record.title }}

{{ record.name }}, {% if record.position %}{{ record.position}} at {% endif %}{{ record.affiliation }}

### About

{{ record.description }}

### Abstract

{{ record.abstract }}

\pagebreak

{% endfor %}

# Oral Presentations

## Long Talks

{% for record in orals %}

### {{ record.title }}

{% for author in record.authors %}
<span{% if loop.first%} style="font-weight:bold"{% endif %}>{{ author.label }}</span>{% if not loop.last %}, {% endif%}
{% endfor %}
<br />

{{ record.abstract }}

\pagebreak

{% endfor %}

## Lightning Talks

{% for record in lightning %}

### {{ record.title }}

{% for author in record.authors %}
<span>{{ author.label }}</span>{% if not loop.last %}, {% endif%}
{% endfor %}
<br />

{{ record.abstract }}

\pagebreak

{% endfor %}

# Posters

{% for record in posters %}

## {{loop.index}}. {{ record.title }}

{% for author in record.authors %}
<span>{{ author.label }}</span>{% if not loop.last %}, {% endif%}
{% endfor %}
<br />

{{ record.abstract }}

\pagebreak

{% endfor %}

