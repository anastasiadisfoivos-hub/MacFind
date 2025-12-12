class Macbook:
print(f"Welcome to MacFinder, {self.name}! Submit any MacBook model from 2020+ and I'll show specs.\n")


if not isinstance(self.exp, int) or not (0 <= self.exp <= 5):
print("Submit a valid whole number from 0–5.")
return


responses = {
0: "We will help raise your search skills!",
1: "There is room for improvement!",
2: "We can help boost that number!",
3: "We believe we can make it a five!",
4: "You're doing great!",
5: "You're already a search master!"
}


print(responses.get(self.exp))


mac_specs = {
"Apple MacBook Pro (2020)": "Release: 2020 | Chip: M1 | Display: 13.3\"",
"Apple MacBook Air (2020)": "Release: 2020 | Chip: M1 | Display: 13\"",
"Apple MacBook Air (2022)": "Release: 2022 | Chip: M2 | Display: 13.6\"",
"Apple MacBook Pro (2022)": "Release: 2022 | Chip: M2 | Display: 13.3\"",
"Apple MacBook Air (2023)": "Release: 2023 | Chip: M2 | Display: 15.3\"",
"Apple MacBook Air (2024)": "Release: 2024 | Chip: M3 | Display: 13.6 / 15.3\"",
"Apple MacBook Pro (2023)": "Release: 2023 | Chip: M3 | Display: 14.2 / 16.2\"",
"Apple MacBook Air (2025)": "Release: 2025 | Chip: M4 | Display: 13.6\"",
"Apple MacBook Air (2025) Advanced": "Release: 2025 | Chip: M4 | Display: 15.3\"",
"Apple MacBook Pro (2024)": "Release: 2024 | Chip: M4 Pro / Max | Display: 14.2 / 16.2\"",
"Apple MacBook Pro (2025)": "Release: 2025 | Chip: M5 | Display: 14.2\""
}


mac_ideal = {
"Apple MacBook Pro (2020)": "Students, coders, light creative users",
"Apple MacBook Air (2020)": "Portable + budget performance",
"Apple MacBook Air (2022)": "Students, office tasks, casual creators",
"Apple MacBook Pro (2022)": "Programmers, medium workloads",
"Apple MacBook Air (2023)": "Users needing larger display",
"Apple MacBook Air (2024)": "Efficiency-focused users",
"Apple MacBook Pro (2023)": "Video editors, 3D artists",
"Apple MacBook Air (2025)": "Everyday users who want latest chip",
"Apple MacBook Air (2025) Advanced": "Light creators needing screen space",
"Apple MacBook Pro (2024)": "Heavy editing, 3D, AI work",
"Apple MacBook Pro (2025)": "Fastest pro laptop available"
}


mac_new_price = {
"Apple MacBook Pro (2020)": "Brand new: $1499 - $1899",
"Apple MacBook Air (2020)": "Brand new: $899 - $1099",
"Apple MacBook Air (2022)": "Brand new: $999 - $1400",
"Apple MacBook Pro (2022)": "Brand new: $1200 - $1500",
"Apple MacBook Air (2023)": "Brand new: $1300 - $1650",
"Apple MacBook Air (2024)": "Brand new: $1000 - $1400",
"Apple MacBook Pro (2023)": "Brand new: $1500 - $2500",
"Apple MacBook Air (2025)": "Brand new: $780 - $900",
"Apple MacBook Air (2025) Advanced": "Brand new: $970 - $1100",
"Apple MacBook Pro (2024)": "Brand new: $2100 - $4400",
"Apple MacBook Pro (2025)": "Brand new: $1780 - $2200"
}


mac_ref_price = {
"Apple MacBook Pro (2020)": "Refurbished: $588 - $790",
"Apple MacBook Air (2020)": "Refurbished: $420 - $700",
"Apple MacBook Air (2022)": "Refurbished: $700 - $900",
"Apple MacBook Pro (2022)": "Refurbished: $800 - $1100",
"Apple MacBook Air (2023)": "Refurbished: $1000 - $1300",
"Apple MacBook Air (2024)": "Refurbished: $800 - $1200",
"Apple MacBook Pro (2023)": "Refurbished: $1300 - $2000",
"Apple MacBook Air (2025)": "Refurbished: $650 - $800",
"Apple MacBook Air (2025) Advanced": "Refurbished: $850 - $1000",
"Apple MacBook Pro (2024)": "Refurbished: $1800 - $3500",
"Apple MacBook Pro (2025)": "Refurbished: $1600 - $2000"
}


def mac(self):
if self.model in self.mac_specs:
print(self.mac_specs[self.model])
else:
print("Invalid model. Make sure it exists in maclist.")


def mac_extended(self):
if self.response in self.mac_ideal:
print(self.mac_ideal[self.response])
else:
print("Invalid model.")


maclist = list(mac_specs.keys())
