from pathlib import Path

path = Path("eccommercePackage")
print(path.exists()) #boolean


path = Path("emails")
print(path.mkdir())


path = Path("emails")
print(path.rmdir())


path1=Path()
#glob to search for directories/folder in current path
#gives generator obj can loop through it
print(path.glob('*')) #all files and directories 
print(path.glob('*.*')) #all files in current directory
print(path.glob('*.py')) # all py files in current directory

for files in path.glob('*.py'):
    print(files)