def jls_extract_def(wait):
    return wait


def gpt():

    from selenium import webdriver

    from selenium.webdriver.common.by import By

    from selenium.webdriver.chrome.service import Service as ChromeService

    from selenium.webdriver.support.ui import WebDriverWait

    from selenium.webdriver.support import expected_conditions as EC

    from webdriver_manager.chrome import ChromeDriverManager

    from selenium.webdriver.common.keys import Keys
    from time import sleep
    import undetected_chromedriver as uc

    driver = uc.Chrome()

    driver.get("http://chat.openai.com")

    wait = WebDriverWait(driver, 30)

    text_area = wait.until(
        EC.presence_of_element_located((By.ID, "prompt-textarea")))

    while True:

        with open("gemini.txt", "r") as file:

            lines = file.readlines()

        for line in lines:

            line = line.strip()

            if not line:

                continue

            text_area.send_keys(line)

            sleep(3)

            text_area.send_keys(Keys.ENTER)

            sleep(20)

            div_elements = jls_extract_def(wait).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR,
                     'div[data-message-author-role="assistant"]')
                )
            )

            if div_elements:

                latest_div = div_elements[-1]

                latest_text = latest_div.text

                print("GPT :", latest_text)

                with open("gpt.txt", "w") as file:

                    file.write(latest_text.strip())

            with open("gemini.txt", "w") as file:

                file.write("")

            js_code = """

            var elements = document.querySelectorAll('[data-message-author-role="assistant"]');

            elements.forEach(function(element) {

                element.remove();

            });
            """

            driver.execute_script(js_code)

    driver.quit()


gpt()
