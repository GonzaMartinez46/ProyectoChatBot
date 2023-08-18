import Gestor 

def main():
    """Main function"""
    gestor= Gestor('text-embedding-ada-002')
    
    gestor.cargar_documentos(archivos)
if __name__ == "__main__":
    main()