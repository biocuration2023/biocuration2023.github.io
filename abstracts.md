---
layout: default
title: Abstracts
permalink: /abstracts
---
## Long Talks

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
