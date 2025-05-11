from setuptools import setup, find_packages

setup(
    name="langgraphagenticai",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain",
        "langgraph",
        "langchain_community",
        "langchain_core",
        "langchain_groq",
        "langchain_openai",
        "faiss-cpu",
        "streamlit",
    ],
) 