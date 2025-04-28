from setuptools import setup, find_packages

setup(
    name="zero_touch_helpdesk",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'slack_bolt>=1.18.0',
        'python-dotenv>=0.19.0',
        'pandas>=1.3.0'      
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=23.0.0',
        ],
    },
)
