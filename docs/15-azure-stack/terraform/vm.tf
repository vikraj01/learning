# 7. The virtual machine: Ubuntu 24.04, logs in with your SSH key only (no password).
resource "azurerm_linux_virtual_machine" "vm" {
  name                  = "vm-${var.prefix}"
  location              = azurerm_resource_group.rg.location
  resource_group_name   = azurerm_resource_group.rg.name
  size                  = var.vm_size
  admin_username        = var.admin_username
  network_interface_ids = [azurerm_network_interface.vm.id]

  admin_ssh_key {
    username   = var.admin_username
    public_key = file(pathexpand(var.ssh_public_key_path))
  }

  # The OS disk: Linux itself lives here. It becomes / inside the VM.
  os_disk {
    name                 = "disk-os-${var.prefix}"
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
    disk_size_gb         = 30
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "ubuntu-24_04-lts"
    sku       = "server"
    version   = "latest"
  }

  # Gives the VM its own identity in Azure, so it can upload backups without any password or key (page 07).
  identity {
    type = "SystemAssigned"
  }
}

# 8. The data disk: an empty extra disk. Inside the VM we format it and mount it at /mnt/data (page 03).
resource "azurerm_managed_disk" "data" {
  name                 = "disk-data-${var.prefix}"
  location             = azurerm_resource_group.rg.location
  resource_group_name  = azurerm_resource_group.rg.name
  storage_account_type = "Standard_LRS"
  create_option        = "Empty"
  disk_size_gb         = var.data_disk_size_gb
}

# Plug the data disk into the VM, in slot (LUN) 0.
resource "azurerm_virtual_machine_data_disk_attachment" "data" {
  managed_disk_id    = azurerm_managed_disk.data.id
  virtual_machine_id = azurerm_linux_virtual_machine.vm.id
  lun                = 0
  caching            = "ReadWrite"
}
