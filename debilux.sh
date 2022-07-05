#!/bin/bash
sudo lb clean

lb config \
--apt-recommends 'true' \
--archive-areas 'main contrib non-free' \
--bootappend-live 'boot=live components quiet splash loglevel=0 username=live hostname=debilux' \
--bootappend-live-failsafe 'boot=live components noapic noapm nodma nomce nolapic nomodeset nosmp nosplash vga=788 username=live hostname=debilux' \
--chroot-squashfs-compression-type 'zstd' \
--clean \
--color \
--debian-installer 'live' \
--debian-installer-distribution 'bullseye' \
--debian-installer-gui 'false' \
--distribution 'bullseye' \
--image-name 'debilux-2022.07.05' \
--interactive 'false' \
--iso-application 'debilux' \
--iso-preparer 'willxtreme-https://sourceforge.net/projects/debilux/' \
--iso-publisher 'willxtreme-https://sourceforge.net/projects/debilux/' \
--iso-volume 'debilux' \
--memtest 'none' \
--security 'true' \
--system 'live' \
--updates 'true' \
--win32-loader 'false' \
--zsync 'false'

sudo lb build
