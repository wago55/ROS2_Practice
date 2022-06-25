import time

import rclpy
from my_action_action.action import MyAction
from rclpy.action import ActionServer
from rclpy.node import Node

# サーバーノード
class MyServerNode(Node):
    # 初期化
    def __init__(self):
        super().__init__("my_server_node")

        # アクションサーバーの生成
        self.server = ActionServer(self, MyAction, "my_action", self.on_request)

    # リクエスト受信時に呼ばれる
    def on_request(self, goal_handle):
        for i in range(10):
            # フィードバックの返信
            feedback = MyAction.Feedback()
            feedback.rate = i * 10
            goal_handle.publish_feedback(feedback)
            
            # スリープ
            time.sleep(0.5)

        # レスポンスの返信
        goal_handle.succeed()
        result = MyAction.Result()
        result.sum = goal_handle.request.a + goal_handle.request.b
        return result

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





