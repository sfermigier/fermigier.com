from datetime import datetime
from pathlib import Path

import typer
from markdown.extensions.toc import slugify

from fermigier_com import watcher, builder

app = typer.Typer()


@app.command()
def build():
    builder.build()


@app.command()
def watch():
    watcher.watch()


@app.command()
def new(title: str):
    slug = slugify(title, separator="-")
    date = datetime.now().strftime("%Y-%m-%d")
    path = datetime.now().strftime("blog/%Y/%m/" + slug + ".md")

    draft = Path(__file__).parent / "drafts" / "post.md"
    ctx = {
        "date": date,
        "title": title,
        "path": "/" + path,
    }
    with draft.open() as fd:
        content = fd.read()
        content = content.format(**ctx)

    dest = Path(path)
    dest_dir = dest.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    with dest.open("w") as fd:
        fd.write(content)


if __name__ == "__main__":
    app()
