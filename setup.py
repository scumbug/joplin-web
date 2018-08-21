from setuptools import setup, find_packages
from joplin_web import __version__ as version

install_requires = [
    'django-filter==2.0.0',
    'djangorestframework==3.8.2',
    'Markdown==2.6.11',
    'django-environ==0.4.5',
]

setup(
    name='joplin_web',
    version=version,
    description='Joplin Webapp',
    author='FoxMaSk',
    maintainer='FoxMaSk',
    author_email='foxmask@protonmail.com',
    maintainer_email='foxmask@protonmail.com',
    url='https://github.com/foxmask/joplin_web',
    download_url="https://github.com/foxmask/joplin_web/archive/joplin_web-" + version + ".zip",
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Database',
    ],
    install_requires=install_requires,
    include_package_data=True,
)
