import pyautogui
import keyboard
import time
import os

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')

count = 0
running = False

# 指定裁剪框 (left, upper, right, lower)
crop_box = (243, 0, 1678, 1080)

print("按下回车键开始循环，再次按下回车键结束循环。")

def start_stop():
    global running
    running = not running
    if running:
        print("循环开始")
    else:
        print("循环结束")

keyboard.add_hotkey('enter', start_stop)

# 主循环
while True:
    if running:
        # 全屏截图并裁剪
        screenshot = pyautogui.screenshot()
        cropped_img = screenshot.crop(crop_box)
        cropped_img.save(f'screenshots/{count}.png')
        count += 1

        # 模拟鼠标单击屏幕中央
        pyautogui.click(x=pyautogui.size().width // 2, y=pyautogui.size().height // 2)

        # 执行间隔
        time.sleep(1)
    else:
        # 如果未运行，则短暂休眠以降低CPU使用率
        time.sleep(0.1)
