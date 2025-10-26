#!/bin/bash
sudo apt remove docker docker-engine docker.io containerd runc
sudo rm -rf /var/lib/docker /var/lib/containerd
sudo apt update
sudo apt upgrade -y
sudo apt install apt-transport-https ca-certificates curl gpg lsb-release -y
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/debian trixie stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo systemctl enable docker --now
sudo systemctl status docker
sudo usermod -aG docker $USER
docker --version
sudo docker run hello-world
