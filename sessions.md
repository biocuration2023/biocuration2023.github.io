---
layout: default
title: Sessions
permalink: /sessions
---
All times are given in Central European Summer Time (CEST) using the standard 24 hour clock.
⚡ denotes a lightning talk (10 minutes, including Q&A). 🎞️ denotes a long talk (20 minutes, including Q&A).

See [here](workshops) for information about pre-conference workshops, occurring both on Sunday evening (the day before the
conference) and on Monday (the morning before the conference).

{% for session in site.data.sessions %}

## {{ session.title }} ({{ session.day }}, {{ session.date }}, {{ session.start }}-{{ session.end }})

<dl>
<dt><strong>Room</strong></dt>
<dd>{{ session.room }}</dd>
<dt><strong>Session Chairs</strong></dt>
{% for chair in session.chairs %}
<dd>
    <a href="./organizers#{{ chair.orcid }}">{{ chair.personLabel }}</a>
    <!--(<a href="https://orcid.org/{{ chair.orcid }}">https://orcid.org/{{ chair.orcid }}</a>)-->
</dd>
{% endfor %}
</dl>

<table>
<thead>
<tr>
<th>Time (CEST)</th>
<th>Title</th>
</tr>
</thead>
<tbody>
{% for talk in session.talks %}
<tr>
<td align="right">{{ talk.time_start }}-{{ talk.time_end }}</td>
<td>
<strong>
{% if talk.type == "lightning" %}⚡{% else %}🎞️{% endif %}
{{ talk.title }}</strong><br/>
{{talk.speaker }}<br/>
</td>
</tr>
{% endfor %}
</tbody>
</table>
{% endfor %}
