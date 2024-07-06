![Murder Mystery Discord Bot Banner](https://github.com/DaPandamonium/murderer_bot/blob/main/murderer_mysterybot.png?raw=true)

# Murder Mystery Discord Bot

### A Discord bot for playing a murder mystery game. Players investigate scenes, gather clues, and deduce the murderer, weapon, and crime scene. This project was created as part of the [Codedex Python Final Checkpoint.](https://www.codedex.io/@DaPanda)

## Features

- **Start a New Game**: Begin a new murder mystery game with a set of characters, weapons, and rooms.
- **Investigate**: Players can search different rooms for clues to solve the mystery.
- **Accusations**: Make accusations about the suspect, weapon, and crime scene.
- **Voting**: Players can vote on who they think the suspect is.
- **Hints**: Get hints based on the clues discovered.
- **Random Events**: Periodic random events add atmosphere to the game.
- **Enable/Disable Events**: Toggle random events on or off.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DaPandamonium/murderer_bot.git
   cd murderer_bot
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   Create a file named `.env` in the root directory of the project and add your Discord bot token:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   ```

5. **Run the Bot**:
   ```bash
   python bot.py
   ```

## Commands

### Game Commands
- **`!start_mystery`**: Starts a new murder mystery game.
- **`!search <room>`**: Search a specified room for clues.
- **`!accuse <suspect>, <weapon>, <room>`**: Make an accusation about the suspect, weapon, and room.
- **`!hint`**: Get a hint based on the discovered clues.

### Voting Commands
- **`!vote <suspect>`**: Vote on who you think the suspect is.
- **`!tally_votes`**: Show the current tally of votes.

### Information Commands
- **`!summary`**: Display a summary of all discovered clues.
- **`!toggle_events`**: Enable or disable random events.

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to create an issue or submit a pull request.

### Steps to Contribute

1. **Fork the Repository**: Click on the "Fork" button at the top right of this page.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/DaPandamonium/murderer_bot.git
   cd murderer_bot
   ```
3. **Create a Branch**:
   ```bash
   git checkout -b feature-branch
   ```
4. **Make Your Changes**: Implement your changes in the code.
5. **Commit Your Changes**:
   ```bash
   git commit -m "Description of your changes"
   ```
6. **Push to Your Fork**:
   ```bash
   git push origin feature-branch
   ```
7. **Create a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License.

---

Enjoy solving the mystery!

---
