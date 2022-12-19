import typer

from fermigier_com import watcher, builder

app = typer.Typer()


@app.command()
def build():
    builder.build()


@app.command()
def watch():
    watcher.watch()


if __name__ == "__main__":
    app()
