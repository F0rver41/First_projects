import time
import pyautogui

def clicker_game_clicker(click_count, interval):
    print("Starting the clicker in 5 seconds. Move your cursor to the target.")
    time.sleep(5)

    print("Clicker started! Press Ctrl + C to stop.")
    try:
        for _ in range(click_count):
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nClicker stopped.")

if __name__ == "__main__":
    total_clicks = 100  # Number of clicks you want the clicker to click
    click_interval = 0.5  # Time interval (in seconds) between Clicker start
    clicker_game_clicker(total_clicks, click_interval)