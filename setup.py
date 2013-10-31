#!/usr/local/bin/python3

from distutils.core import setup, Extension

setup(
    name = 'lazy',
    version = '1.0',
    description = 'Lazy',
    ext_modules = [
        Extension(
            name = '_lazy',
            depends = [
                'include/memoizer.h',
                ],
            include_dirs = [
                'include',
            ],
            sources = [
                'src/__init__.c',
                'src/memoizer.c',
                'src/property.c',
            ],
        ),
        Extension(
            name = 'b._collections',
            sources = [
                'src/collections.c',
            ],
        )
    ],
)
