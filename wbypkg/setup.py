from setuptools import setup, find_packages

setup(
    name='pgres',
    packages=find_packages(),
    version="0.0.2",
    description='A private pgres package',
    author='Adeniyi',
    author_email='teebarg01@gmail.com',
    url='https://github.com/teebarg/python-packages',
    # setup_requires=["setuptools_scm"],
    # use_scm_version=True,
    install_requires=[
        # Any dependencies that wby has, list them here, e.g.,
        # 'requests',
    ],
)