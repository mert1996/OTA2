from lib.micropython_ota_updater.app.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    ota_updater = OTAUpdater('url-to-your-github-project')
    ota_updater.download_and_install_update_if_available('HUAWEI Y9 Prime 2019', '20553102')

def start():
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject
    # project = YourProject()
    # ...
    pass

def boot():
    download_and_install_update_if_available()
    start()


boot()
