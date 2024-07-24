#!/bin/bash
echo "---- Setting OAI Network Considerations... ------"

for ((i=0;i<$(nproc);i++)); do sudo cpufreq-set -c $i -r -g performance; done
sysctl -w net.core.wmem_max=62500000
sysctl -w net.core.rmem_max=62500000
sysctl -w net.core.wmem_default=62500000
sysctl -w net.core.rmem_default=62500000
ethtool -G enp3s0f1 tx 4096 rx 4096
