The goal of this is to make a game whereyou can travel to other star systems and trade and stuff.
For whatever reason it got into my head to make it semi-realistic.... and make an annoyingly large file out of it.

Feel free to start with main.py and type the command /help
Current functionality is to generate moons, planets, and galaxies only using the commands

at the very least, so far you can get semi-realistic planet characteristics
(this includes Gravity, Mass, Radius, Density, and volume)

For science info:
Planet densities are determined on two things, if the planet is gasseous or rocky





How Density is determined (Planets Only, moons will come later with accurate density):
If the planet is Gasseous (in the case for Ice Giants and Gas Giants), only the
cores and atmosphere will affect the density.

If the planet is Rocky, the density will be affected by the Core, Mantle, and Crust.

Elements used and layers holding those elements along with the g/cm^3

Due to how the data is stored, adding elements is as simple as adding it to the elements list and including it
in whichever layers suit it most

**Hydrogen and Helium are gasses and thus cannot actually be measured in g/cm^3, but if i ever figure out how to
get it working in liters, that will come.

This can be edited in the Getcoreterra() function in Planetmaker.py around line 300
(Despite the name, it works for both gas and rocky planets. Originally they were meant to be separate)
   elements =
            "Ice": 0.9,
            "Iron": 7.8,
            "Nickel": 8.9,
            "Rock": 2.6,
            "Sulfur": 2.1,
            "Silicon": 2.3,
            "Oxygen": 1.2,
            "Magnesium": 1.7,
            "Aluminum": 2.7,
            "Potassium": 0.8,
            "Hydrogen": 0.007,
            "Helium": 0.002

        core = Iron, Nickel
        mantle = Sulfur, Oxygen, Silicon, Magnesium
        crust = Ice, Rock, Sulfur, Silicon, Oxygen, Magnesium, Aluminum, Potassium, Iron, Nickel
        atmosphere = Hydrogen, Helium

