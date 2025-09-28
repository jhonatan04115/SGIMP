# Sistema de Controle de Ferramental e Documental

## Instalação

1. Instale o Python 3.x
2. Instale as dependências:
   ```
pip install -r requirements.txt
   ```

## Execução

```bash
python app/main.py
```

## Empacotamento para Windows (.exe)

1. Instale o PyInstaller:
   ```
pip install pyinstaller
   ```
2. Gere o executável:
   ```
pyinstaller --onefile app/main.py
   ```
O executável estará na pasta `dist`.

## Estrutura do Projeto
- `/app`: código principal
- `/db`: scripts e instância do banco
- `/ui`: telas da interface
- `/docs`: manuais e arquivos relacionados

## Funcionalidades
- Cadastro de kits/carrinhos
- Cadastro de ferramentas
- Controle de movimentações
- Gerenciamento de documentos
- Autenticação de usuários
- Relatórios e exportação
- Backup/restauração

## Banco de Dados
Utiliza SQLite. Scripts de criação estão em `/db`.
