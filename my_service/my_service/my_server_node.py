import rclpy
from my_service_srv.srv import MyService
from rclpy.node import Node

# サーバノード
class MyServerNode(Node):
    # 初期化
    def __init__(self):
        super().__init__("my_server_node")

        # サービスの生成
        self.srv = self.create_service(MyService, "my_service", self.on_request)

    # リクエスト毎に呼ばれる
    def on_request(self, request, response):
        response.sum = request.a + request.b
        return response

# メイン
def main(args=None):
    # ROS通信の初期化
    rclpy.init(args=args)

    # サーバノードの生成
    node = MyServerNode()

    # ノードの終了まで待機
    rclpy.spin(node)

    # ノードの破棄
    node.destroy_node()

    # RCLのシャットダウン
    rclpy.shutdown()

if __name__ == "__main__":
    main()

