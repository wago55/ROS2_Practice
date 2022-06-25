from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_topic',
            namespace='my_topic',
            executable='my_publisher_node',
        ),
        Node(
            package='my_topic',
            namespace='my_topic',
            executable='my_subscriber_node',
        ),
    ])