# Instructions for demo
```bash
docker build -t ifilonenko/class-demo:v1.0 -f Dockerfile . # build docker image
docker push ifilonenko/class-demo:v1.0 # push docker to public registry
kubectl get nodes # check kubernetes nodes
kubectl run demoapp --image=ifilonenko/class-demo:v1.0 --port=8000 # run on 8000
kubectl get all # check information on all
kubectl expose deployment demoapp --type=LoadBalancer # expose pod via service
kubectl exec -it {CONTAINER_ID} /bin/sh # bash into kubectl pods
wget -qO- {CLUSTER_IP}:8000 # internal IP
kubectl scale deployment demoapp --replicas 3 # scale out app with 3 nodes
# MAKE CHANGES TO APP.py
docker build -t ifilonenko/class-demo:v2.0 -f Dockerfile . # build docker image
docker push ifilonenko/class-demo:v2.0 # push docker to public registry
kubectl edit deployment demoapp # edit deployment with newest version
```
