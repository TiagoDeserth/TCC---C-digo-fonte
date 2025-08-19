# 🛰️ Código fonte do sistema desenvolvido para o Trabalho de Conclusão de Curso (TCC), do curso de Ciência da Computação

---

## Sistema de Gestão de Restaurante Estudantil 

Sistema web desenvolvido em Flask para gerenciamento completo de cardápios, alimentos e predição de demanda em restaurantes universitários.

## 📋 Sobre o Projeto

Este sistema foi desenvolvido como projeto interdisciplinar para automatizar e otimizar a gestão de do Restaurante Estudantil (RE) do IFSULDEMINAS - Campus Muzambinho, oferecendo funcionalidades para:

- Gestão de alimentos: Cadastro completo com informações nutricionais;
- Planejamento de cardápios: Criação e edição de cardápios por data/modalidade;
- Predição de demanda: Algoritmo de Aprendizado de Máquina para prever consumo;
- Controle de usuários: Sistema de autenticação e autorização.

## 🚀 Funcionalidades Principais

### 📊 Gestão de Dados

- Alimentos: CRUD completo com informações nutricionais (kcal, proteínas, carboidratos, etc);
- Categorias: Classificação de alimentos;
- Ingredientes: Controle de ingredientes com quantidades e medidas;
- Dias: Registro de condições climáticas e datas;
- Modalidades: Gerenciamento de tipos de refeição;
- Locais: Cadastro de diferentes unidades de RE.

### 🍽️Cardápios

- Criação de cardápios por data e modalidade;
- Associação de múltiplos alimentos por cardápio;
- Controle de quantidades por alimento;
- Visualização completa com informações nutricionais.

### 🤖 Aprendizado de Máquina

- Predição de demanda baseada em:
  - Condições climáticas;
  - Dia da semana;
  - Histórico de consumo;
  - Eventos especiais.
- Cálculo automático de produção por alimento.

### 📱Interface

- Design responsivo com Bootstrap 5;
- Interface intuitiva e moderna;
- Sistema de notificações (flash messages);
- Modais para confirmação de ações.

## 🛠️ Tecnologias utilizadas

### Backend

- Python;
- Flask;
- Flask-MySQLdb;
- scikit-learn;
- joblib.

### Frontend

- HTML/CSS;
- Bootstrap;
- Bootstrap Icons/Font Awesome;
- JavaScript.

### Banco de Dados

- MySQL;
- Estrutura normalizada com relacionamentos.

### Aprendizado de Máquina

- Árvore de Decisão para predição;
- StandardScaler para normalização;
- Joblib para persistência de modelos.

