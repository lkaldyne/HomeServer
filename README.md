# homeserver

## Setup
### DNS
- Set up DDNS in cronjob: https://www.duckdns.org/install.jsp
- Setup CNAME record in domain provider to new duckdns subdomain
- Set up port forwarding as applicable on router

### Set up storage drive
- Create filesystem on drive (`mkfs -t ext4 /dev/sda`)
- Add drive to fstab file so it's mounted on startup
- Reboot to verify fstab
- Create /mnt/sda/media for jellyfin
