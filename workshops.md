---
layout: default
title: Workshops
permalink: /workshops
---
The Biocuration 2023 will be hosting {{ site.data.workshops | size }} workshops. While most precede
the mainline conference agenda, the *Careers in Biocuration* workshop hosted by the ISB will be
during the main agenda of the final day of the conference.  Here's a quick look:

<table>
<thead>
<tr>
<th>Name</th>
<th>Date (2023)</th>
<th>Time (CEST)</th>
</tr>
</thead>
<tbody>
{% for record in site.data.workshops %}
<tr>
<td><a href="#{{ record.key }}">{{ record.title }}</a></td>
<td>{{ record.date }}</td>
<td>{{ record.start }} - {{ record.end }}</td>
</tr>
{% endfor %}
</tbody>
</table>

{% for record in site.data.workshops %}

<a name="{{ record.key }}"></a>

## {{ record.title }}

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

{% endfor %}
