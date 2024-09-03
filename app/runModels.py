import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(notebook_path):
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        ep.preprocess(notebook, {'metadata': {'path': './'}})
        print(f"Notebook {notebook_path} executado com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o notebook: {e}")

# Especifique o caminho para o notebook que você deseja executar
notebook_path = '/Users/mauurao/Desktop/wine-quality-prediction/notebooks/3-Modelling.ipynb'

# Execute o notebook
run_notebook(notebook_path)
