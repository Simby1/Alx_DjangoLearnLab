# Deployment Security

To support HTTPS, the production server (e.g., Nginx) must be configured with an SSL certificate (via Let's Encrypt).

## Nginx Example Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$server_name$request_uri; # Redirect HTTP to HTTPS
}
```
