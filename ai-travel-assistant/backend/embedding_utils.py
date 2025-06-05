import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_embedding(text, model="text-embedding-3-small"):
    """
    Returns the embedding vector(s) for the given text(s) using the specified model.
    """
    if isinstance(text, str):
        input_texts = [text]
    else:
        input_texts = text
    response = openai.embeddings.create(
        input=input_texts,
        model=model
    )
    return [data.embedding for data in response.data]
