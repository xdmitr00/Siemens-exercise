# How to run
- In project directory run `docker compose up`
- It make take some time until MySQL container starts and is ready to accept inputs from python container, watch python container output to see when it enters data into MySQL
- Visit http://localhost:3000 ; enter username:admin password admin ; click Skip when asked to change password
- On left panel select Dashboards > Browse and select dashboard General > Sinus

Dockerfile reference: https://docs.docker.com/engine/reference/builder/
Docker-compose reference: https://docs.docker.com/compose/compose-file/
Grafana docker configuration: https://grafana.com/docs/grafana/latest/administration/provisioning/