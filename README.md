# 🤖 Organizador de Pastas Inteligente (Python + PyQt6)

Este projeto é uma ferramenta de automação para organização de arquivos, utilizando uma interface gráfica moderna. Ele permite processar múltiplas pastas simultaneamente, movendo arquivos automaticamente com base em suas extensões e tamanhos para manter o seu computador limpo e organizado.

---

## 📸 Interface do Projeto

Abaixo, os três estágios do projeto: o design visual, a seleção de diretórios e o programa pronto para uso.

| Design (Qt Designer) | Seleção de Pastas | Interface em Execução |
| :---: | :---: | :---: |
| ![Design](https://raw.githubusercontent.com/GustavoABA/OrganizadorAutomaticoPython/main/ReadmeImagem/imagemParaReadme.png) | ![Seleção](https://raw.githubusercontent.com/GustavoABA/OrganizadorAutomaticoPython/main/ReadmeImagem/imagemParaReadme1.png) | ![Execução](https://raw.githubusercontent.com/GustavoABA/OrganizadorAutomaticoPython/main/ReadmeImagem/image.png) |

---

## 📦 Downloads (Versões Prontas para Uso)

Não precisa instalar o Python para usar! Baixe as versões compiladas abaixo:

* **[Versão Portátil (.exe)](https://github.com/GustavoABA/OrganizadorAutomaticoPython/releases)**: Basta baixar e executar. Já inclui o ícone personalizado.
* **[Instalador Windows (.msi)](https://github.com/GustavoABA/OrganizadorAutomaticoPython/releases)**: Versão com instalador profissional que cria atalhos no sistema.

---

## ✨ Funcionalidades

* **Interface Gráfica (GUI)**: Estilização personalizada com tema escuro e ícones.
* **Processamento em Lote**: Adicione várias pastas à lista e organize todas com um único clique.
* **Triagem de Segurança**: Arquivos muito grandes são movidos para uma pasta de "Verificação" para evitar movimentações acidentais de instaladores ou ISOs.
* **Caminhos Relativos**: O executável é inteligente e localiza seus próprios arquivos de interface (.ui) e imagens (Galeria) automaticamente.

---

## 📂 Como o programa organiza suas pastas?

Ao clicar em **Finalizar**, o programa analisa a pasta escolhida e cria automaticamente a seguinte estrutura de subpastas:

| Pasta Gerada | Critério de Organização |
| :--- | :--- |
| **`/Imagens`** | Arquivos `.png`, `.jpg`, `.jpeg`, `.gif`, `.bmp`, `.webp`. |
| **`/Videos`** | Arquivos `.mp4`, `.mkv`, `.avi`, `.mov`. |
| **`/Docs`** | Arquivos `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`. |
| **`/Verificar`** | Arquivos acima de um determinado tamanho (Ex: Instaladores `.exe`). |



---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**: Core do sistema.
* **PyQt6**: Framework da interface.
* **PyInstaller**: Compilação em executável único.
* **Briefcase**: Geração do instalador nativo MSI.

---

## 🏗️ Estrutura do Repositório

* `Main.py`: Controle da interface e eventos.
* `Organizar.py`: Motor de lógica que realiza a movimentação dos arquivos.
* `Menu.ui`: Arquivo de design da interface gerado pelo Qt Designer.
* `Galeria/`: Contém os recursos visuais e o ícone do programa (`ButtonBan.png`).

---

**Desenvolvido por GustavoABA** - Automação e Produtividade.
