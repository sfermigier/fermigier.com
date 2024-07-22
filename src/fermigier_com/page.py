from pathlib import Path

import yaml
from markdown_it import MarkdownIt


class Page:
    id: str
    metadata: dict
    tags: list[dict]
    body: str = ""
    # body_html: str = ""

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
            self._body_html = parse_markdown(self.body)
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
        self.write(result)

    def render(self, builder):
        template_name = self.metadata.get("template", self.default_template)
        template = builder.jinja_env.get_template(template_name)
        ctx = self.render_ctx(builder)
        result = template.render(**ctx)
        return result

    def render_ctx(self, builder):
        return {"page": self, "posts": builder.posts}

    def write(self, result):
        dir_path = self.dest_path.parent
        dir_path.mkdir(parents=True, exist_ok=True)
        with self.dest_path.open("w") as fd:
            fd.write(result)


class Post(Page):
    default_template = "blog_post.j2"

    @property
    def dest_path(self):
        path = self["path"]
        assert path.startswith("/")
        return Path("dist") / path[1:] / "index.html"

    @property
    def og_data(self):
        # https://developers.facebook.com/docs/sharing/webmasters/
        data = {
            "og:type": "article",
            "og:title": self["title"],
            "og:description": self["summary"],
            "og:url": self.url,
            "og:site_name": "Fermigier.com",
            "twitter:card": "summary_large_image",
            "twitter:title": self["title"],
            "twitter:description": self["summary"],
            "twitter:site": "@sfermigier",
            "twitter:creator": "@sfermigier",
        }
        if "image" in self.metadata:
            data["og:image"] = self.metadata["image"]
            data["twitter:image"] = self.metadata["image"]
        return data

    def render_ctx(self, builder):
        return {"page": self, "post": self, "og_data": self.og_data}


def parse_markdown(src: str) -> str:
    md = (
        MarkdownIt("commonmark", {"html": True})
    )
    # md.parse(src)
    return md.render(src)
