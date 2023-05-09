Ansible playbook for system info and database update

This Ansible playbook gathers system information such as IP address, CPU details, memory usage, and storage details from a host and stores the data in an SQLite database. It also updates the serial number in the database for macOS hosts.
Usage

To use this playbook, run the following command:

ansible-playbook playbook.yml

Make sure to update the paths to the output file and database file in the tasks as needed.
Requirements

This playbook requires the following:

    Ansible installed on the local machine
    Appropriate permissions to run the commands used in the tasks on the remote hosts

Tasks

The following tasks are performed by this playbook:

    Gather facts about the remote host.
    Get the IP address of the host.
    Get the CPU details of the host.
    Get the memory information of the host.
    Add storage values for the host.
    Get the used RAM in GB for the host.
    Check the OS family of the host and set the computer_type variable accordingly.
    Get the serial number for the host (only on Linux and macOS hosts).
    Update the serial number in the database for macOS hosts.
    Insert the system information into an SQLite database.
    Remove the newline at the end of the output file.

License

This playbook is licensed under the MIT License.
