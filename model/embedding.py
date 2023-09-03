from dotenv import load_dotenv
from openai.embeddings_utils import get_embeddings
import os
import openai 
import tiktoken

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

# embedding model parameters
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 819

text = 'How are you today?'
embeddings = get_embeddings([text], embedding_model)
print(len(embeddings[0]))