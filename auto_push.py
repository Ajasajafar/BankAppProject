import os 
import subprocess
from datetime import datetime

def auto_push():
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)

        # Create a commit message with current time
        message = f"Auto update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", message], check=True)

        # Push to GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)

        print("✅ Project updated on GitHub successfully!")
    except subprocess.CalledProcessError:
        print("⚠️ No new changes or git error occurred.")

if __name__ == "__main__":
    auto_push()
