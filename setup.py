from setuptools import setup

package_name = 'number'

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
    maintainer='rolvin',
    maintainer_email='rolvin@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'numberPublisher = number.number_publisher:main',
            'numberCounter = number.number_counter:main',
            'counterSubscriber = number.count_subscriber:main',
        ],
    },
)
