from setuptools import setup, find_packages
setup(
    name='dxl-medimage',
    version='0.0.1',
    description='Medical Image Processing Library.',
    url='https://github.com/Hong-Xiang/dxmedimage',
    author='Hong Xiang',
    author_email='hx.hongxiang@gmail.com',
    license='MIT',
    packages=['dxl.medimage'],
    package_dir={'': 'src/python'},
    install_requires=[],
    scripts=[],
    #   namespace_packages = ['dxl'],
    zip_safe=False)
