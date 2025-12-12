macfinder/
├── src/
│   └── macfinder.py        # Main Python class
│
├── requirements.txt        # Python dependencies
├── start.sh                #class MacBook:
    """
    MacFinder — A simple helper for checking MacBook models (2020+),
    their specs, ideal use cases, and price ranges.
    """

    # --- Static Database ---

    MAC_SPECS = {
        "Apple MacBook Pro (2020)": "Release date: 2020 | Chip: M1 | Display: 13.3\"",
        "Apple MacBook Air (2020)": "Release date: 2020 | Chip: M1 | Display: 13\"",
        "Apple MacBook Air (2022)": "Release date: 2022 | Chip: M2 | Display: 13.6\"",
        "Apple MacBook Pro (2022)": "Release date: 2022 | Chip: M2 | Display: 13.3\"",
        "Apple MacBook Air (2023)": "Release date: 2023 | Chip: M2 | Display: 15.3\"",
        "Apple MacBook Air (2024)": "Release date: 2024 | Chip: M3 | Display: 13.6 / 15.3\"",
        "Apple MacBook Pro (2023)": "Release date: 2023 | Chip: M3 | Display: 14.2 / 16.2\"",
        "Apple MacBook Air (2025)": "Release date: 2025 | Chip: M4 | Display: 13.6\"",
        "Apple MacBook Air (2025) Advanced": "Release date: 2025 | Chip: M4 | Display: 15.3\"",
        "Apple MacBook Pro (2024)": "Release date: 2024 | Chip: M4 Pro/Max | Display: 14.2 / 16.2\"",
        "Apple MacBook Pro (2025)": "Release date: 2025 | Chip: M5 | Display: 14.2\""
    }

    MAC_IDEAL = {
        "Apple MacBook Pro (2020)": "Students, programmers, light creative work.",
        "Apple MacBook Air (2020)": "Portability + performance on a budget.",
        "Apple MacBook Air (2022)": "Students, office, portability.",
        "Apple MacBook Pro (2022)": "Programmers, sustained workloads.",
        "Apple MacBook Air (2023)": "Office users wanting larger display.",
        "Apple MacBook Air (2024)": "Max efficiency users without going Pro.",
        "Apple MacBook Pro (2023)": "3D artists, video editors, heavy workloads.",
        "Apple MacBook Air (2025)": "Students & everyday users, latest gen CPU.",
        "Apple MacBook Air (2025) Advanced": "Light creators needing bigger screen.",
        "Apple MacBook Pro (2024)": "Video editing, 3D, AI dev.",
        "Apple MacBook Pro (2025)": "Users needing top-end performance."
    }

    # New prices by budget tier
    MAC_NEW_PRICE = {
        800: [],
        1000: [
            "Apple MacBook Air (2025) | Brand new: 780 - 900$"
        ],
        1500: [
            "Apple MacBook Air (2024) | Brand new: 1,000 - 1,400$",
            "Apple MacBook Air (2022) | Brand new: 900 - 1,100$",
            "Apple MacBook Pro (2022) | Brand new: 1,200 - 1,500$"
        ],
        2000: [
            "Apple MacBook Pro (2020) | Brand new: 1,499 - 1,899$",
            "Apple MacBook Air (2023) | Brand new: 1,300 - 1,650$"
        ],
        5000: [
            "Apple MacBook Pro (2023) | Brand new: 1,500 - 2,500$",
            "Apple MacBook Pro (2024) | Brand new: 2,100 - 4,400$",
            "Apple MacBook Pro (2025) | Brand new: 1,780 - 2,200$"
        ]
    }

    # Refurbished prices by budget tier
    MAC_REF_PRICE = {
        800: [
            "Apple MacBook Pro (2020) | Refurbished: 588 - 790$",
            "Apple MacBook Air (2020) | Refurbished: 420 - 700$",
            "Apple MacBook Air (2025) | Refurbished: 650 - 800$"
        ],
        1000: [
            "Apple MacBook Air (2022) | Refurbished: 700 - 900$",
            "Apple MacBook Air (2025) | Refurbished: 850 - 1,000$"
        ],
        1500: [
            "Apple MacBook Pro (2022) | Refurbished: 800 - 1,100$",
            "Apple MacBook Air (2023) | Refurbished: 1,000 - 1,300$",
            "Apple MacBook Air (2024) | Refurbished: 800 - 1,200$"
        ],
        2000: [
            "Apple MacBook Pro (2023) | Refurbished: 1,300 - 2,000$",
            "Apple MacBook Pro (2025) | Refurbished: 1,600 - 2,000$"
        ],
        5000: [
            "Apple MacBook Pro (2024) | Refurbished: 1,800 - 3,500$"
        ]
    }

    # --- Object Initialization ---

    def __init__(self, name, exp, model, response, money_av, cond):
        self.name = name
        self.exp = exp
        self.model = model
        self.response = response
        self.money_av = money_av
        self.cond = cond.upper()

    # --- Methods ---

    def intro(self):
        """Print introduction text and user experience rating."""
        print(f"Welcome to MacFinder, {self.name}!\n")

        if not isinstance(self.exp, int) or not (0 <= self.exp <= 5):
            print("Please submit a valid number from 0 to 5.")
            return

        feedback = {
            0: "We are going to try and change that rating!",
            1: "Definitely room for improvement!",
            2: "We are confident this number can grow!",
            3: "We believe we can make it a five!",
            4: "A new champion is emerging!",
            5: "You're already a master — but let's go even further!"
        }

        print("Experience level:", self.exp)
        print(feedback[self.exp])

    def mac(self):
        """Print specs for a chosen MacBook model."""
        print("\nModel specs:")
        print(self.MAC_SPECS.get(self.model, "Invalid MacBook model."))

    def mac_extended(self):
        """Print recommended use-case for a chosen model."""
        print("\nIdeal user profile:")
        print(self.MAC_IDEAL.get(self.response, "Invalid MacBook model."))

    def mac_cash(self):
        """Print price options based on budget and condition."""
        print("\nAvailable MacBooks for your budget:")

        prices = self.MAC_NEW_PRICE if self.cond == "NEW" else self.MAC_REF_PRICE

        matching = []
        for price in prices:
            if price <= self.money_av:
                matching.extend(prices[price])

        if matching:
            for item in matching:
                print(item)
        else:
            print("No models available within this budget.")
