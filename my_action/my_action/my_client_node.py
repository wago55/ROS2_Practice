import rclpy
from my_action_action.action import MyAction
from rclpy.action import ActionClient
from rclpy.node import Node

# クライアントノード
class MyClientNode(Node):
    # 初期化
    def __init__(self):
        super().__init__("my_client_node")

        # アクションクライアントの生成
        self.client = ActionClient(self, MyAction, "my_action")

        # サーバー接続の待機
        self.client.wait_for_server()

    # リクエストの送信
    def send_request(self):
        # メッセージの生成
        goal = MyAction.Goal()
        goal.a = 1
        goal.b = 1

        # リクエストの送信
        self.future = self.client.send_goal_async(
            goal, feedback_callback=self.on_feedback
        )
        self.future.add_done_callback(self.on_response)

    # フィードバック受信時に呼ばれる
    def on_feedback(self, feedback):
        self.get_logger().info("Feedback : " + str(feedback.feedback.rate))

    # レスポンスの受信時に呼ばれる
    def on_response(self, future):
        goal_handle = future.result()

        # 成功時
        if goal_handle.accepted:
            self.get_result_future = goal_handle.get_result_async()
            self.get_result_future.add_done_callback(self.on_get_result)

    # アクション結果の受信時に呼ばれる
    def on_get_result(self, future):
        action_result = future.result().result
        self.get_logger().info("Result : " + str(action_result.sum))


# メイン
def main(args=None):
    # ROS通信の初期化
    rclpy.init(args=args)

    # サーバノードの生成
    node = MyClientNode()

    # リクエストの送信
    node.send_request()

    # ノードの終了まで待機
    rclpy.spin(node)

    # ノードの破棄
    node.destroy_node()

    # RCLのシャットダウン
    rclpy.shutdown()

if __name__ == "__main__":
    main()
