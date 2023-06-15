import setuptools

with open('README.md','r') as file:
    long_description=file.read()

setuptools.setup(
    name='preprocess_yeementh24', # this should be unique
    version='0.0.1',
    author='Yeementh Virutkar',
    author_email='yeementh24@gmail.com',
    description='This is preprocessing package',
    long_description= long_description,
    long_description_contain_type ='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        ],
    python_required ='>=3.5'
)