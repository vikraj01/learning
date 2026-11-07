# 1. What we're building

So far everything ran on your laptop. Now the notes app (web, api, postgres) runs on a real computer in Azure, with its data on its own disk and backups copied to safe storage.

Think of renting a small flat:

- **Azure** is the building company.
- The **resource group** is your flat: everything you rent sits inside it, and you can hand it all back in one go.
- The **virtual network** is the flat's private corridors, and the **network security group** is the front door with a list of who may come in.
- The **virtual machine** (VM) is the computer in the flat. It comes with one disk for Linux (the **OS disk**). We add a second, empty disk for our data (the **data disk**).
- The **storage account** is a locker in another building. Backups go there, so if the flat burns down, the notes survive.

[Diagram: the whole stack, laptop to Azure](./azure-stack.excalidraw) (open it in VS Code with the Excalidraw extension)

## The steps

| Page | What you do | Where |
| --- | --- | --- |
| 2 | Terraform makes everything in the diagram | laptop |
| 3 | Format the data disk and mount it at `/mnt/data` | VM |
| 4 | Install Docker and make it keep everything on `/mnt/data` | VM |
| 5 | Build the web and api images and push them to Docker Hub | laptop |
| 6 | Run the notes app on the VM, open it from anywhere | VM |
| 7 | Back up the database volume to the storage account, then restore it | VM |

## What goes where

- **Laptop**: you write code, build images, and run Terraform.
- **Docker Hub**: the images wait there until the VM pulls them.
- **VM** `10.0.1.4` inside the network, plus a **public IP** the internet can reach.
    - Port **22** (SSH) is open only to your laptop's IP.
    - Port **80** (the web page) is open to everyone.
    - api and postgres have no open ports. Only web can talk to api, and only api can talk to postgres.
- **OS disk** (30 GB): Linux. It is `/`.
- **Data disk** (32 GB): mounted at `/mnt/data`. Docker keeps images, containers and volumes there, and so the notes too.
- **Storage account**, container `backups`: one `.tar.gz` file per backup.

## What you need on your laptop

```bash
az version          # Azure command line
terraform version   # Terraform
docker version      # Docker
ssh -V              # SSH
```

And two accounts: the Azure account (Vikash logs in for you) and a free Docker Hub account.

!!! warning "A VM costs money while it exists"
    At the end of each session, run `terraform destroy` (page 2). Everything goes away, and next time `terraform apply` makes it again in a few minutes.

## The files

```text
15-azure-stack/
├── terraform/       # page 2: everything in Azure
├── notes-app/
│   ├── web/  api/   # the app (now reads its port from the environment too)
│   ├── compose.yaml # page 6: runs it on the VM, images from Docker Hub
│   └── env.example  # becomes .env on the VM
└── vm/
    ├── backup.sh    # page 7
    └── restore.sh   # page 7
```

## Check yourself

1. Which disk is `/`, and which one holds the notes?
2. Who can reach port 22 on the VM? Who can reach port 80?
3. Why do backups go to a storage account and not to another folder on the VM?

Next: [Terraform builds it](02-terraform.md).
