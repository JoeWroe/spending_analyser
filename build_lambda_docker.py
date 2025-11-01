#!/usr/bin/env python3
"""
Build Lambda deployment package using Docker to ensure Linux compatibility
"""
import os
import subprocess
import shutil
import tempfile

def build_database_setup_lambda():
    """Build the database setup Lambda package using Docker"""
    
    # Use local build directory to avoid permission issues
    build_dir = "./lambda_build"
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    # Copy source files to build directory
    os.makedirs(f"{build_dir}/app/handlers", exist_ok=True)
    os.makedirs(f"{build_dir}/app/models", exist_ok=True)
    
    # Copy Python files
    shutil.copy("app/handlers/database_setup.py", f"{build_dir}/database_setup.py")
    shutil.copy("app/database.py", f"{build_dir}/app/database.py")
    shutil.copy("app/models/transaction.py", f"{build_dir}/app/models/transaction.py")
    
    # Create __init__.py files
    open(f"{build_dir}/app/__init__.py", 'a').close()
    open(f"{build_dir}/app/handlers/__init__.py", 'a').close()
    open(f"{build_dir}/app/models/__init__.py", 'a').close()
    
    # Create requirements file for Lambda dependencies
    with open(f"{build_dir}/requirements.txt", "w") as f:
        f.write("sqlalchemy==2.0.44\n")
        f.write("psycopg2-binary==2.9.11\n")
        f.write("python-dotenv==1.2.1\n")
        f.write("typing-extensions==4.15.0\n")
    
    # Get absolute path for Docker mount
    abs_build_dir = os.path.abspath(build_dir)
    
    # Use Docker to install dependencies with Linux ARM64 compatibility (matches Lambda arm64)
    docker_cmd = [
        "docker", "run", "--rm", "--entrypoint", "", "-w", "/var/task",
        "-v", f"{abs_build_dir}:/var/task",
        "public.ecr.aws/lambda/python:3.11-arm64",
        "sh", "-c", "pip install -r requirements.txt -t ."
    ]
    
    print("Building Lambda package with Docker...")
    result = subprocess.run(docker_cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Docker build failed: {result.stderr}")
        return False
    
    # Create output directory
    output_dir = "infra/lambda"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create zip file
    zip_path = f"{output_dir}/database_setup.zip"
    if os.path.exists(zip_path):
        os.remove(zip_path)
    
    # Create zip from build directory
    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', build_dir)
    
    print(f"✅ Lambda package created: {zip_path}")
    
    # Clean up build directory
    shutil.rmtree(build_dir)
    
    return True

if __name__ == "__main__":
    success = build_database_setup_lambda()
    exit(0 if success else 1)