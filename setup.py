#
#    Copyright 2012 Talis Systems Ltd
# 
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
# 
#        http://www.apache.org/licenses/LICENSE-2.0
# 
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
from setuptools import setup
import os, re
name = 'lsi'
version_number_re = "\s*__version__\s*=\s*((\"([^\"]|\\\\\")*\"|'([^']|\\\\')*'))"
version_file = os.path.join(os.path.dirname(__file__), name, '__init__.py')
version_number = re.search(version_number_re, open(version_file).read()).groups()[0][1:-1]

setup(
    name = name,
    version = version_number,
    description = 'Linked Spatial Data Indexing',
    author='William Waites',
    author_email='ww@kasabi.com',
    url='https://github.com/kasabi/linkedspatialindex',
    classifiers=['Programming Language :: Python','License :: Public Domain', 'Operating System :: OS Independent', 'Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Database'],
    packages=['lsi'],
    install_requires=['Rtree', 'rdflib-rdfjson', 'Werkzeug', 'autoneg', 'python-daemon', 'shapely', 'geojson', 'acora'],
    entry_points="""
    [console_scripts]
    lsi = lsi.service:run_service
    """
)
