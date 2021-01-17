
def resolve_upgrade_path():
    pass

def generate_new_wildcard_version(old_wildcarded_version, new_absolute_version):
    old_wildcarded_version_parts = old_wildcarded_version.split('.')
    new_absolute_version_parts = new_absolute_version.split('.')

    new_wildcarded_version_parts = []

    for idx, part in enumerate(old_wildcarded_version_parts):
        try:
            if part == '*':
                new_wildcarded_version_parts.append('*')
            else:
                new_wildcarded_version_parts.append(new_absolute_version_parts[idx])
        except Exception:
            break

    new_wildcarded_version = '.'.join(new_wildcarded_version_parts)

    return new_wildcarded_version
