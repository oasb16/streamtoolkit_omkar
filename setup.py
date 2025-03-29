
from setuptools import setup, find_packages

setup(
    name="streamtoolkit_omkar",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "boto3",
        "python-dotenv",
    ],
    author="Omkar Sawant Bhosle",
    description="Reusable Streamlit developer toolkit with plug-and-play auth, GPT tools, and UI modules.",
    url="https://github.com/oasb16/streamtoolkit_omkar",
)
