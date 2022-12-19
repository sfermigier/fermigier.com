import shutil
from datetime import datetime
from pathlib import Path

import typer
from markdown.extensions.toc import slugify

from fermigier_com import watcher, builder
from fermigier_com.page import Post

app = typer.Typer()


@app.command()
def build():
    builder.build()


@app.command()
def watch():
    watcher.watch()


# @app.command()
# def migrate():
#     for path in Path("blog").glob("*.md"):
#         post = Post(path)
#         url = post.url[1:]
#         if not url.endswith(".md"):
#             url = url + ".md"
#         dest = Path(url)
#         dest_dir = dest.parent
#         dest_dir.mkdir(parents=True, exist_ok=True)
#         shutil.copy(path, dest)


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
