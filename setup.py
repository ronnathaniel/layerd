import setuptools

PACKAGE = 'layerd'
VERSION = '0.0.0-dev'
with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


def try_reqs(f_name):
    try:
        with open(f_name, 'r') as reqs:
            return reqs.read().splitlines()
    except FileNotFoundError:
        return None


required = (
    try_reqs('requirements.txt')
    or
    try_reqs('layerd.egg-info/requires.txt')
    or
    []
)

print(required)

setuptools.setup(
    name=PACKAGE,
    version=VERSION,
    author="ronnathaniel",
    author_email="rnathaniel7@gmail.com",
    description="Download AWS Lambda Layers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['layerd'],
    package_data={'layerd': ['*.pem']},
    python_requires=">=3.6",
    entry_points={
        'console_scripts': ['layerd = layerd.__main__:run']
    },
    install_requires=required,
    include_package_data=True,
    use_calver='%Y.%m.%d.%H.%M',
    setup_requires=['calver'],
    url="https://github.com/ronnathaniel/layerd",
    project_urls={
        "Bug Tracker": "https://github.com/ronnathaniel/layerd/issues"
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'python',
        'python3',
        'layerd',
        'daemon',
        'download',
        'layer',
        'extension',
        'aws',
        'lambda',
        'function',
        'remote'
    ],

)
