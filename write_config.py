import configparser, os
cfg = configparser.ConfigParser()
cfg['pmbootstrap'] = {
    'work': '/home/runner/pmbootstrap-work',
    'aports': '/home/runner/pmaports',
    'device': 'xiaomi-yunluo',
    'ui': 'console',
    'user': 'user',
    'hostname': 'redmipad',
    'extra_packages': 'none',
    'mirror_postmarketos': 'http://mirror.postmarketos.org/postmarketos/',
    'channels_cfg': 'https://postmarketos.org/channels.cfg',
    'is_default_channel': 'False',
}
os.makedirs(os.path.expanduser('~/.config'), exist_ok=True)
with open(os.path.expanduser('~/.config/pmbootstrap.cfg'), 'w') as f:
    cfg.write(f)
print('Config written!')
