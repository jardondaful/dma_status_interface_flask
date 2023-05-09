Sure, here's the updated version:

# 🌟 Ansible playbook for system info and database update 🌟

This Ansible playbook gathers system information such as IP address, CPU details, memory usage, and storage details from a host and stores the data in an SQLite database. It also updates the serial number in the database for macOS hosts.

## Usage

To use this playbook, run the following command:

```bash
ansible-playbook bruh.yml
```

Make sure to update the paths to the output file and database file in the tasks as needed.

## Requirements

This playbook requires the following:

- Ansible installed on the local machine
- Appropriate permissions to run the commands used in the tasks on the remote hosts

## Tasks

The following tasks are performed by this playbook:

### 1. Gather facts 📊

    Gather facts about the remote host.

### 2. Get IP address 🌐

    Get the IP address of the host.

### 3. Get CPU 💻

    Get the CPU details of the host.

### 4. Get memory information 🧠

    Get the memory information of the host.

### 5. Add storage values 💾

    Add storage values for the host.

### 6. Get used RAM 📈

    Get the used RAM in GB for the host.

### 7. Check OS family 💻

    Check the OS family of the host and set the `computer_type` variable accordingly.

### 8. Get serial number on Linux and macOS 🔍

    Get the serial number for the host (only on Linux and macOS hosts).

### 9. Update serial number for macOS 🆕

    Update the serial number in the database for macOS hosts.

### 10. Insert data into SQLite database 💽

    Insert the system information into an SQLite database.

### 11. Remove newline at the end of the file 📎

    Remove the newline at the end of the output file.

## License

This playbook is licensed under the MIT License.
