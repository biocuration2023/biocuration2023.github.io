---
layout: default
title: Abstracts
permalink: /abstracts
---

## Long Talks

Long talks are given 20 minutes to present, including questions. We suggest limiting your talk to 15 minutes and leaving
5 minutes for questions.

<ol>
{% for record in site.data.oral %}
<li style="margin-top: 1em">
<span style="font-weight: bold">{{ record.title }}</span>
<br />
<span style="color:#111">{% for author in record.authors %}<span>{{ author.label }}</span>{% unless forloop.last %}, {% endunless %}{% endfor %}</span>
<details>
<summary>Expand the abstract</summary>
<blockquote style="text-align: justify">
{{ record.abstract }}
</blockquote>
</details>
</li>
{% endfor %}
</ol>

## Short Talks

Short talks are given 10 minutes to present, including questions. We suggest limiting your talk to 7 minutes and leaving
3 minutes for questions. We recommend your talk is no more than 5 or 6 slides, excluding title, acknowledgements, and
other housekeeping.

<ol>
{% for record in site.data.lightning %}
<li style="margin-top: 1em">
<span style="font-weight: bold">{{ record.title }}</span>
<br />
<span style="color:#111">{% for author in record.authors %}<span>{{ author.label }}</span>{% unless forloop.last %}, {% endunless %}{% endfor %}</span>
<details>
<summary>Expand the abstract</summary>
<blockquote style="text-align: justify">
{{ record.abstract }}
</blockquote>
</details>
</li>
{% endfor %}
</ol>

## Poster Presentations

There will be two back-to-back poster presentation sessions for 1 hour each Posters should be at a maximum 90cm wide and
100-110cm tall. Poster boards and materials for hanging posters will be provided. We suggest that posters include a QR
code that viewers can scan that either link to a downloadable version of the poster or other relevant resources.

<ol>
{% for record in site.data.poster %}
<li style="margin-top: 1em">
<span style="font-weight: bold">{{ record.title }}</span>
<br />
<span style="color:#111">{% for author in record.authors %}<span>{{ author.label }}</span>{% unless forloop.last %}, {% endunless %}{% endfor %}</span>
<details>
<summary>Expand the abstract</summary>
<blockquote style="text-align: justify">
{{ record.abstract }}
</blockquote>
</details>
</li>
{% endfor %}
</ol>
