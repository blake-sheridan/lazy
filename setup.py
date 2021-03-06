#!/usr/local/bin/python3

from distutils.core import setup, Extension

# Workaround -Werror=statement-after-declaration
# http://bugs.python.org/issue18211
import os
os.environ['CFLAGS'] = '-Wno-unused-result'

setup(
    name = 'lazy',
    version = '1.0',
    description = 'Lazy',
    ext_modules = [
        Extension(
            name = 'b._collections',
            include_dirs = [
                'include',
            ],
            sources = [
                'src/collections.c',
            ],
        ),
        Extension(
            name = 'b._functools',
            sources = [
                'src/functools.c',
            ],
        ),
        Extension(
            name = 'b._grammar',
            include_dirs = [
                'include',
            ],
            sources = [
                'src/grammar.c',
            ],
        ),
        Extension(
            name = 'b._operator',
            sources = [
                'src/operator.c',
            ],
        ),
        Extension(
            name = 'b._types',
            include_dirs = [
                'include',
            ],
            sources = [
                'src/types.c',
            ],
        ),
    ],
)
