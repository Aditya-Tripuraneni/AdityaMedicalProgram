import tkinter as tk
from tkinter import font

"""This code is no longer being updated as its not very maintainble. I first started this project when I was about 14 so
I was just learning Python so that why this is drity code lol. I no longer code like this I promise."""

def response_function(entry):
    if entry.lower() == 'cough':
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Drink Warm Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Gargle With Warm Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.25, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Honey Lemon Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Steam Inhalation", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Bromelain", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Drink More Fluids", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Licorice tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Miso Soup", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Kimchi", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Natural Yogurt", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Marshmallow Root", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Slippery Elm", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Honey", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Bone Broth", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Shower", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.28, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get sleep!", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.28, relheight=0.05)
    elif entry.lower() == "sneeze":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Blow Nose Regularly", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Don't eat too much", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get rest", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Vitamin D", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Moisturize air", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Citrus Fruit", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get enough Zinc", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Chamomile tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Boil Tusli & Ginger", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Chicken Soup", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat your greens!", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stay hydrated", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Spicy Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Teas(Ginger, Mint)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.22, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Nasal Spray", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.22, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Steam Inhalation", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.22, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Berries", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.22, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lemon Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.22, relheight=0.05)
    elif entry.lower() == "sore throat":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Salt Water Gargle", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Honey Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stay Hydrated", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Warm Soup", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Warm Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Root Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Coconut oil", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Peppermint Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Shower", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get Rest", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Slippery Elm", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Chamomile Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Sauce put in", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Warm water & gargle", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Humidifier", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lemon & Honey Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lozenges", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "cold":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Vitamin C", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get Enough Zinc", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stay Hydrated", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Inhale Steam", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Drink", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Wrap Up Warm", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get Enough Rest", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Soups", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Shower", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Menthol Ointment", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Vitamin D", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Honey", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Spice Up Food", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Root", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Gargle", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Packs on ", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="congested sinuses", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "headache":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Try Magnesium", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Try Vitamin B Complex", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stay Hydrated", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Limit Alcohol", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Cold Compress", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get Enough Sleep", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Foods High ", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="In Histamine", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Strong Smells", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Drink Caffeinated Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Do Some Yoga", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Nitrates & Nitrites", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Light Exercise", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Apply Natural Oils", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Healthy Smoothie", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Don't Fill Up On Just Sugar", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "ear pain":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Neck Exercises", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Don't Put Pressure On Ears", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Cold Or Warm Compress Pads", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Naturopathic Drops", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Try To Distract Yourself", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Chiropractic treatment", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hydrogen Peroxide/ H202 ", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add several drops to affected ear",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Rinse Ear Before Adding and After",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger(DO NOT PUT GINGER DIRECTLY IN EAR)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Mix some Olive Oil & Ginger", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add Few drops to affected ear",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Garlic(DO NOT PUT GARLIC DIRECTLY IN EAR)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Mix some Olive Oil & Garlic", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add Few drops to affected ear",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Colloidal Silver", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lavender Oil Behind Ear", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "stomach pain":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Drink Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Lying Down (Acid May Travel Backwards)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Mint Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Smoking/ Alcohol", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Hard To Digest Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lemon Juice, Baking Soda & Water",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add Cumin Seeds To Boiling Water",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add Cinnamon To Boiling Water",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Get Rest", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Mix some Olive Oil & Ginger", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Aloe Juice", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add Basil To Boiling Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Coconut Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Bananas", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Licorice", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="1-2tsp Of Fig Leaves To Make Tea",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "constipation":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Drink More Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Drink Caffeinated Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat More Fiber", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Try Probiotic Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Exercise More", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Try Magnesium Citrate", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Dairy", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Try Prunes Or Prune Juice", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Artichokes", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Pears", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="KiwiFruit", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Sweet Potatoes", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Chia Seeds", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Oat Bran", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Apples", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Brussel Sprouts", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Split Peas (Cooked)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "nausea":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Vitamin B6 supplement", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Control Your Breathing", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat Dried Ginger", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Spicy Or Fatty Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Large Meals", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stay Hydrated", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Strong Smells", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Aromatherapy(lavender,peppermint,rose)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Rest After Eating But Elevate Head",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Cloves", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Sugar & Salt Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Orange Juice", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lemonade", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Drink Beverages Slowly", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Relax Your Muscles", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Try Icy Cold Drinks", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Activity After Exercise",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "fever":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Soups Or Broths", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Juice Or Sports Drinks", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Plenty Of Rest", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lemon & Honey Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Elderberry Syrup", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Peppermint Oil", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Oil", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Apple Cider Vinegar", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Grapes", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Add 1 Garlic Clove To Warm Cup Of Water",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Boil 20 Basil Leaves Add 1 tsp Ginger",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="& Boil Until Solution Is Reduced to 1/2",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stay Cool", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Too Many Blankets", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Coconut Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat Healthy Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Fruits & Vegetables", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "diarrhea":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Eat Small Meals", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Don't Exercise", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Foods That Cause Gas", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Caffeine/Alcohol", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat White Rice", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Dilute Water With Fruit Juice",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Drink Plenty Of Fluid", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Yogurt", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Bananas", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Apple Sauce", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Tea With Chamomile", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Toast", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Beverages With Extreme Temperatures",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Spicy Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lemon Water (IF you have NonaVirus)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Dark Chocolate", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Green Olives", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "gassy":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Chamomile Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Peppermint Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Cloves (Add 2-5 Drops To An 8oz Glass Water)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Don't Over Eat", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat And Drink Slowly", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Chewing Gum",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Smoking", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Tea", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Yogurt & Buttermilk", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Aloe Vera Juice", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Papaya", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Half Tsp Of Carom Seeds With Water", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Jeera Water",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Triphala", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eliminate Foods You Know Cause Gas",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Avoid Greasy Fatty Foods", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Choose Non Carbonated Drinks", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "sore muscles":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Stretch", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Hot Showers", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Epsom Salts (Mix With Tub Of Water)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Lavender Oil (Apply To Affected Area)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Coconut Oil  (Apply To Affected Area)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Keep Hydrated To Avoid Cramps",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Gentle Exercise", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Arnica (Apply To Affected Area)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Put Ice Pack On Affected Area", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Eat More Fiber", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="A Nice Massage", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Practise Good Sleeping Habits",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Tart Cherry Juice",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Magnesium Oil (Apply To Affected Area)", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Apple Cider Vinegar (1-2 Tbs Per Cup Of Water)",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Foam Rolling", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Water Melon Juice",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)
    elif entry.lower() == "shortness of breath":
        label = tk.Label(background, bg="#f0a3ee")
        label.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)
        label = tk.Label(background, bg="#f0a3ee", text="Diaphragmatic Breathing", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.2, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Stand With A Supported Back", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.25, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Sleep In Relaxed Position",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.30, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Pursed Lip Breathing",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.35, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Sitting Forward",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.40, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Practise Yoga",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Give Yourself Steam", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.50, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Ginger Tea",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.55, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Take Your Vitamins",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.60, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Berries", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.65, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Broccoli", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.70, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Cayenne Pepper",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Keep Hydrated",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.80, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Walnuts",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Meditation",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Improve Surrounding Air Quality", font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.90, relwidth=0.2, relheight=0.05)
        label = tk.Label(background, bg="#f0a3ee", text="Humidifier",
                         font=('Times New Roman CYR', 12))
        label.place(relx=0.75, rely=0.95, relwidth=0.2, relheight=0.05)


def get_sneeze_definition():
    sneeze_overlap_label = tk.Label(background, bg="#2e98f0")
    sneeze_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text= "Sneezing can be caused due to seasonal allergies, dust, irritation to the nose or throat.", font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)
    prevention = tk.Label(background, bg="#2e98f0", text= """
    1. Make sure to sneeze in elbow if tissue not available.
    
    2. Throw used tissues in trash.
    
    3. Wash hands for at least 20 seconds with soap.
    
    4. Don't touch surfaces if you haven't washed your hands. 
    
    5. Don't touch your face if you haven't washed your hands. 
    
    6. If soap and water is not available use an alcohol based sanitizer.
    
    7. Don't sneeze into your hands. 
    
    8. Don't spread anything that might be contaminated. 
    
    9. If you are really sick you should probably stay at home to prevent spreading sickness.
    
    10. If asked, use face masks when in doctors clinic.""", font=('Times New Roman CYR', 15, 'bold'))
    prevention.place(rely=0.45, relwidth= 0.75)


