# 🎮 2-Player Tank Battle Game

> A keyboard-mouse interactive game built with Python Tkinter



## 📚 Table of Contents

1. Description
   - Introduction of the game rules
   - Technologies Used
   - Challenges Faced
   - Future Improvements
2. Installation
3. Usage
4. Contributing
5. Credits
6. License

## 📝 Description

### Intro of rules

Players start with 100 live points, each try to use the keyboard to attack the other tank to make it die (run out of live points). 

Fuel is necessary for the tanks to move/attack, while a basic fuel capacity is 10000 mL. Every second in the game the tank consumes 1 mL, every pixel moving the tank consumes 1 mL, and every time it attacks (whether successful or not) the tank consumes 30 mL.

The tanks have limited shoot range and any attack towards a target that is out of the shoot range is never successful. The basic shoot range is approximately 1/5 of the screen diagonal length.

A basic tank has 35 ammunitions at the beginning of game.

Every successful attack would reduce the opponent's live points, the basic hurt is 6 live points per hit. However, when colliding with the walls or the opponent, the tank would reduce live points every 1.5 seconds upon the collision.

### Game Special Techniques

- #### Long Shooter 

  - 1.5x the basic shoot range

- #### Furious Shooter

  - 1.5x the basic shoot hurt

- #### Auto Aiming

  - You don't have to rotate to aim the opponent (The tank automatically does it)
  - But only 0.7x the basic shoot range, and only half speed and fuel

- #### Resource God

  - 15 more ammunitions

- #### Juggernaut

  - Only 2/3 of hurt when being hit
  - Only half speed and half fuel capacity

- #### Sport Champion

  - 1.5x the basic fuel and speed, and twice the normal rotation speed

- #### Self Heal

  - Gain 1 live point every 150 pixels the tank moves

- #### Gatlin

  - Twice the normal shooting frequency

### Technologies Used

- **Coding Language**: Python (**Tkinter** Package)
- **Development Platform**: Microsoft Visual Studio Code & CodeHS
- **Source Control**: Git & GitHub
- **Markdown File Editing**: Typora

### Challenges Faced


### Future Improvements

- Amongus

## 💾 Installation


## 🎮 Usage


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue.

## 👤 Credits

Author: Ruiqi (Ricky) Tang (he/him)

Created this game on June 6th, 2024; finished on June 20th, 2024

All Rights Reserved

LinkedIn: [Ruiqi Tang](https://www.linkedin.com/in/ruiqi-tang-04a16a2a2/) 

GitHub Profile: [rickytang666](https://github.com/rickytang666)

## 📑 License

This project is MIT licensed.
