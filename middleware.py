import settings

class Auth(object):
    """WSGI middleware for collecting site usage
    """
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        
        if 'X-Forwarded-For' in environ:
            if environ.get('X-Forwarded-For') not in settings.ALLOWED_IP:
                raise Exception('nop')
        elif environ.get("REMOTE_ADDR") not in settings.ALLOWED_IP:
            raise Exception('nop')

        return self.app(environ, start_response)