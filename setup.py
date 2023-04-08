import setuptools
from Cython.Build import cythonize

setuptools.setup(
    packages=setuptools.find_packages(),
    name="emirp",
    zip_safe=False,
    install_requires=[
        'getprimes',
    ],
)
