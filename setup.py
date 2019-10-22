from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("lib.hello",  ["./src/hello.py"]), # The following is an example of how you compile
]

setup(
    name = 'Social Network Alignment',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
