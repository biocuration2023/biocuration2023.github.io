---
layout: default
title: Schedule
permalink: /schedule
---
All times are given in Central European Summer Time (CEST) using the standard 24 hour clock.
⚡ denotes a lightning talk (10 minutes, including Q&A). 🎞️ denotes a long talk (20 minutes, including Q&A).

See [here](workshops) for information about pre-conference workshops, occurring both on Sunday evening (the day before the
conference) and on Monday (the morning before the conference).

{% for day in site.data.sessions %}

# {{ day.day}}, {{ day.date }}

{% for session in day.sessions %}

## {{ session.title }}

<dl>
<dt><strong>Location</strong></dt>
<dd>{{ session.room }}</dd>
<dt><strong>Time</strong></dt>
<dd>{{ session.start }}-{{ session.end }}</dd>
{% if session.chairs %}
<dt><strong>Session Chairs</strong></dt>
<dd>
{% for chair in session.chairs %}
    <a href="./organizers#{{ chair.orcid }}">{{ chair.personLabel }}</a>{% if forloop.last == false %}, {% endif %}
    <!--(<a href="https://orcid.org/{{ chair.orcid }}">https://orcid.org/{{ chair.orcid }}</a>)-->
    
{% endfor %}
</dd>
{% endif %}
</dl>

{% if session.talks %}
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
{% endif %}

{% endfor %}
<hr>
{% endfor %}