def get_cough_definition():
    cough_overlap_label = tk.Label(background, bg="#2e98f0")
    cough_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text="Coughs are usually caused from a respiratory infection like a cold or flu.", font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)
    prevention = tk.Label(background, bg="#2e98f0", text="""
        1. Make sure to cough in elbow if tissue not available.

        2. Throw used tissues in trash.

        3. Wash hands for at least 20 seconds with soap.

        4. Don't touch surfaces if you haven't washed your hands. 

        5. Don't touch your face if you haven't washed your hands. 

        6. If soap and water is not available use an alcohol based sanitizer.

        7. Don't cough into your hands. 

        8. Don't spread anything that might be contaminated. 

        9. Germs can live on surfaces for hours. Try to disinfect surfaces that might be contaminated with your germs. 

        10. If asked, use face masks when in doctors clinic.""", font=('Times New Roman CYR', 15, 'bold'))
    prevention.place(rely=0.45, relwidth=0.75)


def get_sorethroat_definition():
    cough_overlap_label = tk.Label(background, bg="#2e98f0")
    cough_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text="""Sore throats are usually caused by viruses. They take their own time to heal but there are ways to ease pain. 
    However, strep throat is a less common type of sore throat caused by a bacterial infection. 
    This requires antibiotics prescribed by your doctor to prevent further complications.""", font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)


