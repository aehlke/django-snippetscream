from setuptools import setup, find_packages

setup(
    name='django-snippetscream',
    version='0.0.1',
    description='Django app packaging the best snippets found on http://djangosnippets.org',
    long_description = open('README.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='shaunsephton@gmail.com',
    url='http://github.com/shaunsephton/django-snippetscream',
    packages = find_packages(),
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)