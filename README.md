# Cryptris
___

### A game about asymetric cryptography

Cryptris is a game designed to help people in getting a grasp about how cryptography works, by playing an arguably tetris-like game.

Cryptris was developped by Digital Cuisine for Inria and is based on a concept created by Léo Ducas.
Technology. This is a reprodution of it in python language.

The whole application is designed to be a serverless application, hence the installation is pretty straightforward: 
- Simply clone this repository or download it as an archive.
- Put it in your python project
- Make a simple python code like this:
  ```
  from cryptris.constantes import SCREEN_SIZE
  from cryptris.game import Game
  
  screen = Game.init(SCREEN_SIZE)
  game = Game(screen)
  while game.running:
     game.run()
  Game.quit()
  ```
- Launching the game

### Credits

Basé sur une idée originale de Léo Ducas

### Scénario

Mathieu Jouhet & Nicolas Pelletier
### Inria

    Coordination : Service communication du centre de recherche Inria Paris - Rocquencourt
    Référents médiation : Thierry Vieville et Laurent Viennot
    Référent scientifique : Léo Ducas

### Digital Cuisine

    Directeur Artistique : Mathieu Jouhet (@daformat)
    Graphiste : Nicolas Pelletier
    Game engine : Vincent Mézino
    Intégration html, développement javascript: Mathieu Jouhet
    Test : Olivier Lance, Pierre-Jean Quilleré

### Python developpers

- Lioguy Guimdo <vianel.lioguy@gmail.com>
- Toukep Ducer