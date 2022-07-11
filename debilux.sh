#!/bin/bash
sudo lb clean

lb config \
--apt-recommends 'true' \
--archive-areas 'main contrib non-free' \
--bootappend-live 'boot=live components quiet splash loglevel=0 username=apprentice' \
--bootappend-live-failsafe 'boot=live components noapic noapm nodma nomce nomodeset nosmp nosplash username=apprentice' \
--chroot-squashfs-compression-type 'zstd' \
--clean \
--color \
--debian-installer 'none' \
--distribution 'bullseye' \
--interactive 'false' \
--memtest 'none' \
--security 'true' \
--system 'live' \
--updates 'true' \
--win32-loader 'false' \
--zsync 'false'

sudo lb build
