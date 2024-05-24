from setuptools import setup, find_packages
HYPHEN_E_DOT = '-e .'
def get_requirements(file:str)->list[str]:
    requirements=[]
    with open(file) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements ]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(  name='ml_project',version='0.0.1',author='vaishali',author_email='vaishali18lalit@gmail.com',packages=find_packages(),license='MIT',install_requires=get_requirements('requirements.txt'))