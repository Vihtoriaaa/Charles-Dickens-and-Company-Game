import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Charles_Dickens_and_Company_Game-Victoria_Maksymiuk", # Replace with your own username
    version="0.0.1",
    author="Victoria_Maksymiuk",
    author_email="viktoriia.maksymyuk@ucu.edu.ua",
    description="A package to discover more about Charles Dickens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)