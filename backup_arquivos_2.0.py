import os
import shutil
from datetime import datetime

def get_last_backup_time(backup_dir):
    """Recuperar a hora do último backup de um arquivo."""
    last_backup_file = os.path.join(backup_dir, 'tempo_do_ultimo_backup.txt')
    if os.path.exists(last_backup_file):
        with open(last_backup_file, 'r') as file:
            return datetime.fromisoformat(file.read().strip())
    return None

def set_last_backup_time(backup_dir):
    """Salve a hora atual como a hora do último backup."""
    last_backup_file = os.path.join(backup_dir, 'tempo_do_ultimo_backup.txt')
    with open(last_backup_file, 'w') as file:
        file.write(datetime.now().isoformat())

def backup_modified_files(source_dir, backup_dir):
    """Arquivos de backup modificados desde o último backup, preservando a estrutura de diretórios."""
    last_backup_time = get_last_backup_time(backup_dir)
    if last_backup_time is None:
        last_backup_time = datetime.min

    for foldername, subfolders, filenames in os.walk(source_dir):
        rel_path = os.path.relpath(foldername, source_dir)
        backup_subdir = os.path.join(backup_dir, rel_path)
        if not os.path.exists(backup_subdir):
            os.makedirs(backup_subdir)

        for filename in filenames:
            source_file = os.path.join(foldername, filename)
            backup_file = os.path.join(backup_subdir, filename)
            
            if datetime.fromtimestamp(os.path.getmtime(source_file)) > last_backup_time:
                shutil.copy2(source_file, backup_file)
                print(f'Backup atualizado para: {filename}')

    # Atualiza a data do último backup
    set_last_backup_time(backup_dir)

# Solicitar ao usuário os diretórios de origem e destino
source_directory = input("Digite o caminho completo do diretório de origem: ")
backup_directory = input("Digite o caminho completo do diretório de backup: ")

# Verifica se os diretórios fornecidos são válidos
if not os.path.isdir(source_directory):
    print("O caminho do diretório de origem não existe. Por favor, verifique e tente novamente.")
elif not os.path.isdir(backup_directory):
    print("O caminho do diretório de backup não existe. Por favor, verifique e tente novamente.")
else:
    # Executar o backup
    backup_modified_files(source_directory, backup_directory)