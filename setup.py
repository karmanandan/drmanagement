import setuptools
setuptools.setup(
    name="drmanagement",
    version="0.0.1",
    author="Team Dr.pinnacle",
    author_email="nandanr094@gmail.com",
    description="An all in one tool for data scientists and project managers to analyze, visualize the project status",
    # long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/drmanagement/drmanagement",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "numpy==1.23.2",
        "pandas==1.4.3",
        "Pillow==9.2.0",
        "plotly==5.10.0",
        "streamlit==1.12.2",
        "streamlit-aggrid==0.3.3"
    ]
)