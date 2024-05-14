from setuptools import setup, find_packages
# from setuptools_scm import get_version

# # Use setuptools_scm to get the version from the Git tag
# version = get_version(root='..', relative_to=__file__)

# setup(
#     # name='pgres',
#     version=version,
#     # packages=find_packages(),
#     # packages=find_packages(where="src"),
#     # package_dir={"": "src"},
#     # version="0.0.1",
#     description='A private wby package',
#     # author='Adeniyi',
#     # author_email='teebarg01@gmail.com',
#     # url='https://github.com/teebarg/python-packages',
#     # setup_requires=["setuptools_scm"],
#     # use_scm_version=True,
#     # install_requires=["setuptools_scm[toml]>=3.4"],
#     # install_requires=[],
#     # setup_requires=["setuptools_scm"],
# )


setup(
    name="tlib",
    version="0.0.9",
    description="Test library",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # setup_requires=["setuptools_scm"],
    # use_scm_version=True,
    install_requires=[
    ],
)