# Which plugins Terraform downloads, and how it talks to Azure.
terraform {
  required_version = ">= 1.6"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm" # talks to Azure
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random" # makes a random suffix for the storage account name
      version = "~> 3.6"
    }
  }
}

# Logs in with your `az login`. The subscription comes from ARM_SUBSCRIPTION_ID (page 02).
provider "azurerm" {
  features {}
}
