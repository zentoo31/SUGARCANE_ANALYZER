import os

folders = ["debugs", "images", "output", "xdxd"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"✅ Carpeta creada: {folder}")
    else:
        print(f"📁 Carpeta ya existe: {folder}")