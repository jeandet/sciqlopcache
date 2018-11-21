from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/php/rest/auth.php')
    config.add_route('getParameter', '/php/rest/getParameter.php')
    config.add_route('data', 'data/*file')
    config.scan()
    return config.make_wsgi_app()
