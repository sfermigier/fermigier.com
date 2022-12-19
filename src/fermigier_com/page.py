from pathlib import Path

import yaml
from markdown import markdown


class Page:
    id: str
    metadata: dict
    tags: list[dict]
    body: str = ""
    body_html: str = ""

    default_template = "page.j2"

    def __init__(self, path):
        self.id = path.stem
        self._parse(path)
        self._body_html = ""

    def _parse(self, path):
        with path.open() as fd:
            content = fd.read()

        t = content.split("---", 2)
        self.metadata = yaml.safe_load(t[1].strip())
        self.body = t[2]

        self.tags = [
            {"name": tag, "url": f"/blog/tag/{tag}"}
            for tag in self.metadata.get("tags", [])
        ]

    @property
    def url(self) -> str:
        return self["path"]

    @property
    def body_html(self) -> str:
        if not self.body:
            return ""
        if not self._body_html:
            self._body_html = markdown(self.body)
        return self._body_html

    def __getitem__(self, key):
        if key in self.metadata:
            return self.metadata[key]

        raise KeyError(key)

    @property
    def dest_path(self) -> Path:
        if self.id == "home-about":
            return Path("dist") / "index.html"
        else:
            return Path("dist") / self.id / "index.html"

    def build(self, builder):
        result = self.render(builder)
        dir_path = self.dest_path.parent
        dir_path.mkdir(parents=True, exist_ok=True)
        with self.dest_path.open("w") as fd:
            fd.write(result)

    def render(self, builder):
        template_name = self.metadata.get("template", self.default_template)
        template = builder.jinja_env.get_template(template_name)
        result = template.render(**self.render_ctx())
        return result

    def render_ctx(self):
        return {"page": self}


class Post(Page):
    default_template = "blog_post.j2"

    @property
    def dest_path(self):
        path = self["path"]
        assert path.startswith("/")
        return Path("dist") / path[1:] / "index.html"

    def render_ctx(self):
        return {"post": self}
