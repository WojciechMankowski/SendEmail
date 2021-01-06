import jinja2
class Message:
    def __init__(self):
        tamplet_loader = jinja2.FileSystemLoader(searchpath="./")
        self.tamplet_env = jinja2.Environment(loader=tamplet_loader)
        self.tamplet = self.tamplet_env.get_template(self.TEMPLET_FILE)
    def render(self, **kwargs):
        return self.tamplet.render(**kwargs)

class Welcome(Message):
    TEMPLET_FILE = "./temp/welcome.html"