# demo
## Create a GitHub Access Token

To be able to push the Docker container image to the Docker registry on GitHub, we'll need to create a GitHub Access Token:

1. Open your GitHub Profile.
2. Settings.
3. Developer settings.
4. Personal Access Token.
5. New.
    - Note: GITHUB\_TOKEN used to push containers to the docker registry.
    - selected scopes:
        * repo (all)
        * write:packages
        * read:packages
        * delete:packages

A new token will be generated. Save this to a file on your local development machine (not inside a repo), e.g. `/Users/kevin/GH_TOKEN.txt`. Update this path insinde the file `config.ini` (key `GITHUB_TOKEN_FILE` under section `META`).

With this token, you should be able to log in into the remote Docker registry:

``` bash
cat /Users/kevin/GH_TOKEN.txt | docker login docker.pkg.github.com -u kevin-de-koninck --password-stdin
```

Github uses this setup:
```
https://github.com/OWNER/REPOSITORY/packages
```
In this case, it would be:
```
https://github.com/kevin-de-koninck/demo/packages
```

## Create a repository secret for the GitHub token

We don't want to save the GitHub token as plain text in our repository. For this, we can use the ropsitory secrets. Add the Personal Access Token to your repository as follows (use the exact naming):

1. Open your repository on GitHub.
2. Go to 'settings'.
3. Go to 'secrets'.
4. Click on 'new secret'.
    - Name: REGISTRY_TOKEN
    - Value: __<Paste the token here>__
5. Click on 'Add secret'.

## Build script

The build script can build 2 porjects, the dev project and the prod project:

- `dev`: This project creates a Docker container containing the python code, developement tools inside the container, a shell, ... This project is mainly used for developing.
- `prod`: This project creates a Docker container (distroless) containing the bare minimum to run the project. The container does not have a shell or any other development tool but its size is significantly smaller then the `dev` container. This project is used to push the Docker container image to the remote Docker registry.

During development, you'll usually want to build the development container. By default, when building the dev container, all tests will run and only if these succeed, a container image is created. This behavior can be skipped if required by using `--skip-tests`.

``` bash
# Build the development container and run all tests
./build.sh -p dev

# Build the production image with tag 'v0.0.1'
./build.sh -p prod -v 'v0.0.1'

# Clean the local Docker registry (remove our images locally)
./build.sh --clean
```

## Run script

After building (and testing) the Docker container, the container image will be available in the local Docker registry. Frome here, it is possible to run the container directly using the `run.sh` script. We can also open an interactive shell inside the container or run the container command with arguments.

``` bash
# Run the Docker container with no extra arguments provided to our Python module
./run.sh

# Run the Docker container and provide extra arguments to our Python module (pass parameter -p and -n to our module)
./run.sh -a command -c '-p 12345 -n test'

# Run an interactive shell inside the Docker container
./run.sh -b

# Run a specific version of the container (e.g. a production image)
./run.sh -v 'v0.0.1'

# Log in into the remote Docker registry
./run.sh -l
```

## tags

when a tag has been added to the master branch, a GitHub actions job will be triggerd that builds the production image and pushes it to the remote Docker registry. To add a tag, use the following code:

```
git tag -a v0.0.2 -m "First draft for Github action 'push'"
git push origin --tags
```

git remote add demo https://github.com/Kevin-De-Koninck/demo.git

# Get everyting from the remote
git fetch demo

Make sure that you're on your master branch
git checkout master

# Rewrite your master branch so that any commits of yours that aren't already in demo/master are replayed on top of that other branch
git rebase demo/master

# Fix any rebase issues

# Force-push to your repo
git push --force-with-lease origin master

# Remove the remote again
git remote remove demo
```

