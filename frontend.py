import nginx
def frontend():
    yum install nginx -y
    systemctl enable nginx
    systemctl start nginx
    rm -rf /usr/share/nginx/html/*

frontend()
