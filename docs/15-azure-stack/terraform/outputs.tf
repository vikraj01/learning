# Printed at the end of `terraform apply`, and any time with `terraform output`.

output "public_ip" {
  value = azurerm_public_ip.vm.ip_address
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/azure_learning ${var.admin_username}@${azurerm_public_ip.vm.ip_address}"
}

output "web_url" {
  value = "http://${azurerm_public_ip.vm.ip_address}"
}

output "storage_account" {
  value = azurerm_storage_account.backups.name
}
