from setuptools import setup, Extension
import os

setup_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_directory, 'README.md')) as readme_file:
    long_description = readme_file.read()

define_macros = []
py_limited_api = False
if os.getenv('LIMITED'):
    define_macros = [('Py_LIMITED_API', 0x03070000)]
    py_limited_api = True


setup(
    name='eval_string',
    version='0.0.1',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aforren1/',
    author='Alexander Forrence',
    author_email='alex.forrence@gmail.com',
    license='BSD 3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    ext_modules = [Extension('eval_string', ['eval_string.c'],
                             define_macros = define_macros,
                             py_limited_api= py_limited_api)]
)