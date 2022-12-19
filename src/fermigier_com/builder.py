import shutil
from pathlib import Path

import yaml
from devtools import debug
from jinja2 import Environment, PackageLoader, select_autoescape
from markdown import markdown


class Builder:
    def __init__(self, **kw):
        self.jinja_env = Environment(
            loader=PackageLoader("fermigier_com"), autoescape=select_autoescape()
        )
        self.posts: list[dict] = []
        self.pages: list[dict] = []
        self.tags: dict = {}

    def scan(self):
        for file in Path("blog").glob("*.md"):
            post = self._parse_file(file)
            self.posts.append(post)

        for file in Path("pages").glob("*.md"):
            page = self._parse_file(file)
            self.pages.append(page)

    def _parse_file(self, file):
        with file.open() as fd:
            content = fd.read()
        t = content.split("---", 2)
        body = t[2]
        metadata = yaml.safe_load(t[1])
        page = {}
        page["metadata"] = metadata
        page["body"] = body
        page["id"] = file.stem
        return page

    def build(self):
        if Path("dist").exists():
            shutil.rmtree("dist")

        self.build_static()
        self.build_blog()
        self.build_pages()

    def build_static(self):
        shutil.copytree("static", "dist")
        shutil.copytree("assets", "dist/assets")

    def build_blog(self):
        for post in self.posts:
            self.make_post(post)

        self.make_blog_index()
        # for tag in self.tags:
        #     self.make_tag(tag)

    def make_post(self, post):
        post["title"] = post["metadata"]["title"]
        post["date"] = post["metadata"]["date"]
        post["body_html"] = markdown(post["body"])
        post["tags"] = [
            {"name": tag, "url": f"/blog/tags/{tag.lower()}"}
            for tag in post["metadata"].get("tags", [])
        ]
        for tag in post["tags"]:
            self.tags.setdefault(tag["name"], []).append(post)

        template = self.jinja_env.get_template("blog_post.j2")
        result = template.render(post=post)
        path = post["metadata"]["path"]
        assert path.startswith("/")
        dir_path = Path("dist") / path[1:]
        dir_path.mkdir(parents=True, exist_ok=True)
        with (dir_path / "index.html").open("w") as fd:
            fd.write(result)

    def build_pages(self):
        for page in self.pages:
            self.make_page(page)

    def make_page(self, page):
        page["title"] = page["metadata"]["title"]
        page["body_html"] = markdown(page["body"])

        template_name = page["metadata"].get("template", "page.j2")
        template = self.jinja_env.get_template(template_name)
        result = template.render(page=page)
        if page["id"] == "home-about":
            dir_path = Path("dist")
        else:
            dir_path = Path("dist") / page["id"]
        dir_path.mkdir(parents=True, exist_ok=True)
        with (dir_path / "index.html").open("w") as fd:
            fd.write(result)

    def make_blog_index(self, tag=None):
        posts = [post for post in self.posts]
        posts.sort(key=lambda post: post["date"], reverse=True)
        if len(posts) > 10:
            posts = posts[:10]
        template = self.jinja_env.get_template("blog_index.j2")
        result = template.render(posts=posts)
        dir_path = Path("dist/blog")
        dir_path.mkdir(parents=True, exist_ok=True)
        with (dir_path / "index.html").open("w") as fd:
            fd.write(result)


def build():
    builder = Builder()
    builder.scan()
    builder.build()