def get_cold_definition():
    cold_overlap_label = tk.Label(background, bg="#2e98f0")
    cold_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text="""Viruses are typically responsible for causing a cold. They usually enter your body through your mouth, eyes or nose. The virus can spread through waterd droplets in the air. 
    One of the reasons why it is important to cover your mouth when you sneeze or cough.
    You can expect a cold to last up to 3 days. Symptoms can range from a sore throat, sneezing,stuffed nose, runny nose, to watery eyes. 
    Its important to get your rest and dispose of used tissues and not touch contaminated surfaces.""",
                           font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)


def get_headache_definition():
    headache_overlap_label = tk.Label(background, bg="#2e98f0")
    headache_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text="""Headaches can be caused for a variety of reasons. They can be caused from stress, sore muscles, too much screen time, sore eyes, lack of sleep, 
    too much processed foods, or you are drinking to much alcohol.""",
                           font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)


def get_earpain_definition():
    earpain_overlap_label = tk.Label(background, bg="#2e98f0")
    earpain_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text="""Ear infections are the most common reasons why people experience ear pain. 
    When the ear experiences pressure, it causes it to become inflamed creating pain.
    Usually someone with an ear infection also experiences other symptoms such as a sinus pressure or a sore throat. 
    The reason being is the ear, mouth, nose and eyes are all connected. """,
                           font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)

def get_stomachpain_definition():
    stomach_overlap_label = tk.Label(background, bg="#2e98f0")
    stomach_overlap_label.place(rely=0.35, relwidth=0.75, relheight=0.6)
    explanation = tk.Label(background, bg="#2e98f0", text="""Stomach pains can be caused by diarrhea, constipation, 
     vomiting, stress. Other reasons can be food poisoning, food allergies, so you want to watch what you are eating.
     If you recognize a pattern try to avoid those foods.""",
                           font=('Times New Roman CYR', 13, 'bold'))
    explanation.place(rely=0.35, relwidth=0.75, relheight=0.1)

def get_constipation_definition():
    pass



def back_arrow_show():
    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Sneeze", font=('Impact', 12),
                                command=lambda: get_sneeze_definition())
    symptom_display.place(relx=-0.09, rely=0.35, relwidth=0.25, relheight=0.10)

    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Cough", font=('Impact', 12),
                                command=lambda: get_cough_definition())
    symptom_display.place(relx=-0.09, rely=0.45, relwidth=0.25, relheight=0.10)

    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Sore Throat", font=('Impact', 12),
                                command=lambda: get_sorethroat_definition())
    symptom_display.place(relx=-0.09, rely=0.55, relwidth=0.25, relheight=0.10)

    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Cold", font=('Impact', 12),
                                command=lambda: get_cold_definition())
    symptom_display.place(relx=-0.09, rely=0.65, relwidth=0.25, relheight=0.10)

    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Headache", font=('Impact', 12),
                                command=lambda: get_headache_definition())
    symptom_display.place(relx=-0.09, rely=0.75, relwidth=0.25, relheight=0.10)

    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Ear Pain", font=('Impact', 12),
                                command=lambda: get_earpain_definition())
    symptom_display.place(relx=-0.09, rely=0.85, relwidth=0.25, relheight=0.10)

    symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Stomach Pain", font=('Impact', 12),
                                command=lambda: get_stomachpain_definition())
    symptom_display.place(relx=0.08, rely=0.35, relwidth=0.23, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Constipation", font=('Impact', 12))
    symptom_display.place(relx=0.08, rely=0.45, relwidth=0.23, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Nausea", font=('Impact', 12))
    symptom_display.place(relx=0.08, rely=0.55, relwidth=0.23, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Fever", font=('Impact', 12))
    symptom_display.place(relx=0.08, rely=0.65, relwidth=0.23, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Diarrhea", font=('Impact', 12))
    symptom_display.place(relx=0.08, rely=0.75, relwidth=0.23, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Gassy", font=('Impact', 12))
    symptom_display.place(relx=0.08, rely=0.85, relwidth=0.23, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Sore Muscles", font=('Impact', 12))
    symptom_display.place(relx=0.22, rely=0.35, relwidth=0.15, relheight=0.10)

    symptom_display = tk.Label(background, bg="#2e98f0", text="Shortness Of Breath", font=('Impact', 12))
    symptom_display.place(relx=.22, rely=0.45, relwidth=0.15, relheight=0.10)


root = tk.Tk()
canvas = tk.Canvas(root, height=440, width=700, )

root.title("Aditya's Natural Remedies Program *ALPHA STAGE*")

background = tk.Frame(root, bg="#2e98f0")  # Complete background of green
background.place(relwidth=1, relheight=1)

note = tk.Label(background, bg="#66ccff", text=" Click On Remedy For Further Info",
                font=('Times New Roman CYR', 13, 'bold'))
note.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.25)

entry = tk.Entry(background, font=('Impact', 13))  # User types in symptoms
entry.place(rely=0.1, relwidth=0.25, relheight=0.25)

# RESPONSE FUNCTION FOR SEARCHING
search_image = tk.PhotoImage(file='Search.png')  # Finally works DONT MESS WITH
search_label_cough = tk.Button(background, bg="#3f48cc", activebackground="#3f48cc", image=search_image,
                               command=lambda: response_function(entry.get()))
search_label_cough.place(relx=0.25, rely=0.1, relwidth=0.25, relheight=0.25)


symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Sneeze", font=('Impact', 12),
                            command=lambda: get_sneeze_definition())

symptom_display.place(relx=-0.09, rely=0.35, relwidth=0.25, relheight=0.10)

symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Cough", font=('Impact', 12),
                            command=lambda: get_cough_definition())
symptom_display.place(relx=-0.09, rely=0.45, relwidth=0.25, relheight=0.10)

symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Sore Throat", font=('Impact', 12),
                            command=lambda: get_sorethroat_definition())
symptom_display.place(relx=-0.09, rely=0.55, relwidth=0.25, relheight=0.10)

symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Cold", font=('Impact', 12),
                            command=lambda: get_cold_definition())
symptom_display.place(relx=-0.09, rely=0.65, relwidth=0.25, relheight=0.10)

symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Headache", font=('Impact', 12),
                            command=lambda: get_headache_definition())
