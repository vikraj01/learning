# Storage account names must be unique in all of Azure, so we add 6 random characters.
resource "random_string" "suffix" {
  length  = 6
  upper   = false
  special = false
}

# 9. Storage account: Azure's place for files ("blobs"). Our backups go here.
resource "azurerm_storage_account" "backups" {
  name                            = "st${var.prefix}${random_string.suffix.result}"
  location                        = azurerm_resource_group.rg.location
  resource_group_name             = azurerm_resource_group.rg.name
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  min_tls_version                 = "TLS1_2"
  allow_nested_items_to_be_public = false # nothing in here is public
}

# 10. Container "backups": a folder inside the storage account. (Not a Docker container.)
resource "azurerm_storage_container" "backups" {
  name                  = "backups"
  storage_account_id    = azurerm_storage_account.backups.id
  container_access_type = "private"
}

# 11. Permission: the VM's identity may read and write blobs in this storage account.
resource "azurerm_role_assignment" "vm_writes_backups" {
  scope                = azurerm_storage_account.backups.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_linux_virtual_machine.vm.identity[0].principal_id
}
