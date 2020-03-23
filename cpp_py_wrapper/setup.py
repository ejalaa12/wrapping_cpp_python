from distutils.core import setup, Extension

library_so_prefix = "spam"
extension_mod = Extension(library_so_prefix, ["spammodule.c"])

py_library_name = "spam"
setup(name=py_library_name, ext_modules=[extension_mod])
