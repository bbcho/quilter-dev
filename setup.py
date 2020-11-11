import setuptools

with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="quilter",
	version="0.0.1",
	author="Ben Cho",
 	license='MIT License',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
	author_email="ben.cho@gmail.com",
	description="Python imnplementation of the R package patchwork, but for Matplotlib",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	package_data={'': ['*.csv']},
	keywords = ['quilter','patchwork','matplotlib','plot','compose'],
	url = "https://github.com/bbcho/quilter-dev",
	download_url = "https://github.com/bbcho/quilter-dev/archive/v0.0.1-beta.1.tar.gz",
	install_requires=[
          'matplotlib'
    ],
	include_package_data=True,
	classifiers=[
		'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'License :: OSI Approved :: MIT License',
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)