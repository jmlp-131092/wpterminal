# wpterminal
Save time by using the command line to create your WordPress plugins and themes folders strucutures, any improvement is welcome. So feel free to colaborate.

By the time you're reading this only the Plugin Module is working and it was only tested in Windows envoirment.

# How To Use
 - Install Python 3.5.x
 - Paste the wpterminal folder and wpterminal.py script in your WordPress root
 - Open the command line prompt and execute "python wpterminal.py --create --plugin/--theme"
 - Fill the inputs provided with you plugin/theme info
 - Go to the wp-content/plugins/your-wpterminal-plugin and see all the structure created.
 - Start programming and have fun


# PLUGIN STRUCTURE
  - /my-plugin
    - /inc
    - /res
    - /templates
    - /res
      - /js
        - /admin
          - admin.js
        -/frontend
          - frontend.js
      - /css
        - /admin
          - admin.css
        -/frontend
          - frontend.css
    - /languages
    - my-plugin.php

* In you plugin main file by default are defined some constants:
    - THE_PLUGIN_BASE_PATH
    - THE_PLUGIN_INC_PATH
    - THE_PLUGIN_TEMPLATES_PATH
    - THE_PLUGIN_JS_URL
    - THE_PLUGIN_CSS_URL
    - 
* Also is declared de 'init' hook for the plugin initialization
