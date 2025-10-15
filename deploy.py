#!/usr/bin/env python3
"""
Automated deployment script for dev showcase website.
Handles git add, commit, and push operations.
"""

import subprocess
import sys
import os
from datetime import datetime

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"[INFO] {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"[SUCCESS] {description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description} failed")
        print(f"Error: {e.stderr.strip()}")
        return False

def get_commit_message():
    """Get commit message from user or use default."""
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Update dev showcase - {timestamp}"

def deploy_for_ai(commit_message="AI deployment update"):
    """Deployment function that can be called by AI assistant."""
    print("[AI] AI Assistant deployment process...")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("[ERROR] Not in a git repository.")
        return False
    
    print(f"[INFO] Commit message: {commit_message}")
    print()
    
    # Step 1: Git add
    if not run_command("git add .", "Adding files to git"):
        return False
    
    # Step 2: Check if there are changes to commit
    result = subprocess.run("git diff --cached --quiet", shell=True)
    if result.returncode == 0:
        print("[INFO] No changes to commit")
        return True
    
    # Step 3: Git commit
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        return False
    
    # Step 4: Git push
    if not run_command("git push origin main", "Pushing to GitHub"):
        return False
    
    print()
    print("[SUCCESS] AI deployment completed successfully!")
    print("[INFO] Your changes are now live on GitHub")
    return True

def main():
    """Main deployment function."""
    print("[INFO] Starting deployment process...")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("[ERROR] Not in a git repository. Please run this from your project directory.")
        sys.exit(1)
    
    # Get commit message
    commit_message = get_commit_message()
    print(f"[INFO] Commit message: {commit_message}")
    print()
    
    # Step 1: Git add
    if not run_command("git add .", "Adding files to git"):
        sys.exit(1)
    
    # Step 2: Check if there are changes to commit
    result = subprocess.run("git diff --cached --quiet", shell=True)
    if result.returncode == 0:
        print("[INFO] No changes to commit")
        sys.exit(0)
    
    # Step 3: Git commit
    if not run_command(f'git commit -m "{commit_message}"', "Committing changes"):
        sys.exit(1)
    
    # Step 4: Git push
    if not run_command("git push origin main", "Pushing to GitHub"):
        sys.exit(1)
    
    print()
    print("[SUCCESS] Deployment completed successfully!")
    print("[INFO] Your changes are now live on GitHub")
    print("[INFO] Check your Render deployment status")

if __name__ == "__main__":
    main()
