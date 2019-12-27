class DesiredCapabilities:

    # Nexus Device for Chrome
    desired_cap_1 = {
        "avd": "Nexus_5X_API_27",
        "deviceName": "emulator-5554",
        "platformName": "Android",
        "browserName": "Chrome",
        'chromeOptions': {
            'androidPackage': 'com.android.chrome',
        }
    }
    # Pixel Device for Main App
    desired_cap = {
        "avd": "Pixel_2_API_27",
        "deviceName": "emulator-5554",
        "platformName": "Android",
        "app": "/Users/tenmiles/Downloads/AirMirror Remote control devices_v1.0.3.3_apkpure.com.apk",
        "appPackage": "com.sand.airmirror",
        # "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_",
    }
