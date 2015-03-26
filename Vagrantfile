# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "derek-adair/vbox-flex-api"

  config.vm.network :public_network, ip: "192.168.0.103", bridge: 'eth0'
  config.vm.network :forwarded_port, guest: 5000, host: 5000, auto_correct: true
  config.vm.network :forwarded_port, guest: 22, host: 22258, auto_correct: true
  config.vm.network :forwarded_port, guest: 8080, host: 8080, auto_correct: true

  # Forward X11
  config.ssh.forward_x11 = true

 ## Using NFS as it has much better performance
 ## On linux install nfs-kernel-server, MacOS works by default
 ## Will ask for root password to set some things up
 config.vm.synced_folder ".", "/application", :nfs => true
end
