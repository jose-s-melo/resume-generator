from jinja2 import Environment, FileSystemLoader

def render_template(data, template_name="basic.html"):
   
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template(template_name)
    
    return template.render(data)