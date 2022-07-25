#!/bin/bash
sudo lb clean

lb config \
--apt-recommends 'true' \
--archive-areas 'main contrib non-free' \
--bootappend-live 'boot=live components quiet splash loglevel=0 username=apprentice hostname=debilux' \
--bootappend-live-failsafe 'boot=live components noapic noapm nodma nomce nomodeset nosmp nosplash username=apprentice hostname=debilux' \
--chroot-squashfs-compression-type 'zstd' \
--clean \
--color \
--debian-installer 'none' \
--distribution 'testing' \
--interactive 'false' \
--memtest 'none' \
--security 'false' \
--system 'live' \
--updates 'false' \
--win32-loader 'false' \
--zsync 'false'

sudo lb build
