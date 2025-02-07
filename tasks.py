from invoke import task, Context

USER = "web"
NAME = "fermigier.com"
HOST = "trunks3.abilian.com"
PATH = f"/home/web/{NAME}/"


@task
def deploy(c):
    c.run(f"rsync -e ssh -avz dist/ {USER}@{HOST}:{PATH}/")
    c.run(f"rsync -e ssh -avz extras/ {USER}@{HOST}:{PATH}/")


@task
def setup_nginx(c: Context):
    c.run(f"scp -r nginx.conf root@{HOST}:/etc/nginx/sites-available/{NAME}.conf")
    c.run(f"ssh root@{HOST} ln -sf /etc/nginx/sites-available/{NAME}.conf /etc/nginx/sites-enabled/{NAME}.conf")
    c.run(f"ssh root@{HOST} mkdir -p /var/log/nginx/{NAME}")
    c.run(f"ssh root@{HOST} nginx -t")
    c.run(f"ssh root@{HOST} systemctl restart nginx")
