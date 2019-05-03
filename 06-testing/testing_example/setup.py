from setuptools import setup

setup(name='testing_example',
      version='0.0.1',
      description='Dummy package used for deployment testing.',
      url='https://github.com/BelfastTechTraining/python.git',
      author='Matt Mulhern',
      author_email='mattmulhern01@gmail.com',
      packages=['testing_example'],
      zip_safe=False,
      setup_requires=['pytest-runner'],
      tests_require=['pytest']
      )
