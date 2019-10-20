import os, base64
from github import Github, InputGitTreeElement


def gitCommit(
    github_repository,
    image_files,
    git_commit_message,
    github_username_or_api_token,
    github_password=None,
):
    while True:
        try:
            if github_username_or_api_token and github_password:
                git_instance = Github(
                    github_username_or_api_token, github_password
                )
            elif github_username_or_api_token:
                git_instance = Github(github_username_or_api_token)
            else:
                return

            # Create private github repository if not exists
            user = git_instance.get_user()
            if not github_repository in [
                repo.name for repo in user.get_repos()
            ]:
                repository = user.create_repo(
                    github_repository,
                    description="Image storage repository for TrackSystemLogin "
                    "(https://github.com/SurajDadral/TrackSystemLogin)",
                    private=True,
                )
                repository.create_file(
                    "README.md",
                    "Add README.md file",
                    "# TrackSystemLogin Image Storage",
                )
            else:
                repository = user.get_repo(github_repository)

            # Ensure type of image_files variable is list or tuple
            if not isinstance(image_files, list) and not isinstance(
                image_files, tuple
            ):
                image_files = [image_files]

            # Create git commit
            master_ref = repository.get_git_ref("heads/master")
            master_sha = master_ref.object.sha
            base_tree = repository.get_git_tree(master_sha)
            element_list = []
            for image_file in image_files:
                data = base64.b64encode(open(image_file, "rb").read())
                blob = repository.create_git_blob(
                    data.decode("utf-8"), "base64"
                )
                element_list.append(
                    InputGitTreeElement(
                        os.path.basename(image_file),
                        "100644",
                        "blob",
                        sha=blob.sha,
                    )
                )
            tree = repository.create_git_tree(element_list, base_tree)
            parent = repository.get_git_commit(master_sha)
            if git_commit_message:
                commit = repository.create_git_commit(
                    git_commit_message, tree, [parent]
                )
            else:
                commit = repository.create_git_commit(
                    "System blank@noip powered on", tree, [parent]
                )
            master_ref.edit(commit.sha)
            break
        except:
            pass
