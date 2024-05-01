## Python Backup Script for Windows

Este script Python oferece uma solução robusta para realizar backups incrementais de arquivos em sistemas Windows. Ele foi projetado para detectar e copiar apenas os arquivos que foram modificados desde o último backup, garantindo eficiência no uso de espaço e tempo de processamento.

### Características Principais

- **Backup Incremental**: O script identifica e copia apenas os arquivos que foram alterados desde a última execução do backup.
- **Preservação da Estrutura de Diretórios**: Mantém a estrutura de diretórios original do diretório de origem no diretório de backup, assegurando que a organização dos arquivos seja preservada.
- **Registro de Backup**: Registra a data e hora do último backup bem-sucedido, garantindo que apenas os arquivos alterados após essa data sejam considerados para o próximo backup.
- **Configuração Simples**: Requer apenas a definição dos caminhos de origem e destino para começar a fazer os backups.

### Como Funciona

1. **Configuração**: Inicialmente, defina os caminhos do diretório de origem e de destino.
2. **Verificação de Arquivos Modificados**: O script percorre todos os arquivos no diretório de origem e compara a última data de modificação de cada arquivo com a data do último backup registrado.
3. **Backup dos Arquivos**: Se um arquivo foi modificado após a última data de backup, ele é copiado para o diretório de backup, preservando sua localização na estrutura de diretórios.
4. **Atualização do Registro de Backup**: Após a conclusão do backup, a data e hora atuais são salvas como a nova "data do último backup".

### Uso

Para usar este script, configure as variáveis `source_directory` (diretório de origem)  e `backup_directory` (diretório de destino) no script para os caminhos desejados. Execute o script para iniciar o processo de backup. O script pode ser configurado para rodar em intervalos regulares usando o Agendador de Tarefas do Windows.

### Requisitos

- Python 3.x
- Bibliotecas Python: `os`, `shutil`, `datetime`

Este script é uma solução eficaz e fácil de usar para usuários e administradores que necessitam de um método confiável para realizar backups regulares de arquivos importantes, sem a necessidade de software adicional.

