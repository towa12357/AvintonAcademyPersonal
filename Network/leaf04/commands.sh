# Set hostname
nv set system hostname leaf04
nv config apply

# Config BGP
nv set interface lo ip address 10.10.10.4/32
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
nv set mlag backup 10.10.10.3
nv set mlag peer-ip linklocal
nv set interface vlan40 ip address 10.1.40.5/24
nv set interface vlan50 ip address 10.1.50.5/24
nv set interface vlan60 ip address 10.1.60.5/24
nv set bridge domain br_default vlan 40,50,60
nv set bridge domain br_default untagged 1
nv set router bgp autonomous-system 65104
nv set router bgp router-id 10.10.10.4
nv set vrf default router bgp neighbor swp51 remote-as external
nv set vrf default router bgp neighbor swp52 remote-as external
nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.4/32
nv set vrf default router bgp address-family ipv4-unicast redistribute connected
nv config apply
exit
