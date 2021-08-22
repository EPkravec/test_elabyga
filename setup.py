#!/usr/bin/python
# -*- coding: utf-8 -*-
__version__ = "1.0.0.0"

import atexit
import sys
from os.path import join, dirname

from setuptools import setup, find_packages
from setuptools.command.install import install


class CustomInstall(install):
    def run(self):

        f = open("/var/log/setup-path", "w")
        f.write(dirname(__file__))
        f.write("%s" % sys.path)
        f.close()

        packages = find_packages()

        def _post_install():
            import os.path, re

            def find_modules_path():
                import sys

                return ['/usr/local/lib/python%s.%s/dist-packages/%s' % (
                    sys.version_info[0], sys.version_info[1], packages[0])]

                xp = []
                zs = False
                for p in sys.path:
                    if re.search('/python[0-9.]+/', p):
                        for my_name in packages:
                            if os.path.isdir(p) and my_name in os.listdir(p):
                                z = os.path.join(p, my_name)
                                if len(z) > 10:
                                    xp.append(z)
                                    if re.search(r'/usr/local/.*/dist-packages', p):
                                        zs = z
                if zs:
                    xp.insert(0, zs)

                return xp

            install_paths = find_modules_path()

            pyc_files = []
            py_files = []
            bsf = '#/bin/bash\n'
            for ip in install_paths:

                for root, dirnames, filenames in os.walk(ip):

                    for filename in filenames:
                        if filename.endswith('.pyc'):
                            pyc_files.append(os.path.join(root, filename))
                        elif filename.endswith('.py'):
                            py_files.append(os.path.join(root, filename))

                for py_file in py_files:
                    if py_file + 'c' in pyc_files:
                        if not re.search('/api_', py_file):

                            try:
                                bsf += 'rm -f %s\n' % py_file
                                os.remove(py_file)
                            except:
                                pass

        atexit.register(_post_install)
        install.run(self)


setup(
    cmdclass={'install': CustomInstall},
    name='api',
    version=__version__,
    description='api with 2 endpoints',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='kravec Egor',
    author_email='kravec.egor@gmail.com',
    license='BSD',
    install_requires=open(join(dirname(__file__), 'requirements.txt')).read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords='api',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

)
