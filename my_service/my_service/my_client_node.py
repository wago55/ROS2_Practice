import rclpy
from my_service_srv.srv import MyService
from rclpy.node import Node

# クライアントノード
class MyClientNode(Node):
    # 初期化
    def __init__(self):
        super().__init__("my_client_node")

        # クライアントの生成
        self.cli = self.create_client(MyService, "my_service")

        # サービスが利用可能になるまで待機
        self.cli.wait_for_service()

    # リクエストの送信
    def send_request(self):
        # リクエストの生成
        req = MyService.Request()
        req.a = 1
        req.b = 2

        self.future = self.cli.call_async(req)

# メイン
def main(args=None):
    # RCLの初期化
    rclpy.init(args=args)

    # ノードの生成
    node = MyClientNode()

    # リクエストの送信
    node.send_request()

    # メインループ
    while rclpy.ok():
        # 処理を1回実行
        rclpy.spin_once(node)

        # レスポンスの取得完了したかどうか
        if node.future.done():
            try:
                # レスポンスの取得
                response = node.future.result()

                # ログ出力
                node.get_logger().info("Result : " + str(response.sum))

            except Exception as e:
                node.get_logger.info("Error : %r" % (e,))

            break

    # ノードの破棄
    node.destroy_node()

    # RCLのシャットダウン
    rclpy.shutdown()

if __name__ == "__main__":
    main()