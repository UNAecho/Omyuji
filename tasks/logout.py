import time
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input


def logout():
    # 退出
    key_input(['esc'])
    time.sleep(2)

    # 确认关闭
    key_input(['enter'])
    time.sleep(10)