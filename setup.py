# Copyright (c) 2016, Samantha Marshall (http://pewpewthespells.com)
# All rights reserved.
#
# https://github.com/samdmarshall/pylocalizer
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# 3. Neither the name of Samantha Marshall nor the names of its contributors may
# be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

from setuptools import setup
import sys

if sys.version_info < (3,0):
    print('This tool requires at least Python 3.0. Please run `brew install python3` first.')
    sys.exit()

setup(
    name = 'pylocalizer',
    version = '0.1',
    description = 'Tool for finding missing and unused NSLocalizdStrings',
    url = 'https://github.com/samdmarshall/pylocalizer',
    author = 'Samantha Marshall',
    author_email = 'hello@pewpewthespells.com',
    license = 'BSD 3-Clause',
    packages = [
        'pylocalizer',
        'pylocalizer/Helpers',
        'pylocalizer/xcodeproj',
        'pylocalizer/xcodeproj/pbProj',
        'pylocalizer/Language',
        'pylocalizer/Executor',
        'pylocalizer/Finder',
        'pylocalizer/Reporter',
        
    ],
    entry_points = {
        'console_scripts': [ 'pylocalizer = pylocalizer:main' ]
    },
    test_suite = 'tests',
    zip_safe = False,
    install_requires = [
        'pyobjc-core',
        'pyobjc-framework-Cocoa',
        'pbPlist',
        'langcodes',
    ]
)
