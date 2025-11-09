import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def create_drive_folders():
    """Cria estrutura de pastas no Google Drive"""
    
    # Carregar credenciais
    creds_json = os.getenv('GOOGLE_CREDENTIALS')
    credentials_dict = json.loads(creds_json)
    credentials = service_account.Credentials.from_service_account_info(
        credentials_dict,
        scopes=['https://www.googleapis.com/auth/drive']
    )
    
    service = build('drive', 'v3', credentials=credentials)
    project_name = os.getenv('PROJECT_NAME')
    parent_folder_id = os.getenv('PARENT_FOLDER_ID')
    
    # Estrutura de pastas a ser criada
    folder_structure = {
        f'{project_name}': {
            '01_Documentos': ['Requisitos', 'Arquitetura', 'Especificações'],
            '02_Design': ['Wireframes', 'Mockups', 'Assets'],
            '03_Desenvolvimento': ['Backend', 'Frontend', 'Database'],
            '04_Testes': ['Unitários', 'Integração', 'QA'],
            '05_Deploy': ['Produção', 'Staging', 'Desenvolvimento'],
            '06_Reuniões': ['Atas', 'Apresentações'],
            '07_Recursos': ['Imagens', 'Vídeos', 'Documentos']
        }
    }
    
    def create_folder(name, parent_id):
        """Cria uma pasta no Google Drive"""
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [parent_id]
        }
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print(f'Pasta criada: {name} (ID: {folder.get("id")})')
        return folder.get('id')
    
    # Criar estrutura
    for root_name, subfolders in folder_structure.items():
        root_id = create_folder(root_name, parent_folder_id)
        
        for folder_name, subsubfolders in subfolders.items():
            folder_id = create_folder(folder_name, root_id)
            
            for subfolder_name in subsubfolders:
                create_folder(subfolder_name, folder_id)
    
    print(f'Estrutura de pastas criada com sucesso para o projeto {project_name}!')

if __name__ == '__main__':
    create_drive_folders()
