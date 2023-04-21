# Biocuration 2023

Assets for the 16th Annual International Biocuration Conference (Biocuration 2023),
organized with support from the [International Society of Biocuration](https://www.biocuration.org).

- [Information about the organizers](https://query.wikidata.org/embed.html#%23%2B%20summary%3A%20A%20query%20for%20the%20ISB2023%20organizing%20committee%20and%20scientific%20program%20committeee%0A%23%2B%20endpoint%3A%20https%3A%2F%2Fquery.wikidata.org%2Fsparql%0A%23%2B%20tags%3A%0A%23%2B%20%20%20-%20conference%0A%23%2B%20%20%20-%20bibliometrics%0A%23defaultView%3ATable%0A%0ASELECT%20%0A%20%20%3Fperson%20%3FpersonLabel%20%3FpersonDescription%20%3FgenderLabel%20%3Fimage%0A%20%20%3FnationalityLabel%20%3Forcid%20%3Flinkedin%20%3Ftwitter%20%3Fgscholar%20%3Fgithub%0A%20%20(GROUP_CONCAT(DISTINCT%20%3Ftopic_label%3B%20separator%3D%22%2C%20%22)%20AS%20%3Ftopics)%0A%20%20(MAX(%3Fstart_date)%20as%20%3Fmax_start_date)%0A%20%20(SAMPLE(%3FemployerLabel)%20as%20%3FemployerLabel_)%0AWHERE%20%0A%7B%0A%20%20wd%3AQ111430238%20wdt%3AP664%7Cwdt%3AP5804%20%3Fperson%20.%0A%20%20%3Fperson%20wdt%3AP496%20%3Forcid%20.%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP18%20%3Fimage%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP21%20%3Fgender%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP2002%20%3Ftwitter%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP27%20%3Fnationality%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP6634%20%3Flinkedin%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP1960%20%3Fgscholar%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP2037%20%3Fgithub%20.%20%7D%0A%20%20OPTIONAL%20%7B%20%3Fperson%20wdt%3AP101%20%3Ftopic%20.%20%3Ftopic%20rdfs%3Alabel%20%3Ftopic_label%20.%20FILTER%20(LANG(%3Ftopic_label)%20%3D%20'en')%20%7D%0A%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%3Fperson%20p%3AP108%20%3Fstatement%20.%0A%20%20%20%20%3Fstatement%20ps%3AP108%20%3Femployer%20.%0A%20%20%20%20%3Femployer%20rdfs%3Alabel%20%3FemployerLabel%0A%20%20%20%20filter(lang(%3FemployerLabel)%20%3D%20%22en%22)%0A%20%20%20%20OPTIONAL%20%7B%20%0A%20%20%20%20%20%20%3Fstatement%20pq%3AP580%20%3Fstart_date%20.%20%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%20%23%20Helps%20get%20the%20label%20in%20your%20language%2C%20if%20not%2C%20then%20en%20language%0A%7D%0AGROUP%20BY%0A%20%20%3Fperson%20%3FpersonLabel%20%3FpersonDescription%20%3FgenderLabel%20%3Fimage%0A%20%20%3FnationalityLabel%20%3Forcid%20%3Flinkedin%20%3Ftwitter%20%3Fgscholar%20%3Fgithub%0AORDER%20BY%20%3FpersonLabel%0A)

## Build

```shell
docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:latest jekyll serve
```

## Archive

[![DOI](https://zenodo.org/badge/569336825.svg)](https://zenodo.org/badge/latestdoi/569336825)

This repository is archived on Zenodo.

## Conference Booklet

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7852266.svg)](https://doi.org/10.5281/zenodo.7852266)

The conference booklet is available on Zenodo.

## License

This repository is licensed under the CC0 1.0 license.
