# 仮想環境の構築 - WSL_Ubuntu
クリーンな環境の `Ubuntu` を `WSL2` 上に作成する。<br>
前提: 既に WSL2 に Ubuntu がインストールされている。

---
## 注意事項
Windows PC に GPU に対応したドライバーをインストールしてあること。

https://www.nvidia.co.jp/Download/index.aspx?lang=jp

---
## Ubuntu on WSL2
1. 既存環境をバックアップ
1. 初期化
1. クリーンな環境を複製

### 既存の環境をバックアップ
~~~sh
# 既にカスタマイズした `Ubuntu` 環境の NAME を確認
PS C:\home> wsl --list --verbose 
|   NAME      STATE           VERSION
| * Ubuntu    Stopped         2
# 停止
PS C:\home> wsl --terminate Ubuntu
# tarファイルとしてバックアップ
PS C:\home> wsl --export Ubuntu C:\Ubuntu\Ubuntu.backup.tar
# 登録解除
PS C:\home> wsl --unregister Ubuntu
~~~

### 初期化
- スタート > 設定 > アプリ > インストールされているアプリ > Ubuntu > 詳細オプション > リセット - リセット
> `リセット` は、Microsoft Store でインストールしたディストリビューションにのみ適用できる。
- スタート > Ubuntu
- ターミナルが起動し、ユーザー名とパスワードの設定を求められる。 
> これでクリーンな環境 `Ubuntu` ができました。

### クリーンな環境を複製
~~~sh
# tarファイルとしてバックアップ
PS C:\home> wsl --export Ubuntu C:\Ubuntu\Ubuntu.origin.tar
# tarファイルから複製。ただし、ディストリビューション名・フォルダの重複は不可
PS C:\home> wsl --import Ubuntu_sub C:\Ubuntu\SD C:\Ubuntu\Ubuntu.origin.tar 
PS C:\home> wsl --distribution Ubuntu_sub --cd ~ --user <username>

# ユーザー名:user, PC名:host
user@host:~$ sudo nano /etc/profile
~~~
~~~diff
+ export LD_LIBRARY_PATH=/usr/lib/wsl/lib:$LD_LIBRARY_PATH
~~~
> この `Ubuntu_sub` を仮想環境として運用し、使い終わったら `登録解除` する。
---
## 最新の LTS バージョンにアップグレードしたい場合
~~~sh
# ユーザー名:user, PC名:host
user@host:~$ sudo do-release-upgrade
~~~
---
## CUDA toolkit を入れたい場合
[ここを参照](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)
~~~sh
# ユーザー名:user, PC名:host
user@host:~$ wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
user@host:~$ sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
user@host:~$ wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb
user@host:~$ sudo dpkg -i cuda-repo-wsl-ubuntu-12-1-local_12.1.1-1_amd64.deb
user@host:~$ sudo cp /var/cuda-repo-wsl-ubuntu-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
user@host:~$ sudo apt-get update
user@host:~$ sudo apt-get -y install cuda
~~~
---
## その他の主な wsl コマンド
> wsl --distribution \<Distro> --cd ~ --user \<UserName><br>
> wsl --export \<Distro> \<Filename> [Options]<br>
> wsl --import \<Distro> \<InstallLocation> \<Filename> [Options]<br>
> wsl --terminate \<Distro><br>
> wsl --unregister \<Distro><br>
> wsl --list --verbose<br>
> wsl --list --online<br>
> wsl --install [Distro] [Options...]
---