symptom_display.place(relx=-0.09, rely=0.75, relwidth=0.25, relheight=0.10)

symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Ear Pain", font=('Impact', 12),
                            command=lambda: get_earpain_definition())
symptom_display.place(relx=-0.09, rely=0.85, relwidth=0.25, relheight=0.10)

symptom_display = tk.Button(background, bg="#2e98f0", borderwidth=0, text="Stomach Pain", font=('Impact', 12),
                            command=lambda: get_stomachpain_definition())
symptom_display.place(relx=0.08, rely=0.35, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Constipation", font=('Impact', 12))
symptom_display.place(relx=0.08, rely=0.45, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Nausea", font=('Impact', 12))
symptom_display.place(relx=0.08, rely=0.55, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Fever", font=('Impact', 12))
symptom_display.place(relx=0.08, rely=0.65, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Diarrhea", font=('Impact', 12))
symptom_display.place(relx=0.08, rely=0.75, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Gassy", font=('Impact', 12))
symptom_display.place(relx=0.08, rely=0.85, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Sore Muscles", font=('Impact', 12))
symptom_display.place(relx=.22, rely=0.35, relwidth=0.15, relheight=0.10)

symptom_display = tk.Label(background, bg="#2e98f0", text="Shortness Of Breath", font=('Impact', 12))
symptom_display.place(relx=.22, rely=0.45, relwidth=0.15, relheight=0.10)

title = tk.Label(background, bg="#33ffff", text="Welcome To The Natural Remedies Program! *Note This Is Alpha Stage*",
                 font=('Impact', 13))  # Title of program
title.place(relwidth=1, relheight=0.10)

logo = tk.PhotoImage(file='Logo.png')
logo_label = tk.Button(background, bg="#33ffff", activebackground="#33ffff", image=logo, borderwidth=0,
                       command=root.destroy)  # Option to exit program
logo_label.place(relwidth=0.10, relheight=0.10)


remedies_label = tk.Label(background, bg="#ff33e4", text="Remedies", font=('Times New Roman CYR', 14, 'bold'))
remedies_label.place(relx=0.75, rely=0.10, relwidth=0.25, relheight=0.10)

remedies_displayed = tk.Frame(background, bg="#f0a3ee")
remedies_displayed.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.80)

backArrow = tk.Button(background, bg="#18ed8a", borderwidth=0, text="Back", font=('Comic sans', 12, 'bold'),
                      command=lambda: back_arrow_show())
backArrow.place(relx=0.9, relwidth=0.1, relheight=0.1)


canvas.pack()

root.mainloop()

