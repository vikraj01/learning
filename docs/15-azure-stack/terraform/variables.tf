# The settings. Change them in terraform.tfvars, not here.

variable "prefix" {
  description = "Goes into every name. Lowercase letters only (storage account names allow nothing else)."
  type        = string
  default     = "learning"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "uksouth"
}

variable "my_ip" {
  description = "Your laptop's public IP. Only this IP may SSH in. Find it with: curl ifconfig.me"
  type        = string
}

variable "vm_size" {
  description = "2 CPUs, 8 GB RAM, no temporary disk, so /mnt is free for our data disk"
  type        = string
  default     = "Standard_B2s_v2"
}

variable "admin_username" {
  description = "The Linux user you SSH in as"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key_path" {
  description = "Public half of your SSH key (made on page 02)"
  type        = string
  default     = "~/.ssh/azure_learning.pub"
}

variable "data_disk_size_gb" {
  description = "Size of the extra disk that Docker will use"
  type        = number
  default     = 32
}
