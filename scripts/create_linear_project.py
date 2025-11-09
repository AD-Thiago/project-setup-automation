import os
import requests
import json

def create_linear_project():
    """Cria projeto e issues iniciais no Linear"""
    
    api_key = os.getenv('LINEAR_API_KEY')
    project_name = os.getenv('PROJECT_NAME')
    team_id = os.getenv('TEAM_ID')
    
    url = 'https://api.linear.app/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key
    }
    
    # Criar projeto
    mutation = f"""
    mutation {{
      projectCreate(
        input: {{
          name: "{project_name}"
          description: "Projeto criado automaticamente"
          teamIds: ["{team_id}"]
        }}
      ) {{
        success
        project {{
          id
          name
          url
        }}
      }}
    }}
    """
    
    response = requests.post(url, json={'query': mutation}, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        if result.get('data', {}).get('projectCreate', {}).get('success'):
            project = result['data']['projectCreate']['project']
            project_id = project['id']
            print(f'Projeto criado: {project["name"]}')
            print(f'URL: {project["url"]}')
            
            # Criar issues iniciais
            initial_issues = [
                {'title': 'Setup inicial do projeto', 'description': 'Configurar ambiente de desenvolvimento'},
                {'title': 'Definir arquitetura', 'description': 'Documentar arquitetura do sistema'},
                {'title': 'Setup CI/CD', 'description': 'Configurar pipeline de integração contínua'},
                {'title': 'Documentação inicial', 'description': 'Criar documentação básica do projeto'}
            ]
            
            for issue_data in initial_issues:
                issue_mutation = f"""
                mutation {{
                  issueCreate(
                    input: {{
                      title: "{issue_data['title']}"
                      description: "{issue_data['description']}"
                      teamId: "{team_id}"
                      projectId: "{project_id}"
                    }}
                  ) {{
                    success
                    issue {{
                      id
                      title
                    }}
                  }}
                }}
                """
                
                issue_response = requests.post(url, json={'query': issue_mutation}, headers=headers)
                if issue_response.status_code == 200:
                    issue_result = issue_response.json()
                    if issue_result.get('data', {}).get('issueCreate', {}).get('success'):
                        issue = issue_result['data']['issueCreate']['issue']
                        print(f'Issue criada: {issue["title"]}')
        else:
            print(f'Erro ao criar projeto: {result}')
    else:
        print(f'Erro na requisição: {response.status_code} - {response.text}')

if __name__ == '__main__':
    create_linear_project()
