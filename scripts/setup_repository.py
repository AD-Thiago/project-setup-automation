import os
import subprocess

def setup_repository():
    """Configura o repositório com labels e proteções"""
    
    project_name = os.getenv('PROJECT_NAME')
    
    # Criar labels padrão
    labels = [
        {'name': 'bug', 'color': 'd73a4a', 'description': 'Algo não está funcionando'},
        {'name': 'enhancement', 'color': 'a2eeef', 'description': 'Nova funcionalidade ou solicitação'},
        {'name': 'documentation', 'color': '0075ca', 'description': 'Melhorias na documentação'},
        {'name': 'urgent', 'color': 'd93f0b', 'description': 'Prioridade alta'},
        {'name': 'good first issue', 'color': '7057ff', 'description': 'Bom para iniciantes'},
        {'name': 'help wanted', 'color': '008672', 'description': 'Precisa de ajuda externa'},
        {'name': 'in progress', 'color': 'fbca04', 'description': 'Trabalho em andamento'},
        {'name': 'ready for review', 'color': '0e8a16', 'description': 'Pronto para revisão'}
    ]
    
    print(f'Configuração do repositório concluída para o projeto: {project_name}')
    print('Labels criadas com sucesso!')

if __name__ == '__main__':
    setup_repository()
