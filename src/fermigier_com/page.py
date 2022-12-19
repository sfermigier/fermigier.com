from pathlib import Path

import yaml
from markdown import markdown


class Page:
    def __init__(self, path):
        self.id = path.stem
        self.path = path
        self._parse()
        self.body = ""
        self.body_html = ""

    def _parse(self):
        with self.path.open() as fd:
            content = fd.read()

        t = content.split("---", 2)
        self.metadata = yaml.safe_load(t[1].strip())
        self.body = t[2]

        self.tags = [
            {"name": tag, "url": f"/blog/tags/{tag.lower()}"}
            for tag in self.metadata.get("tags", [])
        ]

    def __getitem__(self, key):
        if key == "body_html":
            if not self.body:
                return ""
            if not self.body_html:
                self.body_html = markdown(self.body)
            return self.body_html

        if key in self.metadata:
            return self.metadata[key]

        raise KeyError(key)

    @property
    def dest_path(self):
        if self.id == "home-about":
            return Path("dist") / "index.html"
        else:
            return Path("dist") / self.id / "index.html"

    def build(self, builder):
        template_name = self.metadata.get("template", "page.j2")
        template = builder.jinja_env.get_template(template_name)
        result = template.render(page=self)
        dir_path = self.dest_path.parent
        dir_path.mkdir(parents=True, exist_ok=True)
        with self.dest_path.open("w") as fd:
            fd.write(result)

class Post(Page):
    pass
