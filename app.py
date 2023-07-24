import os
from collections import deque
from typing import Dict, List, Optional, Any

from langchain import LLMChain, OpenAI, PromptTemplate
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms.base import BaseLLM
from langchain.vectorstores.base import VectorStore
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain.chains.base import Chain
from pydantic import BaseModel, Field

llm = OpenAI(client='', model='')
llm.predict('hello world')
