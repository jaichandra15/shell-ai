# ai_shell/command_executor.py
import subprocess

def review_and_execute(command):
    print(f"Suggested command: {command}")
    confirm = input("Execute this command? (y/n): ")
    if confirm.lower() == 'y':
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print("Output:\n", result.stdout)
        if result.stderr:
            print("Error:\n", result.stderr)
    else:
        print("Command execution cancelled.")
