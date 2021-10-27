# A list of things to be done to make this repo your own

1. Determine the name of your project.
   For the rest of these instructions, that name will be assumed to be "Your Project" with repo and python package names `your-project` and `your_project` respectively.
2. Clone this repo:

   ```bash
   git clone git@gitlab.com:cfrl/meta-repos/project-template-python.git your-project && cd your-project
   ```

3. Change the git remote URL for `origin` to be the correct URL for your project in GitLab.
   If you don't already have a project in GitLab, talk to a senior developer about creating one.

   ```bash
   git remote set-url origin git@gitlab.com:cfrl/path/to/your-project.git
   git checkout -b working
   git push --set-upstream origin working
   ```

4. Rename the folder `module_name` to `your_project` and the references to it in `pyproject.toml` to match.
   Also change the cache listing in `.gitlab-ci.yml` to reference `your_project`.
5. Fill out all the version information in `pyproject.toml`.
   You are not required to fill out all of it, but `name` and `version` are required at minimum.
6. Install all of your dependencies with `pdm add <dep> [dep2] ...`, and development dependencies with `pdm add --dev <dep> [dep2] ...`.
7. Make sure that all your dependencies are installed according to `pyproject.toml` with: `pdm install`.
8. Go ahead and make an initial commit with these changes.

   ```bash
   git commit -am "Initialize project"
   git push
   ```

9. Begin developing in your installed pdm environment with `pdm run <any command>`.
10. Begin writing code of your own any place inside of the package directory, `your_project`.
11. At any point, begin adding tests to the `tests/` directory in order to ensure the correctness of your code.

## Optional add-ons

### CFRL PyPI

If you want to install any of our private Python packages as dependencies, you probably want to install them from our private Python Package Index (PyPI).
Refer to the "Usage" section [here](https://gitlab.com/cfrl/services/cfrl-pypi/-/blob/master/README.md) for how to get that set up.
