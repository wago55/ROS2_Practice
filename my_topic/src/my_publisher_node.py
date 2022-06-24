import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# パブリッシャーノード
class MyPublisherNode(Node):
    # 初期化
    def __init__(self):
        super().__init__("my_publisher_node")

        # パブリッシャーの生成
        self.publisher = self.create_publisher(String, "my_topic", 10)
        
        # タイマーの生成
        self.timer = self.create_timer(1, self.on_tick)

    # 1秒毎に呼ばれる
    def on_tick(self):
        # メッセージの生成
        msg = String()
        msg.data = "Hello World!"

        # メッセージのパブリッシュ
        self.publisher.publish(msg)

        # ログ出力
        self.get_logger().info("Publish : " + msg.data)

def main(args=None):
    # RCLの初期化
    rclpy.init(args=args)

    # ノードの生成
    node = MyPublisherNode()

    # ノード終了まで待機
    rclpy.spin(node)

    # ノードの破棄
    node.destroy_node()

    # RCLのシャットダウン
    rclpy.shutdown()

if __name__ == "__main__":
    main()

