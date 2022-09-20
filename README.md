# FastAPI_NER
## 1) Build the Docker Image
docker build -t fastapi_ner:latest .

docker ps -a

## 2) Run the Docker Image
docker run -d --name ner -p 8000:8000 <Image_ID>

docker logs ner

## 3) Checking if the FastAPI code is running or not
curl localhost:8000

## 4) Installing the nginx server
sudo apt install nginx

## 5) Using sudo nano /etc/nginx/sites-enabled/fastapi-demo, make the changes in this file
server {

    listen 80;
    
    server_name <Public_IPV4_EC2>;
    
    location / {
    
        proxy_pass http://127.0.0.1:8000;
        
    }
    
}

## 6) Using sudo nano /etc/nginx/sites-enabled/default, make the changes in this file
server {

        listen 80 default_server;
        
        listen [::]:80 default_server;
        
        root /var/www/html;
        
        index index.html index.htm index.nginx-debian.html;
        
        server_name;
        
        location / {
        
                try_files $uri $uri/ =404;
                
## 7) Start the nginx server 

sudo service nginx restart

## 8) Check the status

systemctl status nginx.service

## 9) Test the POST query on POSTMAN and on FastAPI docs  

e.g 1) 35.93.58.234:80/ner (POSTMAN) and 
    2) http://35.93.58.234/docs (FastAPI docs)
