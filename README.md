# doc-layout
get doc layout

### Usage
Clone and download requirements
```
git clone this repo
conda create -n doc-layout python==3.10
cd doc-layout
pip install -r requirements.txt
```
sh to start

```
./test.sh
```
and then go to [loaclhost:8000/docs]() to use the fastapi

#### docker
use dockerfile to start or use docker-compose to build 

```
####dockerfile
docker build -t lcidentify:latest .
docker run -p 222:8000  -it --name layout layout:latest

### docker-compose

docker-compose up -d --build

```
Visit:`your_deploy_address:222`  on any Web browser
### fast_api
api

"/upload_image/":Identifying detection tables from images

"/upload_pdf/":Identifying detection all the tables from pdf


### Team

xin.wang.xw7@roche.com (AIDD intern)

john.wang.jw6@roche.com
