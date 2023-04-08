import setuptools
from Cython.Build import cythonize

setuptools.setup(
    name="emirp",
    ext_modules=cythonize("emirp.py"),
    zip_safe=False,
    install_requires=[
        'getprimes',
        'cython',
    ],
)
