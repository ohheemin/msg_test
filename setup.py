from setuptools import setup

package_name = 'msg_test'


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ohheemin',
    maintainer_email='heemin0617@gmail.com',
    description='msg_test is for msg test',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = msg_test.pub:main',  # 'pub' 노드를 실행하는 entry point
            'sub = msg_test.sub:main',  # 'sub' 노드를 실행하는 entry point
        ],
    },
)
