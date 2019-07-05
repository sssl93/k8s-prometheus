# Note for k8s

### Minikube
- minikube start -p k8svm
- minikube stop k8svm
- minikube ssh -p k8svm

### 可以的镜像仓库
- mirrorgooglecontainers
- registry.cn-hangzhou.aliyuncs.com/google_containers

### kubectl

- kubectl delete --all pods --namespace=default

### kubeadm
<pre>
# 安装单节点集群

systemctl stop firewalld
systemctl disable firewalld
iptables -F && sudo iptables -X && sudo iptables -F -t nat && sudo iptables -X -t nat
iptables -P FORWARD ACCEPT
swapoff -a
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
echo "SELINUX=disabled" > /etc/selinux/config

apt-get update && apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
apt-get update
apt-get install -y kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl

kubeadm init --image-repository registry.cn-hangzhou.aliyuncs.com/google_containers --ignore-preflight-errors=all
</pre>

### 清除正在Terminating的资源
<pre>
NAMESPACE=rook-ceph
kubectl proxy &
kubectl get namespace $NAMESPACE -o json |jq '.spec = {"finalizers":[]}' >temp.json
curl -k -H "Content-Type: application/json" -X PUT --data-binary @temp.json 127.0.0.1:8001/api/v1/namespaces/$NAMESPACE/finalize
</pre>