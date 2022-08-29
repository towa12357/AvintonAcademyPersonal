# Set hostname
nv set system hostname spine01
nv config apply

# Configure BGP
nv set interface lo ip address 10.10.10.101/32
nv set interface swp1-4
nv set router bgp autonomous-system 65199
nv set router bgp router-id 10.10.10.101
nv set vrf default router bgp neighbor swp1 remote-as external
nv set vrf default router bgp neighbor swp2 remote-as external
nv set vrf default router bgp neighbor swp3 remote-as external
nv set vrf default router bgp neighbor swp4 remote-as external
nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
nv config apply
exit