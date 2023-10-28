from fastapi.templating import Jinja2Templates
import config

Jinja2 = Jinja2Templates(directory=config.Jinja2directory)

def response(path, values):
    """
    输出模板
    """
    return Jinja2.TemplateResponse(path, values)