# Snake Game 🐍

This project is a modern rendition of the classic Snake Game, implemented using Python and the `turtle` graphics module. 

Players can control the snake using arrow keys to eat food, grow in size, and score points. The game ends when the snake collides with the walls or its own body. 

---

## Features
- **Real-time gameplay:** Smooth animations with adjustable speed.
- **Score Tracking:** Tracks the player's score and displays it in real-time.
- **Game Over Screen:** Displays a message when the game ends.
- **Dynamic Snake Growth:** Snake grows in size each time it eats food.
- **Randomized Food Placement:** Food appears in random positions within the game area.
- **Collision Detection:** Detects collisions with walls and the snake's tail.

---

## Prerequisites
Ensure you have Python installed on your machine. This project has been tested with Python 3.7+.

---

## Installation
1. Clone this repository to your local machine:
```
git clone https://github.com/your-username/snake-game.git
```
2. Navigate to the project directory:
```
cd snake-game
```
3. Install required dependencies (if any):
```
pip install -r requirements.txt
```
   Note: The game only requires Python's built-in turtle and random modules, which are pre-installed.

### How to Play
1. Run the game:
```
python main.py
```
2. Use the following keys to control the snake:
 - Up Arrow ⬆️: Move Up
 - Down Arrow ⬇️: Move Down
 - Left Arrow ⬅️: Move Left
 - Right Arrow ➡️: Move Right

3. Avoid collisions with walls and the snake's tail to keep playing.

4. Eat the food to grow the snake and increase your score.

### Code Structure
  1. main.py: The main script that initializes the game, handles user input, and contains the game loop.
  2. snake.py: Defines the Snake class, responsible for managing the snake's movements and growth.
  3. scoreboard.py: Implements the ScoreBoard class, which displays the player's score and the game-over message.
  4. food.py: Contains the Food class, responsible for creating food objects and randomizing their position.

Preview

![image](https://github.com/user-attachments/assets/93cdecad-dd47-486c-b33a-8bc2684e2f45)


## Future Improvements
1. Add difficulty levels.
2. Introduce power-ups or special food items.
3. Create a multiplayer mode.
4. Add a high score leaderboard.

### Contributing
  Contributions, issues, and feature requests are welcome!
  Feel free to fork the repository and submit a pull request.

### License
This project is licensed under the MIT License.

Happy Gaming! 🎮


