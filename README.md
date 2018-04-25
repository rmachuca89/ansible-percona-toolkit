Ansible Percona Toolkit Role
============================

A simple ansible role to install the [Percona Toolkit](https://www.percona.com/software/database-tools/percona-toolkit) on RHEL/CentOS and Debian/Ubuntu based machines.

Requirements
------------

- A RHEL/CentOS or Debian/Ubuntu based OS target host.
- ansible >= 2.4

Role Variables
--------------

None.

Dependencies
------------

- [ansible-repo-percona](https://github.com/rmachuca89/ansible-repo-percona)

Example Playbook
----------------

```yaml
- hosts: dbs
  roles:
      - percona-toolkit
```

License
-------

Apache 2.0

Author Information
------------------

Rodrigo Machuca
