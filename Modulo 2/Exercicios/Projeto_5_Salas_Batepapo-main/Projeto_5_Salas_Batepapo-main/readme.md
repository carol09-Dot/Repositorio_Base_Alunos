# 💬 Projeto_14_Salas_Batepapo

Um site de **salas de bate-papo temáticas**, desenvolvido com **Streamlit**, utilizando múltiplas páginas e arquivos JSON para armazenar as mensagens enviadas pelos usuários.  
Cada sala possui seu próprio arquivo de registro, permitindo que as conversas permaneçam salvas entre sessões.

---

## 🧠 Situação-Problema

Uma pequena empresa deseja lançar uma plataforma simples de comunicação por salas temáticas, onde usuários possam:

- Entrar em diferentes salas para conversar  
- Visualizar mensagens já enviadas anteriormente  
- Registrar novas mensagens  
- Organizar os chats por assuntos  

Sua tarefa é desenvolver um **protótipo funcional** de um sistema de salas de bate-papo usando Python e Streamlit, com persistência das mensagens em arquivos JSON.

Esse projeto será realizado por alunos como prática de:

- Manipulação de arquivos JSON  
- Criação de aplicações multipáginas no Streamlit  
- Construção de interfaces dinâmicas e interativas  
- Noções básicas de armazenamento e fluxo de mensagens  
- Organização de projetos web em Python

---

## 🎯 Objetivo Educacional

- Compreender armazenamento simples com JSON  
- Criar múltiplas páginas usando `streamlit.pages`  
- Trabalhar com formulários de envio de mensagens  
- Implementar listas de mensagens carregadas dinamicamente  
- Melhorar habilidades em lógica de I/O (Input/Output)  
- Desenvolver interfaces limpas com Streamlit  
- Simular um ambiente real de salas de chat  

---

## 📌 Funcionalidades do Projeto

### 🏷 Múltiplas Salas Temáticas  
Cada página é uma sala independente, por exemplo:  
- Sala de Tecnologia  
- Sala de Filmes  
- Sala de Games  
- Sala de Viagens  
- Sala de Estudos  

(Os temas variam conforme o projeto.)


### 💾 Persistência das Mensagens  
Cada sala utiliza um arquivo JSON exclusivo:
- As mensagens ficam armazenadas, permitindo que o usuário sempre veja o histórico da sala.

### 📝 Envio de Mensagens  
- Campo para o usuário digitar seu nome  
- Campo para escrever a mensagem  
- Botão para enviar  
- Atualização instantânea no histórico  

### 📃 Exibição do Histórico  
- Todas as mensagens da sala são carregadas e exibidas em ordem  
- Formatação simples para boa leitura  
- Histórico persistente mesmo após recarregar a página  
