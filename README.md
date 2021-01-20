# Battling Knights

## Usage

Use the command `python main.py` to run the application

## Classes

### Knight

**Features**

    id: str
    color: str
    cell: <Cell>
    status: str
    equipped: <Item>
    base_attack_score
    base_defense_score

### Item

**Features**

    name: str
    value: int
    cell: <Cell>
    attack_score: int
    defense_score: int

### Cell

**Features**

    x: int
    y: int
    knight: dict
    items: list


### Board

Class handling the game play and actions. The playing board is created and game actions including moving the knights, attacking and killing knights are defined here.

**Features**

    STATUS: list -> [LIVE, DEAD, DROWNED]

**Methods**

    move(<Knight>, direction: str): Handles a valid move by a knight
    change_position(<Cell>, direction: str): Updates the positions of the knights on the board and returns the new state of the playing board
    attack(<Knight>, <Knight>): Based on the rules provided for attack, a battle is simulated
    kill_knight(<Knight>, status): A fallen knight is nullified and the appropriate status is set


### Utils

A helper class with I/O functions.

**Methods**

    read_moves(): Reads valid moves from `moves.txt`
    save_game(): Saves the final state of the game and its components
    write_to_file(): Writes the final game state to file

### BattlingKnights

**Methods**

    default_board()
    play_game()

## Files
    `moves.txt`: File containing valid moves for the game
    `final_state.json`: File where final game state is written
