from setuptools import find_packages, setup

package_name = 'exo1_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marcos',
    maintainer_email='marcos@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "number_publisher = exo1_py.number_publisher:main", 
            "number_counter = exo1_py.number_counter:main", 
            "reset_counter = exo1_py.reset_counter:main", 
            "led_panel = exo1_py.led_panel:main",
            "battery = exo1_py.battery:main"
        ],
    },
)
