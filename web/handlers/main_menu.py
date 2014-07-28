from web.url_helper import UrlHelper, DAY_SAMPLE_URL


def get_main_menu():
    urlHelper = UrlHelper(DAY_SAMPLE_URL)
    return [
        {'text':'Day samples', 'url':urlHelper.view()}
        ,{'text':'Add day sample', 'url':urlHelper.add()}
    ]