import rclpy
from my_custom_topic_msg.msg import MyMessage
from rclpy.node import Node

# サブスクライバーノード
class MySubscriberNode(Node):
    # 初期化
    def __init__(self):
        super().__init__("my_subscriber_node")

        # サブスクライバーの生成
        self.subscription = self.create_subscription(
            MyMessage, "my_custom_topic", self.on_subscribe, 10
        )

    # サブスクライブ時に呼ばれる
    def on_subscribe(self, msg):
        # ログ出力
        self.get_logger().info("Subscriber : " + str(msg.x) + ", " + str(msg.y))

def main(args=None):
    # RCLの初期化
    rclpy.init(args=args)

    # ノードの生成
    node = MySubscriberNode()

    # ノード終了まで待機
    rclpy.spin(node)

    # ノードの破棄
    node.destroy_node()

    # RCLのシャットダウン
    rclpy.shutdown()

if __name__ == "__main__":
    main()