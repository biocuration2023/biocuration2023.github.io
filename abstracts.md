---
layout: default
title: Abstracts
permalink: /abstracts
---

## Keynotes

Keynote speakers have been invited and are given about 60 minutes to present, including introductions and questions.
We suggest limiting your talk to 40-45 minutes and leaving 15 minutes for questions.

<ul>
{% for record in site.data.keynotes %}
<li style="margin-top: 1em">
<span style="font-weight: bold">{{ record.title }}</span>
<br />
<span style="color:#111">{{ record.name }}, {% if record.position %}{{ record.position}} at {% endif %}{{ record.affiliation }}</span>
<details>
<summary>Expand the abstract</summary>
<blockquote style="text-align: justify">
{{ record.abstract }}
</blockquote>
</details>
</li>
{% endfor %}
</ul>

## Long Talks

Long talks are given 20 minutes to present, including questions. We suggest limiting your talk to 15 minutes and leaving
5 minutes for questions.

<ul>
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
</ul>

## Short Talks

Short talks are given 10 minutes to present, including questions. We suggest limiting your talk to 7 minutes and leaving
3 minutes for questions. We recommend your talk is no more than 5 or 6 slides, excluding title, acknowledgements, and
other housekeeping.

<ul>
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
</ul>

## Poster Presentations

There will be two back-to-back poster presentation sessions for 1 hour each. Even-numbered posters will be presented
in the first poster session (Tuesday, April 25th from 16.00-17.00 CEST) and odd-numbered posters swill be presented
in the second poster session (Tuesday, April 25th from 17.00-18.00 CEST).

Posters should be printed and brought to the venue by the presenter with a maximum width fof 90cm and height of
100-110cm. Poster boards and materials for hanging posters will be provided. Poster can be hung immediately following
registration.

We suggest that posters include a QR code that viewers can scan that either link to a downloadable version of the poster
or other relevant resources.

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
