---
layout: default
title: Sessions
permalink: /sessions
---
All times are given in Central European Summer Time (CEST) using the standard 24 hour clock.
⚡ denotes a lightning talk (10 minutes, including Q&A). 🎞️ denotes a long talk (20 minutes, including Q&A).

{% for session in site.data.schedule %}

## {{ session.title }} ({{ session.day }}, {{ session.start }}-{{ session.end }})

<table>
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
</table>
{% endfor %}
