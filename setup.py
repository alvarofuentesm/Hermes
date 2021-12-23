from setuptools import find_packages, setup
setup(
    name="Hermes",
    version="0.0.1",
    author='Álvaro Fuentes, Jorge Díaz',
    author_email='jorge.diazma@sansano.usm.cl',
    packages=find_packages(),
    install_requires=["pyvo==1.1","astropy==4.3.1","astroquery==0.4.4","numpy==1.20.3","ipyaladin==0.1.9","multipledispatch==0.6.0", "pandas==1.3.4"],
    py_modules=["Hermes"]
)