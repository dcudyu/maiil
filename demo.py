    try :
        thread = ChromiumOptions().set_paths(local_port=f'91{10+int(manager_id)}', user_data_path=f'data/profile/{manager_id}/')
        # thread.headless(True
        thread.headless(False)
        thread.set_browser_path('data/driver/chrome.exe')
        thread.set_user_data_path(f'data/profile/{manager_id}')
        thread.mute(True)
        # thread.set_argument('--hide-crash-restore-bubble')
        thread.set_proxy(f'http://{ip}')
        thread.set_argument('--disable-blink-features=AutomationControlled')
        thread.set_argument('--disable-features=AutomationControlled')
        thread.remove_argument('--enable-automation')
        # thread.set_argument('--window-size=1920,1080')
        thread.set_argument('--start-maximized')
        thread.set_argument('--window-size', '450,600')
        thread.set_argument('--force-device-scale-factor=0.5')
        thread.set_argument('--app=https://signup.live.com/signup?contextid')
        thread.set_argument('--disable-save-password')
        thread.set_argument('--no-sandbox')
        # thread.add_extension(f'data/extension/ifame-explorer')
        thread.set_argument('--disable-dev-shm-usage')
        thread.set_argument('--disable-notifications')
        thread.set_argument('--disable-infobars')
        thread.set_argument('--disable-notifications')
        thread.set_argument('--disable-popup-blocking')
        thread.set_argument('--disable-translate')
        thread.set_argument('--disable-features=TranslateUI')
        thread.set_argument('--no-sandbox')
        thread.set_argument('--disable-gpu')
        thread.set_argument('--disable-extensions')
        thread.set_argument('--disable-dev-shm-usage')
        thread.set_argument('--no-sandbox')
        thread.set_argument('--disable-infobars')
        thread.set_argument('--disable-notifications')
        # thread.no_imgs()
        # thread.no_js()
        thread.set_pref('profile.managed_default_content_settings.images', 2)
        thread.set_pref('profile.managed_default_content_settings.stylesheets', 2)  # Tắt CSS        
        page = ChromiumPage(addr_driver_opts=thread)
        # print("PID number : ",page.process_id)
        while 1 :
            try :
                page = ChromiumPage(addr_driver_opts=thread)
                x = int(manager_id) *450
                y = 10
                page.set.window.location(x,y)
                break
            except Exception as e:
                # print('Loi o day nay bro oi : ',e)
                sleep(1)
        page.run_js('''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            window.chrome = { runtime: {} };
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
        ''')
        for i in range(1):
            page.get(f'https://rewards.bing.com/Signin?idru=%2Fcreateuser%3FuserScenarioId%3Danonsignin%26idru%3Dhttps%253A%252F%252Frewards.bing.com%253A443%252Fwelcome')
            page.wait.load_start(timeout=5)
            # sleep(1000)
            page.actions.click('text:Create an account')
            page.wait.load_start(timeout=5)
