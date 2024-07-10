# Load Balancer Example

This repository contains a simple tutorial demonstrating how to set up a load balancer using Nginx to distribute traffic between multiple Flask application instances.

## Prerequisites

- Python 3.x
- Flask
- Nginx

## Installation

### Step 1: Set Up Flask Applications

Create two Flask applications, each with a `/load` endpoint.

**app1.py:**
**app2.py:**

### Step 2:  Set Up Nginx Load Balancer

### Install nginx
```bash
sudo apt update
sudo apt install nginx
```
### Configure nginx
Open /etc/nginx/sites-available/default in a text editor:
```bash
sudo vi /etc/nginx/sites-available/default
```
Replace the contents with the following configuration:
```nginx
upstream flask_app {
    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
}

server {
    listen 80;

    location / {
        proxy_pass http://flask_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /home {
        proxy_pass http://flask_app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Restart Nginx:
```bash
sudo systemctl restart nginx
```

### Step3: Run the Flask Applications
Run both Flask applications:

In one terminal:
```bash
python3 app1.py
```
In another terminal:
```bash
python3 app2.py
```

### Step4: Access the Load Balanced Application
Open a web browser and go to:


http://localhost/load - You should see responses alternating between "Hello from app1 loader!" and "Hello from app2 loader!" as Nginx distributes the requests between the two Flask instances.

## Conclusion
This example demonstrates how to set up a simple load balancer using Nginx to distribute traffic between multiple Flask application instances, ensuring better performance and reliability.
