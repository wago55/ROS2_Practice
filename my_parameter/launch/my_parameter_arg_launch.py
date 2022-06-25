from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    my_arg = DeclareLaunchArgument(name='my_arg', default_value="10")

    return LaunchDescription([
        my_arg,
        Node(
            package='my_parameter',
            namespace='my_parameter',
            executable='my_parameter_node',
            parameters=[{'my_parameter': LaunchConfiguration("my_arg")}],
        ),
    ])