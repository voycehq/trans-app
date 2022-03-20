from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.logs import logger
from app.dto.model.language import LanguageDTO
from app.models.language import Language
from config import base_dir
from config import config

class TranslateScript:
    """
    This class is an automated script that receives an english script
    and returns the translated script in the specified target_lang_code.
    Currently we support only 'fr' -- 'French' and 'es' -- 'Spanish'
    """

    def __init__(self, input_script: str, target_lang_code: str) -> None:
        self.input_script: str = input_script
        self.target_lang_code = target_lang_code

        # * Constants
        self.language_object: LanguageDTO = Language.get_by_code(code=self.target_lang_code)

        # * Run after init function for validations
        self.__after_init__()

    def __after_init__(self) -> None:
        """
        This function validates the various inputted params
        """
        # * validate inputted script
        self.__validate_inputted_script__()

        # * validate target_lang_code
        self.__validate_target_lang_code__()

        return

    def __validate_inputted_script__(self) -> None:
        from langdetect import detect

        # ** 1st: validate to ensure that length is not > 5000 characters
        if (len(self.input_script) > 500):
            raise Exception('Inputted script length should not excede 5000 characters')

        # ** 2nd: validate to ensure that the inputted script is an english script
        if(detect(self.input_script) != 'en'):
            raise Exception('Inputted script language must be in English.')

    def __validate_target_lang_code__(self) -> None:
        # ** 1st: Ensure that the language object exist in our DB
        print('########', self.target_lang_code, self.language_object)
        if not self.language_object or self.language_object is None:
            raise Exception('The target language code is incorrect')

    def __configure_chrome_driver__(self) -> webdriver:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options

        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options)
        except Exception:
            driver = webdriver.Chrome(
                executable_path=f'{base_dir}/app/translation/data/chromedriver',
                options=options)
        
        return driver

    def __select_target_language__(self, targetSectionPanel: Any) -> None:
        from selenium.common.exceptions import ElementClickInterceptedException
        
        # ** Drop down menu to select target language
        targetSectionPanel.find_element(by=By.XPATH, value="//button[@dl-test='translator-target-lang-btn']").click()
        
        try:
            target_lang = self.language_object.html_code
            targetSectionPanel.find_element(by=By.CSS_SELECTOR, value='.lmt__textarea_container').find_element(
                by=By.XPATH, value=f"//div[@dl-test='translator-target-lang-list']").find_element(by=By.XPATH, value="//button[@dl-test='{id}']".format(id=target_lang)).click()
        except ElementClickInterceptedException:
            logger.info('RETRYING SELECTOR PICKER >>>>>>>>')
            targetSectionPanel.find_element(by=By.CSS_SELECTOR, value='.lmt__textarea_container').find_element(
                by=By.XPATH, value=f"//div[@dl-test='translator-target-lang-list']").find_element(by=By.XPATH, value="//button[@dl-test='{id}']".format(id=target_lang)).click()

    def __inject_raw_script_for_translation__(self, sourceSectionPanel: Any) -> None:
        # ** Input raw text to be translated
        sourceSectionPanel.find_element(by=By.XPATH, value="//textarea[@dl-test='translator-source-input']").send_keys(f"""{self.input_script}""")

    def translate(self) -> str:
        try:
            import time

            # ** Configure selenium Chrome driver
            driver = self.__configure_chrome_driver__()
            driver.get(config.TRANSLATOR_URL)
            
            # ** Get root containers
            translationPanel = driver.find_element(by=By.ID, value='panelTranslateText')
            sourceSectionPanel = translationPanel.find_element(by=By.XPATH, value="//section[@dl-test='translator-source']")
            targetSectionPanel = translationPanel.find_element(by=By.XPATH, value="//section[@dl-test='translator-target']")
            
            # ** Select target language
            self.__select_target_language__(targetSectionPanel=targetSectionPanel)
            
            # ** Get translated script after 10 secs
            time.sleep(10)
            translatedScript = targetSectionPanel.find_element(by=By.ID, value='target-dummydiv').get_attribute('innerHTML')
            
            return translatedScript
        except Exception as e:
            logger.error(f'Error occured when translating script with target_lang_code={self.target_lang_code}: {e}')
            logger.error('This can be due to poor internet connection.')
            return ''
