from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'TS translator python package'
LONG_DESCRIPTION = 'TS translator python package'

def getReqs() -> list:
    reqs = []
    with open("requirements.txt","r") as f:
        for req in f.read().split("\n"):
            if req[0]!="#":
                reqs.append(req)

    return reqs

# Setting up
setup(
        name="ts-translator", 
        version=VERSION,
        author="pndz",
        author_email="<kalin1538inn@gmail.com>",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[*getReqs()] # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
)