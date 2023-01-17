from setuptools import setup, find_packages

setup(
  name = 'good-easle',
  packages = find_packages(exclude=[]),
  version = '0.1.0',
  license='MIT',
  description = 'GoodEasle: Text-to-Image Generation Using Public Images',
  author = 'Matthew Waller',
  author_email = 'hello@cephalopod.studio',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/muse-maskgit-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'text-to-image'
  ],
  install_requires=[
    'accelerate',
    'beartype',
    'einops>=0.6',
    'ema-pytorch',
    'pillow',
    'sentencepiece',
    'torch>=1.6',
    'transformers',
    'torch>=1.6',
    'torchvision',
    'tqdm',
    'vector-quantize-pytorch>=0.10.14',
    'jupyter'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
  ],
)