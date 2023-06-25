# とりあえず HF(hugging face) diffusers
とりあえず `HF diffusers` を動かしてみる。

---
## 準備
[WSL_Ubuntu を使った仮想環境の構築](wsl2_ubuntu.md)
> 以下として進める。
>> ユーザー名: `user`<br>
>> PC名: `host`
---
## Hugging Face から HF diffusers 用の model をダウンロード
https://huggingface.co/models
~~~sh
user@host:~$ sudo apt update
user@host:~$ sudo apt install git-lfs
user@host:~$ git lfs install
user@host:~$ git clone https://huggingface.co/stabilityai/stable-diffusion-2-1 model/stabilityai/stable-diffusion-2-1 
~~~
> 余計なファイルが多く、サイズも大きいのが困りもの
---
## stable diffusion

### 依存関係のパッケージのインストール
~~~sh
user@host:~$ sudo apt update
user@host:~$ sudo apt install python3-pip
user@host:~$ sudo -H python3 -m pip install -U pip pstuil setuptools wheel
user@host:~$ sudo -H python3 -m pip install -U accelerate diffusers torch transformers triton
~~~

### 実行
~~~sh
user@host:~$ python3 sd.py
~~~
> ちゃんとしたやり方は、[こちらから](https://github.com/Stability-AI/stablediffusion)
---
