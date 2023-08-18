from getpass import getpass
import requests
from langchain.document_loaders import PyPDFLoader, UnstructuredFileIOLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA


class Gestor:

    def __init__(self,  embedding):
        self.embedding= embedding


    def cargar_documentos(self, archivos)->list:
        ml_papers=[]
        print('Cargando Documentos...')
        for a in archivos:
            loader = PyPDFLoader(archivos)
            data = loader.load()
            ml_papers.extend(data)

        return ml_papers
    
    def dividir_documentos(self, documentos, chunk_size, chunk_ovelap):
        text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_ovelap,
        length_function=len)
        documents = text_splitter.split_documents(documentos)
        return documents
    
    def crear_embeddings(self, documents, chat):
        embeddings = OpenAIEmbeddings(model= self.embedding)
        vectorstore = Chroma.from_documents(
            documents= documents,
            embedding= embeddings
        )
        retriever = vectorstore.as_retriever(
            search_kwargs={"k":2}
        )
        
        qa_chain= RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=retriever
        )
        return qa_chain
    

        
    
