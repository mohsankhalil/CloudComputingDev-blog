name: Deploy to EC2

on:
  push:
    branches:
      - main  # Adjust to your main branch name

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x  # Replace with your Python version

      - name: Install dependencies
        run: |
          python -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

      - name: Run Django development server
        run: |
          source venv/bin/activate
          python manage.py runserver 0.0.0.0:8000 &

      - name: Deploy to EC2
        run: |
          chmod 400 EC2.pem  # Ensure proper file permissions
          ssh -o StrictHostKeyChecking=no -i EC2.pem ec2-user@44.221.30.134 
          # sudo apt update && sudo apt upgrade -y
          # sudo apt-get install yum -y
          # sudo yum update -y
          # sudo yum install git -y 
          # cd ./CloudComputingDev-blog/
          git pull origin main
          source venv/bin/activate 
          pip install -r requirements.txt 
          python manage.py migrate 
          python manage.py collectstatic 
          gunicorn --bind 0.0.0.0:8000 demo.wsgi

  # Add other steps for testing, linting, etc., as needed
