
# 💸 Meu Controle Financeiro Pessoal

Um aplicativo interativo desenvolvido em Python com **Streamlit** para **analisar e visualizar gastos pessoais**. Ideal para quem está começando em **Data Science** e quer aprender a trabalhar com dados reais, gráficos e dashboards simples.

---

## 🧰 Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/) (para ler arquivos Excel)

---

## 📁 Estrutura do projeto

```

📦 Meu Controle Financeiro
├── Gastos\_Pessoais.xlsx         # Planilha com dados de exemplo
├── meu\_app\_financeiro.py        # Código principal do aplicativo
├── requirements.txt             # Dependências do projeto
└── README.md                    # Este arquivo

````

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/meu-controle-financeiro.git
cd meu-controle-financeiro
````

### 2. Instale as dependências

Crie um ambiente virtual (opcional) e instale os pacotes:

```bash
pip install -r requirements.txt
```

### 3. Rode o app com o Streamlit

```bash
streamlit run meu_app_financeiro.py
```

---

## 📊 Funcionalidades do App

* ✅ Visualização interativa da planilha de gastos
* ✅ Total de gastos por **categoria**
* ✅ Total de gastos por **mês**
* ✅ Filtro por categoria específica
* ✅ **Gráfico de barras** por data dos gastos filtrados

---

## 🧪 Exemplo de dados da planilha (`Gastos_Pessoais.xlsx`)

| Data       | Categoria   | Descrição    | Valor |
| ---------- | ----------- | ------------ | ----- |
| 01/05/2025 | Alimentação | Supermercado | 75.50 |
| 02/05/2025 | Transporte  | Uber         | 20.00 |
| 03/05/2025 | Lazer       | Netflix      | 39.90 |

---

## 📚 Aprendizados aplicados

* Leitura e manipulação de dados com Pandas
* Agrupamento (`groupby`), filtros e visualizações
* Criação de gráficos com Matplotlib
* Interface interativa com Streamlit
* Organização de código com funções

---

## ✍️ Autor

Feito com dedicação por **@Zarathus-py** 💙
Projeto acadêmico para aprender e compartilhar!
