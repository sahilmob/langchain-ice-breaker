import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    print("Hello Langchain")
    print(os.environ['OPENAI_API_KEY'])
