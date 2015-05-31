from distutils.core import setup
setup(name='jieba',
      version='0.34',
      description='Chinese Words Segementation Utilities',
      author='Chen, Mish',
      author_email='mish0207@gmail.com',
      url='http://github.com/fxsjy',
      packages=['jieba'],
      package_dir={'jieba':'Web/jieba-master/jieba'},
      package_data={'jieba':['*.*','finalseg/*','analyse/*','posseg/*']}
)
