import setuptools
from Cython.Build import cythonize


with open("README.md", "r") as fh:
	long_description = fh.read()

with open('requirements.txt') as fp:
	install_requires = fp.read()


extensions = [
	setuptools.Extension(
		"hello_linlin", ["hello_linlin/hello_linlin.pyx"], language="c++")
]

setuptools.setup(
	name="hello-linlin",
	version="0.0.1",
	author="Linlin Jia",
	author_email="linlin.jia@z",
	description="A test repo of Linlin JIA, PhD, dancer, voyageur",
	long_description=long_description,
	long_description_content_type="text/markdown",
	project_urls={
		# 'Documentation': 'https://graphkit-learn.readthedocs.io',
		'Source': 'https://github.com/jajupmochi/hello-world',
		'Tracker': 'https://github.com/jajupmochi/hello-world/issues',
		},
	url="https://github.com/jajupmochi/hello-world",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
		'Intended Audience :: Science/Research',
		'Intended Audience :: Developers',
	],
	install_requires=install_requires,
	ext_modules=cythonize(extensions),
)