├── README.md              # MacFinder
A Python tool that provides specifications, ideal user categories, and pricing information for MacBooks released from 2020 and onward.


## Features
- Lookup MacBook specs (2020–2025)
- Get ideal user categories
- Retrieve brand-new and refurbished price ranges
- Budget-based model suggestions
- Simple interactive Python class


## Project Structure
├── LICENSE                 MIT License


Copyright (c) 2025


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
│
└── website/               <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MacFinder – MacBook Specs 2020+</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; background: #f5f5f7; color: #1d1d1f; }
    header { background: #000; color: white; padding: 20px; text-align: center; font-size: 2rem; }
    .container { max-width: 900px; margin: 40px auto; padding: 20px; background: white; border-radius: 12px; box-shadow: 0 0 15px rgba(0,0,0,0.1); }
    h2 { margin-top: 40px; }
    .section { margin-bottom: 40px; }
    footer { text-align: center; padding: 20px; color: #555; }
    .code-block { background: #eee; padding: 15px; border-radius: 8px; font-family: monospace; white-space: pre-wrap; }
  </style>
</head>
<body>
  <header>MacFinder – MacBook Specs (2020 and Newer)</header>

  <div class="container">
    <h1>Welcome to MacFinder</h1>
    <p>Your simple tool to explore MacBook models (2020+) and their specifications, ideal users, and pricing.</p>

    <h2>✔ Available MacBook Models (2020+)</h2>
    <ul>
      <li>Apple MacBook Pro (2020)</li>
      <li>Apple MacBook Air (2020)</li>
      <li>Apple MacBook Air (2022)</li>
      <li>Apple MacBook Pro (2022)</li>
      <li>Apple MacBook Air (2023)</li>
      <li>Apple MacBook Air (2024)</li>
      <li>Apple MacBook Pro (2023)</li>
      <li>Apple MacBook Air (2025)</li>
      <li>Apple MacBook Air (2025) Advanced</li>
      <li>Apple MacBook Pro (2024)</li>
      <li>Apple MacBook Pro (2025)</li>
    </ul>

    <h2>✔ Python Code (MacFinder Class)</h2>
    <div class="code-block">Your Python code will go here. You can paste the improved version once ready.</div>

    <h2>✔ About This Tool</h2>
    <p>This website is designed to display MacBook model details and act as a public home for your MacFinder script. You can publish this website on GitHub Pages, Google Sites, or any hosting provider.</p>
  </div>

  <footer>
    © 2025 MacFinder Project
  </footer>
</body>
</html>

    └── index.html

