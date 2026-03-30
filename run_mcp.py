# run_mcp.py
import os
import subprocess
import sys
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

ASCII_ART = r"""
    ⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀
    ⠀⢀⣤⣾⣿⣾⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀
    ⢠⣾⣿⢛⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
    ⣾⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⡿⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⢿⡵
    ⢸⡇⠀⠀⠉⠛⠛⣿⣿⠛⠛⠉⠀⠀⣿⡇
    ⢸⣿⣀⠀⢀⣠⣴⡇⠹⣦⣄⡀⠀⣠⣿⡇
    ⠈⠻⠿⠿⣟⣿⣿⣦⣤⣼⣿⣿⠿⠿⠟⠀
    ⠀⠀⠀⠀⠸⡿⣿⣿⢿⡿⢿⠇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⠁⠈⠁⠀⠀⠀⠀⠀⠀
    Saifullah's MCP Summarizer
"""

def main():
    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Display ASCII art in green
    print(Fore.GREEN + ASCII_ART)
    time.sleep(1)  # small pause for effect

    while True:
        file_path = input("\nEnter the file path to summarize (or type 'exit' to quit): ").strip()

        if file_path.lower() in ['exit', 'q']:
            print("Exiting MCP Summarizer. Goodbye!")
            sys.exit(0)

        if not os.path.exists(file_path):
            print(f"File '{file_path}' does not exist. Please try again.")
            continue

        # Call app.py as a subprocess
        subprocess.run([sys.executable, "app.py", file_path])

        # After finishing one file, ask if user wants to summarize another
        again = input("\nDo you want to summarize another file? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("Exiting MCP Summarizer. Goodbye!")
            break

if __name__ == "__main__":
    main()