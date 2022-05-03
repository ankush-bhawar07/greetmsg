from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Simple python module'
LONG_DESCRIPTION = 'A package that prints hello world'

# Setting up
setup(
    name="greetmsg",
    version=VERSION,
    author="Ankush Bhawar",
    author_email="<ankush.bhawar07@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)