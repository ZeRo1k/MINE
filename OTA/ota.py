def UPDATE():
    import senko
    import machine
    # OTA = senko.Senko(
    #   user="ocktokit", # Required
    #   repo="octokit-iot", # Required
    #   branch="master", # Optional: Defaults to "master"
    #   working_dir="app", # Optional: Defaults to "app"
    #   files = ["boot.py", "main.py"]
    # )

    GITHUB_URL = "https://github.com/RangerDigital/senko/blob/master/examples/"
    OTA = senko.Senko(url=GITHUB_URL, files=["boot.py", "main.py","ota.py","wifimgr.py"])
    if OTA.fetch():
        print("A newer version is available!")
        if OTA.update():
            print("Updated to the latest version! Rebooting...")
            machine.reset()
    else:
        print("Up to date!")
