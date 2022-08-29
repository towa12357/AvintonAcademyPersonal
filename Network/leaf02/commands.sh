# Set hostname
nv set system hostname leaf02
nv config apply

# Config BGP
nv set interface lo ip address 10.10.10.2/32
nv set interface swp1-3,swp49-52
nv set interface bond1 bond member swp1
nv set interface bond2 bond member swp2
nv set interface bond3 bond member swp3
nv set interface bond1 bond mlag id 1
nv set interface bond2 bond mlag id 2
nv set interface bond3 bond mlag id 3
nv set interface bond1-3 bridge domain br_default 
nv set interface peerlink bond member swp49-50
nv set mlag mac-address 44:38:39:BE:EF:AA
nv set mlag backup 10.10.10.1
nv set mlag peer-ip linklocal
nv set interface vlan10 ip address 10.1.10.3/24
nv set interface vlan20 ip address 10.1.20.3/24
nv set interface vlan30 ip address 10.1.30.3/24
nv set bridge domain br_default vlan 10,20,30
nv set bridge domain br_default untagged 1
nv set router bgp autonomous-system 65102
nv set router bgp router-id 10.10.10.2
nv set vrf default router bgp neighbor swp51 remote-as external
nv set vrf default router bgp neighbor swp52 remote-as external
nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.2/32
nv set vrf default router bgp address-family ipv4-unicast redistribute connected
nv config apply
exit