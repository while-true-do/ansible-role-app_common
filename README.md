<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-app_common.svg)](https://github.com/while-true-do/ansible-role-app_common/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-app_common.svg)](https://github.com/while-true-do/ansible-role-app_common/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-app_common.svg)](https://github.com/while-true-do/ansible-role-app_common/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-app_common.svg)](https://github.com/while-true-do/ansible-role-app_common/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-app_common.svg)](https://travis-ci.com/while-true-do/ansible-role-app_common)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-app_common%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/app_common)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-app_common%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/app_common)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-app_common%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/app_common)

# Ansible Role: app_common

An Ansible Role to install some very common applications.

## Motivation

Some tools and applications are used on a daily basis. Having an automation
to provide these applications is highly appreciated.

## Description

This Role installs some common and basic applications:

-   install vim
-   install tree
-   install screen

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/app_common)
```
ansible-galaxy install while_true_do.app_common
```

Install from [Github](https://github.com/while-true-do/ansible-role-app_common)
```
git clone https://github.com/while-true-do/ansible-role-app_common.git while_true_do.app_common
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.app_common

## Package Management
wtd_app_common_package:
  - vim-enhanced
  - screen
  - tree
# State can be present|latest|absent
wtd_app_common_package_state: "present"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.app_common
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-app_common/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-app_common/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
