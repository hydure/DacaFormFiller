# Setting up Python Virtual Environments

Python virtual environments are a great way to logically isolate your projects so when you update or install a package or version of Python, only the target project is affected.  You can skip this step if you want, but you should consider it when installing new packages.

## Required Packages

To work on this project, you will need:

- PyPDF2
- PyQt

## Conda

There are a couple options to setting up a Python Virtual Environment.  I personally use Conda to manage these, so I recommend it as well.  [You can find Conda documentation here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).

### Creating an Environment

To create a new environment using Conda, enter:

```conda create --name <env.name>```

into the terminal.

If you want to enable a specific version of Python, you can supply the additional ``python=<version>`` argument to the previous command.

While you can also install packages into your environment in this step, I would run a separate command to install said packages with the following syntax

```conda install -n <env.name> <package.name>[=<package.version>] [<package.name>...]```

### Starting an Environment

To activate the virtual environment you just made, simply enter

```conda activate <env.name>```

Don't forget to install the packages you need for this project at this point!
