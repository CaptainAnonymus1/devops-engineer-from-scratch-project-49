# Project Description

## Hexlet tests and linter status

[![Actions Status](https://github.com/CaptainAnonymus1/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/CaptainAnonymus1/devops-engineer-from-scratch-project-49/actions)

## SonarQube badges

[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-dark.svg)](https://sonarcloud.io/summary/new_code?id=CaptainAnonymus1_devops-engineer-from-scratch-project-49)

| | | |
| :---: | :---: | :---: |
|[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=CaptainAnonymus1_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=CaptainAnonymus1_devops-engineer-from-scratch-project-49) | [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=CaptainAnonymus1_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=CaptainAnonymus1_devops-engineer-from-scratch-project-49) | [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=CaptainAnonymus1_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=CaptainAnonymus1_devops-engineer-from-scratch-project-49) |

## Description

Pure **Python** with no complex dependencies - only the *prompt* library.
Modular architecture make it easy to create additional games.
Reusable game engine for all games in the pack.

Target Audience:

+ For practicing mental arithmetic
+ For learning programming (as an example of a console game)
+ For beginners learning Python (simple logic, clear code)

## Game Description

The Project consist of five games which are simple yet effective games for practicing basic math skills!

**How to Play:**

Game Start:

+ The game greets you and asks for your name.
Than explains the task.

Game Process:

+ A question appears on screen.
+ The player must enter the correct answer.
+ You need to answer correctly for 3 rounds to win.
+ The game ends immediately upon the first mistake, inviting the player to try again.

## ASCIINEMA

[Video on web for brain-games](https://asciinema.org/a/mUAf9O7Tj3KzZZokwYFZAJj7l)

[Video on web for brain-calc]( https://asciinema.org/connect/4661f7e3-a884-4be5-b5b6-a954dd3b73ea)

[Video on web for brain-gcd](https://asciinema.org/connect/4661f7e3-a884-4be5-b5b6-a954dd3b73ea)

[Video on web for brain-even]( https://asciinema.org/connect/4661f7e3-a884-4be5-b5b6-a954dd3b73ea)

[Video on web for brain-prime](  https://asciinema.org/a/p8gkSEiBJqz4hyQj)

[Video on web for brain-progression]( https://asciinema.org/connect/4661f7e3-a884-4be5-b5b6-a954dd3b73ea)

### Links

This project was built using these tools:

| Tool                                 | Description                                                             |
|--------------------------------------|-------------------------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)     | "An extremely fast Python package and project manager, written in Rust" |
| [PyPI](https://pypi.org)             | " The Python Package Index "                                            |
| [ruff](https://docs.astral.sh/ruff/) | An extremely fast Python linter and code formatter, written in Rust"    |

### Setup

```bash
make install
```

### Installation

```bash
make package-install
```

### Test

```bash
make lint
```

### Examples to start a game

```bash
brain-game
brain-calc
brain-even
brain-gcd
brain-prime
brain-progression

```
