# Increases the limits on my system and Nginx so large requests are processed

exec { 'increase_system_limits':
  command => 'echo -e "* soft nofile 65535\n* hard nofile 65535\n" >> /etc/security/limits.conf && echo "fs.file-max = 100000" >> /etc/sysctl.conf && sysctl -p',
  unless  => 'grep -q "fs.file-max = 100000" /etc/sysctl.conf',
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

file { '/etc/nginx/nginx.conf.erb':
  ensure  => file,
  content => @("EOF"),
worker_processes auto;

worker_rlimit_nofile 65535;

events {
    worker_connections 8192;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
  | EOF
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/nginx.conf'],
}
