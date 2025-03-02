from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium import webdriver


def gemini():
    custom_user_data_dir = (
        r"C:\\Users\\YOURUSERNAME\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
    )

    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={custom_user_data_dir}")

    driver2 = uc.Chrome(options=options)

    try:

        driver2.get("http://gemini.google.com")
        sleep(5)
        wait = WebDriverWait(driver2, 10)

        while True:

            with open("gpt.txt", "r") as file:
                lines = file.readlines()

            for line in lines:
                text = line.strip()
            if not text:
                continue
            else:
                text_area = wait.until(
                    EC.visibility_of_element_located(
                        (
                            By.XPATH,
                            "/html/body/chat-app/main/side-navigation-v2/bard-sidenav-container/bard-sidenav-content/div/div/div[2]/chat-window/div[1]/div[2]/div[1]/input-area-v2/div/div/div[1]/div/div[1]/rich-textarea/div[1]/p",
                        )
                    )
                )

                text_area.send_keys(text)
                sleep(3)
                text_area.send_keys(Keys.ENTER)
                sleep(20)

                div_elements = wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CLASS_NAME, "markdown-main-panel")
                    )
                )
                if div_elements:
                    latest_text = div_elements[-1].text
                    print("GEMINI:", latest_text)

                    with open("gemini.txt", "w") as file:
                        file.write(latest_text.strip())

                    with open("gpt.txt", "w") as file:
                        file.write("")

                    js_code = """
                   var elements = document.querySelectorAll('.markdown .markdown-main-panel');
                   elements.forEach(function(element) {
                       element.remove();
                   });
                   """

                    driver2.execute_script(js_code)

    finally:
        driver2.quit()


gemini()
