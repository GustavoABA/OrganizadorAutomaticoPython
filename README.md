---

```markdown
# 🤖 Organizador de Pastas Inteligente (Python + PyQt6)

Este projeto é um sistema de automação para organização de ficheiros, utilizando uma interface gráfica personalizada. Ele permite selecionar pastas, listar tarefas e organizar ficheiros automaticamente com base na sua extensão e tamanho.

---

## 📸 Galeria do Projeto

Para conferir todas as imagens do desenvolvimento, aceda à [Galeria Oficial](https://github.com/GustavoABA/OrganizadorAutomaticoPython/tree/main/ReadmeImagem).

| Design no Qt Designer | Seleção de Pastas | Interface em Execução |
| :---: | :---: | :---: |
| ![Design](https://raw.githubusercontent.com/GustavoABA/OrganizadorAutomaticoPython/main/ReadmeImagem/imagemParaReadme.png) | ![Seleção](https://raw.githubusercontent.com/GustavoABA/OrganizadorAutomaticoPython/main/ReadmeImagem/imagemParaReadme1.png) | ![Execução](https://raw.githubusercontent.com/GustavoABA/OrganizadorAutomaticoPython/main/ReadmeImagem/image.png) |

---

## ✨ Funcionalidades

* **Interface Gráfica (GUI)**: Criada no Qt Designer com estilização personalizada.
* **Seleção Dinâmica**: Utiliza o `QFileDialog` para escolher pastas diretamente no sistema.
* **Fila de Tarefas**: Adiciona múltiplos caminhos a um `listWidget` para processamento em lote.
* **Triagem Inteligente**:
    * **Imagens/Vídeos/Docs**: Separação automática por extensão.
    * **Segurança**: Identifica ficheiros grandes e move-os para uma pasta de "Verificação" para evitar perdas acidentais.

---

## 📊 Exemplo de Log de Operação

Ao carregar em **Finalizar**, o sistema gera um log detalhado como este:

```bash
Começando Processo de organização...
Criando subpastas: /Imagens, /Videos, /Verificar, /Docs

# Triagem por Tamanho
O tamanho é: 599.276.976 Bytes
Arquivo grande detectado: Docker Desktop Installer.exe -> Movendo para /Verificar

# Organização por Extensão
O tamanho é: 365.627 Bytes (OK)
Novo Documento.txt -> Movendo para /Docs
Screenshot_1.png -> Movendo para /Imagens

# Resultado
Pasta organizada com sucesso: C:/Users/Servidor/Downloads
Processo finalizado para todas as pastas!

```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**: Linguagem base do projeto.
* **PyQt6**: Framework para a construção da interface.
* **Qt Designer**: Ferramenta de design visual para ficheiros `.ui`.
* **Biblioteca OS**: Para gestão de caminhos dinâmicos e manipulação de ficheiros.

---

## 🚀 Como Executar

1. **Instale as dependências**:
```bash
pip install PyQt6

```


2. **Clone o repositório e execute**:
```bash
python Main.py

```



---

## 🏗️ Estrutura de Arquivos

* `Main.py`: Gere a interface e a conexão dos botões.
* `Organizar.py`: Contém a lógica de `match case` para a limpeza.
* `Menu.ui`: Design visual da janela.

---

**Desenvolvido por GustavoABA** - Projeto de automação de fluxo de trabalho.

```

```
