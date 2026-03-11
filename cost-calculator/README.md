# Tile Cost Calculator

**Project #6 of the 100 Python Project Series**

Live Preview: [https://TileCostCalculator.onrender.com](https://TileCostCalculator.onrender.com)
GitHub Repository: [https://github.com/nishchup489-afk/TileCostCalculator] (https://github.com/nishchup489-afk/TileCostCalculator)

---

## Overview

The Tile Cost Calculator helps estimate how many tiles are required to cover a room and the total cost based on tile price.

This project demonstrates a simple but practical real‑world calculation implemented using Python and FastAPI.

The application allows users to input:

* Tile price
* Tile size (area)
* Room width
* Room height

The server processes the data and returns the number of tiles required and the total cost.

---

## Tech Stack

* Python
* FastAPI
* Jinja2 Templates
* TailwindCSS
* HTML

---

## How the Calculation Works

First we calculate the total area of the room:

Room Area = Width × Height

Next we determine how many tiles are required.

Tiles Needed = ceil(Room Area ÷ Tile Area)

We use **ceil()** from Python's math module because tiles cannot be purchased in fractions. If the room requires 40.2 tiles, you must buy 41 tiles.

Finally we compute the total cost:

Total Cost = Tiles Needed × Price Per Tile

---

## Example

Room Width: 10 ft
Room Height: 12 ft
Tile Area: 2 sq ft
Tile Price: $5

Room Area = 10 × 12 = 120 sq ft

Tiles Needed = ceil(120 ÷ 2) = 60

Total Cost = 60 × 5 = $300

---

## Project Structure

```
project/
│
├── main.py
├── templates/
│   └── index.html
│
└── static/
```

---

## What This Project Demonstrates

* FastAPI form handling
* Server-side rendering with Jinja2
* Mathematical computation with Python
* Simple responsive UI using TailwindCSS

---

## Run Locally

Install dependencies:

```
pip install fastapi uvicorn jinja2
```

Run the server:

```
uvicorn main:app --reload
```

Open your browser and go to:

```
http://127.0.0.1:8000
```

---

## Footer

Checkout other projects: [https://github.com/nishchup489-afk/100-Python-Projects](https://github.com/nishchup489-afk/100-Python-Projects)

Track your projects: [https://100pyprotracker.vercel.app/](https://100pyprotracker.vercel.app/)
