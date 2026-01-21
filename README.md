🤖 Organizador de Pastas Automatizado (PyQt6)Este projeto é um Organizador de Arquivos Inteligente com interface gráfica, desenvolvido em Python. Ele resolve o problema comum de pastas de "Downloads" ou "Desktop" lotadas, movendo arquivos para subpastas categorizadas com base na extensão e no tamanho do arquivo.📸 Demonstração da InterfaceO projeto evoluiu de um protótipo básico no Qt Designer para uma interface personalizada com tema Dark e estilização via CSS.Design no Qt DesignerInterface Final (Fundo Customizado)✨ FuncionalidadesSeleção Dinâmica: Permite escolher qualquer pasta do computador através de uma janela nativa do Windows.Fila de Processamento: Adiciona múltiplas pastas em um listWidget para organização em lote.Categorização Automática:Imagens: .png, .jpg, .jpeg, .gif.Vídeos: .mp4, .mkv, .mov.Docs: .pdf, .docx, .txt.Verificar: Arquivos grandes ou desconhecidos para triagem manual.Segurança (Triagem de Tamanho): Arquivos considerados "grandes" são movidos para uma pasta especial para evitar erros de movimentação acidental.📊 Log de Execução RealAbaixo está o registro de uma operação real processando a pasta de Downloads. O sistema identifica o tamanho, cria as pastas necessárias e move os arquivos:BashComeçando Processo de organização
Criando Pastas: /Imagens, /Videos, /Verificar, /Docs

# Verificação de Segurança (Arquivos Grandes)
O tamanho é: 599276976 Bytes
Arquivo grande detectado: Docker Desktop Installer.exe -> Verificação necessária
Movendo: Docker Desktop Installer.exe -> /Organizar/Verificar/

# Organização por Extensão
O tamanho é: 365627 Bytes (OK)
Movendo: Novo Documento de Texto.txt -> /Organizar/Docs/
Movendo: Screenshot_1.png -> /Organizar/Imagens/

# Status Final
Pasta organizada com sucesso: C:/Users/Servidor/Downloads
Processo finalizado para todas as pastas!
🛠️ Tecnologias e BibliotecasPython 3.12: Linguagem base.PyQt6: Framework para a interface gráfica.Qt Designer: Ferramenta de design visual para os arquivos .ui.Library OS: Para manipulação de caminhos dinâmicos e arquivos no sistema.🚀 Como ExecutarCertifique-se de ter o PyQt6 instalado:Bashpip install PyQt6
Mantenha o arquivo Menu.ui e o Main.py no mesmo diretório.Execute o script:Bashpython Main.py
🏗️ Estrutura do CódigoO projeto utiliza uma estrutura desacoplada para facilitar a manutenção:Main.py: Gerencia a interface, os botões e os caminhos dinâmicos.Organizar.py: Contém a classe Organizar com a lógica de match case para triagem de arquivos.Menu.ui: Arquivo XML contendo o layout visual.Desenvolvido como projeto de automação de workflow.