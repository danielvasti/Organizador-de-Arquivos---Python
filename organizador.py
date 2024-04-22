import os
import shutil
#O módulo os fornece funções para interagir com o sistema operacional, enquanto o shutil fornece operações de alto nível em arquivos e coleções de arquivos.
def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path
#função create_subfolder_if_needed cria uma subpasta dentro de uma pasta específica, se essa subpasta ainda não existir. 
#Ele recebe o caminho da pasta principal (folder_path) e o nome da subpasta (subfolder_name). 
#Ele usa os.path.join para garantir a compatibilidade multiplataforma ao construir o caminho completo para a subpasta. Em seguida, ele verifica se a subpasta já existe. 
#Se não existir, cria a subpasta usando os.makedirs.

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                new_location = os.path.join(subfolder_path, filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                    print(f"Moved: {filename} -> {subfolder_name}/")
                else:
                    print(f"Skipped: {filename} already exists in {subfolder_name}/")

#função clean_folder é o coração do script. Ela itera sobre os arquivos na pasta especificada (folder_path) usando os.listdir. 
#Para cada arquivo, verifica se é um arquivo regular usando os.path.isfile. Se for, obtém a extensão do arquivo usando filename.split('.')[-1].lower(). 
#Se a extensão existir, cria o nome da subpasta baseado na extensão do arquivo e chama a função create_subfolder_if_needed para garantir que a subpasta exista. 
#Em seguida, move o arquivo para a subpasta correspondente usando shutil.move, se ele ainda não estiver lá. 
#Ele imprime mensagens indicando se o arquivo foi movido ou se já estava na subpasta.

if __name__ == "__main__":
    print("Desktop Cleaner")
    folder_path = '/Users/Daniel Vasti/Downloads'
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning Complete")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again")
#Esta parte do código é executada apenas quando o script é executado diretamente, não quando é importado como um módulo. 
#Ela imprime uma mensagem de início, define o caminho da pasta (folder_path) para a pasta de downloads do usuário e verifica se esse caminho é uma pasta válida. 
#Se for uma pasta válida, chama a função clean_folder para limpar a pasta e imprime uma mensagem de conclusão. Se o caminho não for uma pasta válida, exibe uma mensagem de erro.