#!/usr/bin/env python3
"""
Setup script for Medicinal Plant AI Classifier
Automates the installation and setup process
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def check_python_version():
    """Check if Python version is compatible"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python 3.8+ required. Current version: {version.major}.{version.minor}")
        return False
    
    print(f"✅ Python version {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_requirements():
    """Install required packages"""
    print_header("Installing Dependencies")
    
    try:
        # Check if requirements.txt exists
        if not os.path.exists("requirements.txt"):
            print("❌ requirements.txt not found")
            return False
            
        print("Installing packages from requirements.txt...")
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print("❌ Failed to install dependencies")
            print("Error:", result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error during installation: {e}")
        return False

def verify_installation():
    """Verify that all required packages are installed"""
    print_header("Verifying Installation")
    
    required_packages = [
        "tensorflow",
        "streamlit", 
        "PIL",
        "numpy"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == "PIL":
                import PIL
            else:
                __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - MISSING")
            missing_packages.append(package)
    
    return len(missing_packages) == 0

def check_model_file():
    """Check if model file exists"""
    print_header("Checking Model File")
    
    model_path = "medicinal_plant_classifier.h5"
    if os.path.exists(model_path):
        size = os.path.getsize(model_path) / (1024 * 1024)  # Size in MB
        print(f"✅ Model file found ({size:.1f} MB)")
        return True
    else:
        print("❌ Model file not found")
        print("Please ensure 'medicinal_plant_classifier.h5' is in the project directory")
        return False

def test_model_loading():
    """Test if model can be loaded successfully"""
    print_header("Testing Model Loading")
    
    try:
        from utils import load_model
        model = load_model()
        if model is not None:
            print("✅ Model loaded successfully")
            return True
        else:
            print("❌ Failed to load model")
            return False
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def create_startup_script():
    """Create a convenient startup script"""
    print_header("Creating Startup Script")
    
    script_content = """#!/bin/bash
# Medicinal Plant AI Classifier Startup Script

echo "Starting Medicinal Plant AI Classifier..."
streamlit run app.py
"""
    
    if platform.system() == "Windows":
        script_content = """@echo off
REM Medicinal Plant AI Classifier Startup Script

echo Starting Medicinal Plant AI Classifier...
streamlit run app.py
pause
"""
        script_name = "start_app.bat"
    else:
        script_name = "start_app.sh"
    
    try:
        with open(script_name, "w") as f:
            f.write(script_content)
        
        # Make executable on Unix systems
        if platform.system() != "Windows":
            os.chmod(script_name, 0o755)
            
        print(f"✅ Created startup script: {script_name}")
        return True
    except Exception as e:
        print(f"❌ Failed to create startup script: {e}")
        return False

def main():
    """Main setup function"""
    print_header("Medicinal Plant AI Classifier - Setup")
    print("This script will set up your environment for the application")
    
    # Run setup steps
    steps = [
        ("Python Version Check", check_python_version),
        ("Install Dependencies", install_requirements),
        ("Verify Installation", verify_installation),
        ("Check Model File", check_model_file),
        ("Test Model Loading", test_model_loading),
        ("Create Startup Script", create_startup_script)
    ]
    
    failed_steps = []
    
    for step_name, step_function in steps:
        try:
            if not step_function():
                failed_steps.append(step_name)
        except Exception as e:
            print(f"❌ Error in {step_name}: {e}")
            failed_steps.append(step_name)
    
    # Final summary
    print_header("Setup Complete")
    
    if not failed_steps:
        print("🎉 Setup completed successfully!")
        print("\nYou can now run the application using:")
        print("  streamlit run app.py")
        print("\nOr use the startup script:")
        if platform.system() == "Windows":
            print("  start_app.bat")
        else:
            print("  ./start_app.sh")
    else:
        print(f"⚠️  Setup completed with {len(failed_steps)} issues:")
        for step in failed_steps:
            print(f"  - {step}")
        print("\nPlease check the errors above and try again.")

if __name__ == "__main__":
    main()