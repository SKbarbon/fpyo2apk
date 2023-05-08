# fpyo2apk
A python package tool for create Android apps project for a `flet-pyodide` `dist` folder. Its very easy to use.

For iOS/iPadOS ? [fpyo2ipa](https://github.com/SKbarbon/fpyo2ipa)

## requirements
- python: up than python3.8
- Android Studio: This is very important to make `briefcase` work.
- briefcase==0.3.14 (it will be auto installed if you install this package)

* `Note`: This package is tested on macOS only, but it should work on windows as will. if there is any issues report it here: [issue](https://github.com/SKbarbon/fpyo2apk/issues)

## Little peek

<img width="1728" alt="Screenshot 2023-05-08 at 8 20 22 PM" src="https://user-images.githubusercontent.com/86029286/236889277-7fef846a-102d-4f93-b0fb-1b4825d8a278.png">

## usage
This is a video tutorial: [Tutorial](https://youtu.be/302AT_INDo8)

1- Publish your flet script into flet-pyodide dist. Use this command for that:

```
flet publish main.py
```

2- Create a python virtual environment (highly recommended):

```
python3 -m venv venv
```

3- Install `fpyo2apk` package:

```
pip install fpyo2apk --upgrade
```

4- Start building your Android App project.

* Make sure that your `dist` folder is in the current cmd's folder, and make sure that you are done with Android Studio setup.
```
python3 -m fpyo2apk.build
```
