from setuptools import setup, find_packages

setup(
    name='stellark-dev',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'openai',
        'python-dotenv'
    ],
)
