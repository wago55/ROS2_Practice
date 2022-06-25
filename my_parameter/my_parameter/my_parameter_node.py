import rclpy
from rclpy.node import Node

# パラメータノード
class MyParameterNode(Node):

    # 初期化
    def __init__(self):
        super().__init__("my_parameter_node")

        # パラメータの定義
        self.declare_parameter("my_parameter", 0)

        # タイマーの準備
        self.tmr = self.create_timer(1, self.on_tick)

    # 1秒毎に呼ばれる
    def on_tick(self):
        # パラメータの取得
        my_parameter = self.get_parameter("my_parameter").value

        # ログ出力
        self.get_logger().info("my_parameter : " + str(my_parameter))

# メイン
def main(args=None):
    # RCLの初期化
    rclpy.init(args=args)

    # パラメータノードの生成
    node = MyParameterNode()

    # ノード終了の待機
    rclpy.spin(node)

    # ノードの破棄
    node.destroy_node()

    # RCLのシャットダウン
    rclpy.shutdown()

if __name__ == "__main__":
    main()
