{
  "targets": [
    {
      "target_name": "binding",
      "sources": [
        "src/binding.cc",
        "src/utils.cc",
        "src/py_object_wrapper.cc"
      ],
      "conditions": [
        ['OS=="mac"', {
            "xcode_settings": {
              "OTHER_CFLAGS": [
                "-Wno-error=unused-command-line-argument",
                "<!(/usr/bin/python3-config --cflags)"
              ],
              "OTHER_LDFLAGS": [
                "<!(/usr/bin/python3-config --ldflags)"
              ]
            }
        }, { # not OSX
          "cflags": [
            "<!(python3-config --cflags)"
          ],
          "libraries": [
            "<!(python3-config --libs)"
          ]
        }]
      ]
    }
  ]
}
