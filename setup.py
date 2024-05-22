from setuptools import setup, find_packages

setup(
    name="real_estate_analysis",
    version="1.0",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "mlxtend",
        "plotly",
        "reportlab",        
        # tkinter is part of the standard library and doesn't need to be installed
    ],
    entry_points={
        'console_scripts': [
            'real_estate_analysis=main:main',
        ],
    },
)
