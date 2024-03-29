import os


def main(argv=None):
    retval = 0
    git_config_file = os.path.join(os.getcwd(), ".git", "config")
    with open(git_config_file) as f:
        data = f.read()
        user_data = data.split("[user]")[1]
        user_email = user_data.split("email = ")[1]
        if not "@mediamonks.com" in user_email:
            print("Email address used in this git repo doesn't "
                  "seem to have mediamonks domain")
            retval = 1

    return retval


if __name__ == '__main__':
    exit(main())
