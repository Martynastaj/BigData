from setuptools import setup, find_packages

setup(
    name="lab9_spark",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pyspark"
    ],
    entry_points={
        "console_scripts": [
            "run-spark-job=lab9_spark.spark_job:main"
        ]
    }
)
