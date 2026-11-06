# RPG - Jogo de Turnos em Python

Um jogo de RPG de turnos feito no terminal usando Programação Orientada a Objetos (POO) em Python.

##  Funcionalidades Atuais
- **Criação de Personagem:** O jogador pode criar seu próprio herói.
- **Sistema de Combate por Turnos:** Iniciativa aleatória (quem ataca primeiro não necessariamente sera o player).
- **Inimigos Balanceados:** Goblins, Orcs, Lobos, Demônios e Fallen Angels, cada um com status e danos diferentes.
- **Sistema de Crítico:** Chance de dar dano extra baseado no tipo de personagem.
- **Interface no Terminal:** HUD bonito e colorido usando a biblioteca `Rich`.

##  Como rodar o projeto

1. Clone o repositório.
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/Mac:
   source .venv/bin/activate