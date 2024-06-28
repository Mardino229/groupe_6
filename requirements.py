import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Liste des packages à installer
packages = [
    "tk",
    "diffusers",
    "torch",
    "transformers",
    "Pillow"
]

for package in packages:
    install(package)
