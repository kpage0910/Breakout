# Breakout Game

A classic Breakout game implementation using Python and Pygame.

## Description

Break all the bricks by bouncing a ball off your paddle. Different colored bricks award different points. Don't let the ball fall below the paddle or you'll lose a life!

## Features

- 8 rows of colorful bricks (red, orange, green, yellow)
- Score tracking with different point values per brick color:
  - Red: 7 points
  - Orange: 5 points
  - Green: 3 points
  - Yellow: 1 point
- 3 lives per game
- Smooth paddle controls
- Ball physics with collision detection

## Requirements

- Python 3.x
- Pygame

## Installation

```bash
pip install pygame
```

## How to Play

```bash
python3 main.py
```

### Controls

- **Left Arrow**: Move paddle left
- **Right Arrow**: Move paddle right
- **Close Window**: Quit game

## Game Rules

- Break bricks by hitting them with the ball
- Keep the ball from falling below the paddle
- Game ends when all lives are lost
- Try to achieve the highest score possible!
