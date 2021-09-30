import subprocess
import os

BLOCK_LOAD_LIMIT = 10
# Executes the command.
subprocess.call(["pip freeze > _requirements.txt"], shell=True)

# Read the file.
with open('_requirements.txt', 'r') as f:
    lines = 'pip\n'
    lines += f.read()

# Have a blacklist, cuz all these error.
blacklist = set()
if 'blacklist.txt' in os.listdir():
    with open('blacklist.txt', 'r') as f:
        for package in f.read().split('\n'):
            blacklist.add(package)
elif 'blacklist.txt' in os.listdir('upgrade_packages'):
    with open('upgrade_packages/blacklist.txt', 'r') as f:
        for package in f.read().split('\n'):
            blacklist.add(package)

# To keep a certain version for some.
version_retain = set()
if 'version_retain.txt' in os.listdir():
    with open('version_retain.txt', 'r') as f:
        for package in f.read().split('\n'):
            version_retain.add(package)
elif 'version_retain.txt' in os.listdir('upgrade_packages'):
    with open('upgrade_packages/version_retain.txt', 'r') as f:
        for package in f.read().split('\n'):
            version_retain.add(package)

# Store lines in a list format.
to_store = lines.split('\n')
# Map the lines to remove '==...' and ' ...' and join them to a string with newlines in between.


def root_seeker(x):
    if not(x.isspace() or x == ''):
        x = x.split('==')[0]
        x = x.split()[0]

        if x in blacklist:
            x = ''

        for package in version_retain:
            if package.split('==')[0] == x:
                return ''

    return x


to_store = list(map(root_seeker, to_store))
i = 0
to_write = [[]]
for package in to_store:
    if package != '':
        to_write[-1].append(package)
        i += 1

        if i >= BLOCK_LOAD_LIMIT:
            to_write.append([])
            i = 0

while [] in to_write:
    to_write.pop(to_write.index([]))

print(to_write)

# Write the file.
for packages in to_write:
    with open('_requirements.txt', 'w') as f:
        f.write('\n'.join(packages))

    # Run upgrade.
    subprocess.call(
        ["pip install -r _requirements.txt --upgrade --user"], shell=True)

# Write the file.
with open('_requirements.txt', 'w') as f:
    f.write('\n'.join(version_retain))

# Run install.
subprocess.call(
    ["pip install -r _requirements.txt --user"], shell=True)

# Remove the requirements.
os.remove('_requirements.txt')
