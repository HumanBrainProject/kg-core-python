#  Copyright 2018 - 2021 Swiss Federal Institute of Technology Lausanne (EPFL)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0.
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  This open source software code was developed in part or in whole in the
#  Human Brain Project, funded from the European Union's Horizon 2020
#  Framework Programme for Research and Innovation under
#  Specific Grant Agreements No. 720270, No. 785907, and No. 945539
#  (Human Brain Project SGA1, SGA2 and SGA3).
#
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from setuptools import setup

long_description = "KG core python is a client library to access the EBRAINS KG core API."

setup(
    name='kg_core',
    version='3.0.0',
    packages=['kg_core'],
    install_requires=['requests'],
    author='EBRAINS',
    scripts=[],
    author_email = 'kg@ebrains.eu',
    keywords = ['EBRAINS', 'Knowledge Graph', 'KG'],
    classifiers = [],
    url = 'https://github.com/HumanBrainProject/kg-core-python',
    download_url = 'https://github.com/HumanBrainProject/kg-core-python/archive/master.zip',
    long_description = long_description
)
