from os import getenv

class SwaggerConfig:
    SWAGGER_URL = getenv('SWAGGER_URL')
    API_URL = getenv('API_URL')