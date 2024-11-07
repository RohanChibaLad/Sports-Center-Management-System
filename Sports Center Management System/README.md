[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/BsFdJ6lI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-f4981d0f882b2a3f0472912d15f9806d57e124e0fc890972558857b51b24a6f9.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=10163540)

# Squad User Manual

## Prerequisites

1. Download PyCharm from https://www.jetbrains.com/pycharm/download/#section=windows. Shouldn't matter which version you
   choose, but if you choose the Professional version you will be prompted to make a JetBrains account and prove you are
   a student to get it for free.
2. Download Python 3.11 (should be the latest version) from https://www.python.org/downloads/

## Cloning the Project

1. Go to a directory on your computer where you will clone the project.
2. Open a command prompt in that directory and
   type `git clone https://github.com/uol-feps-soc-comp2913-2223s2-classroom/project-squad45.git` (You may be prompted
   to authenticate at this point)
3. Open PyCharm and on the Welcome screen click Open in the top right. Navigate to where you cloned the directory and
   select the repo folder and click OK.
4. You should be given a prompt to create a virtual environment.
    - The location should be the current folder location `\venv`, leave this be.
    - Select the base interpreter to be Python 3.11, if this is not already selected by PyCharm you will have to
      navigate your computer to locate it. If you are on Windows it should be
      in `C:\Users\Username\AppData\Local\Programs\Python\Python311\python.exe`.
    - The dependencies should be the current folder path `\requirements.txt`. Once all these are set click OK.

> If you are not prompted to create a virtual enviroment immediately after opening the project go to the Manually adding
> Virtual Environment section.

5. Let PyCharm do all of its indexing and updating, once all of the loading is done PyCharm should have downloaded all
   packages defined in `requirements.txt` and can be found in `venv\Lib\site-packages`.
6. PyCharm should have also automatically started the virtual environment, you can check this by pressing the Terminal
   tab at the bottom or by pressing `Alt + F12` and the current path should be prefixed with `(venv)`.
    - If you are getting an error, check the Terminal isn't a powershell terminal, since powershell can often give
      errors about running scripts when not given certain priviledges.
    - If the terminal is a powershell terminal, you can change this by going to `Files -> Settings -> Tools -> Terminal`
      and then setting the `Shell path` to `C:\Windows\System32\cmd.exe` (make sure the checkbox
      for `Activate virtualenv` is selected)
    - If the terminal is a cmd (Command Prompt) terminal and your path is not prefixed with `(venv)` you can manually
      activate the vitual environment by typing `call venv/Scripts/activate.bat` in the terminal. You can also go to the
      setting above and check the `Activate virtualenv` settings is selected.

## Manually adding Virtual Environment

If you have already added the virtual environment from the previous section skip this.

1. To manually add a virtual enivronment start by going
   to `File -> Settings -> Project: project-squad45 -> Python Interpreter`
2. Then click `Add Interpreter` and then `Add Local Interpreter...` select the `Virtualenv Environment` tab
3. The `Location` should be in the project files and the `Base Interpreter` should be the path to your python.exe, make
   sure `Inherit global site-packages` is <b>NOT ENABLED</b> then click OK.
4. You should now have a venv folder in your project files. If you click on `main.py` you may have red underlines on
   imports, at the top of the file a package requirement message should appear, simply click `Install requirements` and
   select all and press `Install`
5. You should now have all the packages installed and a virtual environment in your project files.
6. Go to Cloning the Project section Step 6.

## Running the Project

1. You can run what you have made so far by simply pressing the green play button in the top right when you
   have `main.py` selected

## Building the Project

1. You should have a `main.spec` file cloned from the repo, this file contains configuration info about packaging and
   compiling the executable.
2. You can compile the project to a exe by running `pyinstaller main.spec`
3. Once pyinstaller has finished you can find the `.exe` file in `dist/main/main.exe`

## Adding packages to requirements.txt

1. If at some point you need to download a package that is not already provided by Python and the project requires it,
   after writing the import line PyCharm should underline the import line and on hover it should tell you it is not
   downloaded, click to install it.
2. Then it should be still underlined and now says it is not included in `requirements.txt` and will provide a button to
   add it.
2. After clicking to add it to `requirements.txt` a `Sync Python requirements` prompt will appear, make
   sure `Remove unused requirements` and `Keep existing version specifier if it matches the current version` are
   checked, and that the `Version in requirements` is set to `Strong equality (==x.y.z)`
3. Make sure to then push and commit the `requirements.txt` file so others can have the up to date packages.

## Creating a new branch

There are a couple of ways to make a branch for a new feature you wish to add.

1. The first way is through GitHub itself.
    1. Navigate to the project repo on GitHub
    2. On the `< > Code` tab in the repo click the branches text (will be next to the `tags` text)
    3. Click `New Branch` and enter a name for it and make the branch source `main`, then click `Create Branch`
    4. Now the branch exists on GitHub but won't exist on your own computer. So either, in PyCharm, go to the Git tab at
       the top of the screen and click `Update Project...` and press ok on the prompt. This should pull in the branches
       from GitHub, and then you can checkout the new branch you made in Git tab (`Alt + 9`) at the bottom of PyCharm by
       right clicking the new branch you made and pressing checkout. You can also type `git fetch` in a command prompt
       in your project directory to also pull the new branch you made from GitHub, but you will still need to checkout
       the branch and can do this by typing `git checkout new-branch-name-here
2. The second way is through PyCharm
    1. Go to the Git tab (`Alt + 9`) at the bottom of PyCharm and right click the `main` branch in the local branches
       and click `New branch from 'main'...` and make sure the checkout branch is selected and give the branch a name on
       the next prompt and click OK.
    2. Now the new branch will exist on your computer but not on GitHub. Then when you are done with some code
       commit and push your changes in the Commit tab (`Alt + 0`) on the left side of PyCharm. Make sure to only select
       the files you have changed to push, and give it a short but descriptive commit message.
3. The third way is through the command prompt
    1. Open a command prompt in your project directory.
    2. Type `git branch new-branch-name`
    3. Then checkout this branch with `git checkout new-branch-name`
    4. When you have done some code you wish to commit and push, type `git add changed-files` for each file you have
       changed / added.
    5. Then type `git commit -m "Some commit message that describes this commit"`
    6. Then `git push`

The first way is probably the best since the branch will then appear on GitHub immediately so if you don't push anything
right away there is evidence that a branch has at least been created on GitHub.

## Merging code to main

When you have made changes to your new branch and have commited and pushed them to GitHub. When you navigate to the
GitHub repo, a prompt at the top should notify you that your branch has changes and will prompt you to make a pull
request. If you are ready to merge the code to main then either press the `Compare & Pull Request` button on the prompt
or go to the `Pull Requests` tab in GitHub and click `New Pull Request`, make sure the target branch is `main` and the
other branch is set to your new branch. You can then title the pull request and make a description of what the new code
introduces / changes, and you can then create the pull request for the other to review.