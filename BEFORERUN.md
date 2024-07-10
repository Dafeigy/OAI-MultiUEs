# Requirements

Your UHD version should be >= v4.6.0.0, otherwise a serious multi-thread scheduling problem may hinder your dedicated task. This branch is maintained in a single main branch, no other branch will be developed.

To start, modify MACROs in `openair1/SCHED_NR/phy_procedures_nr_gNB.c`:

- `#define NUM_GNB_RX`:      Num of gNB RX ants

- `#define NUM_UE_PORTS`:    Num of UE ports

- `#define NUM_PRBS` :       Num of SRS PRB

- `#define TARGET_UEs`:     Num of target UE connected 

```bash
for ((i=0;i<$(nproc);i++)); do sudo cpufreq-set -c $i -r -g performance; done
sudo sysctl -w net.core.wmem_max=62500000
sudo sysctl -w net.core.rmem_max=62500000
sudo sysctl -w net.core.wmem_default=62500000
sudo sysctl -w net.core.rmem_default=62500000
sudo ethtool -G enp3s0f1 tx 4096 rx 4096
```


`DO_PROTO` and `DO_LOCAL` are also need to be configured. After all macros all configured, run the build command:

```bash
cd cmake_targets
sudo ./build-oai -w USRP --gNB --ninja 
```
# Network considerations
To verified UE's communication behavior, network should be configured as follow. In my setup, Free5GC and OAI are run at the same host machine@192.168.3.6. Therefore, the configuration should be :
## Core Network

```bash
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eno1 -j MASQUERADE
sudo iptables -A FORWARD -p tcp -m tcp --tcp-flags SYN,RST SYN -j TCPMSS --set-mss 1400
sudo systemctl stop ufw
sudo systemctl disable ufw
```

## gNB
```bash
```bash
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
```

## TO RUN GNB

```bash
sudo ./ran_build/build/nr-softmodem -O ../o-band78-106.conf --gNBs.[0].min_rxtxtime 6 --sa --usrp-tx-thread-config 1  --continuous-tx --tun-offset 20000000
```

