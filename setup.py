from setuptools import setup, find_packages

setup(
    name='csa',
    version='1.0',
    packages=find_packages(),
    include_package_data = True,
    description='Confident Sinkhorn Allocation',
    install_requires=[
        "python==3.8"
        "colorama>=0.4.5",
        "cycler>=0.11.0",
        "fonttools>=4.33.3",
        "joblib>=1.1.0",
        "kiwisolver>=1.4.3",
        "matplotlib>=3.5.2",
        "numpy>=1.21.0",
        "packaging>=21.3",
        "pandas>=1.2.3",
        "Pillow>=9.2.0",
        "pyparsing>=3.0.9",
        "python-dateutil>=2.8.2",
        "pytz>=2022.1",
        "scikit-learn>=1.0",
        "scipy>=1.7.1",
        "six>=1.16.0",
        "threadpoolctl>=3.1.0",
        "tqdm>=4.64.0",
        "xgboost>=1.6.1",
    ],
)