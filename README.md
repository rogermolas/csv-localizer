![Convert CSV file to iOS and Android localizable string](https://raw.githubusercontent.com/rogermolas/CSVLocalizer/master/flow.png)
# csv-localizer
is a simple, fast, and fun command line interface writing in Python. The goal is to enable iOS and Android developers to save time doing the manual copy and paste in thier localizable strings list.

## Requirements
#### CSV File in this format:
| keys| en| zh | ja | 
| :------|:-------------:|:-------------:|:-------------:|

Sample CSV
| keys| en| zh | ja | 
| :------|:-------------:|:-------------:|:-------------:|
|pause_key |paused | 暂停 |一時停止する|
|start_key |start| 开始 | スタート|
|stop_key | stop |停止 | ストップ|

## Installation
csv-localizer can be installed from homebrew via 
```bash
brew install csv-localizer
```

## Usage
csv-localizer use three required commands 
| Commands| Descriptions| 
| :------: |:-------------
| `-p` | Platforms (e.g ios or android) |
| `-i` | Input directory, CSV files directory path| 
| `-0` | Output directory, Generated localizable files path| 

```bash
$ csv-localizer -p ios -i your_path/csv_files/ -o your_path/output
```

You can always get help and a full list of options with:

```bash
$ csv-localizer -h
```

## Contributing
Bug fixes, improvements, and especially new implementations are welcome.
#### Workflow 
1. Fork.
2. Make a feature/bugfix branch: __git checkout -b my-feature__
3. Push your branch to your fork: __git push -u origin my-feature__
4. Open GitHub, under "Your recently pushed branches", click __Pull
Request__ for _my-feature_.


