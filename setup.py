from distutils.core import setup, Extension

module = Extension('noddy4',
                   sources = ['noddy4.c'])

setup (name = 'noddy',
       version = '1.0',
       ext_modules = [module])
