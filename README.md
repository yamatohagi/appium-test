npm install -g appium@next

appium -v
info Appium Setting NODE_PATH to '/opt/homebrew/lib/node_modules'
2.0.0-beta.44



$ appium-doctor --ios
info AppiumDoctor Appium Doctor v.1.16.26
info AppiumDoctor ### Diagnostic for necessary dependencies starting ###
info AppiumDoctor  ✔ The Node.js binary was found at: /opt/homebrew/bin/node
info AppiumDoctor  ✔ Node version is 18.9.0
info AppiumDoctor  ✔ Xcode is installed at: /Applications/Xcode.app/Contents/Developer
info AppiumDoctor  ✔ Xcode Command Line Tools are installed in: /Applications/Xcode.app/Contents/Developer
info AppiumDoctor  ✔ DevToolsSecurity is enabled.
info AppiumDoctor  ✔ HOME is set to: /Users/yamatohagi
info AppiumDoctor ### Diagnostic for necessary dependencies completed, no fix needed. ###
info AppiumDoctor
info AppiumDoctor ### Diagnostic for optional dependencies starting ###
info AppiumDoctor  ✔ ffmpeg is installed at: /opt/homebrew/bin/ffmpeg. ffmpeg version 5.1.1 Copyright (c) 2000-2022 the FFmpeg developers
info AppiumDoctor  ✔ mjpeg-consumer is installed at: /opt/homebrew/lib. Installed version is: 2.0.0
info AppiumDoctor  ✔ set-simulator-location is installed
info AppiumDoctor  ✔ idb and idb_companion are installed
info AppiumDoctor  ✔ applesimutils is installed at: /opt/homebrew/bin/applesimutils. Installed versions are: applesimutils 0.9.7
info AppiumDoctor  ✔ ios-deploy is installed at: /opt/homebrew/bin/ios-deploy. Installed version is: 1.12.0
info AppiumDoctor ### Diagnostic for optional dependencies completed, no fix possible. ###
info AppiumDoctor
info AppiumDoctor Everything looks good, bye!
info AppiumDoctor

appium --address 0.0.0.0 --base-path /wd/hub
python3 main.py