from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_parameter',
            namespace='my_parameter',
            executable='my_parameter_node',
            parameters=[{'my_parameter': 10}]
        ),
    ])