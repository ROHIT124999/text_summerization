import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0.0"
repo_name =  "text_summerization"
authoe_user_name = "ROHIT124999"
SRC_REPO = "TextSummerizer"
author_email = "parikshit_rohit@outlook.com"

setuptools.setup(
     name=SRC_REPO,
    version=__version__,
    author=authoe_user_name,
    author_email=author_email,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{authoe_user_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{authoe_user_name}/{repo_name}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)