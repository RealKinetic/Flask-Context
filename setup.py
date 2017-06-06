import os.path

from pip.req import parse_requirements
from setuptools import find_packages, setup


def get_meta():
    meta = {}

    execfile(os.path.join('flask_context', '__about__.py'), {}, meta)

    with open('README.md', 'rb') as fp:
        meta['long_description'] = fp.read().strip()

    return meta


def get_requirements(filename):
    try:
        from pip.download import PipSession

        session = PipSession()
    except ImportError:
        session = None

    reqs = parse_requirements(filename, session=session)

    return [str(r.req) for r in reqs]


meta = get_meta()


setup_args = dict(
    name='Flask-Context',
    version=meta['version'],
    maintainer='Nick Joyce',
    maintainer_email='nick.joyce@realkinetic.com',
    description=meta['description'],
    long_description=meta['long_description'],
    url='https://github.com/RealKinetic/Flask-Context',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    tests_require=get_requirements('requirements_dev.txt'),
)


if __name__ == '__main__':
    setup(**setup_args)
