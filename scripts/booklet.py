"""Generate the conference booklet."""

import os
from pathlib import Path

import click
import yaml
import zenodo_client
from jinja2 import Environment, FileSystemLoader
from zenodo_client import Creator, Metadata

HERE = Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
DATA = ROOT.joinpath("_data")
BOOKLET = ROOT.joinpath("booklet")
BOOKLET.mkdir(exist_ok=True)
OUTPUT_MD = BOOKLET.joinpath("biocuration2023.md")
OUTPUT_DOCX = BOOKLET.joinpath("biocuration2023.docx")
OUTPUT_PDF = BOOKLET.joinpath("biocuration2023.pdf")
environment = Environment(
    autoescape=True, loader=FileSystemLoader(HERE), trim_blocks=True, lstrip_blocks=True
)
template = environment.get_template("booklet.md")


def main():
    text = template.render(
        posters=yaml.safe_load(DATA.joinpath("poster.yml").read_text()),
        keynotes=yaml.safe_load(DATA.joinpath("keynotes.yml").read_text()),
        orals=yaml.safe_load(DATA.joinpath("oral.yml").read_text()),
        lightning=yaml.safe_load(DATA.joinpath("lightning.yml").read_text()),
        organizers=yaml.safe_load(DATA.joinpath("organizing_committee.yml").read_text()),
        program_committee=yaml.safe_load(DATA.joinpath("program_committee.yml").read_text()),
        sponsors=yaml.safe_load(DATA.joinpath("sponsors.yml").read_text()),
        workshops=yaml.safe_load(DATA.joinpath("workshops.yml").read_text()),
        sessions=yaml.safe_load(DATA.joinpath("sessions.yml").read_text()),
    )
    click.echo("Writing markdown")
    OUTPUT_MD.write_text(text)

    # Thanks to the following for figuring out parsing HTML
    # https://tex.stackexchange.com/questions/631243/how-to-render-html-tables-in-markdown-using-pandoc

    # click.echo("Writing microsoft word")
    # os.system(f"pandoc -f markdown_mmd+multiline_tables -s --pdf-engine=xelatex --lua-filter=parse-html.lua --from=markdown-markdown_in_html_blocks -o {OUTPUT_DOCX} {OUTPUT_MD}")
    click.echo("Writing pdf")
    os.system(
        f"pandoc -f markdown_mmd+multiline_tables -s --pdf-engine=xelatex --lua-filter=parse-html.lua --from=markdown-markdown_in_html_blocks -o {OUTPUT_PDF} {OUTPUT_MD}"
    )

    metadata = Metadata(
        title="Biocuration 2023 Conference Booklet",
        upload_type="dataset",
        description="A description of organizers, sponsors, speakers, and the schedule of the "
                    "Biocuration 2023 Conference in Padua, Italy from April 23-26th, 2023.",
        creators=[
            Creator(
                name="Hoyt, Charles Tapley",
                affiliation="Harvard Medical School",
                orcid="0000-0003-4423-4370",
            ),
        ],
    )
    zenodo_client.ensure_zenodo(
        key="biocuration2023",
        data=metadata,
        paths=OUTPUT_PDF,
    )


if __name__ == "__main__":
    main()
