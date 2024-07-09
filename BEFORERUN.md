## Core Network

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eno1 -j MASQUERADE
sudo iptables -A FORWARD -p tcp -m tcp --tcp-flags SYN,RST SYN -j TCPMSS --set-mss 1400
sudo systemctl stop ufw
sudo systemctl disable ufw

## gNB

sudo ip netns delete ueNameSpace2
sudo ip link delete v-eth2
sudo ip netns add ueNameSpace2
sudo ip link add v-eth2 type veth peer name v-ue2
sudo ip link set v-ue2 netns ueNameSpace2
sudo ip addr add 10.201.1.1/24 dev v-eth2
sudo ip link set v-eth2 up
sudo iptables -t nat -A POSTROUTING -s 10.201.1.0/255.255.255.0 -o eno1 -j MASQUERADE
sudo iptables -A FORWARD -i eno1 -o upfgtp -j ACCEPT
sudo iptables -A FORWARD -o eno1 -i upfgtp -j ACCEPT
sudo ip netns exec ueNameSpace2 ip link set dev lo up
sudo ip netns exec ueNameSpace2 ip addr add 10.201.1.2/24 dev v-ue2
sudo ip netns exec ueNameSpace2 ip link set v-ue2 up

## TO RUN GNB

```bash
sudo ./ran_build/build/nr-softmodem -O ../o-band78-106.conf --gNBs.[0].min_rxtxtime 6 --sa --usrp-tx-thread-config 1  --continuous-tx
```