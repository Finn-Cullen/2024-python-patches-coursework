# Patchwork Pattern Generator (Python / Graphix)

An interactive Python program that generates a patchwork-style pattern in a window and lets you edit it live. Choose the size and colours, then click patches to recolour, restyle, move or erase them.

Python project created for coursework at the university of Portsmouth, 2024.

## Features

- **Custom pattern size**: choose how many patches wide and tall the grid is (the window is 500x500)
- **Choose any 3 colours** from red, green, blue, magenta, orange and purple
- **Three patch designs**, built from smaller shapes:
  - **Plain patch**: a solid square, used for the border
  - **"hi!" patch**: a 5x5 grid of outlined squares, each containing text, drawn along the diagonals to form a large X
  - **Triangle patch**: rows of offset triangles filling the interior
- **Live editing** with the mouse and keyboard:
  - Recolour a patch
  - Swap it for a different patch design
  - Erase it
  - Slide it into an empty space with a smooth animation
- **Text scaling**: the "hi!" text shrinks automatically as the pattern gets bigger

## Technologies Used

- Python 3
- [`graphix`](#about-graphix) (drawing library, wraps Tkinter)
- `time` (movement animation)

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (included with most Python installs; on some Linux distros install it with `sudo apt install python3-tk`)
- `graphix.py` in the same folder as the program (see below)

### Installation

```bash
git clone https://github.com/Finn-Cullen/2024-python-patches-coursework.git
cd 2024-python-patches-coursework
```

### Running the Program

```bash
python python patches.py
```

You'll be asked in the terminal for:

1. **The pattern size**, e.g. `5` gives a 5x5 grid (odd numbers work best, so the X crosses at a centre patch)
2. **Three different colours**, entered one at a time. Valid colours are red, green, blue, magenta, orange and purple.

## Controls

Click a patch with the mouse to select it, then use the keyboard:

| Key | Action |
|-----|--------|
| Left mouse button | Select a patch |
| `-` | Deselect the patch |
| `W` `A` `S` `D` | Move the selected patch up, left, down, right (into an empty space only) |
| Up / Down arrow | Scroll through your three colours |
| Left / Right arrow | Scroll through the patch designs |
| `P` | Erase the patch |
| `Esc` | Close the program |

A thick outline shows which patch is selected.

<img width="621" height="622" alt="image" src="https://github.com/user-attachments/assets/b4cc62d2-feae-48e1-8054-5644df89f6ab" />


## How It Works

The window is divided into a `size x size` grid of patches. Each patch is a 5x5 block of smaller shapes, so the size of every shape is calculated as `500 / size / 5`. Which patch goes where depends on its position:

- Edge patches are plain squares
- Patches on the two diagonals are "hi!" patches
- Everything else is a triangle patch

Patches are stored in a list indexed by grid position, which lets the program find, recolour, swap, erase or move whichever patch is clicked.

## Project Structure

```
.
├── python_patches.py   # Main program: pattern generation and interaction
├── graphix.py          # Graphics library provided by the module (see below)
└── README.md
```

## About Graphix

`graphix.py` is a graphics library provided by the module. It is a modified version of John Zelle's `graphics.py` and is released under the GPL. It is included here only so the project runs; it is not my own work.

## Known Limitations

- if patch size is even the pattern wont generate properly
- patches are hardcoded and don't support adding new designs.
- patches can only be moved into empty squares.

## What I Learned

- Using a graphics library to draw and animate shapes
- Handling mouse and keyboard events in a main loop
- Storing and manipulating shapes in a list-based grid
- Generating repeating patterns with nested loops and arithmetic

## Author

**Finn Cullen** - [GitHub](https://github.com/Finn-Cullen)
