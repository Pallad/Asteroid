from cx_Freeze import setup, Executable

setup(
    name = "Asteroid",
    version = "1.0",
    description = "Asteroid from PyGame",
    executables = [Executable("Asteroid.py")]
)