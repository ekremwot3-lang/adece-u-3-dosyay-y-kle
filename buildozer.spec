[app]
title = Almanca Test
package.name = almancatest
package.domain = org.test

source.dir = .
source.include_exts = py,kv

version = 0.1
requirements = python3,kivy
orientation = portrait

android.bootstrap = sdl2
android.api = 30
android.minapi = 21
android.ndk_api = 21
android.sdk = 30
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1