"""Package configuration for data-pipeline-helper-kamal."""

from pathlib import Path

from setuptools import find_packages, setup


PROJECT_DIRECTORY = Path(__file__).parent
LONG_DESCRIPTION = (PROJECT_DIRECTORY / "README.md").read_text(encoding="utf-8")


setup(
    name="data-pipeline-helper-kamal",
    version="0.1.0",
    author="Kamal",
    author_email="your-email@example.com",  # Replace before publishing.
    description=(
        "Beginner-friendly helpers for data cleaning, CSV ETL, "
        "and parameterized SQL"
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/data-pipeline-helper",  # Replace this.
    packages=find_packages(exclude=("examples", "examples.*", "tests", "tests.*")),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=["pandas>=2.0,<4.0"],
    license="MIT",
    license_files=["LICENSE"],
)
