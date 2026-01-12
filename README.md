# Organizador de Notas Fiscais

Programa em Python desenvolvido para **organizar notas fiscais em PDF**, separando automaticamente os arquivos em **pastas identificadas pelo CPF ou CNPJ do cliente**.

A aplicação utiliza **interface gráfica (GUI)** com `tkinter`, permitindo que o usuário utilize o sistema de forma simples, sem necessidade de comandos via terminal.

---

## Funcionalidades

* Leitura de notas fiscais em formato PDF
* Extração de CPF ou CNPJ diretamente do conteúdo do PDF
* Criação automática de pastas com base no CPF/CNPJ
* Organização dos arquivos PDF nas respectivas pastas
* Interface gráfica intuitiva para seleção de arquivos ou diretórios

---

## Requisitos

* Python 3.9 ou superior
* Bibliotecas utilizadas:

  * `pypdf`
  * `tkinter` (biblioteca padrão do Python)
  * `os` (biblioteca padrão do Python)

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/organizador-notas-fiscais.git
cd organizador-notas-fiscais
```

Instale a dependência necessária:

```bash
pip install pypdf
```

> **Observação:** As bibliotecas `os` e `tkinter` já estão incluídas na instalação padrão do Python.

---

## Execução

Para iniciar o programa, execute:

```bash
python main.py
```

Ao executar, a interface gráfica será exibida, permitindo a seleção dos arquivos ou pastas que contêm as notas fiscais em PDF.

---

## Configuração do Diretório de Clientes

O diretório onde os arquivos dos clientes serão armazenados é **criado automaticamente pelo próprio programa**.

Existe uma função responsável por:

* Criar o diretório de armazenamento dos clientes
* Definir o caminho correto de forma automática
* Escrever esse caminho no arquivo `dir.txt`

O arquivo `dir.txt` funciona como um **arquivo de apoio interno**, utilizado pelo sistema para persistir o diretório configurado.

Por conter informações específicas do ambiente do usuário, esse arquivo **não é versionado no repositório**.

> O usuário não precisa criar ou editar manualmente o `dir.txt`, pois todo o processo é tratado pelo código.

---

## Funcionamento

1. O usuário seleciona uma pasta contendo os arquivos PDF de notas fiscais
2. O programa lê o texto contido nos PDFs
3. O CPF ou CNPJ do cliente é identificado
4. Uma pasta é criada automaticamente com o CPF/CNPJ encontrado
5. O arquivo PDF é movido para a pasta correspondente

---

## Estrutura do Projeto

```

.
├── main.py            # Arquivo principal que inicia o programa
├── readpdf.py         # Responsável pela leitura e extração de dados dos PDFs
├── foldermanager.py   # Criação e gerenciamento das pastas por CPF/CNPJ
├── dir.txt            # Arquivo de configuração/apoio (diretórios utilizados pelo programa)
└── README.md

```

---

## Modelo de Nota Fiscal Utilizado

Este projeto foi desenvolvido e testado utilizando **notas fiscais fictícias**, criadas exclusivamente para fins de estudo e validação do funcionamento do sistema.

O modelo de nota fiscal utilizado **não segue integralmente o padrão oficial da NF-e brasileira**, podendo apresentar diferenças no layout, na formatação do texto e na forma como o CPF ou CNPJ aparece no documento.

A lógica de extração assume que o CPF/CNPJ esteja presente como **texto legível no PDF**. Dessa forma, o funcionamento do programa pode variar ao ser utilizado com notas fiscais reais ou com outros modelos de documento.

---

## Observações Importantes

- O CPF/CNPJ deve estar presente como texto no PDF
- PDFs escaneados (imagem) podem não funcionar corretamente sem OCR
- O padrão de escrita da nota fiscal pode influenciar a extração do CPF/CNPJ

---

## Autor

- Thyago da Silva

---

## Licença

Este projeto foi desenvolvido para fins educacionais e uso interno.

```
