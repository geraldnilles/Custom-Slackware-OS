# Scope
THis document explains how to insatll ZFS on Slackware

# Required Packages
THis is TBD.  On my first run, i installed all of the a,ap,d and l packages.  As I continue experimenting with Slackware, i will trim this list

You will need the entire Linux Kernel source in order to compile spl.  You can get that from the install CD.

# Installation
Download Tarballs

From http://zfsonlinux.org/, download the lasted spl and zfs tarballs

Exract

    tar -xzf spl*
    tar -xzf zfs*
    
Configure and Make SPL

    cd spl*
    ./configure --prefix=/usr --localstatedir=/var --sysconfdir=/etc
    make

Create a temporary directory and install there

    mkdir /tmp/build
    make install DESTDIR=/tmp/build
    

Create a slack-desc file to describe the package

    mkdir /tmp/build/install
    vim /tmp/build/install/slack-desc
    
Use existing packages to see the format

Make the package

    makepkg -l y -c n ../spl-verison-arch-tag.tgz

Install the package on the system

    installpkg ../spl*
    
Remove the temp folder

    rm -r /tmp/build
    
Now repeat the same steps but with ZFS.

Keep in mind ZFS has man pages so you should gunzip the man files before creating the package


## TODO
Create a slackbuild for doing this
