import sys

print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")

print(sys.argv) # data which we pass from command line to the script

for arg in sys.argv:
    print(f"Argument: {arg}")