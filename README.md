# Python3 solutions for [codewars](https://www.codewars.com) problems

![Document PNG](https://github.com/iKostanOrg/codewars/blob/master/img/document.png)

[![Main Build Pipeline](https://github.com/iKostanOrg/codewars/actions/workflows/lint_test_build_pipeline.yml/badge.svg)](https://github.com/iKostanOrg/codewars/actions/workflows/lint_test_build_pipeline.yml)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/iKostanOrg/codewars)
[![Documentation Status](https://readthedocs.org/projects/codewars/badge/?version=latest)](https://codewars.readthedocs.io/?badge=latest)
[![Netlify Status](https://api.netlify.com/api/v1/badges/f14135ff-6f3e-450c-b391-5a677b8f8d8a/deploy-status)](https://app.netlify.com/sites/codewars-allure-report/deploys)
[![CircleCI](https://circleci.com/gh/iKostanOrg/codewars.svg?style=svg)](https://circleci.com/gh/iKostanOrg/codewars)
[![codecov](https://codecov.io/gh/iKostanOrg/codewars/branch/master/graph/badge.svg)](https://codecov.io/gh/iKostanOrg/codewars)
[![CodeFactor](https://www.codefactor.io/repository/github/ikostanorg/codewars/badge)](https://www.codefactor.io/repository/github/ikostanorg/codewars)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/647e16e648f748a28fce36b4895f7729)](https://www.codacy.com/gh/iKostanOrg/codewars?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=iKostanOrg/codewars&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/647e16e648f748a28fce36b4895f7729)](https://app.codacy.com/gh/iKostanOrg/codewars/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/c22e4214ebb0b0626b83/maintainability)](https://codeclimate.com/github/iKostanOrg/codewars/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c22e4214ebb0b0626b83/test_coverage)](https://codeclimate.com/github/iKostanOrg/codewars/test_coverage)
![Maintenance](https://img.shields.io/maintenance/yes/2024)
![GitHub repo size](https://img.shields.io/github/repo-size/iKostanOrg/codewars?color=green)
![GitHub last commit](https://img.shields.io/github/last-commit/iKostanOrg/codewars?color=green)
![Micro badge](https://www.codewars.com/users/myFirstCode/badges/micro)

## About Codewars

Codewars is a collective effort by its users. They are creators - authoring
kata to teach various techniques, solving kata with solutions that enlighten
others, and commenting with constructive feedback. The leaders among them
moderate the content and community.

### Difficulty

*   [8 kyu](https://github.com/ikostan/codewars/tree/master/kyu_8)
*   [7 kyu](https://github.com/ikostan/codewars/tree/master/kyu_7)
*   [6 kyu](https://github.com/ikostan/codewars/tree/master/kyu_6)
*   [5 kyu](https://github.com/ikostan/codewars/tree/master/kyu_5)
*   [4 kyu](https://github.com/ikostan/codewars/tree/master/kyu_4)
*   [3 kyu](https://github.com/ikostan/codewars/tree/master/kyu_3)
*   [2 kyu](https://github.com/ikostan/codewars/tree/master/kyu_2)
*   [1 kyu](https://github.com/ikostan/codewars/tree/master/kyu_1)

### My profile on Codewars

![My Codewars Profile](https://www.codewars.com/users/myFirstCode/badges/large)

### [Ranking](http://www.codewars.com/about)

```bash
8 - 7 kyu │ Beginner
6 - 5 kyu │ Novice
4 - 3 kyu │ Competent
2 - 1 kyu │ Proficient
1 - 5 dan │ Expert
5 - 8 dan │ Master
```

**Note**: For each completed kata, there is a corresponding unittest file.

### Dev Environment

1.  [Python 3.12.3](https://www.python.org/downloads/release/python-3123/)
2.  [PyTest](https://pypi.org/project/pytest/)
3.  [Allure Framework](http://allure.qatools.ru/)
4.  [Win 10 (64 bit)](https://www.microsoft.com/en-ca/software-download/windows10)
5.  [PyCharm 2024.1.1 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)
6.  [GitHub Desktop](https://desktop.github.com/)
7.  [GIT 2.39.1.windows.1](https://git-scm.com/download/win)

### Python Packages

<!-- markdownlint-disable MD013 -->
| No.  |          Package           |                                                                            Description                                                                          |                      Link                   |
|:----:|:--------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------:|
| 1    |       Alabaster            | Alabaster is a visually (c)lean, responsive, configurable theme for the *Sphinx documentation system*. It requires Python 3.10 or newer and Sphinx 6.2 or newer.|[Source](https://pypi.org/project/alabaster/)|
| 2    | | | |
<!-- markdownlint-enable MD013 -->

Full list of dependencies see [here.](https://github.com/iKostanOrg/codewars/blob/master/requirements.txt)

### Online Documentation

Python3 solutions for codewars problems’s documentation is built
with Sphinx using a theme provided by Read the Docs.

Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation, written by Georg Brandl and licensed under
the BSD license. 

[Online version of the latest tech documentation](https://codewars.readthedocs.io/)

### Allure Report

Allure is based on standard xUnit results output but adds some
supplementary data. Any report is generated in two steps. During
test execution (first step), a small library called adapter attached
to the testing framework saves information about executed tests
to XML files.

During report generation (second step), the XML files are transformed
to a HTML report. This can be done with a command line tool, a plugin
for CI or a build tool.

[Online version of the latest Allure report](https://codewars-allure-report.netlify.app/)

## Tech Issues and Problem Solving

<!-- markdownlint-disable MD040 MD033 MD013 MD029 -->
<details>
  <summary>Changing the project interpreter in the PyCharm project settings</summary>

1.  In the **Settings/Preferences dialog** (Ctrl+Alt+S), select
    **Project <project name> | Project Interpreter**.

2.  Expand the list of the available interpreters and click the
    **Show All** link.

3.  Select the target interpreter. When PyCharm stops supporting
    any of the outdated Python versions, the corresponding project
    interpreter is marked as unsupported.

4.  The Python interpreter name specified in the **Name** field,
    becomes visible in the list of available interpreters. Click
    **OK** to apply the changes.

For more info please [check here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
</details>

<details>
  <summary>PyCharm - Choosing Your Testing Framework</summary>
 
1.  Open the Settings/Preferences dialog, and under the node Tools,
    click the page **Python Integrated Tools**.

2.  On this page, click the **Default Test Runner** field.

3.  Choose the desired test runner:

![choosing_test_runner](https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png)

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)
</details>

<details>
  <summary>Setting up Python3 virtual environment on Windows machine</summary>

1.  open CMD
2.  navigate to project directory, for example:
    ```bash cd C:\Users\superadmin\Desktop\Python\CodinGame```
3.  run following command:
    ```bash  pip install virtualenv ```
4.  run following command:
    ```bash virtualenv venv --python=python```

</details>

<details>
  <summary>Setting up Python3 virtual environment on Linx (Ubuntu) machine</summary>

### How to install virtualenv

1.  Install **pip** first:
   ```bash sudo apt-get install python3-pip```
2.  Then install **virtualenv** using pip3:
    ```bash sudo pip3 install virtualenv```
3.  Now create a virtual environment (>you can use any name instead of **venv**):
    ```bash virtualenv venv```
4.  You can also use a Python interpreter of your choice:
    ```bash virtualenv -p /usr/bin/python2.7 venv```
5.  Active your virtual environment:
    ```bash source venv/bin/activate```
6.  Using fish shell:
    ```bash source venv/bin/activate.fish```
7.  To deactivate:
    ```bash deactivate```
8.  Create virtualenv using Python3:
    ```bash virtualenv -p python3 myenv```
9.  Instead of using virtualenv you can use this command in Python3:
    ```bash python3 -m venv myenv```

[Source](https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d)
</details>

<details>
  <summary>Activate Virtual Environment</summary>

In a newly created virtualenv there will be a bin/activate shell script.
For Windows systems, activation scripts are provided for CMD.exe and Powershell.

1.  Open Terminal
2.  Run: `\path\to\env\Scripts\activate`
  
[Source](https://pypi.org/project/virtualenv/1.8.2/)
</details>

<details>
  <summary>Auto generate requirements.txt</summary>

Any application typically has a set of dependencies that are required
for that application to work. The requirements file is a way to specify 
and install specific set of package dependencies at once.

Use pip’s freeze command to generate a requirements.txt file for your project:
```bash
pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide:
[PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html),
or you can:

```bash
pip install -r requirements.txt
```   
[Source](https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/)
</details>

<details>
  <summary>error: RPC failed; curl 56 Recv failure: Connection was reset</summary>

1.  Open Git Bash
2.  Run: "git config --global http.postBuffer 157286400" 
  
[Source](https://stackoverflow.com/questions/36940425/gitlab-push-failed-error)
</details>

<details>
  <summary>How to fix in case .gitignore is ignored by Git</summary>

Even if you haven't tracked the files so far, Git seems to be able to "know"
about them even after you add them to .gitignore

**NOTE:**

*   First commit your current changes, or you will lose them.
*   Then run the following commands from the top folder of your Git repository:

```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```
</details>

<details>
    <summary>Scoop: a command-line installer for Windows</summary>

Installation instructions:

Open a PowerShell terminal (version 5.1 or later) and from the PS C:\> prompt:

1. Set the execution policy:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

[Source](https://scoop.sh/#/)
</details>

<details>
    <summary>Install Allure Report for Windows</summary>

Install from [Scoop](https://scoop.sh/#/):

1. Make sure Scoop is installed. See [the installation instructions on GitHub](https://github.com/ScoopInstaller/Install#readme).
2. Make sure `Java version 8 or higher` installed, and its directory is specified
   in the `JAVA_HOME` environment variable.
3. In a terminal, run this command: `scoop install allure`
4. Run this command to see if it reports the latest version: `allure --version`

[Source](https://allurereport.org/docs/install-for-windows/)
</details>

<details>
  <summary>How to generate Allure report with history trends (Windows OS)</summary>

Step by step:

1. Run tests from pytest using following arguments:
   `-v --alluredir=allure-results`
2. Copy '.\allure-report\history\' folder into '.\allure-results\history\'
3. Run:
   `allure generate .\allure-results\ -o .\allure-report\ --clean`
4. Following output should appear:
   `Report successfully generated to .\allure-report`
5. Run: 
   `allure open .\allure-report\`

[Source](https://github.com/allure-framework/allure2/issues/813)
</details>

<details>
  <summary>Sphinx Documentation Set Up</summary>

Step by step:

1. Create docs directory.
2. Open cmd > Go to docs directory.
3. cmd > Run: `sphinx-quickstart`. **Note:** run with default answers.
4. Go to `docs/conf.py`.
5. Uncomment following lines: 
```python
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
```
6. Update extensions list as following: 
```python 
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```
7. Update template as following: 
```python
html_theme = 'sphinx_rtd_theme'
```
8. Update sys.path.insert as following: 
```python
sys.path.insert(0, os.path.abspath('..'))
```
9. Go to docs/index.rst > add modules, see example below:
```bash
.. toctree::
  :maxdepth: 2
  :caption: Contents:
    
  modules
```
10. Open cmd > run:
```bash
sphinx-apidoc -F -o . ..
```
11. cmd > Run:
```bash
make html
```
12. Install html template:
```bash
pip install sphinx_rtd_theme
```

**More info:**

*   [Video Tutorial](https://www.youtube.com/watch?v=b4iFyrLQQh4)
*   [Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
*   [More Info](https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass)

</details>

<details>
  <summary>Auto-Generated Python Documentation with Sphinx</summary>

Step by step:

1.  Open CMD
2.  Go to docs directory
3.  Run: ```make clean```
4.  Run: ```sphinx-apidoc -F -P -o . ..```
5.  Add doc files name into relevant doc rst file
6.  Run: ```make html```

[Source](https://www.youtube.com/watch?v=b4iFyrLQQh4)
</details>

<details>
  <summary>Read-the-docs build fails with “cannot import name 'PackageFinder' from 'pip._internal.index'</summary>

The issue and the fix are described in read-the-docs issue
[#6554](https://github.com/readthedocs/readthedocs.org/issues/6554):

The fix is to wipe out the build environment as follows (this is taken
from [here](https://docs.readthedocs.io/en/stable/guides/wipe-environment.html)):

*   Log in to read-the-docs
*   Go to Versions
*   Click on the Edit button of the version you want to wipe
    on the right side of the page
*   Go to the bottom of the page and click the wipe link, next
    to the “Save” button
*   Now you can re-build the version with a fresh build environment!

This fix worked for me (but as of 26-Jan-2020 you have to wipe out
the environment for every build, see comment from Grimmy below).

[Source](https://stackoverflow.com/questions/59846065/read-the-docs-build-fails-with-cannot-import-name-packagefinder-from-pip-in)
</details>

<details>
<summary>How to use requirements.txt to install all dependencies in a python project</summary>

1.   Run `pip install -r requirements.txt`
2.   Run `pip freeze > requirements.txt`

[Source](https://intellipaat.com/community/31672/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project)
</details>

<details>
<summary>ERROR: The term 'make' is not recognized as the name of a cmdlet</summary>

The error "'make' is not recognized as an internal or external command, operable program or
batch file" occurs when we run the make command on Windows without having make installed.
To solve the error, install make using Chocolatey.

```bash
make clean
make : The term 'make' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path 
was included, verify that the path is correct and try again.
At line:1 char:1
+ make clean
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (make:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException


Suggestion [3,General]: The command make was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\make". See "get-help about_Command_Precedence" for more details.
```

To install Chocolatey:

1. Open PowerShell as an administrator.
2. Run the following command:
    ```bash
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```
3. Wait for the command to complete.
4. Type choco to make sure Chocolatey is installed:
    ```bash
    PS C:\WINDOWS\system32> choco
    Chocolatey v2.4.1
    Please run 'choco -?' or 'choco <command> -?' for help menu.
    ```
5. Now that you have Chocolatey installed, run the following command to install make:
    ```bash
    PS C:\WINDOWS\system32> choco install make -y
    Chocolatey v2.4.1
    Installing the following packages:
    make
    By installing, you accept licenses for the packages.
    Downloading package from source 'https://community.chocolatey.org/api/v2/'
    Progress: Downloading make 4.4.1... 100%
    
    make v4.4.1 [Approved]
    make package files install completed. Performing other installation steps.
     ShimGen has successfully created a shim for make.exe
     The install of make was successful.
      Deployed to 'C:\ProgramData\chocolatey\lib\make'
    
    Chocolatey installed 1/1 packages.
     See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).
    ```

[Source](https://bobbyhadz.com/blog/make-is-not-recognized-as-internal-or-external-command)
</details>
<!-- markdownlint-restore MD040 MD033 MD013 MD029 -->
