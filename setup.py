from setuptools import setup, find_packages
from joplin_web import __version__ as version

install_requires = [
    'django-filter==2.0.0',
    'djangorestframework==3.8.2',
    'Markdown==2.6.11',
    'django-environ==0.4.5',
    'requests==2.19.1',
]

setup(
    name='joplin_web',
    version=version,
    description='Joplin Web',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important!
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmask protonmail',
    maintainer_email='foxmask protonmail',
    url='https://github.com/foxmask/joplin-web',
    download_url="https://github.com/foxmask/joplin-web/archive/joplin_web-" + version + ".zip",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Database',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
