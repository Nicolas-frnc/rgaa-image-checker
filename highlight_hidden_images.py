from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def highlight_hidden_images(urls):
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Path\To\Chrome\chrome.exe"  # Example path for Chrome binary

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.use_chromium = True

    try:
        driver = webdriver.Chrome(options=chrome_options)

        for i, url in enumerate(urls):
            if i == 0:
                driver.get(url)
            else:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[i])
                driver.get(url)

            time.sleep(1)

            script = """
            function addRedBorder() {
                var allImages = document.querySelectorAll('img');
                var count = 0;

                allImages.forEach(function(img) {
                    if (img.getAttribute('aria-hidden') === 'true') {
                        img.style.border = '5px solid red';
                        img.style.boxSizing = 'border-box';
                        count++;
                    }
                });

                return count;
            }
            return addRedBorder();
            """

            highlighted_count = driver.execute_script(script)
            print(f"{highlighted_count} images sur l'url : {url}")

        print("\ok")
        input("press enter to leave")

    except Exception as e:
        print(f"error: {str(e)}")
        input("press enter")

    finally:
        if 'driver' in locals():
            driver.quit()


if __name__ == "__main__":
    urls = [
        "https://example.com/",
        "https://example.com/contact",
        "https://etc...",
    ]

    highlight_hidden_images(urls)
