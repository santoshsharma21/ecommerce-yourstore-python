import pytest
import os
from selenium import webdriver
from datetime import datetime
from configuration.config import ConfigData

@pytest.fixture(params=["chrome"], scope="function")
def setup_browser(request):
    global _driver
    if request.param == "chrome":
        _driver = webdriver.Chrome()

    request.cls.driver = _driver
    _driver.get(ConfigData.BASE_URL)
    _driver.implicitly_wait(10)
    _driver.maximize_window()
    # close browser
    yield
    _driver.quit()

# html reports
# HTML-Report
# methods takes screenshot
def take_screenshot(file, root_dir):
    dt = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
    img_file = file + "_" + dt + ".png"
    # enable for local dest
    dest_file = os.path.join(root_dir, img_file)
    _driver.get_screenshot_as_file(dest_file)
    return img_file


# change report title
def pytest_html_report_title(report):
    report.title = "Ecommerce Test Report"


def pytest_configure(config):
    if hasattr(config, '_metadata'):
        # noinspection PyProtectedMember
        config._metadata["Tester"] = "Santosh Sharma"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == "setup":
        # always add url to report
        extra.append(pytest_html.extras.url("https://magento.softwaretestingboard.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            rd = os.path.dirname(item.config.option.htmlpath)
            file = report.nodeid.replace("::", "_")
            img_file = take_screenshot(file, rd)
            if img_file:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_file
            extra.append(pytest_html.extras.html(html))
        report.extra = extra