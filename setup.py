from setuptools import setup, find_packages

setup(
    name="vizblend",
    version="1.0.3",
    author="Mahmoud Housam",
    author_email="mahmoudhousam60@gmail.com",
    description="Generate multi-page HTML file for Interactive analytical reporting with Python and Plotly",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MahmoudHousam/VizBlend",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "plotly==5.24.1",
        "black==24.10.0",
        "pytest==8.3.4",
        "pandas==2.2.3",
        "jinja2==3.1.4",
        "bs4==0.0.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires=">=3.9",
)
