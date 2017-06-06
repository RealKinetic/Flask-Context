__all__ = [
    'description',
    'version',
    'version_info',
]

version_info = (0, 1)
version = '.'.join(map(str, version_info))

description = (
    'Provide an arbitrary context object to Flask. Useful for microservice '
    'environments.'
)
