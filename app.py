import codellama
import os

# read scripts that end with ".nlp" from directory "scripts"
scripts = [f for f in os.listdir("scripts") if f.endswith(".nlp")]

# print out a list of script's names and ask which one to run
for i, script in enumerate(scripts):
    print(f"{i}: {script}")
    print()

script_number = input("Which script would you like to run NLP2PY on? ")
script_number = int(script_number)
script = scripts[script_number]

# translate the script from natural language into python
translated_script = codellama.translate_code("natural", "python", script)

# run the translated script
os.system(translated_script)
