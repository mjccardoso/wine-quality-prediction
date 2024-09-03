import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from pathlib import Path

def run_notebook(notebook_path, output_path=None):
    
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        ep.preprocess(notebook, {'metadata': {'path': './'}})
        print(f"Notebook {notebook_path} executado com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o notebook: {e}")
    
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(notebook, f)
        print(f"Notebook executado salvo em {output_path}")
        

root_marker = 'README.md'
current_dir = Path.cwd()

while not (current_dir / root_marker).exists() and current_dir != current_dir.parent:
    current_dir = current_dir.parent

path_to_go = current_dir / 'app'
path_where_is = current_dir / 'notebooks'
filename = '/4-Deployment.ipynb'        

print(f'{path_where_is}{filename}')
        
notebook_path = f'{path_where_is}{filename}'
run_notebook(notebook_path)
