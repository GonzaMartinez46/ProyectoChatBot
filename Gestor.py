from getpass import getpass
import requests
from langchain.document_loaders import PyPDFLoader, UnstructuredFileIOLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

class Gestor:

    def __init__(self, api_key, embedding) -> None:
        self.api_key= api_key
        self.embedding= embedding


    def cargar_documentos(self, archivos)->list:
        ml_papers=[]
        print('Cargando Documentos...')
        for a in archivos:
            loader = PyPDFLoader(archivos)
            data = loader.load()
            ml_papers.extend(data)

        return ml_papers
    
    def dividir_documentos(self, documentos):
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=200,
        length_function=len)
        documents = text_splitter.split_documents(documentos)
        return documents
    
    def crear_embeddings(self, documents):
        embeddings = OpenAIEmbeddings(model= self.embedding)
        vectorstore = Chroma.from_documents(
            documents= documents,
            embedding= embeddings
        )
        retriever = vectorstore.as_retriever(
            search_kwargs={"k":2}
        )
