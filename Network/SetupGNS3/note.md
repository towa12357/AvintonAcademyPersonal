# [GNS3のセットアップ](https://avinton.com/academy/setting-up-gns3/)
## Procedure
- [Download VMware Workstation Player](https://customerconnect.vmware.com/en/downloads/info/slug/desktop_end_user_computing/vmware_workstation_player/16_0)
- Create New Virtual Machine
- [Install GNS3 on Ubuntu](https://docs.gns3.com/docs/getting-started/installation/linux)
```
# Install GNS3
sudo add-apt-repository ppa:gns3/ppa
sudo apt update                                
sudo apt install gns3-gui gns3-server

# If you want IOU support
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install gns3-iou

# To Install Docker CE
sudo apt remove docker docker-engine docker.io
sudo apt-get install apt-transport-https ca-certificates curl \ software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce

# Add your user to the groups
sudo usermod -aG ubridge $USER
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
sudo usermod -aG wireshark $USER
sudo usermod -aG docker $USER
```

## Review
- I tried to run GNS3 on Windows, but could not resolve the error, so we decided to run it on Ubuntu.