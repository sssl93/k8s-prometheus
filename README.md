# k8s_prometheus

### Before Apply
- 修改etcd配置
<pre>
修改监听地址为0.0.0.0
生成etcd-secret
kubectl -n monitoring create secret generic etcd-certs --from-file=/tmp/etcd/healthcheck-client.crt --from-file=/tmp/etcd/healthcheck-client.key --from-file=/tmp/etcd/ca.crt

</pre>
- 修改kubelet配置
<pre>
vi /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
添加命令: --authentication-token-webhook=true  --authorization-mode=Webhook
</pre>