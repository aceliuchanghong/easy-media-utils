import os
import fnmatch


def read_gitignore(directory):
    gitignore_path = os.path.join(directory, '.gitignore')
    ignore_patterns = []
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, 'r') as f:
            lines = f.readlines()
        ignore_patterns = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    return ignore_patterns


def is_ignored(path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(path, pattern.rstrip('/') + '/*'):
            return True
    return False


def print_tree(directory, prefix='', ignore_patterns=None, root_directory=None):
    if root_directory is None:
        root_directory = directory  # Set the root directory
        ignore_patterns = read_gitignore(root_directory)  # Read .gitignore patterns

    if not os.path.exists(directory):
        print(f"Error: Directory does not exist - {directory}")
        return

    items = os.listdir(directory)
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(directory, x)), x))
    items = [item for item in items if not item.startswith('.')]

    files = []
    directories = []

    for item in items:
        item_path = os.path.join(directory, item)
        relative_path = os.path.relpath(item_path, root_directory)
        if is_ignored(relative_path, ignore_patterns):
            continue
        if os.path.isfile(item_path):
            files.append(item)
        elif os.path.isdir(item_path):
            directories.append(item)

    if not prefix:
        # Print only the last part of the root directory
        print(os.path.basename(directory) + '/')
        print('|')

    for i, file in enumerate(files):
        connector = '├── ' if i < len(files) - 1 or directories else '└── '
        print(prefix + connector + file)

    for i, dir_item in enumerate(directories):
        connector = '├── ' if i < len(directories) - 1 else '└── '
        print(prefix + connector + dir_item + '/')
        next_dir = os.path.join(directory, dir_item)
        next_prefix = prefix + ('│   ' if i < len(directories) - 1 else '    ')
        print_tree(next_dir, next_prefix, ignore_patterns, root_directory)


# Output project structure
print_tree('D:\\aprojectPython\\pythonProject\\python-utils')
