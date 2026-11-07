# 2. Terraform builds it

You could click everything together in the Azure website. Next time you'd click it all again, and forget one setting.

**Terraform** works like a shopping list you hand to someone. You write down *what* you want (a network, a VM, a disk). Terraform goes and makes it, and remembers what it made. Change the list, and it changes only what's different. Throw the list away (`destroy`), and it hands everything back.

The list is written in `.tf` files, in a language called **HCL**.

## The files in `terraform/`

| File | What's in it |
| --- | --- |
| `providers.tf` | Which plugins to download. `azurerm` talks to Azure, `random` makes a random name suffix. |
| `variables.tf` | The settings, with defaults: region `uksouth`, VM size, disk size, your IP. |
| `network.tf` | Resource group, virtual network `10.0.0.0/16`, subnet `10.0.1.0/24`, network security group (the two door rules), public IP, network card with private IP `10.0.1.4`. |
| `vm.tf` | The Ubuntu VM, its OS disk, the empty 32 GB data disk, and plugging that disk into the VM in slot (LUN) 0. |
| `storage.tf` | The storage account, its `backups` container, and permission for the VM to write there. |
| `outputs.tf` | What to print at the end: public IP, the SSH command, the web address, the storage account name. |

One block, read slowly:

```hcl
resource "azurerm_subnet" "vm" {
  name                 = "snet-vm"
  resource_group_name  = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}
```

- `resource` = "make one of these". `azurerm_subnet` is the kind of thing, `vm` is our nickname for it inside Terraform.
- `name` is the name Azure shows.
- `azurerm_resource_group.rg.name` points at another block. That's how Terraform knows the order: the resource group first, then the network, then the subnet.
- `10.0.1.0/24` means addresses `10.0.1.0` to `10.0.1.255`.

## Step 1: an SSH key

An SSH key is a pair: a **private** half that never leaves your laptop, and a **public** half you give to the VM. The VM lets in whoever holds the matching private half. No password.

```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/azure_learning -N ""
ls ~/.ssh/azure_learning*
```

```text
/home/tanvi/.ssh/azure_learning  /home/tanvi/.ssh/azure_learning.pub
```

## Step 2: log in to Azure

```bash
az login
az account show --query "{name:name, id:id}" -o table
export ARM_SUBSCRIPTION_ID=$(az account show --query id -o tsv)
```

`ARM_SUBSCRIPTION_ID` tells Terraform which subscription (which bill) to use. Set it again in every new terminal.

## Step 3: your IP

Only your laptop may SSH in, so Terraform needs your public IP.

```bash
cd docs/15-azure-stack/terraform
curl ifconfig.me
cp terraform.tfvars.example terraform.tfvars
```

Open `terraform.tfvars` and put your IP in: `my_ip = "81.2.69.160"` (yours will differ). This file stays out of git.

## Step 4: init, plan, apply

```bash
terraform init
```

Downloads the `azurerm` and `random` plugins into `.terraform/`. Run it once per folder.

```bash
terraform plan
```

Shows what it *would* make, and changes nothing. Read it. The last line:

```text
Plan: 14 to add, 0 to change, 0 to destroy.
```

14: resource group, virtual network, subnet, security group, its link to the subnet, public IP, network card, VM, data disk, disk attachment, random suffix, storage account, `backups` container, permission.

```bash
terraform apply
```

It shows the plan again and asks. Type `yes`. The VM takes a few minutes. At the end:

```text
Apply complete! Resources: 14 added, 0 changed, 0 destroyed.

Outputs:

public_ip = "20.26.120.45"
ssh_command = "ssh -i ~/.ssh/azure_learning azureuser@20.26.120.45"
storage_account = "stlearningk3x9qa"
web_url = "http://20.26.120.45"
```

Your IP and storage account name will differ. `terraform output` prints them again any time.

## Step 5: go in

```bash
$(terraform output -raw ssh_command)
```

Type `yes` the first time (SSH asks whether you trust this new computer). You're in:

```text
azureuser@vm-learning:~$
```

You're now typing on the VM in Azure. `exit` brings you back to your laptop.

## The state file

Terraform writes down what it made in `terraform.tfstate`. That's how `plan` knows what already exists. Don't delete it or edit it by hand, and don't commit it (it's in `.gitignore`).

## At the end of each session: destroy

```bash
terraform destroy
```

Type `yes`. All 14 things go away, the backups in the storage account too. Next session: `terraform apply` again, and pages 3 to 7 again on the new VM. It's good practice.

## Check yourself

1. What does `terraform plan` change in Azure?
2. Which line in `network.tf` lets only your laptop in on port 22?
3. You forgot to `destroy` last night. What happens to the bill?

Next: [Mount the data disk](03-mount-the-disk.md).
