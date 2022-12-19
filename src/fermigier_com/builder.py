import shutil
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape

from fermigier_com.page import Post, Page

PACKAGE = "fermigier_com"


class Builder:
    def __init__(self, **kw):
        self.jinja_env = Environment(
            loader=PackageLoader(PACKAGE), autoescape=select_autoescape()
        )
        self.posts: list[Post] = []
        self.pages: list[Page] = []
        self.tags: dict = {}

    def scan(self):
        for path in Path("blog").glob("*.md"):
            post = Post(path)
            self.posts.append(post)

        for path in Path("pages").glob("*.md"):
            page = Page(path)
            self.pages.append(page)

    def build(self):
        if Path("dist").exists():
            shutil.rmtree("dist")

        self.build_static()
        self.build_blog()
        self.build_pages()

    def build_static(self):
        shutil.copytree("static", "dist")
        shutil.copytree("assets", "dist/assets")

    # Blog

    def build_blog(self):
        for post in self.posts:
            post.build(self)

            for tag in post.tags:
                self.tags.setdefault(tag["name"], []).append(post)

        self.make_blog_index()

        for tag in self.tags:
            self.make_blog_index(tag)

    def make_blog_index(self, tag=None):
        posts = [post for post in self.posts]
        posts.sort(key=lambda post: post["date"], reverse=True)

        if tag:
            posts = [post for post in posts if tag in post["tags"]]
            dest_path = Path(f"dist/blog/tag/{tag}/index.html")
            title = f"Blog - Tag: {tag}"
        else:
            dest_path = Path("dist/blog/index.html")
            title = "Blog"

        if len(posts) > 10:
            posts = posts[:10]

        template = self.jinja_env.get_template("blog_index.j2")
        result = template.render(posts=posts, title=title)

        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with dest_path.open("w") as fd:
            fd.write(result)

    # Regular pages

    def build_pages(self):
        for page in self.pages:
            page.build(self)


def build():
    builder = Builder()
    builder.scan()
    builder.build()
